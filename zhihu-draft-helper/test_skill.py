#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知乎草稿助手技能测试脚本
测试技能是否正常加载和基本功能
"""

import os
import sys

def test_skill_files():
    """测试技能文件是否存在"""
    skill_dir = "/var/minis/skills/zhihu-draft-helper"
    files_to_check = [
        ("SKILL.md", "主技能文件"),
    ]
    
    print("=== 知乎草稿助手技能测试 ===")
    print(f"技能目录: {skill_dir}")
    print()
    
    all_ok = True
    for filename, description in files_to_check:
        filepath = os.path.join(skill_dir, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"✅ {description}: {filename} ({size} bytes)")
        else:
            print(f"❌ {description}: {filename} (文件不存在)")
            all_ok = False
    
    # 检查技能描述
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    if os.path.exists(skill_md_path):
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read(500)  # 读取前500字符
            
        # 检查YAML frontmatter
        if content.startswith('---'):
            print("✅ 技能文件格式: 包含YAML frontmatter")
        else:
            print("⚠️  技能文件格式: 可能缺少YAML frontmatter")
            
        # 检查关键内容
        keywords = ["zhihu-draft-helper", "知乎", "草稿", "API"]
        found_keywords = [kw for kw in keywords if kw in content]
        print(f"✅ 关键词检查: 找到 {len(found_keywords)}/{len(keywords)} 个关键词")
    
    print()
    print("=== 工具文件检查 ===")
    
    # 检查GitHub仓库中的工具文件
    tool_dir = "/var/minis/shared/my_mini_skills/zhihu-draft-tool"
    if os.path.exists(tool_dir):
        tool_files = os.listdir(tool_dir)
        print(f"✅ 工具目录存在: {tool_dir}")
        print(f"   包含文件: {len(tool_files)} 个")
        for file in sorted(tool_files)[:5]:  # 显示前5个文件
            print(f"   - {file}")
    else:
        print(f"⚠️  工具目录不存在: {tool_dir}")
        all_ok = False
    
    print()
    if all_ok:
        print("✅ 技能测试通过！")
        return 0
    else:
        print("⚠️  技能测试发现一些问题")
        return 1

if __name__ == "__main__":
    sys.exit(test_skill_files())