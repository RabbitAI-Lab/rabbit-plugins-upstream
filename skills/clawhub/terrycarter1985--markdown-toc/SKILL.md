---
name: markdown-toc
description: Generate a table of contents (TOC) for a Markdown file by extracting its headers. Use when asked to create, update, or insert a TOC into a Markdown document, or to summarize the heading structure of a .md file.
---

# Markdown TOC

Generate a table of contents from a Markdown file's headers.

## Steps

1. Read the target Markdown file.
2. Run the generator script to produce a TOC block:

   ```bash
   python3 scripts/gen_toc.py <path/to/file.md>
   ```

   The script prints a fenced TOC block listing each `#`-prefixed header as a
   GitHub-style anchor link, indented by heading level.
3. Optionally insert the TOC into the file (place it after the title or front
   matter). Keep the original headers unchanged.

## Output

A Markdown list like:

```
- [Introduction](#introduction)
  - [Goals](#goals)
- [Usage](#usage)
```
