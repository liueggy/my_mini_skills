# 🚀 my_mini_skills

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/liueggy/my_mini_skills?style=flat&color=4f46e5)
![GitHub stars](https://img.shields.io/github/stars/liueggy/my_mini_skills?style=flat&color=f59e0b)
![GitHub forks](https://img.shields.io/github/forks/liueggy/my_mini_skills?style=flat&color=10b981)
![License](https://img.shields.io/github/license/liueggy/my_mini_skills?style=flat&color=6b7280)

**用于存放自定义 Minis / OpenMini 技能文件的个人仓库**

</div>

---

## 📦 技能列表

<div align="center">

| 技能 | 描述 | 场景 |
|:---:|:---|:---|
| ![ROS](https://img.shields.io/badge/-ROS-228B22?style=flat) | **ROS / ROS2** | 机器人中间件、导航、SLAM、URDF、rviz、gazebo |
| ![STM32](https://img.shields.io/badge/-STM32-03234B?style=flat) | **STM32 嵌入式** | 裸机/HAL、驱动开发、FreeRTOS、HardFault 排障 |
| ![DOCX](https://img.shields.io/badge/-DOCX-2B579A?style=flat) | **Word 文档** | .docx 创建/编辑/分析、模板、排版、图表 |
| ![PDF](https://img.shields.io/badge/-PDF-F40F2B?style=flat) | **PDF 处理** | 读取、合并、拆分、填充表单、水印、OCR |
| ![Obsidian](https://img.shields.io/badge/-Obsidian-7C3AED?style=flat) | **知识管理** | Obsidian 笔记结构、元数据、模板、工作流 |
| ![Skill](https://img.shields.io/badge/-Skill%20Creator-EC4899?style=flat) | **技能创建** | 编写 SKILL.md、触发词设计、示例编写 |
| ![GitHub](https://img.shields.io/badge/-GitHub%20Sync-181717?style=flat) | **GitHub 同步** | 仓库同步、自动化、工作流 |
| ![Self-Improving](https://img.shields.io/badge/-Self%20Improving-F59E0B?style=flat) | **自改进代理** | 学习日志、错误记录、功能请求追踪 |

</div>

---

## 📂 目录结构

```
my_mini_skills/
├── README.md                    # ← 你在这里
│
├── 📁 ros/                      # 🤖 ROS 技能
│   ├── SKILL.md
│   └── references/
│       ├── noetic-workspace-guide.md
│       ├── noetic-cli-cheatsheet.md
│       ├── common-errors.md
│       └── architecture-patterns.md
│
├── 📁 stm32-embedded/           # 🔧 STM32 嵌入式技能
│   ├── SKILL.md
│   └── references/
│       ├── uart-spi-i2c-debug-checklist.md
│       ├── hardfault-debug-guide.md
│       └── common-stm32-pitfalls.md
│
├── 📁 docx/                     # 📝 Word 文档技能
│   ├── SKILL.md
│   ├── LICENSE.txt
│   └── scripts/
│       ├── office/validators/
│       └── templates/
│
├── 📁 pdf/                      # 📄 PDF 处理技能
│   ├── SKILL.md
│   ├── LICENSE.txt
│   ├── reference.md
│   ├── forms.md
│   └── scripts/
│
├── 📁 obsidian-knowledge-manager/  # 📚 Obsidian 知识管理
│   ├── SKILL.md
│   ├── templates/
│   ├── scripts/
│   └── references/
│
├── 📁 skill-creator/            # ✨ 技能创建指南
│   └── SKILL.md
│
├── 📁 self-improving-agent/     # 🧠 自改进代理
│   ├── SKILL.md
│   ├── scripts/
│   └── data/
│
├── 📁 pdf/                      # 🔄 PDF 处理
│
├── 📁 find-skills/              # 🔍 技能发现
│
└── 📁 example-skill/            # 📋 示例模板
    ├── SKILL.md
    ├── templates/
    ├── scripts/
    └── examples/
```

---

## 🎯 快速开始

### 1. 使用已有技能

当你在 AI 对话中提到相关关键词时，技能会自动触发：

```markdown
"帮我写一个 ROS publisher"        → 自动触发 ros 技能
"STM32 UART 怎么配置"             → 自动触发 stm32-embedded 技能
"创建一个 Word 报告"              → 自动触发 docx 技能
"PDF 怎么合并"                    → 自动触发 pdf 技能
```

### 2. 添加新技能

```bash
# 1. 克隆仓库到本地
gh repo clone liueggy/my_mini_skills /var/minis/skills/

# 2. 创建新技能目录
mkdir -p my-new-skill/{templates,scripts,examples}

# 3. 编写 SKILL.md
cat > my-new-skill/SKILL.md << 'EOF'
---
name: my-new-skill
description: 技能描述，触发关键词
---

# 我的新技能

## 用途说明
...
EOF
```

---

## 📖 技能规范

每个技能目录推荐结构：

```
<skill-name>/
├── SKILL.md           # ✅ 必需：技能主说明文件
├── templates/         # 可选：模板文件
├── scripts/           # 可选：辅助脚本
├── examples/          # 可选：使用示例
└── references/        # 可选：参考资料
```

### SKILL.md 必须包含

```yaml
---
name: <skill-name>           # 技能名称（英文小写）
description: <description>    # 触发场景描述
---
```

---

## 🤝 贡献

欢迎提交 PR 或 Issue！

1. Fork 本仓库
2. 创建新技能分支：`git checkout -b skill/your-skill-name`
3. 遵循目录结构规范
4. 提交并推送
5. 创建 Pull Request

---

## 📜 License

MIT License - 查看 [LICENSE](LICENSE) 了解更多

---

<div align="center">

Made with ❤️ by [liueggy](https://github.com/liueggy)

</div>