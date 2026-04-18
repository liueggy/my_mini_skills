# 知乎草稿直连发布器

一个绕过知乎富文本编辑器，直接通过API操作草稿的工具。

## 功能特性

- ✅ **草稿创建**：通过API直接创建新草稿
- ✅ **草稿读取**：获取草稿完整信息（标题、内容、设置等）
- ✅ **草稿更新**：更新标题、内容、摘要、评论权限等
- ⚠️ **正式发布**：仍需在网页端点击"发布"按钮完成最终发布

## 已验证的API接口

1. `POST /api/v4/editor/default-settings` - 创建草稿
2. `GET /api/v4/editor/default-settings?content_token={id}` - 读取草稿
3. `PATCH /api/v4/editor/default-settings?content_token={id}` - 更新草稿

## 快速开始

### 1. 获取知乎Cookie
```bash
# 在浏览器中登录知乎，然后获取Cookie
# 使用浏览器工具获取cookie环境文件
```

### 2. 使用包装脚本
```bash
# 创建草稿
./zhihu_draft_tool_wrapper.sh create \
  --base-id 2028607956032176996 \
  --title "文章标题" \
  --content-file content.md \
  --summary "文章摘要" \
  --comment-permission all

# 更新草稿
./zhihu_draft_tool_wrapper.sh update \
  --id 2028871642558787933 \
  --title "新标题"

# 获取草稿
./zhihu_draft_tool_wrapper.sh get --id 2028871642558787933
```

### 3. 直接使用Python脚本
```bash
python3 zhihu_draft_tool.py create \
  --cookie "your_cookie_string" \
  --base-id 2028607956032176996 \
  --title "标题" \
  --content-file content.md
```

## 文件说明

- `zhihu_draft_tool.py` - 主工具脚本
- `zhihu_draft_tool_wrapper.sh` - 包装脚本（自动加载cookie）
- `docs/` - API分析文档
  - `zhihu_publish_context.txt` - 发布接口上下文分析
  - `zhihu_publish_fields.txt` - 发布字段分析

## 测试结果

### 成功验证的功能
1. **草稿创建** - 创建了测试草稿（ID: `2028867948278822109`）
2. **草稿读取** - 成功获取草稿完整信息
3. **草稿更新** - 成功更新标题和设置
4. **文件同步** - 支持从Markdown文件读取内容

### 实际应用案例
将CSDN上发布的大学随记《不是每一天都闪闪发光，但也都算数》同步到知乎草稿：
- 草稿ID: `2028871642558787933`
- 编辑链接: https://zhuanlan.zhihu.com/p/2028871642558787933/edit

### 限制说明
- 需要有效的知乎登录Cookie
- 需要提供一个基础草稿ID作为模板
- 最终发布仍需在网页端完成
- 新账号发布可能需要审核

## 技术原理

### 绕过编辑器限制
知乎的富文本编辑器（DraftEditor）对前端状态管理严格，通过DOM写入或模拟输入难以激活发布按钮。本工具直接调用后端API，完全绕过前端编辑器。

### API逆向过程
1. 通过浏览器开发者工具监控网络请求
2. 分析知乎前端JS包（`column.app.js`）
3. 定位草稿操作接口
4. 还原请求参数结构

### 已知的发布接口
正式发布接口为 `POST /api/v4/content/publish`，但请求体结构复杂，包含多层嵌套对象。当前工具专注于已验证可用的草稿API。

## 使用场景

1. **批量内容发布** - 自动化创建多个草稿
2. **内容同步** - 将本地Markdown文件同步到知乎
3. **绕过编辑器限制** - 避免与富文本编辑器交互
4. **API集成** - 作为其他工具的组件

## 注意事项

1. **Cookie安全** - 不要分享或泄露Cookie
2. **使用频率** - 避免高频请求，防止被封禁
3. **内容审核** - 知乎对内容有审核机制
4. **基础ID** - 需要有效的草稿ID作为模板

## 许可证

MIT License