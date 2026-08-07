---
name: web-crawler
description: "网页爬取统一工具。支持单页精确抓取（CSS选择器/自定义JS/自动降级）和整站BFS爬取（断点续爬/内容清洗）。Playwright渲染JS + requests静态fallback。"
version: 1.0.0
tags: [web, crawl, fetch, playwright, spa, bfs]
---

# web-crawler

统一网页爬取工具，合并了原 crawler + web-fetch-enhanced 两个 skill 的能力。

## 两种模式

| 模式 | 命令 | 场景 |
|------|------|------|
| **单页抓取** | `python scripts/web_crawler.py fetch <url>` | SPA/动态页面/精确提取 |
| **整站爬取** | `python scripts/web_crawler.py crawl <url>` | 文档站/批量内容采集 |

---

## 模式一：单页抓取（fetch）

### 基本用法

```bash
# 基本抓取
python scripts/web_crawler.py fetch https://example.com

# SPA 页面，等待网络空闲
python scripts/web_crawler.py fetch https://spa-app.com --wait networkidle

# 只提取文章内容
python scripts/web_crawler.py fetch https://blog.com/post --selector "article"

# 移除特定元素
python scripts/web_crawler.py fetch https://example.com --remove ".popup,.newsletter"

# 页面加载后执行 JS（处理无限滚动等）
python scripts/web_crawler.py fetch https://example.com --js "window.scrollTo(0, document.body.scrollHeight)"

# 强制使用 fallback 模式（不用 Playwright）
python scripts/web_crawler.py fetch https://example.com --no-playwright

# 输出到文件
python scripts/web_crawler.py fetch https://example.com -o result.md

# JSON 格式输出（含元数据）
python scripts/web_crawler.py fetch https://example.com --json
```

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `url` | str | 必填 | 要抓取的 URL |
| `--wait` | str | "load" | 页面加载完成判定：`load` / `domcontentloaded` / `networkidle` |
| `--timeout` | int | 30000 | 超时时间（毫秒） |
| `--selector` | str | None | 只提取此 CSS selector 内的内容 |
| `--remove` | str | None | 额外移除的元素（逗号分隔） |
| `--js` | str | None | 页面加载后执行的 JS 代码 |
| `--no-playwright` | bool | False | 强制使用 requests + BeautifulSoup |
| `--output` / `-o` | str | None | 输出文件路径（默认 stdout） |
| `--json` | bool | False | JSON 格式输出 |

### 自动降级机制

```
Playwright 可用？
├── 是 → 使用 Playwright 渲染
│   ├── 成功 → 返回 markdown
│   └── 失败 → 降级为 requests + BeautifulSoup
└── 否 → 使用 requests + BeautifulSoup
    └── 自动检测主内容区域（main > article > [role=main] > .content > body）
```

### 自动清洗元素

默认移除以下元素（无需手动指定）：
- 导航栏：`nav`, `header`, `[role='navigation']`
- 侧边栏：`aside`, `.sidebar`
- 页脚：`footer`, `[role='contentinfo']`
- 广告：`.ads`, `.advertisement`, `.advert`
- 弹窗：`.popup`, `.modal`, `.cookie-banner`
- 社交分享：`.social-share`, `.share-buttons`
- 订阅框：`.newsletter-signup`
- 脚本/样式：`script`, `style`, `noscript`

---

## 模式二：整站爬取（crawl）

### 基本用法

```bash
# 爬取整站（默认最多 50 页）
python scripts/web_crawler.py crawl https://example.com

# 限制页面数
python scripts/web_crawler.py crawl https://example.com --max-pages 20

# 允许跨域
python scripts/web_crawler.py crawl https://example.com --no-same-domain

# 显示浏览器窗口（调试用）
python scripts/web_crawler.py crawl https://example.com --no-headless

# 重新开始（不使用断点续爬）
python scripts/web_crawler.py crawl https://example.com --no-resume

# 指定输出目录
python scripts/web_crawler.py crawl https://example.com --output-dir ./my_output
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `url` | (必填) | 起始 URL |
| `--max-pages` | 50 | 最大爬取页面数 |
| `--no-same-domain` | false | 允许跨域爬取 |
| `--output-dir` | workspace/crawl_results/ | 输出目录 |
| `--no-headless` | false | 显示浏览器窗口 |
| `--no-resume` | false | 不使用断点续爬，从头开始 |

### 输出格式

结果保存为 `crawl_results/crawl_{domain}.json`：
```json
[
  {
    "url": "https://example.com/page1",
    "title": "Page Title",
    "text": "Extracted plain text content...",
    "depth": 0,
    "publish_time": "2026-07-08T10:00:00Z"
  }
]
```

### 功能特性

1. **BFS 爬取**：从起始 URL 开始，逐层发现并爬取子页面
2. **同域过滤**：默认只爬取同域名下的页面
3. **JS 渲染**：使用 Playwright 渲染 JavaScript 页面
4. **内容清洗**：去除导航栏、侧边栏、页脚、广告，提取正文
5. **断点续爬**：自动保存进度，中断后可继续
6. **资源过滤**：自动跳过 PDF、图片、CSS、JS 等非页面资源

### 断点续爬

爬取过程中会自动保存 checkpoint 文件。如果中断，再次运行相同命令会自动从断点继续。
要重新开始，使用 `--no-resume` 参数。

---

## 何时使用此 Skill

| 场景 | 推荐 |
|------|------|
| 普通静态页面 | 内置 `web_fetch` 更快 |
| SPA / React / Vue 页面 | ✅ web-crawler fetch |
| 需要 CSS 选择器精确提取 | ✅ web-crawler fetch |
| 需要执行 JS 后提取 | ✅ web-crawler fetch |
| 整站文档爬取 | ✅ web-crawler crawl |
| 需要断点续爬 | ✅ web-crawler crawl |

## 依赖

```bash
pip install playwright beautifulsoup4 markdownify requests
python -m playwright install chromium
# 可选（提升内容清洗质量）
pip install readability-lxml
```

## 文件结构

```
web-crawler/
├── SKILL.md                    # 本文档
└── scripts/
    ├── web_crawler.py          # 统一入口（fetch/crawl 子命令）
    ├── web_fetch_enhanced.py   # 单页抓取引擎
    ├── crawler.py              # 整站 BFS 爬取引擎
    └── content_cleaner.py      # 内容清洗模块
```
