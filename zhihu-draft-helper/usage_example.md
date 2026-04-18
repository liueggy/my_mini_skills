# 知乎草稿助手技能使用示例

## 场景：将本地Markdown文章发布到知乎

### 步骤1：准备内容文件
```markdown
# 我的技术文章

这是一篇关于Python异步编程的文章。

## 主要内容
- asyncio基础
- async/await语法
- 协程和任务
- 实际应用示例

## 代码示例
```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
```

---

*创建时间：2026年4月18日*
```

### 步骤2：使用技能创建草稿
当用户说："帮我把这篇文章发布到知乎"时，技能会自动触发。

技能会执行以下操作：

1. **检查工具文件**：确认`zhihu_draft_tool.py`存在
2. **获取Cookie**：使用浏览器获取知乎登录状态
3. **创建草稿**：调用API创建新草稿
4. **返回结果**：提供草稿ID和编辑链接

### 步骤3：网页端发布
技能会指导用户在浏览器中完成最终发布：
1. 打开编辑页面：`https://zhuanlan.zhihu.com/p/{草稿ID}/edit`
2. 添加话题和封面图（可选）
3. 点击"发布"按钮
4. 验证发布状态

## 实际命令示例

### 获取Cookie
```bash
browser_use navigate --url https://zhuanlan.zhihu.com/write
browser_use get_cookies
# 环境文件：/var/minis/offloads/env_cookies_zhihu_com_*.sh
```

### 创建草稿
```bash
cd /var/minis/shared/my_mini_skills/zhihu-draft-tool
./zhihu_draft_tool_wrapper.sh create \
  --base-id 2028607956032176996 \
  --title "Python异步编程入门" \
  --content-file python_async.md \
  --summary "Python asyncio模块的入门指南，包含基础概念和代码示例。" \
  --comment-permission all
```

### 网页发布
```bash
browser_use navigate --url https://zhuanlan.zhihu.com/p/2028871642558787933/edit
browser_use wait_for_dom_stable --timeout 10
browser_use click --selector .Button--primary.Button--blue
```

## 技能触发关键词

当用户提到以下内容时，技能会自动触发：

- "知乎发文"、"知乎发布文章"
- "知乎草稿"、"知乎编辑文章"
- "知乎API"、"知乎直连发布"
- "知乎草稿工具"、"知乎内容同步"
- "绕过知乎编辑器"、"知乎批量发布"
- "帮我发一篇知乎测试文章"
- "帮我在知乎上操作网页"

## 技能优势

### 1. 绕过编辑器限制
- 直接操作API，避免富文本编辑器问题
- 支持批量操作
- 格式转换更稳定

### 2. 自动化程度高
- 从文件读取内容
- 自动设置元数据
- 提供完整工作流

### 3. 已验证可用
- 在实际环境中测试通过
- 包含完整的错误处理
- 有实际成功案例

## 注意事项

1. **Cookie有效期**：知乎Cookie可能过期，需要重新获取
2. **审核机制**：新内容可能需要审核时间
3. **API限制**：避免高频请求
4. **内容合规**：遵守知乎社区规范

## 扩展使用

### 批量发布
```bash
# 批量处理多个Markdown文件
for file in articles/*.md; do
  title=$(basename "$file" .md)
  ./zhihu_draft_tool_wrapper.sh create \
    --base-id 2028607956032176996 \
    --title "$title" \
    --content-file "$file"
done
```

### 内容同步
- 从CSDN、博客园等平台同步内容
- 保持格式一致性
- 自动化更新已发布内容

### API集成
- 集成到自动化发布流水线
- 作为内容管理系统的组件
- 提供RESTful API接口