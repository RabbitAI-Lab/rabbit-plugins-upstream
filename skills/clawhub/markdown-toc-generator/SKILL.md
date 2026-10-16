---
name: markdown-toc-generator
description: >
  Insert or refresh a table of contents for Markdown headings. Use when a
  long doc needs an up-to-date TOC under a marker comment.
metadata: {"clawdbot":{"emoji":"📑","requires":{"bins":["python3"]}}}
---

# Markdown TOC Generator

## Purpose / Overview
Builds a nested TOC from `#`–`######` headings.

## When to Use
- README or design doc grew long
- User asks to "update the TOC"

## Usage / Instructions
1. Take the Markdown path from the user.
2. Run `python3 scripts/make_toc.py <path>`.
3. Show the TOC; write back only if the user confirms.

## Examples
```bash
python3 scripts/make_toc.py ./README.md
```

## Requirements / Dependencies
python3 (stdlib).

## Limitations / Caveats
Skips fenced code blocks when detecting headings (best-effort).

## Security / Permissions
Reads (and optionally writes) only the path provided. No network.

## Attribution / License
MIT-0
