#!/usr/bin/env python3
"""
Obsidian 知识库管理技能测试脚本
测试技能的基本功能
"""

import os
import sys
import tempfile
from pathlib import Path

def test_file_operations():
    """测试文件操作功能"""
    print("🧪 测试文件操作功能...")
    
    # 测试路径
    test_dir = Path("/var/minis/mounts/obsidian/main/测试目录")
    test_file = test_dir / "测试文件.md"
    
    try:
        # 创建测试目录
        test_dir.mkdir(exist_ok=True)
        print(f"  ✅ 创建目录: {test_dir}")
        
        # 创建测试文件
        content = """---
分类: 测试
标签: [测试, 技能]
创建日期: 2026-04-16
最后修改: 2026-04-16
状态: 测试中
---

# 测试文件

这是一个测试文件，用于验证技能的文件操作功能。

## 测试内容

- 功能1: 文件创建
- 功能2: 文件读取
- 功能3: 文件编辑

> 测试完成时间: 2026-04-16
"""
        
        test_file.write_text(content, encoding='utf-8')
        print(f"  ✅ 创建文件: {test_file}")
        
        # 读取文件
        read_content = test_file.read_text(encoding='utf-8')
        assert "测试文件" in read_content
        print("  ✅ 读取文件成功")
        
        # 检查文件大小
        file_size = test_file.stat().st_size
        print(f"  ✅ 文件大小: {file_size} 字节")
        
        # 清理测试文件
        test_file.unlink()
        test_dir.rmdir()
        print("  ✅ 清理测试文件")
        
        return True
        
    except Exception as e:
        print(f"  ❌ 文件操作测试失败: {e}")
        return False

def test_template_loading():
    """测试模板加载功能"""
    print("\n🧪 测试模板加载功能...")
    
    template_dir = Path("/var/minis/skills/obsidian-knowledge-manager/templates")
    
    try:
        # 检查模板文件
        templates = list(template_dir.glob("*.md"))
        print(f"  ✅ 找到 {len(templates)} 个模板文件:")
        
        for template in templates:
            size = template.stat().st_size
            print(f"    - {template.name} ({size} 字节)")
            
            # 检查模板内容
            content = template.read_text(encoding='utf-8')
            assert "{{" in content  # 应该包含模板变量
            assert "}}" in content
        
        # 检查特定模板
        kb_template = template_dir / "knowledge-base.md"
        if kb_template.exists():
            content = kb_template.read_text(encoding='utf-8')
            assert "{{TITLE}}" in content
            assert "{{CATEGORY}}" in content
            print("  ✅ 知识库模板格式正确")
        
        return True
        
    except Exception as e:
        print(f"  ❌ 模板加载测试失败: {e}")
        return False

def test_script_execution():
    """测试脚本执行功能"""
    print("\n🧪 测试脚本执行功能...")
    
    script_dir = Path("/var/minis/skills/obsidian-knowledge-manager/scripts")
    
    try:
        # 检查分析脚本
        analyze_script = script_dir / "analyze-structure.py"
        if analyze_script.exists():
            # 检查脚本权限
            if os.access(analyze_script, os.X_OK):
                print("  ✅ 分析脚本有执行权限")
            else:
                print("  ⚠️  分析脚本无执行权限，尝试修复...")
                analyze_script.chmod(0o755)
                print("  ✅ 已修复脚本权限")
            
            # 检查脚本内容
            content = analyze_script.read_text(encoding='utf-8')
            assert "ObsidianAnalyzer" in content
            assert "parse_frontmatter" in content
            print("  ✅ 分析脚本内容完整")
        
        return True
        
    except Exception as e:
        print(f"  ❌ 脚本执行测试失败: {e}")
        return False

def test_reference_docs():
    """测试参考文档"""
    print("\n🧪 测试参考文档...")
    
    ref_dir = Path("/var/minis/skills/obsidian-knowledge-manager/references")
    
    try:
        # 检查参考文档
        ref_files = list(ref_dir.glob("*.md"))
        print(f"  ✅ 找到 {len(ref_files)} 个参考文档:")
        
        for ref_file in ref_files:
            size = ref_file.stat().st_size
            lines = len(ref_file.read_text(encoding='utf-8').split('\n'))
            print(f"    - {ref_file.name} ({size} 字节, {lines} 行)")
            
            # 检查内容
            content = ref_file.read_text(encoding='utf-8')
            assert len(content) > 100  # 文档应该有一定长度
        
        # 检查特定文档
        if (ref_dir / "directory-structure.md").exists():
            content = (ref_dir / "directory-structure.md").read_text(encoding='utf-8')
            assert "目录结构" in content
            print("  ✅ 目录结构文档内容完整")
        
        return True
        
    except Exception as e:
        print(f"  ❌ 参考文档测试失败: {e}")
        return False

def test_skill_main_file():
    """测试主技能文件"""
    print("\n🧪 测试主技能文件...")
    
    skill_file = Path("/var/minis/skills/obsidian-knowledge-manager/SKILL.md")
    
    try:
        # 检查文件存在
        assert skill_file.exists()
        print("  ✅ 主技能文件存在")
        
        # 检查文件大小
        size = skill_file.stat().st_size
        print(f"  ✅ 文件大小: {size} 字节")
        
        # 检查内容
        content = skill_file.read_text(encoding='utf-8')
        
        # 检查 YAML 前端
        assert content.startswith("---\n")
        assert "name: obsidian-knowledge-manager" in content
        assert "description:" in content
        print("  ✅ YAML 前端格式正确")
        
        # 检查技能描述
        assert "Obsidian" in content
        assert "知识库" in content
        print("  ✅ 技能描述完整")
        
        # 检查功能说明
        assert "核心功能" in content
        assert "使用指南" in content
        print("  ✅ 功能说明完整")
        
        return True
        
    except Exception as e:
        print(f"  ❌ 主技能文件测试失败: {e}")
        return False

def main():
    """运行所有测试"""
    print("🚀 开始测试 Obsidian 知识库管理技能")
    print("=" * 50)
    
    tests = [
        ("文件操作", test_file_operations),
        ("模板加载", test_template_loading),
        ("脚本执行", test_script_execution),
        ("参考文档", test_reference_docs),
        ("主技能文件", test_skill_main_file),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"  ❌ {test_name} 测试异常: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("📊 测试结果汇总:")
    
    passed = 0
    total = len(results)
    
    for test_name, success in results:
        status = "✅ 通过" if success else "❌ 失败"
        print(f"  {status} - {test_name}")
        if success:
            passed += 1
    
    print(f"\n🎯 测试完成: {passed}/{total} 项测试通过")
    
    if passed == total:
        print("🌟 所有测试通过！技能创建成功！")
        return 0
    else:
        print("⚠️  部分测试失败，请检查问题")
        return 1

if __name__ == "__main__":
    sys.exit(main())