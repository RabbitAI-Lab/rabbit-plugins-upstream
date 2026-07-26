---
name: kepler-agent-search
description: >
  从多个平台搜索内容，实现统一搜索和内容提取，帮助AI Agent获取全网信息。
  支持 Bing 通用搜索、知乎中文问答社区搜索、小红书生活方式社区搜索。
  务必使用此 skill 当用户需要：搜索网络信息、查询知乎内容、浏览小红书种草笔记、多源搜索对比、
  获取最新资讯、调研某个主题、查找资料、提取网页文章、搜索中文知识问答、探索生活方式分享等。
  即使用户没有明确说"搜索"或"skill"，只要涉及获取网络信息的需求，都应使用此 skill。
compatibility: Requires mcp__kepler__web_search and mcp__kepler__web_reader tools
---

## 前置要求

本技能依赖 **Kepler MCP 服务**，使用前需配置 MCP 服务器。

**快速配置**：
```json
{
  "mcpServers": {
    "kepler": {
      "type": "sse",
      "url": "https://apisec.cn/sse",
      "headers": { "Authorization": "Bearer <API-KEY>" }
    }
  }
}
```

📖 **[完整安装指南](references/mcp-setup.md)** — 支持 Claude Code、OpenClaw、Codex 等多个 Agent 平台

## 常驻规则（全程适用）

1. **数据源选择策略**：
   - 通用问题 → 使用 Bing 搜索
   - 中文知识问答/经验分享 → 优先搜索知乎
   - 生活方式/种草/攻略/消费决策 → 优先搜索小红书 (xhs)
   - 综合调研 → 多数据源并行搜索

2. **搜索优先原则**：涉及时效性内容（新闻、最新动态）时，先用 web_search 获取最新信息，不要依赖训练数据。

3. **知乎/小红书内容特殊处理**：
   - 优先使用知乎/小红书搜索，遇到不可用的时候可以降级为通用搜索，关键词需要加上 "site:zhihu.com" 或 "site:xiaohongshu.com"
   - 知乎文章/回答可以直接使用 web_reader 读取完整内容
   - 小红书笔记支持内容提取，可直接使用 web_reader 读取

4. **参数规范**（重点！engines 参数每次只能指定单个引擎）：
   - web_search: `query` (必填), `engines` (可选, 默认 ['bing'], 可选值: ['bing'], ['zhihu'], ['xhs']), `max_results` (可选, 默认10, 最大50)
   - web_reader: `url` (必填), `format` (可选, markdown/text/html, 默认 markdown), `extract_article` (可选, 默认 true)

## 搜索路由表

| 用户意图 | 推荐策略 | 工具 | 参数示例 |
|---------|---------|------|---------|
| 通用搜索 | Bing 搜索 | mcp__kepler__web_search | `engines: ["bing"]` |
| 知乎搜索 | 指定 zhihu 引擎 | mcp__kepler__web_search | `engines: ["zhihu"]` |
| 小红书搜索 | 指定 xhs 引擎 | mcp__kepler__web_search | `engines: ["xhs"]` |
| 多源对比 | 依次执行多个引擎 | mcp__kepler__web_search | 先 `engines: ["bing"]` 再 `engines: ["zhihu"]` 再 `engines: ["xhs"]` |
| 读取网页 | 直接访问 URL | mcp__kepler__web_reader | `url: "..."` |
| 深度调研 | 搜索 → 读取 → 分析 | 两者组合 | - |

## 搜索模式

### 模式一：单源搜索

**Bing 通用搜索：**
```
用户：「搜索 Python 异步编程最佳实践」
→ 调用 web_search，query="Python 异步编程最佳实践"
```

**知乎定向搜索（使用 engines 参数）：**
```
用户：「知乎上关于 Python 异步编程的讨论」
→ 调用 web_search，query="Python 异步编程", engines=["zhihu"]
```

**知乎定向搜索（使用关键词）：**
```
用户：「知乎上关于 Python 异步编程的讨论」
→ 调用 web_search，query="Python 异步编程 site:zhihu.com" 或 "Python 异步编程 知乎"
```

### 模式二：多引擎搜索（推荐！）

**同时使用 Bing、知乎和小红书搜索：**
```
用户：「搜索 Python 异步编程」
→ 依次执行三次搜索：
   1. 调用 web_search，query="Python 异步编程", engines=["bing"]
   2. 调用 web_search，query="Python 异步编程", engines=["zhihu"]
   3. 调用 web_search，query="Python 异步编程", engines=["xhs"]
→ 自动返回来自 Bing、知乎和小红书的综合结果

注意：多引擎搜索只能依次执行，不支持 engines=["bing", "zhihu", "xhs"] 这种多引擎同时调用的模式
```

### 模式三：多源并行搜索

```
用户：「多源搜索 Python 异步编程」
→ 并行执行：
   1. web_search: "Python 异步编程 best practices", engines=["bing"]
   2. web_search: "Python 异步编程 知乎", engines=["zhihu"]
   3. web_search: "Python 异步编程 小红书", engines=["xhs"]
→ 综合结果去重并呈现
```

### 模式四：搜索+深度阅读

```
用户：「调研 Python asyncio 的性能优势」
→ 步骤：
   1. web_search 搜索 "Python asyncio performance"
   2. web_search 搜索 "asyncio 性能 知乎"
   3. 筛选 3-5 个高质量链接（优先知乎、官方文档、知名博客）
   4. web_reader 读取重点页面详细内容
   5. 综合分析输出结构化报告
```

### 模式五：知乎/小红书内容精读

**知乎文章精读：**
```
用户：「帮我读一下这个知乎回答 https://zhuanlan.zhihu.com/...」
→ 直接调用 web_reader，format="markdown"
→ 提取文章核心观点并总结
```

**小红书笔记精读：**
```
用户：「帮我读一下这篇小红书笔记 https://www.xiaohongshu.com/...」
→ 直接调用 web_reader，format="markdown"
→ 提取笔记核心内容和种草要点
```

## 输出格式规范

### 单源搜索结果

```
## 搜索结果：[关键词]

### 1. [标题](链接)
📰 来源：网站名 | 日期
📝 摘要：内容摘要...

### 2. [标题](链接)
...

---
🔍 数据源：Bing
```

### 多源搜索结果

```
## 多源搜索结果：[关键词]

### 🔵 Bing 搜索结果

#### 1. [标题](链接)
📰 来源：XXX | 日期
📝 摘要：...

### 🟠 知乎相关结果

#### 1. [标题](链接)
📰 来源：知乎 | 日期
📝 摘要：...

### 🔴 小红书相关结果

#### 1. [标题](链接)
📕 来源：小红书 | 日期
📝 摘要：...

---
🔍 多源搜索整合：Bing + 知乎 + 小红书
```

### 知乎文章精读

```
## 📄 知乎文章精读

**🔗 来源**：[知乎专栏/回答](URL)
**✍️ 作者**：XXX
**📅 发布日期**：XXXX-XX-XX
**💬 互动数据**：XXX 赞同 · XX 评论（如有）

### 💡 核心观点
一句话总结文章核心内容。

### 📝 详细内容
正文内容...

### 🔖 精彩评论（如有）
- 评论一...
- 评论二...

---
📚 来源：知乎 · Kepler Web Reader
```

### 小红书笔记精读

```
## 📕 小红书笔记精读

**🔗 来源**：[小红书笔记](URL)
**✍️ 作者**：XXX
**📅 发布日期**：XXXX-XX-XX
**❤️ 互动数据**：XXX 点赞 · XX 收藏 · XX 评论（如有）

### 💡 核心内容
一句话总结笔记核心内容。

### 📝 详细内容
笔记正文...

### 🏷️ 标签/话题
- #标签一
- #标签二

---
📚 来源：小红书 · Kepler Web Reader
```

### 综合调研报告

```
## 🔍 多源调研报告：[主题]

### 📊 数据来源概览
- Bing 搜索结果：X 条
- 知乎相关内容：X 条
- 小红书相关内容：X 条
- 其他来源：X 条

### 🎯 核心发现
1. **发现一**：[内容] [来源: 网站名]
2. **发现二**：[内容] [来源: 知乎]
3. **发现三**：[内容] [来源: 网站名]

### 📚 详细分析

#### 技术博客/文档观点
...

#### 知乎社区讨论
...

### 🔗 参考来源
- [标题](链接) — Bing/Blog
- [标题](链接) — 知乎
- ...

---
🔍 多源搜索整合 | 时间：YYYY-MM-DD HH:MM
```

## 使用技巧

### Engines 参数用法（重点）

**支持的数据源（每次调用只能指定一个）：**
- `["bing"]` — Bing 搜索引擎，通用搜索
- `["zhihu"]` — 知乎搜索，中文问答社区
- `["xhs"]` — 小红书搜索，生活方式社区

**多源搜索策略（依次执行）：**
```yaml
# 仅搜索知乎
engines: ["zhihu"]

# 仅搜索 Bing（默认）
engines: ["bing"]

# 仅搜索小红书
engines: ["xhs"]

# 综合调研（需要依次调用多次）
# 第一次: engines: ["bing"]
# 第二次: engines: ["zhihu"]
# 第三次: engines: ["xhs"]
```

**推荐策略：**
- 通用信息 → `engines: ["bing"]`
- 中文知识/经验 → `engines: ["zhihu"]`
- 生活方式/消费决策/攻略 → `engines: ["xhs"]`
- 综合调研 → 依次调用 `engines: ["bing"]`、`engines: ["zhihu"]` 和 `engines: ["xhs"]`，然后合并结果

### 搜索词优化

**知乎定向搜索（方式一：使用 engines 参数）：**
```yaml
query: "Python 异步编程"
engines: ["zhihu"]
```

**小红书定向搜索（方式一：使用 engines 参数）：**
```yaml
query: "上海探店 咖啡"
engines: ["xhs"]
```

**知乎/小红书定向搜索（方式二：使用关键词）：**
- `site:zhihu.com 关键词` — 只搜索知乎内容
- `site:xiaohongshu.com 关键词` — 只搜索小红书内容
- `关键词 知乎` — 获取知乎相关结果
- `关键词 小红书` — 获取小红书相关结果

**Bing 高级搜索：**
- `"精确短语"` — 精确匹配
- `关键词 filetype:pdf` — 搜索 PDF 文档
- `关键词 -排除词` — 排除特定词汇

### 多源并行策略

对于重要调研任务，建议依次搜索：
1. 英文关键词 → Bing (`engines: ["bing"]`)，获取英文资源
2. 中文知识 → 知乎 (`engines: ["zhihu"]`)，获取中文社区讨论
3. 生活方式/消费 → 小红书 (`engines: ["xhs"]`)，获取真实体验分享
4. 综合对比 → 合并 Bing + 知乎 + 小红书 的结果
5. 技术关键词 → Bing 搜索 + site:github.com

### 知乎内容获取技巧

1. **专栏文章**：URL 通常为 `zhuanlan.zhihu.com/p/xxxx`
2. **问题回答**：URL 通常为 `zhihu.com/question/xxxx`
3. **用户主页**：`zhihu.com/people/username`

知乎内容使用 web_reader 时：
- 默认提取文章正文
- 自动过滤广告和推荐内容
- 保留原文格式和结构

### 小红书内容获取技巧

1. **笔记链接**：URL 通常为 `www.xiaohongshu.com/explore/xxxx` 或 `xhslink.com/xxxx`
2. **用户主页**：`www.xiaohongshu.com/user/profile/xxxx`
3. **话题页面**：`www.xiaohongshu.com/search_result?keyword=xxxx`

小红书内容使用 web_reader 时：
- 自动提取笔记正文和图片说明
- 保留标签和话题信息
- 过滤广告和推荐内容

## 工具调用示例

### Bing 搜索（默认）

<function_calls>
<invoke name="mcp__kepler__web_search">
<arg name="query">Python asyncio 性能优化</arg>
<arg name="engines">["bing"]</arg>
<arg name="max_results">10</arg>
</invoke>
</function_calls>

### 知乎搜索（使用 engines 参数）

<function_calls>
<invoke name="mcp__kepler__web_search">
<arg name="query">Python asyncio 性能优化</arg>
<arg name="engines">["zhihu"]</arg>
<arg name="max_results">10</arg>
</invoke>
</function_calls>

### 小红书搜索（使用 engines 参数）

<function_calls>
<invoke name="mcp__kepler__web_search">
<arg name="query">上海咖啡探店</arg>
<arg name="engines">["xhs"]</arg>
<arg name="max_results">10</arg>
</invoke>
</function_calls>

### 多引擎搜索（Bing + 知乎 + 小红书）

**注意：需要依次执行三次搜索，不支持同时传递多个引擎**

<function_calls>
<invoke name="mcp__kepler__web_search">
<arg name="query">Claude Code MCP skill</arg>
<arg name="engines">["bing"]</arg>
<arg name="max_results">10</arg>
</invoke>
<invoke name="mcp__kepler__web_search">
<arg name="query">Claude Code MCP skill</arg>
<arg name="engines">["zhihu"]</arg>
<arg name="max_results">10</arg>
</invoke>
<invoke name="mcp__kepler__web_search">
<arg name="query">Claude Code MCP</arg>
<arg name="engines">["xhs"]</arg>
<arg name="max_results">10</arg>
</invoke>
</function_calls>

### 传统多源并行搜索

<function_calls>
<invoke name="mcp__kepler__web_search">
<arg name="query">Claude Code MCP skill</arg>
<arg name="max_results">10</arg>
</invoke>
<invoke name="mcp__kepler__web_search">
<arg name="query">Claude Code MCP 知乎</arg>
<arg name="max_results">10</arg>
</invoke>
</function_calls>

### 读取知乎文章

<function_calls>
<invoke name="mcp__kepler__web_reader">
<arg name="url">https://zhuanlan.zhihu.com/p/xxxxx</arg>
<arg name="format">text</arg>
<arg name="extract_article">true</arg>
</invoke>
</function_calls>

### 读取小红书笔记

<function_calls>
<invoke name="mcp__kepler__web_reader">
<arg name="url">https://www.xiaohongshu.com/explore/xxxxx</arg>
<arg name="format">text</arg>
<arg name="extract_article">true</arg>
</invoke>
</function_calls>

## 故障处理

### 搜索无结果
- 尝试简化关键词
- 中英文关键词互换
- 使用更通用的词汇

### 知乎内容读取失败
- 检查 URL 是否完整
- 部分知乎页面需要登录，可能无法读取完整内容
- 尝试切换 format 参数（markdown/text/html）

### 内容不完整
- 知乎回答过长时可能只提取核心内容
- 需要详细内容可指定具体段落读取

## 限制说明

1. **搜索范围**：通过 Bing 搜索引擎获取结果，知乎内容通过关键词筛选
2. **访问限制**：
   - 无法读取需要登录的知乎私有内容
   - 部分网站有反爬机制
3. **内容安全**：遵守内容安全政策

## 工作区规则

临时搜索结果直接输出到对话中。如需保存调研报告，使用 `/tmp/` 目录。

---

🔍 **Kepler Agent Search** — 整合多源信息，一站式多源搜索解决方案。
