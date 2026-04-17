#!/usr/bin/env python3
"""
Obsidian 知识库结构分析脚本
用于分析知识库的目录结构、笔记数量、字数统计等
"""

import os
import sys
import yaml
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter

class ObsidianAnalyzer:
    def __init__(self, obsidian_root="/var/minis/mounts/obsidian"):
        self.obsidian_root = Path(obsidian_root)
        if not self.obsidian_root.exists():
            raise FileNotFoundError(f"Obsidian 目录不存在: {obsidian_root}")
        
        self.stats = {
            "total_notes": 0,
            "total_size_kb": 0,
            "total_words": 0,
            "by_category": defaultdict(lambda: {"count": 0, "size_kb": 0, "words": 0}),
            "by_status": defaultdict(int),
            "by_year": defaultdict(int),
            "by_month": defaultdict(int),
            "tags": Counter(),
            "recent_notes": [],
            "largest_notes": [],
            "categories": set()
        }
    
    def parse_frontmatter(self, content):
        """解析 YAML 前端元数据"""
        if not content.startswith("---\n"):
            return {}
        
        try:
            # 提取 YAML 部分（更健壮的方法）
            lines = content.split("\n")
            yaml_lines = []
            yaml_started = False
            yaml_ended = False
            
            for i, line in enumerate(lines):
                if i == 0 and line.strip() == "---":
                    yaml_started = True
                    continue
                
                if yaml_started and not yaml_ended:
                    if line.strip() == "---":
                        yaml_ended = True
                        break
                    else:
                        yaml_lines.append(line)
            
            if yaml_lines:
                yaml_content = "\n".join(yaml_lines)
                # 尝试解析，如果失败返回空字典
                try:
                    return yaml.safe_load(yaml_content) or {}
                except:
                    # 如果 YAML 解析失败，尝试简单提取关键字段
                    return self.extract_basic_fields(yaml_content)
        except Exception as e:
            # 静默失败，返回空字典
            pass
        
        return {}
    
    def extract_basic_fields(self, yaml_content):
        """从有问题的 YAML 中提取基本字段"""
        result = {}
        lines = yaml_content.split("\n")
        
        for line in lines:
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                
                # 处理常见字段
                if key in ["分类", "标签", "创建日期", "最后修改", "状态"]:
                    # 清理值
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    
                    # 特殊处理标签
                    if key == "标签" and value.startswith("[") and value.endswith("]"):
                        try:
                            # 简单解析列表
                            value = value[1:-1].split(",")
                            value = [v.strip().strip('"\'') for v in value if v.strip()]
                        except:
                            value = []
                    
                    result[key] = value
        
        return result
    
    def count_words(self, content):
        """粗略统计中文字数"""
        # 移除 YAML 前端
        if content.startswith("---\n"):
            parts = content.split("---\n", 2)
            if len(parts) >= 3:
                content = parts[2]
        
        # 统计中文字符（包括标点）
        chinese_chars = sum(1 for char in content if '\u4e00' <= char <= '\u9fff')
        # 统计英文单词（简单分割）
        english_words = len(content.split())
        
        return chinese_chars + english_words
    
    def analyze_note(self, filepath):
        """分析单个笔记文件"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 获取文件信息
            file_size = os.path.getsize(filepath)
            file_stat = os.stat(filepath)
            
            # 解析前端元数据
            frontmatter = self.parse_frontmatter(content)
            
            # 统计字数
            word_count = self.count_words(content)
            
            # 提取信息
            category = frontmatter.get("分类", "未分类")
            status = frontmatter.get("状态", "未知")
            tags = frontmatter.get("标签", [])
            create_date = frontmatter.get("创建日期", "")
            
            # 更新统计
            self.stats["total_notes"] += 1
            self.stats["total_size_kb"] += file_size / 1024
            self.stats["total_words"] += word_count
            
            # 分类统计
            cat_stats = self.stats["by_category"][category]
            cat_stats["count"] += 1
            cat_stats["size_kb"] += file_size / 1024
            cat_stats["words"] += word_count
            
            # 状态统计
            self.stats["by_status"][status] += 1
            
            # 时间统计
            if create_date:
                try:
                    date_obj = datetime.strptime(create_date, "%Y-%m-%d")
                    self.stats["by_year"][date_obj.year] += 1
                    self.stats["by_month"][f"{date_obj.year}-{date_obj.month:02d}"] += 1
                except:
                    pass
            
            # 标签统计
            if isinstance(tags, list):
                for tag in tags:
                    self.stats["tags"][tag] += 1
            
            # 记录分类
            self.stats["categories"].add(category)
            
            # 记录最近和最大的笔记
            note_info = {
                "path": str(filepath.relative_to(self.obsidian_root)),
                "size_kb": file_size / 1024,
                "words": word_count,
                "category": category,
                "status": status,
                "modified": datetime.fromtimestamp(file_stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                "created": create_date
            }
            
            self.stats["recent_notes"].append(note_info)
            self.stats["largest_notes"].append(note_info)
            
        except Exception as e:
            print(f"分析文件失败 {filepath}: {e}")
    
    def analyze_directory(self, directory=None):
        """分析整个目录"""
        if directory is None:
            directory = self.obsidian_root
        
        dir_path = Path(directory)
        
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".md"):
                    filepath = Path(root) / file
                    self.analyze_note(filepath)
        
        # 排序
        self.stats["recent_notes"].sort(key=lambda x: x["modified"], reverse=True)
        self.stats["largest_notes"].sort(key=lambda x: x["size_kb"], reverse=True)
        
        # 限制数量
        self.stats["recent_notes"] = self.stats["recent_notes"][:10]
        self.stats["largest_notes"] = self.stats["largest_notes"][:10]
    
    def generate_report(self):
        """生成分析报告"""
        report = {
            "summary": {
                "total_notes": self.stats["total_notes"],
                "total_size_mb": round(self.stats["total_size_kb"] / 1024, 2),
                "total_words_k": round(self.stats["total_words"] / 1000, 1),
                "avg_words_per_note": round(self.stats["total_words"] / max(self.stats["total_notes"], 1)),
                "categories_count": len(self.stats["categories"])
            },
            "by_category": {
                cat: {
                    "count": data["count"],
                    "size_mb": round(data["size_kb"] / 1024, 2),
                    "words_k": round(data["words"] / 1000, 1),
                    "percentage": round(data["count"] / max(self.stats["total_notes"], 1) * 100, 1)
                }
                for cat, data in sorted(
                    self.stats["by_category"].items(),
                    key=lambda x: x[1]["count"],
                    reverse=True
                )
            },
            "by_status": dict(sorted(self.stats["by_status"].items())),
            "by_year": dict(sorted(self.stats["by_year"].items())),
            "top_tags": dict(self.stats["tags"].most_common(20)),
            "recent_notes": self.stats["recent_notes"][:5],
            "largest_notes": self.stats["largest_notes"][:5],
            "categories": sorted(self.stats["categories"])
        }
        
        return report
    
    def print_markdown_report(self):
        """输出 Markdown 格式的报告"""
        report = self.generate_report()
        
        md = "# 📊 Obsidian 知识库分析报告\n\n"
        md += f"**分析时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        md += f"**分析目录**: {self.obsidian_root}\n\n"
        
        # 摘要
        md += "## 📈 知识库摘要\n\n"
        summary = report["summary"]
        md += f"- **笔记总数**: {summary['total_notes']} 篇\n"
        md += f"- **总大小**: {summary['total_size_mb']} MB\n"
        md += f"- **总字数**: {summary['total_words_k']}K 字\n"
        md += f"- **平均字数**: {summary['avg_words_per_note']} 字/篇\n"
        md += f"- **分类数量**: {summary['categories_count']} 个\n\n"
        
        # 分类统计
        md += "## 🗂️ 分类统计\n\n"
        md += "| 分类 | 笔记数 | 占比 | 大小 | 字数 |\n"
        md += "|------|--------|------|------|------|\n"
        
        for cat, data in report["by_category"].items():
            md += f"| {cat} | {data['count']} | {data['percentage']}% | {data['size_mb']}MB | {data['words_k']}K |\n"
        md += "\n"
        
        # 状态统计
        md += "## 📋 状态分布\n\n"
        for status, count in report["by_status"].items():
            percentage = round(count / summary['total_notes'] * 100, 1)
            md += f"- **{status}**: {count} 篇 ({percentage}%)\n"
        md += "\n"
        
        # 年度统计
        md += "## 📅 创建时间分布\n\n"
        md += "### 按年度\n"
        for year, count in report["by_year"].items():
            md += f"- **{year}年**: {count} 篇\n"
        md += "\n"
        
        # 热门标签
        md += "## 🏷️ 热门标签\n\n"
        for tag, count in report["top_tags"].items():
            md += f"- `{tag}`: {count} 次\n"
        md += "\n"
        
        # 最近更新
        md += "## 🔄 最近更新的笔记\n\n"
        for note in report["recent_notes"]:
            md += f"- **{note['path']}**\n"
            md += f"  - 分类: {note['category']}, 状态: {note['status']}\n"
            md += f"  - 大小: {note['size_kb']:.1f}KB, 字数: {note['words']}\n"
            md += f"  - 修改时间: {note['modified']}\n"
        md += "\n"
        
        # 最大笔记
        md += "## 📦 最大的笔记\n\n"
        for note in report["largest_notes"]:
            md += f"- **{note['path']}**\n"
            md += f"  - 大小: {note['size_kb']:.1f}KB, 字数: {note['words']}\n"
            md += f"  - 分类: {note['category']}\n"
        md += "\n"
        
        # 所有分类
        md += "## 📁 所有分类\n\n"
        for i, cat in enumerate(report["categories"], 1):
            md += f"{i}. {cat}\n"
        
        return md

def main():
    """主函数"""
    # 检查参数
    if len(sys.argv) > 1:
        obsidian_path = sys.argv[1]
    else:
        obsidian_path = "/var/minis/mounts/obsidian"
    
    try:
        print("开始分析 Obsidian 知识库...")
        analyzer = ObsidianAnalyzer(obsidian_path)
        analyzer.analyze_directory()
        
        # 生成报告
        report_md = analyzer.print_markdown_report()
        
        # 输出到文件
        output_file = f"obsidian_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_md)
        
        print(f"分析完成！报告已保存到: {output_file}")
        print("\n" + "="*50 + "\n")
        print(report_md[:2000])  # 预览前2000字符
        
    except Exception as e:
        print(f"分析失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()