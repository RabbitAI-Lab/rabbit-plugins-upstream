---
name: pptx-generator-agent
description: Behavioral rules for pptx-generator skill. JSON spec generation, script execution, error handling, and output management.
---

# Agent Rules — PowerPoint Generator

## Rule 1 — Venv Required
All Python scripts must run via `/save_data/venv/pptx/bin/python3`.
Never use system python — the venv has python-pptx and Pillow.

```bash
/save_data/venv/pptx/bin/python3 ../../scripts/build_deck.py <spec.json>
/save_data/venv/pptx/bin/python3 ../../scripts/read_deck.py <deck.pptx>
/save_data/venv/pptx/bin/python3 ../../scripts/edit_deck.py <deck.pptx> list
```

## Rule 2 — Dry-Run First
Before generating any deck, ALWAYS:
1. Write the JSON spec to a temp file in `../../examples/`
2. Run `build_deck.py --dry-run <spec.json>`
3. Verify no errors
4. Only then run without `--dry-run`

## Rule 3 — Path Convention
All script paths are relative to this skill directory (`clawhub/openclaw/`):
```
scripts/            = ../../scripts/
examples/           = ../../examples/
output_*.pptx       = ../../<filename>
assets/             = ../../assets/
```

Always resolve back from the skill root using `../` prefixes.

## Rule 4 — Output Management
- Generated decks go to `../../<output_name>.pptx`
- Never overwrite existing files without asking
- Use `-o <output.pptx>` flag on edit_deck.py when modifying existing decks
- If specs ask for same output name, increment: `output_demo.pptx` → `output_demo_2.pptx`

## Rule 5 — Error Handling
- If `build_deck.py` returns non-zero → capture stderr output, show to user
- Common errors:
  - Missing `output` field in spec → ask user to add it
  - Missing slide `type` → default to `bullets`
  - Image download failure → script uses fallback placeholder (non-fatal)
  - Missing python-pptx → `/save_data/venv/pptx/bin/pip install python-pptx Pillow`

## Rule 6 — Spec Generation Guidelines
When generating specs from user description:
- **Color palette**: Pick harmonious 3-color palette based on context (dark theme for tech, light for business)
- **Slide count**: 1 title + ToC + as many content slides as needed
- **Bullets max**: 7 per slide (script auto-splits, but try to stay under)
- **Card grids**: Prefer for feature overviews, team listings, capability showcases
- **Tables**: Prefer for comparisons, metrics, pricing
- **Speaker notes**: Add presenter notes for each slide explaining the talking points
- **Background**: Support both `bg_color` and `bg_image_url`

## Rule 7 — Session Start
At session start (if resuming):
- Check `errors/raw/` for failed generation attempts
- Check `memory/` for active deck work in progress
- Surface pending items

## Rule 8 — Deck Editing Safety
- Use `list` first to show current slide structure
- Use `--dry-run` mentally: confirm the operation before running
- `delete` is irreversible — always confirm with user before deleting slides
- `reorder` — confirm the new order with user before applying
- `replace` — show count of occurrences before replacing

## Rule 9 — Spec as Source of Truth
The JSON spec IS the source of truth. Keep it alongside the generated .pptx.
If user asks to regenerate with changes → edit the spec, not the pptx directly.
Save edited spec back to `../../examples/<name>.json`.
