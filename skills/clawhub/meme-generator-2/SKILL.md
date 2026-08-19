---
name: meme-generator
description: Generate SVG-based memes from text — classic templates (Drake, Stonks, This is Fine, Doge, etc.), batch generation, quote packs, animated effects. Pure Python stdlib, crisp at any resolution.
author: Denis Voronin
license: MIT
version: 1.0.0
language: python
tags: [meme, svg, viral, social, fun]
categories:
  - creative
---

# Meme Generator

Create shareable SVG memes from text input. Pure Python stdlib — no external dependencies.

## Quick Start

```bash
# Single meme
python scripts/meme_gen.py make 'Unit tests?' 'No tests.' --template drake --output meme.svg

# Batch across all templates
python scripts/meme_gen.py batch 'Coffee is debug code' --all-templates --output-dir memes/

# Get quote ideas
python scripts/meme_gen.py quote --category programming --count 5

# Pipe mode
echo 'When it works on production' | python scripts/meme_gen.py --template this_is_fine

# List all templates
python scripts/meme_gen.py list
```

## Templates

| Template | Key | Format |
|---|---|---|
| Drake | `drake` | Two-panel reject/approve |
| Distracted Boyfriend | `distracted_boyfriend` | Three-character scene |
| Two Buttons | `two_buttons` | Dilemma choice |
| Change My Mind | `change_my_mind` | Table + sign |
| Galaxy Brain | `galaxy_brain` | Ascending brain levels |
| Stonks | `stonks` | Suit guy + arrow |
| This is Fine | `this_is_fine` | Dog in fire |
| Doge | `doge` | Shiba + colorful text |
| Expanding Brain | `expanding_brain` | Four-stage brain glow |
| Panik Kalm | `panik_kalm` | Three-panel panic/calm |

Aliases: `cmm` → change_my_mind, `brain` → expanding_brain, `fine` → this_is_fine, `stocks` → stonks, etc.

## Quote Categories

- **programming** — dev life struggles (20 quotes)
- **startup** — hustle culture satire (15 quotes)
- **productivity** — procrastination humor (15 quotes)
- **student** — academic chaos (15 quotes)

## Options

- `--html` — Also export HTML (easy browser viewing)
- `--animate` — Add SVG text animations (fade-in)
- `--all-templates` — Batch with every template
- `--output / --output-dir` — Control output paths

## Custom Templates

Create an SVG file with `{{TOP}}` and `{{BOTTOM}}` placeholders, then:

```bash
python scripts/meme_gen.py custom 'Hello' 'World' --template-file my_template.svg
```

## Output

- **SVG**: Standalone, scalable, tiny file size (~3-5 KB each)
- **HTML**: Wraps SVG in a centered page for browser viewing
- Watermark-free
