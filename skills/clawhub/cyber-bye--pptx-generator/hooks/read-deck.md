---
name: read-deck
description: Dump text content and structure of an existing .pptx file.
usage: python3 ../../scripts/read_deck.py <deck.pptx>
---

# read-deck — Inspect Existing Presentation

## Description
Reads a .pptx file and prints every slide's text content, layout name, shape names,
and placeholder types. Also shows total slide count and dimensions.

## Trigger
- User asks: "read this deck", "show me what's in this pptx", "inspect presentation"
- User uploads or references an existing .pptx file

## Usage

```bash
/save_data/venv/pptx/bin/python3 ../../scripts/read_deck.py ../../output_demo.pptx
```

## Input
- Path to an existing .pptx file

## Output
- Slide count and dimensions
- Per-slide: layout name, shape names, text content per paragraph

## Exit Codes
- 0: Success
- 1: File not found / cannot open as pptx
