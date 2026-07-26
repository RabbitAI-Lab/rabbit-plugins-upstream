---
name: markdown-toolkit
description: Markdown 排版工具箱。格式化中文混排、转换微信公众号/小红书格式、生成目录、检查链接和标题层级。当用户需要排版、美化、转换 Markdown 文件时使用本技能。
---

# Markdown 排版工具箱

一站式 Markdown 排版工具，支持中文混排优化、微信公众号格式转换、表格处理、文档检查。

## 功能

### 1. 中文排版格式化

脚本：`scripts/format_md.py fix-spacing <文件>`

- **中英文间加空格**：`使用Python` → `使用 Python`
- **全角/半角标点修正**：中文括号/冒号自动转全角，英文转半角
- **中英文括号**：`中文(English)` → `中文（English）`（括号随内容语言切换）

### 2. 微信公众号格式转换

脚本：`scripts/format_md.py to-wechat <文件>`

将标准 Markdown 转换为微信公众号可用的 HTML，包含：
- 标题 → 带字号样式的 `<h1>`~`<h6>`（24px~14px）
- 加粗/斜体 → `<strong>` / `<em>`
- 行内代码 → 带背景色的 `<code>`
- 代码块 → 带背景的 `<pre><code>`
- 引用块 → 绿色左边框的 `<blockquote>`
- 链接 → 带微信品牌色的 `<a>`
- 段落间距为 1.75 倍行高，适合手机阅读

### 3. 表格处理

- **表格 → CSV**：`scripts/format_md.py table-to-csv <文件>`，提取 Markdown 中所有表格
- **CSV → 表格**：`scripts/format_md.py csv-to-table <文件>`，CSV 转回 Markdown 表格

### 4. 文档检查

- **字数统计**：`scripts/format_md.py stats <文件>`，含总字符、中文字数、英文单词、行数、段落数
- **自动生成目录**：`scripts/format_md.py toc <文件>`，根据标题层级生成 Markdown 目录
- **链接提取**：`scripts/format_md.py check-links <文件>`，提取所有链接

## 使用方式

直接描述需求即可，例如：

> "帮我格式化这个 README.md，中英文加空格"
> "把这篇 Markdown 转成公众号格式"
> "把这个表格转成 CSV"
> "检查一下文档有多少字"
> "给这篇文章生成目录"
