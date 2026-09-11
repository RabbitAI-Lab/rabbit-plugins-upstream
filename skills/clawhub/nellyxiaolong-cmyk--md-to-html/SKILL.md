---
name: md-to-html
description: Convert Markdown (.md) files to styled, self-contained HTML pages. Use when the user uploads or mentions a Markdown file and wants to convert it to HTML, view it in a browser, or share it as a formatted web page. Triggers on phrases like "md转html", "markdown转网页", "把md转成html", "markdown to html", "转html格式".
---

# Markdown to HTML

Convert Markdown files into standalone HTML pages with clean, responsive styling.

## Supported Input

- `.md` files (standard Markdown)
- Mixed Chinese/English content
- Technical documentation, API docs, notes, READMEs

## Supported Markdown Elements

| Element | HTML Output |
|---------|------------|
| `# H1` – `#### H4` | Styled headings with bottom borders |
| `**bold**`, `*italic*` | `<strong>`, `<em>` |
| `` `inline code` `` | Inline `<code>` |
| `\`\`\`code blocks\`\`\`` | `<pre><code>` with scroll |
| `\| table \|` | Styled HTML tables with alternating rows |
| `- list`, `* list` | `<ul>` |
| `1. ordered` | `<ol>` |
| `> quote` | Left-border blockquote |
| `---` | Horizontal rule |
| Paragraphs | Properly spaced `<p>` |

## Workflow

### Step 1: Locate the Markdown file

Get the file path from the user or workspace context.

### Step 2: Run the conversion script

Execute the bundled Python script:

```bash
python3 scripts/md2html.py <input.md> [output.html]
```

If `output.html` is omitted, the script defaults to `<input>.html` in the same directory.

### Step 3: Report results

Tell the user:
- Output file path
- File size
- Title extracted from first H1 heading

## Output Style

The generated HTML includes embedded CSS with:

- Responsive layout (max-width 960px, centered)
- System font stack with CJK support
- Clean table styling with header background
- Code block scroll and inline code highlighting
- Blockquote left accent border
- Alternating table row colors

## Limitations

- Does not render: nested lists beyond one level, footnotes, task checkboxes, math blocks, Mermaid diagrams
- Links are preserved as plain text (not clickable `<a>` tags)
- Images referenced by URL are not embedded
- No dark mode (light theme only)

## Script Reference

The conversion logic lives in `scripts/md2html.py`. It is a pure-Python script with no external dependencies beyond the standard library (`re`, `html`, `sys`, `os`).
