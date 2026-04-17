# my_mini_skills

用于存放我自己创建的 Minis / OpenMini 技能文件。

## 目录约定

每个技能使用一个独立目录，推荐结构如下：

```text
<skill-name>/
├── SKILL.md
├── templates/
├── scripts/
└── examples/
```

其中：
- `SKILL.md`：技能主说明文件，必须存在
- `templates/`：模板文件，可选
- `scripts/`：辅助脚本，可选
- `examples/`：示例文件，可选

## 推荐做法

1. 一个技能一个目录
2. 技能目录名尽量使用英文、小写、短横线命名
3. 在 `SKILL.md` 中写清楚：用途、触发场景、输入输出约定、示例
4. 如果技能依赖额外脚本或模板，也一起放到对应目录下
5. 用 Git 维护版本，方便后续同步到本地 `/var/minis/skills/`

## 示例技能

仓库已附带一个示例技能目录：`example-skill/`

你可以直接复制它作为新技能模板。
