---
name: markdown-to-html
description: Convert Markdown files to standalone styled HTML with syntax highlighting, table of contents, and responsive design. Use when the user wants to publish markdown content as a web page, blog post, or documentation page with professional styling.
metadata:
  {
    "openclaw":
      {
        "requires": { "bins": ["node"] }
      }
  }
---

# Markdown to HTML Converter

Converts Markdown files to standalone, styled HTML pages.

## Usage

```bash
node scripts/convert.mjs input.md -o output.html
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-o, --output <path>` | Output HTML file path | `<input>.html` |
| `-t, --title <text>` | Page title | Derived from filename |
| `--toc` | Include table of contents | `false` |
| `--theme <name>` | Theme: `light`, `dark`, `classic` | `light` |
| `--highlight` | Enable syntax highlighting | `true` |

### Examples

```bash
# Basic conversion
node scripts/convert.mjs README.md

# With TOC and dark theme
node scripts/convert.mjs article.md -o article.html --toc --theme dark

# Custom title
node scripts/convert.mjs notes.md -o notes.html -t "My Notes"
```

## Output Features

- Responsive design (mobile-friendly)
- Syntax highlighting for code blocks
- Optional auto-generated table of contents
- Print-friendly styles
- Standalone single file (no external dependencies)
