---
name: wechat-article-fetcher
description: 抓取微信公众号文章内容并提取结构化摘要。Use when user shares a mp.weixin.qq.com link and wants the article content extracted, summarized, or analyzed. Also use when needing to fetch and archive WeChat articles for reference.
---

# 微信公众号文章抓取

## 问题

微信公众号文章（mp.weixin.qq.com）通过 web_fetch 通常只能获取标题，正文被 JS 渲染屏蔽。

## 解决方案

### 方案1：请求用户辅助（推荐）

微信文章内容无法直接抓取时，请用户：
- 截图发送（OCR 可读）
- 复制正文文字粘贴发送
- 使用微信"收藏"后导出

### 方案2：尝试 web_fetch

```
web_fetch(url, maxChars=30000)
```

有时能获取部分内容，但不稳定。标题和公众号名称通常可获取。

### 方案3：使用浏览器自动化

如果有 Agent Browser skill，可尝试：
1. 打开 URL
2. 等待页面加载
3. snapshot 获取正文内容

## 获取后的处理

1. **提取结构化信息**：标题、作者、日期、核心观点
2. **生成摘要**：300字以内
3. **归档**：保存到飞书文档或本地 markdown
4. **关联分析**：与当前工作上下文关联

## 注意事项

- 微信文章有防爬机制，web_fetch 成功率约 30%
- 优先请用户辅助，效率最高
- 版权内容仅用于内部参考，不要原文公开发布
