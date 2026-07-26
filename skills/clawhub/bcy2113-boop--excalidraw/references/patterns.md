# Excalidraw Patterns for Obsidian Plugin

## Bound text inside a rectangle

```json
{
  "type": "rectangle",
  "id": "mybox",
  "x": 100, "y": 100, "width": 180, "height": 50,
  "roundness": { "type": 3 },
  "backgroundColor": "#a5d8ff",
  "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
  "boundElements": [{ "id": "mybox_t", "type": "text" }, { "id": "arrow1", "type": "arrow" }]
},
{
  "type": "text",
  "id": "mybox_t",
  "x": 0, "y": 0, "width": 100, "height": 20,
  "text": "Label",
  "originalText": "Label",
  "fontSize": 14, "fontFamily": 1,
  "strokeColor": "#1e1e1e",
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": "mybox",
  "autoResize": true
}
```

## Element-bound arrow (vertical, parent→child)

Parent at (300, 200) size 200x50 → center bottom at (400, 250)
Child  at (350, 300) size 100x40 → center top    at (400, 300)

```json
{
  "type": "arrow",
  "id": "a_parent_child",
  "x": 400, "y": 250,
  "width": 0, "height": 50,
  "points": [[0, 0], [0, 50]],
  "endArrowhead": "arrow",
  "roughness": 1, "strokeColor": "#1e1e1e", "strokeWidth": 2,
  "startBinding": { "elementId": "parent", "fixedPoint": [0.5, 1], "focus": 0, "gap": 1 },
  "endBinding":   { "elementId": "child",  "fixedPoint": [0.5, 0], "focus": 0, "gap": 1 }
}
```

## Element-bound arrow (horizontal, left→right)

Source at (200, 180) size 180x40 → right edge center at (380, 200)
Target at (420, 180) size 160x40 → left  edge center at (420, 200)

```json
{
  "type": "arrow",
  "id": "a_left_right",
  "x": 380, "y": 200,
  "width": 40, "height": 0,
  "points": [[0, 0], [40, 0]],
  "endArrowhead": "arrow",
  "roughness": 1, "strokeColor": "#868e96", "strokeWidth": 2,
  "startBinding": { "elementId": "source", "fixedPoint": [1, 0.5], "focus": 0, "gap": 1 },
  "endBinding":   { "elementId": "target", "fixedPoint": [0, 0.5], "focus": 0, "gap": 1 }
}
```

## Tree layout formula

For parent at (px, py) size (pw, ph) → child at (cx, cy) size (cw, ch)

```
arrow.x = px + pw * sp[0]      // sp = start fixedPoint
arrow.y = py + ph * sp[1]
dx = (cx + cw * ep[0]) - arrow.x   // ep = end fixedPoint
dy = (cy + ch * ep[1]) - arrow.y
arrow.width = dx
arrow.height = dy
```

For top-down tree (sp=[0.5,1], ep=[0.5,0]):
```
dx = (cx + cw/2) - (px + pw/2)
dy = cy - (py + ph)
```

For children spread evenly under a parent:
```
child_count = N
total_width = sum of all child widths
available = parent_pw * 2  // total horizontal span for children (wider than parent)
spacing = available / (N + 1)
for i in 0..N-1:
    cx = (px + pw/2) - available/2 + spacing * (i + 1) - child_width/2
```

## Semi-transparent layer backgrounds

Use behind related elements to show grouping:

```json
{
  "type": "rectangle",
  "id": "layer_bg",
  "x": 40, "y": 300, "width": 1200, "height": 200,
  "roundness": { "type": 3 },
  "backgroundColor": "#b2f2bb",
  "fillStyle": "solid", "strokeWidth": 0, "roughness": 0, "opacity": 15
}
```

Set `opacity` 15-30 for subtle background, `strokeWidth: 0` for borderless.

## Agent detail sub-panel pattern

```json
// Large container rectangle for agent
{ "type": "rectangle", "id": "agent_xd", "x": 30, "y": 350, "width": 260, "height": 300,
  "backgroundColor": "#b2f2bb", "roughness": 1 },

// Title inside
{ "type": "text", "id": "xd_t", "x": 42, "y": 356, "text": "🎓 小导 · 科研助手  🔒私用",
  "fontSize": 13, "strokeColor": "#2b8a3e" },

// Sub-items indented
{ "type": "text", "id": "xd1", "x": 50, "y": 378, "text": "📁 xiaodao-workspace/", "fontSize": 12 },
{ "type": "text", "id": "xd2", "x": 50, "y": 398, "text": "📂 projects/", "fontSize": 12 },
{ "type": "text", "id": "xd3", "x": 60, "y": 415, "text": "├─ knowledge-building",
  "fontSize": 11, "strokeColor": "#495057" },
```

## Complete minimal valid drawing

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "openclaw/excalidraw-skill",
  "elements": [
    { "type": "rectangle", "id": "bg", "x": 0, "y": 0, "width": 600, "height": 400,
      "backgroundColor": "#ffffff", "fillStyle": "solid", "strokeWidth": 0, "roughness": 0 },
    { "type": "rectangle", "id": "box1", "x": 200, "y": 50, "width": 160, "height": 50,
      "roundness": { "type": 3 }, "backgroundColor": "#a5d8ff", "fillStyle": "solid",
      "strokeWidth": 2, "roughness": 1, "boundElements": [{ "id": "box1_t", "type": "text" }] },
    { "type": "text", "id": "box1_t", "x": 0, "y": 0, "width": 100, "height": 18,
      "text": "Hello", "originalText": "Hello", "fontSize": 16, "fontFamily": 1,
      "strokeColor": "#1e1e1e", "textAlign": "center", "verticalAlign": "middle",
      "containerId": "box1", "autoResize": true }
  ],
  "appState": { "viewBackgroundColor": "#ffffff" }
}
```
