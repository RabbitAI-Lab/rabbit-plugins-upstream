---
name: markdown-toc
description: Generate a Table of Contents from Markdown headings. Pure Python stdlib, no deps.
---
# markdown-toc — Generate Table of Contents from Markdown

## What It Does
Reads a Markdown file, extracts all headings (H1-H6), and outputs a clickable TOC string you can paste back into the document.

## Usage
```
python scripts/generate_toc.py <file.md>
python scripts/generate_toc.py <file.md> --ol       # ordered list (1. 2. 3.)
python scripts/generate_toc.py <file.md> --min 2    # start from H2 (skip H1)
python scripts/generate_toc.py <file.md> --flat     # no indentation, flat bullet list
```

## Options
| Flag | Description |
|------|-------------|
| `--ol` | Ordered list (1. 2. 3.) instead of bullets |
| `--min N` | Skip headings below level N (default: 1) |
| `--flat` | No indentation — flat list regardless of depth |
| `--anchor` | Show anchor links inline: `- [Section](#section)` |

## Output Format
- Default: indented bullet list matching heading depth
- `--ol`: same structure but numbered
- `--min N`: skip H1 (or lower based on N)
- Heading text slugified to anchor: `## My Awesome Section` -> `#my-awesome-section`

## Anchor Slug Rules
- Lowercase
- Spaces/colons -> hyphens
- Stripped: `!?.,'()[]{}` and special chars
- Chinese/Japanese/Korean/accents: stripped to ASCII equivalent where possible
- Collapses multiple hyphens

## Examples

**Input (sample.md):**
```markdown
# Introduction
## Background
### History
## Installation
```

**Output:**
```markdown
- [Introduction](#introduction)
  - [Background](#background)
    - [History](#history)
  - [Installation](#installation)
```

**With `--ol --min 2`:**
```markdown
1. [Background](#background)
     1. [History](#history)
2. [Installation](#installation)
```

## Files
- `SKILL.md` — this file
- `scripts/generate_toc.py` — main CLI script
