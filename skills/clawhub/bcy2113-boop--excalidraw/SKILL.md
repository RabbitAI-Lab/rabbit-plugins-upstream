---
name: excalidraw
description: "Generate, compress, and save .excalidraw.md drawings for the Obsidian Excalidraw plugin with proper element-bound arrows, LZ-String compression, and tree/flow/architecture layout patterns."
---

# Excalidraw Drawing Skill

Generate drawings for the **Obsidian Excalidraw plugin** (`.excalidraw.md` format with LZ-String compression). Drawings are viewable and editable in Obsidian's Excalidraw view.

## Output location

Obsidian vault: `/mnt/c/Users/adminb/系统面板/Excalidraw/`
Windows path: `C:\Users\adminb\系统面板\Excalidraw\`

File extension: `.excalidraw.md` (not `.excalidraw`)

## File format

Generated file must contain:

1. **YAML frontmatter** with `excalidraw-plugin: parsed`
2. **Text Elements** section listing all standalone texts
3. **Drawing** section with LZ-String compressed JSON in a `compressed-json` codeblock

```
---
excalidraw-plugin: parsed
tags: [excalidraw]
---
⚠ Switch to EXCALIDRAW VIEW...

# Excalidraw Data

## Text Elements
Label1 ^id1
Label2 ^id2

%%
## Drawing
```compressed-json
<LZ-String compressed base64>
```
%%
```

## Compression

Use **LZ-String** (`compressToBase64` / `decompressFromBase64`), NOT zlib/pako.

Helper script: `scripts/compress.cjs` — converts `.excalidraw` JSON → `.excalidraw.md`.
  Usage: `node scripts/compress.cjs input.excalidraw [output.excalidraw.md]`
  (Use `.cjs` extension — parent workspace uses ES modules.)

## Arrow bindings (CRITICAL)

For arrows to follow elements when dragged, every arrow MUST have:

```json
"startBinding": { "elementId": "source_id", "fixedPoint": [X, Y], "focus": 0, "gap": 1 },
"endBinding":   { "elementId": "target_id", "fixedPoint": [X, Y], "focus": 0, "gap": 1 }
```

fixedPoint convention:
- `[0.5, 0]` = top center (for child receiving from parent)
- `[0.5, 1]` = bottom center (for parent sending to child)
- `[0, 0.5]` = left edge center
- `[1, 0.5]` = right edge center

Arrow coordinate calculation:
```
arrow.x = source.x + source.width * fp[0]    // start point
arrow.y = source.y + source.height * fp[1]
arrow.width = (target.x + target.width * fp[0]) - arrow.x    // delta x
arrow.height = (target.y + target.height * fp[1]) - arrow.y   // delta y
arrow.points = [[0, 0], [width, height]]
```

Source element must list all outgoing arrow IDs in its `boundElements`.

## Element IDs

Use short, readable IDs (not random hashes):
- Rectangles: `user`, `feishu`, `gw`, `main`, `agent_xd`, `infra_box`
- Bound text: same as parent's ID with `_t` suffix (e.g., `user_t` for `user`'s label)
- Arrows: `a_uf` (user→feishu), `a_gm` (gateway→main), `a_xd_ws` (xiaodao→workspace)
- Standalone text: short abbreviation (e.g., `lbl_msg`, `legend_1`)

## Layout patterns

### Tree diagram (recommended for architecture)

Top-down hierarchy with one root branching to children at each level.

```
x spacing: parent centered, children spread evenly
y spacing: 80-100px between levels
```

Each level's elements should be horizontally centered under their parent.

### Swimlane / layered box

Use semi-transparent background rectangles (`opacity: 20-40`) behind each layer.
Layer labels top-left of each lane.
Layer colors: user=#fff3bf, channel=#a5d8ff, gateway=#d0bfff, agent=#b2f2bb, infra=#c3fae8, model=#ffc9c9

### Agent detail sub-tree

Use one large rectangle per agent with internal text elements positioned inside.
Keep font 11-12px for details, 13-14px for titles.
Use `#495057` for sub-items to create visual hierarchy.
Use `#868e96` for notes/secondary info.
Use `🔒` for private resources, `🔓` for shared services.

## Color palette

| Usage | Color | Hex |
|---|---|---|
| User | light orange | `#ffd8a8` |
| Channel | light blue | `#a5d8ff` |
| Gateway | light purple | `#d0bfff` |
| Main agent | bright green+thick border | `#69db7c`, strokeWidth=3 |
| Sub-agent | light green | `#b2f2bb` |
| Infrastructure | light teal | `#c3fae8` |
| Model/external | light red | `#ffc9c9` |
| Shared services | light pink bg | `#fcc2d7` opacity=20 |
| Special (ACP/Obsidian) | light gray | `#dee2e6` / `#e9ecef` |
| Sub-text/secondary | gray | `#495057` |
| Notes | lighter gray | `#868e96` / `#adb5bd` |

## Container rectangles

Every rectangle needs:
```
"roundness": { "type": 3 },    // rounded corners
"fillStyle": "solid",
"roughness": 1,                // hand-drawn look
```

## Standalone vs bound text

- **Bound text**: labels INSIDE rectangles → use `containerId` and `"textAlign": "center"`, `"verticalAlign": "middle"`
- **Standalone text**: labels/notes OUTSIDE any rectangle → no `containerId`, `textAlign: "left"`

Keep standalone text IDs unique and descriptive. Bound text IDs should end with `_t`.

## AppState

Minimum:
```json
"appState": { "viewBackgroundColor": "#ffffff", "gridSize": null }
```
