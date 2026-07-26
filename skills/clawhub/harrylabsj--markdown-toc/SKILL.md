---
name: markdown-toc
description: Generate a Table of Contents (TOC) from Markdown headings. Supports heading extraction, multiple output formats, and configurable level filtering.
version: v1.0.0
tags: markdown, table-of-contents, developer-tools, documentation
---
# markdown-toc

Generate a Table of Contents (TOC) from Markdown headings.


## Usage Scenarios

### Scenario 1: Generate TOC for a README
**User input:** "帮我给这个README.md生成目录。"

**Expected output:** Run toc generator on README.md, output a bullet list of all headings from level 1 to 6 with proper hierarchical indentation, skipping headings inside code blocks.

### Scenario 2: Filter by Heading Level
**User input:** "只需要二级和三级标题的目录。"

**Expected output:** Generate TOC filtered to include only heading levels 2 and 3, preserving hierarchy and indentation for the selected levels.

### Scenario 3: Generate TOC with Anchor Links
**User input:** "生成带锚点链接的目录，方便跳转，不想要纯列表。"

**Expected output:** Generate linked TOC with markdown anchor references `[Heading](#heading)` for each entry, allowing quick navigation when used in markdown viewers that support anchor links.
### Scenario 4: 给飞书文档生成目录
**User input:** "我在飞书上写了一篇项目的万字文档，想快速生成一个目录方便同事阅读，能不能帮我做？"
**Expected output:** 根据markdown语法格式，提取文档中所有#标题，自动生成带锚点链接的目录（TOC）。由于飞书自带目录功能有层级限制，可以提供markdown格式的TOC供用户复制嵌入文档顶部。同时支持Github风格的[TOC]标签和Gitbook的{{summary}}格式。

## Description

This skill extracts headings from Markdown files and generates a well-formatted table of contents. It supports standard Markdown heading syntax (`#`, `##`, `###`, etc.) and outputs a clean, indented TOC that can be inserted back into your document.

## Usage

```bash
# Generate TOC from a markdown file
python ~/.openclaw/skills/markdown-toc/markdown_toc.py <input-file> [options]

# Options:
#   --output, -o    Output file (default: stdout)
#   --min-level     Minimum heading level to include (default: 1)
#   --max-level     Maximum heading level to include (default: 6)
#   --format        Output format: "list" or "links" (default: list)
```

## Examples

```bash
# Basic usage - print TOC to stdout
python ~/.openclaw/skills/markdown-toc/markdown_toc.py README.md

# Save TOC to a file
python ~/.openclaw/skills/markdown-toc/markdown_toc.py README.md -o toc.md

# Include only level 2-3 headings
python ~/.openclaw/skills/markdown-toc/markdown_toc.py README.md --min-level 2 --max-level 3

# Generate TOC with anchor links
python ~/.openclaw/skills/markdown-toc/markdown_toc.py README.md --format links
```

## Features

- Extracts headings from `#` to `######` (levels 1-6)
- Supports both bullet list and linked TOC formats
- Configurable heading level filtering
- Handles duplicate headings with unique anchors
- Preserves heading text formatting (bold, italic, code)
- Skips headings inside code blocks

## Output Formats

### List Format (default)
```markdown
- Heading 1
  - Heading 2
    - Heading 3
```

### Links Format
```markdown
- [Heading 1](#heading-1)
  - [Heading 2](#heading-2)
    - [Heading 3](#heading-3)
```
