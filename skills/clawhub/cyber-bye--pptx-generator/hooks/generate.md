---
name: generate
description: Generate a PowerPoint deck from a JSON spec file.
usage: python3 ../../scripts/build_deck.py <spec.json> [--dry-run]
---

# generate — Build PowerPoint Deck

## Description
Takes a JSON specification file and generates a widescreen (16:9) .pptx presentation
with auto table of contents, cross-fade transitions, dynamic contrast text, and more.

## Trigger
- User asks: "generate a presentation", "build a deck", "make a pptx", "create slides"
- User provides a description of what they want → agent converts to JSON spec first

## Usage

```bash
# Dry-run (verify spec first)
/save_data/venv/pptx/bin/python3 ../../scripts/build_deck.py --dry-run ../../examples/my_spec.json

# Full generation
/save_data/venv/pptx/bin/python3 ../../scripts/build_deck.py ../../examples/my_spec.json
```

## Input
- JSON spec file path (absolute or relative to skill root)

## Output
- `.pptx` file at path specified in spec's `output` field
- Paths in output are resolved relative to project root (`../../`)

## Exit Codes
- 0: Success
- 1: Spec validation failure / missing required fields
- 2: Generation runtime error

## Errors
- Missing `output` field → ask user to provide output filename
- Missing slide types → default to `bullets`
- Image URL fails to download → non-fatal, placeholder used
- Missing python-pptx → run: `/save_data/venv/pptx/bin/pip install python-pptx Pillow`
