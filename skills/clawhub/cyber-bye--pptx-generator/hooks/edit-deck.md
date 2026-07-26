---
name: edit-deck
description: CRUD operations on an existing .pptx — list, delete, duplicate, reorder, update-text, replace.
usage: python3 ../../scripts/edit_deck.py <deck.pptx> <operation> [args...] [-o output.pptx]
---

# edit-deck — CRUD Operations on Existing Deck

## Description
Modifies an existing .pptx presentation without needing the original JSON spec.
Supports: list slides, delete slide, duplicate slide, reorder slides, update text,
and global find-and-replace.

## Trigger
- User asks: "edit this slide", "delete slide 3", "duplicate slide 1", "reorder", "change text"
- User says: "update the title on slide 2", "find and replace X with Y"

## Usage

```bash
/save_data/venv/pptx/bin/python3 ../../scripts/edit_deck.py ../../output_demo.pptx list
/save_data/venv/pptx/bin/python3 ../../scripts/edit_deck.py ../../output_demo.pptx delete 2 -o ../../output_demo_edited.pptx
/save_data/venv/pptx/bin/python3 ../../scripts/edit_deck.py ../../output_demo.pptx duplicate 0 --after 3
/save_data/venv/pptx/bin/python3 ../../scripts/edit_deck.py ../../output_demo.pptx reorder "0,2,1,3"
/save_data/venv/pptx/bin/python3 ../../scripts/edit_deck.py ../../output_demo.pptx update-text 1 0 "New Title"
/save_data/venv/pptx/bin/python3 ../../scripts/edit_deck.py ../../output_demo.pptx replace "old" "new"
```

## Operations

| Op | Args | Description |
|----|------|-------------|
| `list` | none | Print slide index, layout, title |
| `delete` | `<index>` | Remove slide at 0-based index |
| `duplicate` | `<index> [--after <idx>]` | Clone a slide (default: after source) |
| `reorder` | `"<csv>"` | Reorder by slide indices: `"2,0,1,3"` |
| `update-text` | `<idx> <shape> "<text>"` | Replace text in one shape/placeholder |
| `replace` | `"<find>" "<replace>"` | Global find-and-replace across all runs |

## Safety
- Always `list` first to show current structure
- `delete` is permanent — confirm with user
- Use `-o <file>` to create a new file; without `-o`, input is overwritten
- Prefer `-o` unless user explicitly confirms in-place edit
