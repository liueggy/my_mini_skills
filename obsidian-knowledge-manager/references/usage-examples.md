# Obsidian 知识库管理技能使用示例

## 🚀 快速开始

### 基本使用流程
1. **触发技能**：当你说出相关关键词时，技能自动触发
2. **选择功能**：根据你的需求选择相应功能
3. **提供参数**：根据需要提供主题、分类等信息
4. **执行操作**：技能自动执行并返回结果
5. **验证结果**：在 Obsidian 中查看生成或修改的笔记

### 触发关键词
- "创建 Obsidian 笔记"
- "管理我的知识库"
- "分析笔记结构"
- "批量更新标签"
- "生成学习笔记"
- "整理 Obsidian"
- "知识库统计"
- "笔记模板"

## 📝 使用示例

### 示例1：创建新的知识笔记
**用户请求**：
```
帮我创建一个关于 Python 异步编程的知识笔记
```

**技能执行步骤**：
1. 确定分类：`工具/Python`
2. 选择模板：`knowledge-base.md`
3. 填充元数据：
   - 分类：编程
   - 标签：[Python, 异步, 编程]
   - 状态：进行中
4. 生成结构化内容
5. 保存到：`知识库/工具/Python异步编程.md`

**生成的笔记**：
```markdown
---
分类: 编程
标签: [Python, 异步, 编程]
创建日期: 2026-04-16
最后修改: 2026-04-16
状态: 进行中
---
> [!note] 📝
> Python 异步编程
> Python 异步编程的核心概念和使用方法。

## 1. 这是什么

Python 异步编程是一种**非阻塞的编程模式**，常用于处理 I/O 密集型任务，如网络请求、文件操作等。

你可以把它理解成：

- **单线程并发**：在单个线程中处理多个任务
- **事件驱动**：基于事件循环调度任务
- **协程协作**：任务间主动让出控制权

它解决的是"如何高效处理大量 I/O 操作而不阻塞主线程"的问题。
```

### 示例2：批量更新标签
**用户请求**：
```
给所有 Linux 笔记添加"系统"标签
```

**技能执行步骤**：
1. 查找所有 Linux 目录下的笔记
2. 读取每个笔记的 YAML 前端
3. 在标签列表中添加"系统"
4. 使用 `file_edit` 更新
5. 统计更新数量

**执行命令**：
```bash
# 查找 Linux 笔记
find /var/minis/mounts/obsidian/main/知识库/Linux -name "*.md"

# 批量更新标签
for file in $(find /var/minis/mounts/obsidian/main/知识库/Linux -name "*.md"); do
  # 读取当前标签
  # 添加新标签
  # 更新文件
done
```

### 示例3：分析知识库结构
**用户请求**：
```
分析我的知识库结构，生成报告
```

**技能执行步骤**：
1. 运行分析脚本：`analyze-structure.py`
2. 生成统计报告
3. 输出 Markdown 格式结果
4. 提供改进建议

**生成的报告**：
```markdown
# 📊 Obsidian 知识库分析报告

**分析时间**: 2026-04-16 01:30:00
**分析目录**: /var/minis/mounts/obsidian

## 📈 知识库摘要
- **笔记总数**: 14 篇
- **总大小**: 0.34 MB
- **总字数**: 85.7K 字
- **平均字数**: 6122 字/篇
- **分类数量**: 4 个

## 🗂️ 分类统计
| 分类 | 笔记数 | 占比 | 大小 | 字数 |
|------|--------|------|------|------|
| 未分类 | 8 | 57.1% | 0.25MB | 65.2K |
| 命令工具 | 3 | 21.4% | 0.06MB | 6.6K |
| 操作系统 | 1 | 7.1% | 0.02MB | 5.6K |
| 人工智能 | 1 | 7.1% | 0.01MB | 2.4K |
```

### 示例4：创建学习笔记
**用户请求**：
```
我刚学习了 Docker 网络，帮我创建学习笔记
```

**技能执行步骤**：
1. 确定分类：`工具/Docker`
2. 选择模板：`learning-note.md`
3. 填充学习信息：
   - 学习来源：官方文档
   - 学习时间：2小时
   - 掌握程度：7/10
4. 生成学习记录
5. 保存到：`知识库/工具/Docker网络学习笔记.md`

### 示例5：创建项目文档
**用户请求**：
```
为我的新项目"智能家居系统"创建项目文档
```

**技能执行步骤**：
1. 确定位置：`项目/智能家居系统/`
2. 选择模板：`project-doc.md`
3. 填充项目信息：
   - 项目类型：物联网
   - 技术栈：[Python, MQTT, Home Assistant]
   - 负责人：我
4. 生成完整项目文档结构
5. 保存到：`项目/智能家居系统/README.md`

## 🔧 高级用法

### 自定义模板使用
```bash
# 使用自定义模板创建笔记
python3 create_note.py \
  --template custom-template.md \
  --title "我的笔记" \
  --category "自定义" \
  --tags "标签1,标签2" \
  --output /path/to/note.md
```

### 批量操作示例
```bash
# 批量更新所有笔记的"最后修改"日期
find /var/minis/mounts/obsidian -name "*.md" -exec sh -c '
  file="$1"
  today=$(date +%Y-%m-%d)
  sed -i "s/最后修改:.*/最后修改: $today/" "$file"
' _ {} \;

# 批量添加标签
find /var/minis/mounts/obsidian -name "*.md" -exec sh -c '
  file="$1"
  if grep -q "标签:" "$file"; then
    sed -i '/标签:/s/\]/, 新标签\]/' "$file"
  fi
' _ {} \;
```

### 自动化工作流
```python
# 自动整理新笔记的脚本
import os
from pathlib import Path

def organize_new_notes():
    """整理收件箱中的新笔记"""
    inbox = Path("/var/minis/mounts/obsidian/main/收件箱")
    
    for note in inbox.glob("*.md"):
        # 分析内容确定分类
        category = analyze_category(note)
        
        # 移动到对应目录
        target_dir = Path(f"/var/minis/mounts/obsidian/main/知识库/{category}")
        target_dir.mkdir(exist_ok=True)
        
        # 更新元数据
        update_metadata(note, category)
        
        # 移动文件
        note.rename(target_dir / note.name)
```

## 📁 文件位置参考

### 技能文件位置
```
/var/minis/skills/obsidian-knowledge-manager/
├── SKILL.md                    # 主技能文件
├── templates/                  # 笔记模板
│   ├── knowledge-base.md      # 知识库笔记模板
│   ├── learning-note.md       # 学习笔记模板
│   ├── project-doc.md         # 项目文档模板
│   └── daily-note.md          # 日常笔记模板
├── scripts/                   # 实用脚本
│   ├── analyze-structure.py   # 知识库结构分析
│   └── test-skill.py          # 技能测试脚本
└── references/                # 参考文档
    ├── directory-structure.md # 目录结构说明
    ├── metadata-schema.md     # 元数据规范
    └── usage-examples.md      # 使用示例（本文档）
```

### 用户知识库位置
```
/var/minis/mounts/obsidian/    # Obsidian 根目录
└── main/                      # 主知识库
    ├── 知识库/                # 核心知识存储
    ├── 项目/                  # 项目文档
    ├── 日记/                  # 日常记录
    ├── 收件箱/                # 临时收集
    └── ...                    # 其他目录
```

## 🚨 故障排除

### 常见问题

#### Q1：技能没有触发？
A：检查是否使用了正确的触发关键词，或直接说"使用 Obsidian 技能"。

#### Q2：文件写入失败？
A：检查 Obsidian 目录权限，确保 `/var/minis/mounts/obsidian/` 可写。

#### Q3：模板变量没有替换？
A：模板中的 `{{变量名}}` 需要在创建笔记时提供具体值。

#### Q4：分析脚本报错？
A：确保已安装 Python 和 py3-yaml 模块：
```bash
apk add python3 py3-yaml
```

#### Q5：链接不工作？
A：Obsidian 内部链接使用 `[[笔记名称]]` 语法，确保笔记存在。

### 调试技巧
```bash
# 检查目录权限
ls -la /var/minis/mounts/obsidian/

# 测试文件写入
echo "测试" > /var/minis/mounts/obsidian/test.txt && rm /var/minis/mounts/obsidian/test.txt

# 检查 Python 环境
python3 --version
python3 -c "import yaml; print('YAML 模块正常')"
```

## 📈 最佳实践

### 笔记创建
1. **先规划后创建**：确定分类、标签、结构再创建
2. **使用模板**：保持格式一致性
3. **及时更新**：修改后更新最后修改日期
4. **添加链接**：建立知识关联

### 知识库维护
1. **定期分析**：每月分析知识库结构
2. **批量整理**：使用脚本批量处理重复任务
3. **备份重要**：操作前备份关键笔记
4. **渐进优化**：不要一次性大改，逐步优化

### 技能使用
1. **明确需求**：清楚说明要做什么
2. **提供上下文**：说明笔记用途和受众
3. **检查结果**：在 Obsidian 中验证生成内容
4. **反馈改进**：提出改进建议

## 🔮 未来扩展

### 计划功能
1. **智能分类**：基于内容自动分类
2. **知识图谱**：可视化知识关联
3. **学习计划**：生成个性化学习路径
4. **内容推荐**：推荐相关学习资源
5. **多库同步**：支持多个 Obsidian 库

### 集成可能
1. **Git 集成**：自动提交和版本控制
2. **API 集成**：与外部服务集成
3. **导出功能**：导出为 PDF、HTML 等格式
4. **分享功能**：一键分享到博客或社区

---

**最后更新**：2026-04-16
**技能版本**：1.0.0
**示例状态**：已完成