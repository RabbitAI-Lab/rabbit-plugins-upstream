---
name: web-browsing
slug: web-browsing
displayName: "Web Browsing"
version: "1.0.0"
summary: "浏览总结网站、从URL提取内容、搜索网络信息,一站式网页内容处理工具"
description: "浏览总结网站、从URL提取内容、搜索网络信息,一站式网页内容处理工具。Browse and summarize websites, extract content from URLs, search the。触发关键词: web, websites, browsing, summarize, content, browse, extract。"
license: "MIT-0"
tools:
  - read
---

# Web Browsing

This skill enables browsing websites, extracting content from URLs, and searching the web for information.

## When to Use

**Use this skill when:**

* User asks you to visit a website (e.g., "Check out example.com")
* User wants webpage content summarized
* User needs current information that requires internet search
* User provides a URL and wants it analyzed
* User asks to search for something online

## How It Works

### 1. Direct URL Access

When given a specific URL:

```markdown
User: "What's on https://example.com?"
→ Visit the page, extract main content, summarize key points
```

### 2. Web Search

When user asks to search:

```markdown
User: "Find information about climate change"
→ Perform web search, present top results with summaries
```

### 3. Content Extraction

For specific data extraction:

```markdown
User: "Get the latest news from techcrunch.com"
→ Navigate to site, extract relevant articles/headlines
```

## Tools Available

* **web_search**: Search the web for information
* **fetch_url**: Visit and retrieve webpage content
* **extract_content**: Parse HTML and extract structured data

## Best Practices

1. **Be specific** - Tell me what you want from the page (summary, specific data, latest news)
2. **Provide URLs** - If you have a specific page, share the URL directly
3. **Clarify intent** - Let me know if you need:
   * Quick summary
   * Detailed analysis
   * Specific data points
   * Latest updates

## 示例

```markdown
✅ "Visit https://news.ycombinator.com and summarize today's top stories"
✅ "Search for the latest React.js tutorial"
✅ "Check what's on Wikipedia's page about quantum computing"
✅ "Find pricing information from apple.com/iphone"
❌ Just say "browse the web" - be more specific!
```

## Limitations

* Cannot interact with JavaScript-heavy sites (may miss dynamic content)
* Some sites block automated access
* Video/audio content cannot be played, only described if available
* Login-required pages won't work without credentials

---

**Ready to browse!** Just give me a URL or tell me what to search for. 🌐

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent( Code / Cursor / Codex /  CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+execute(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- Browse and summarize websites, extract content from URLs, search the
  web for information
- 触发关键词: web, websites, browsing, summarize, content, browse, extract

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Web Browsing？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Web Browsing有什么限制？
A: 请参考已知限制章节了解具体限制。
