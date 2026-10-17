---
name: wechat-article-formatter
description: "Create WeChat public account articles as fully-formatted HTML compatible with the WeChat rich-text editor. Use when user asks to write, format, or layout articles for WeChat 公众号 (mp.weixin.qq.com), including article composition, styling, color schemes, video/image placeholder insertion, CTA sections, and editor-compatible HTML output."
agent_created: true
---

# 微信公众号文章排版器

将文章内容编排为**微信公众号编辑器完全兼容的 HTML 页面**，用户可直接复制到微信编辑器中使用。

## 触发场景

- 用户要求写一篇公众号文章并排版
- 用户要求把 Markdown/草稿转换为公众号格式
- 用户提到"微信公众号""公众号编辑器""推文排版"
- 需要生成带样式的、可直接粘贴到微信编辑器的 HTML

## 工作流程

### 第一步：确认内容素材

在开始排版前，先明确：
1. **文章主题和角度** — 核心论点/故事线是什么？
2. **关键信息来源** — 是否有参考链接、数据截图、引用源？
3. **插入位需求** — 哪些位置需要插入视频/图片？（标记为占位符）
4. **账号信息** — 公众号名称、作者名（用于文末关注引导）

### 第二步：撰写文章正文

按照公众号阅读习惯组织内容：
- **开篇钩子**：前 3 句必须抓注意力（数据/反常现象/个人感受）
- **章节结构**：用小标题分段，每段 3-5 段文字
- **节奏控制**：每 300-400 字安排一个视觉停顿点（引用块/卡片/图片位）
- **情感递进**：从事实到感受到思考，层层深入
- **结尾 CTA**：文末必须有关注引导 + 下篇预告/互动提问

### 第三步：应用排版样式（核心）

输出一个完整 HTML 文件。详细 CSS 兼容性规则和可复用组件代码模板，
请参阅 `references/css-components.md` 文件。

核心原则速查：

**安全可用：**
- `border-left` 彩色竖线（最可靠装饰）
- `background` 单色浅底背景块
- `color` / `font-weight` 文字变色加粗
- `border` / `border-radius` 边框和圆角
- 所有间距属性（padding/margin/line-height）

**避免使用：**
- `display: flex` + `gap`（必然被过滤）
- `box-shadow` 带 rgba 颜色值（易被过滤）
- `linear-gradient` 渐变（大概率被过滤）
- SVG 图标/图形（会被清除）
- `position: absolute` / `transform`（不稳定）

**格式规范：**
- 全部使用内联 style，不用 class 或 style 标签
- 颜色只用 hex 格式如 `#07c160`
- 容器宽度限制 max-width:677px
- 正文行高 1.75-1.85

### 第四步：交付与说明

- 将 HTML 写入 article.html（或用户指定路径）
- 用 preview_url 展示预览效果
- 列出所有需要手动替换的内容（视频占位符、图片链接等）
- 提供标题候选建议（2-4 个选项）

## 配色方案速查

| 角色 | 颜色值 | 用途 |
|------|--------|------|
| 主色调 | `#07c160` 微信绿 | 竖线、关键词、正向引导 |
| 强调红 | `#e74c3c` | 数字强调、警示语句 |
| 浅蓝底 | `#f0f7ff` | 信息卡片、背景知识 |
| 浅绿底 | `#f0fdf4` | 建议/结论框 |
| 暖白底 | `#fffbf0` | 结尾关注引导区 |
| 浅灰底 | `#fafafa` / `#f6f8f7` | 引用块背景 |
| 正文 | `#333` | 主要段落文字 |
| 说明 | `#555` | 次要段落文字 |
| 辅助 | `#888` / `#999` | 来源标注、时间戳 |

完整组件 HTML 代码模板见 `references/css-components.md`。
HTML 文档骨架模板见 `assets/template.html`。
