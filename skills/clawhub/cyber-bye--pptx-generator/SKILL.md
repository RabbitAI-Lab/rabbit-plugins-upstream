---
name: pptx-generator
description: Professional PowerPoint (.pptx) presentation generator. Builds widescreen (16:9) decks from JSON specs with auto ToC, card grids, comparison tables, image contrast checks, cross-fade transitions, and speaker notes. Supports slide CRUD (list/delete/duplicate/reorder/replace). Uses python-pptx and Pillow.
version: 1.0.0
metadata:
  openclaw:
    emoji: 📊
    requires:
      bins:
        - python3
      env: []
    primaryEnv: ""
---

# PowerPoint Generator — OpenClaw Skill

## Overview
Generates high-fidelity, template-compliant PowerPoint (.pptx) presentations using `python-pptx` and `Pillow`. Designed for widescreen (16:9) format with dynamic contrast checking, auto table of contents, responsive card grids, and slide-level CRUD operations.

## Prerequisites

```bash
# Venv (required)
/save_data/venv/pptx/bin/python3

# Dependencies (already installed in venv)
/save_data/venv/pptx/bin/pip install python-pptx Pillow
```

## Scripts Reference (relative to skill root: `../../scripts/`)

| Script | Purpose | Usage |
|--------|---------|-------|
| `build_deck.py` | Generate deck from JSON spec | `python3 build_deck.py <spec.json>` |
| `build_deck.py --dry-run` | Verify spec without generating output | `python3 build_deck.py --dry-run <spec.json>` |
| `read_deck.py` | Dump text content of existing deck | `python3 read_deck.py <file.pptx>` |
| `read_notes.py` | Extract speaker notes only | `python3 read_notes.py <file.pptx>` |
| `edit_deck.py` | Slide CRUD ops | See below |

### edit_deck.py Operations

| Operation | Command |
|-----------|---------|
| List slides | `python3 edit_deck.py <deck.pptx> list` |
| Delete slide | `python3 edit_deck.py <deck.pptx> delete <index>` |
| Duplicate slide | `python3 edit_deck.py <deck.pptx> duplicate <index> [--after <index>]` |
| Reorder slides | `python3 edit_deck.py <deck.pptx> reorder "0,2,1,3"` |
| Update text | `python3 edit_deck.py <deck.pptx> update-text <index> <shape> "<text>"` |
| Replace text | `python3 edit_deck.py <deck.pptx> replace "<find>" "<replace>"` |
| Output override | Add `-o <output.pptx>` to any command |

## JSON Spec Format

Full spec documentation is in root `SKILL.md` (project level). Key elements:

```json
{
  "output": "presentation.pptx",
  "palette": { "primary": "1B1F3B", "secondary": "708090", "accent": "E4572E" },
  "slides": [
    { "type": "title", "title": "Title", "subtitle": "Subtitle" },
    { "type": "bullets", "title": "Section", "bullets": ["point 1", "point 2"] },
    { "type": "section", "title": "Section Header", "text": "intro" },
    { "type": "two_column", "title": "Compare", "left": [...], "right": [...] },
    { "type": "comparison", "title": "VS", "left_header":"A","left_content":"...", "right_header":"B","right_content":"..." },
    { "type": "title_only", "title": "Just Title" },
    { "type": "grid_cards", "title": "Cards", "cards": [{"title":"...", "description":"..."}] },
    { "type": "table", "title": "Metrics", "headers": ["Col1","Col2"], "rows": [["a","b"]] }
  ]
}
```

See `examples/` dir for working JSON spec files:
- `build_deck.py ../examples/test_spec_demo.json`
- `build_deck.py ../examples/test_spec_enhanced.json`
- `build_deck.py ../examples/demo.json`

## Slide Types

| Type | Layout ID | Description |
|------|-----------|-------------|
| `title` | 0 | Title + subtitle. Auto ToC as slide 2 |
| `bullets` | 1 | Title + bullet list (auto-splits >7 items) |
| `section` | 2 | Section header with description |
| `two_column` | 3 | Title + left/right columns |
| `comparison` | 4 | Title + side-by-side headers+bodies |
| `title_only` | 5 | Title only, with custom overlays |
| `grid_cards` | custom | Responsive card grid (2-4 cols or 2 rows) |
| `table` | custom | Data table with alternating row colors |

## Design Features
- **Auto Table of Contents**: Auto-generated as slide 2 (single or two-column)
- **Cross-fade transitions**: XML-based on every slide
- **Dynamic contrast text**: PIL brightness check → dark/light text auto
- **Title divider**: 1pt accent line under content slide titles
- **Custom overlays**: `custom_textboxes` + `custom_images` on any slide
- **Speaker notes**: Per-slide presenter notes from `notes` field
- **Slide-level palette**: Override colors per individual slide
- **Image brightness**: Auto text color vs background images

## Folder Structure

```
pptx/
├── clawhub/openclaw/       ← THIS SKILL
│   ├── SKILL.md
│   ├── AGENT.md
│   ├── SOUL.md
│   ├── hooks/
│   ├── core-extra/config/
│   ├── memory/
│   ├── crons/
│   └── errors/
├── scripts/                 ← Python generation scripts
│   ├── build_deck.py
│   ├── read_deck.py
│   ├── read_notes.py
│   └── edit_deck.py
├── examples/                ← JSON spec examples
├── assets/                  ← Generated slide assets
└── README.md
```

## Core-Extra Config
All owner/company specific data lives in `core-extra/config/profile.md` — never hardcoded.
