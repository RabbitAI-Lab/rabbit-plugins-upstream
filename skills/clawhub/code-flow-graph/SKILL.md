---
name: code_flow_graph
description: >
  Generate interactive HTML node-graph diagrams for code visualization. Trigger
  when user asks to: visualize code architecture, diagram module dependencies,
  map call chains, graph class relationships, show UI event flows, display widget
  hierarchy layouts, or understand how code connects. Keywords: "visualize",
  "diagram", "graph", "map out", "call chain", "architecture", "code flow",
  "widget hierarchy", "UI layout", "界面布局", "调用链", "代码架构", "可视化",
  "模块依赖", "函数关系", "类图", "事件流".
---

# Code Flow Graph

Generate interactive node-graph HTML diagrams that visualize code structure and call relationships.

## Output

Two files in `<project>/docs/code_graph/` (or user-specified / `config.json` path):

1. **`code_flow_graph.html`** — rendering engine (copy verbatim from `example/code_flow_graph.html` in THIS skill's directory)
2. **`code_flow_graph_data.js`** — diagram data (you generate this; use `templates/diagram_skeleton.js` as starting point)

## Workflow

> This is a guide, not a script. Adapt steps based on project size, user needs, and context. Skip or merge steps when appropriate.

1. **Analyze** — Read the project structure; identify architecture type, entry points, key modules. See `references/analysis_guide.md` for inclusion/exclusion criteria.
2. **Generate Overview** — Produce a module-level dependency diagram immediately as the first deliverable. One node per module/class — NOT per function.
3. **Offer Options** — Present deep-dive choices via `ask_followup_question` with dynamic options based on discovered entry points. Always include "自定义：分析其他函数或模块" as last option.
4. **Deep-Dive** — Generate selected call-chain / UI event / data type diagrams. See `references/deep_dive_types.md`.
5. **Validate** — Run `scripts/validate_data.js` on the generated file; fix any errors before delivering.
6. **Iterate** — Append more diagrams on demand without regenerating existing content; update session state.

### Config

Check `config.json` in this skill's directory for user preferences. If missing, use defaults:
- Output: `<project>/docs/code_graph/`
- Language: Chinese for descriptions, English for code identifiers
- Scope: entire project unless user specifies otherwise

### Session Tracking

On first run for a project, create `state/code_flow_graph_session.json`:

```json
{
  "project": "<absolute-project-path>",
  "created_at": "<ISO8601>",
  "updated_at": "<ISO8601>",
  "analyzed_entries": ["func1", "func2"],
  "generated_diagrams": ["overview", "func1_callchain"],
  "pending_items": ["func3_callchain", "ui_events"],
  "last_config_hash": "<sha256-of-config.json>"
}
```

On subsequent runs, read this file to resume context: skip re-analysis of completed entries, continue from `pending_items`.

### Data Format & Templates

- **Full spec**: `references/data_format.md`
- **Composable patterns**: `templates/node_patterns.js` (6 node types + connections + groups)
- **File skeleton**: `templates/diagram_skeleton.js` (copy as starting point)
- **Deep-dive types**: `references/deep_dive_types.md`
- **Analysis strategy**: `references/analysis_guide.md`

### Locating the HTML Template

The template is at `example/code_flow_graph.html` **relative to THIS skill's SKILL.md file**. Use the absolute path based on the skill's installation directory. Do NOT resolve it relative to the user's project root.

## Gotchas

### 1. HTML Template Source Path

**Why**: The HTML engine lives inside the skill directory, not the user's project. Resolving relative to the project root yields "file not found."

```js
// ❌ Wrong — resolves against user's project (file won't exist there)
fs.copyFileSync('example/code_flow_graph.html', outputDir);

// ✅ Right — resolve against THIS skill's installation directory
fs.copyFileSync(path.join(SKILL_DIR, 'example/code_flow_graph.html'), outputDir);
```

### 2. Connection Anchors Must Use `offsetTop`, Not `getBoundingClientRect`

**Why**: The canvas uses `CSS transform: scale()` for zoom. `getBoundingClientRect()` returns screen-space coordinates that include the scale factor, causing connections to misalign at any zoom level other than 1x.

```js
// ❌ Wrong — misaligns at zoom ≠ 1x
var relY = (el.getBoundingClientRect().top - nodeEl.getBoundingClientRect().top) + el.offsetHeight / 2;

// ✅ Right — layout-space coordinates, zoom-independent
var relY = el.offsetHeight / 2;
var cur = el;
while (cur && cur !== nodeEl) { relY += cur.offsetTop; cur = cur.offsetParent; }
```

### 3. Sync Transform Before Measuring

**Why**: After `switchDiagram()` resets `scale = 1; panX = 0; panY = 0;`, measurements in `redrawConnections()` read stale CSS transform values unless `applyTransform()` runs first.

```js
// ❌ Wrong — measurements happen against stale transform
switchDiagram(key);
requestAnimationFrame(() => redrawConnections());

// ✅ Right — apply transform before requesting redraw
switchDiagram(key);
applyTransform();
requestAnimationFrame(() => redrawConnections());
```

### 4. `callChain[].id` Must Match Attr IDs Exactly

**Why**: The detail panel uses `callChain` item IDs to highlight the corresponding node/attr on click. A mismatch silently breaks click-to-highlight with no error.

```js
// ❌ Wrong — inconsistent ID format
{ id: 'method_name', name: 'method_name()', ... }  // Missing NodeId prefix

// ✅ Right — format is always NodeId.method_name
{ id: 'ClassName.method_name', name: 'method_name()', ... }
// Must exactly match an existing attr's id in the same diagram
```

### 5. Data File Must Be Valid JavaScript

**Why**: The file is loaded via `<script src>`. A single syntax error (missing comma, unescaped quote, unbalanced brace) silently breaks the entire viewer with no user-visible error.

```js
// ❌ Wrong — missing comma between array items, unescaped string
attrs: [
  { id: 'A.foo', name: 'foo()' }   // ← missing comma
  { id: 'A.bar', name: "it's broken" }  // ← unescaped quote
]

// ✅ Right — valid JS, properly escaped
attrs: [
  { id: 'A.foo', name: 'foo()' },
  { id: 'A.bar', name: "it\\'s fixed" },
]
```

**Validation**: Always run `node scripts/validate_data.js <file>` before delivering.

### 6. Large Codebases: Raise Thresholds

**Why**: Default thresholds (fan-out >= 2, fan-in >= 3) produce unreadably dense diagrams on large codebases (> 500 lines per diagram page).

```js
// ❌ Wrong — default thresholds on a large project → 80+ nodes
fan_out_threshold: 2, fan_in_threshold: 3

// ✅ Right — raised thresholds for large projects
fan_out_threshold: 3, fan_in_threshold: 4
// Also: collapse deeper calls into `children`, summarize repetitive patterns
```

### 7. Overview Must Stay Module-Level

**Why**: The Overview is for architecture comprehension. Per-function detail belongs in deep-dive diagrams. Mixing levels makes the Overview unreadable.

```js
// ❌ Wrong — Overview with individual functions as nodes
DIAGRAMS.overview.NODES = [
  { id: 'parse_args', type: 'function', ... },
  { id: 'validate_input', type: 'function', ... },
];

// ✅ Right — one node per module/class in Overview
DIAGRAMS.overview.NODES = [
  { id: 'cli', label: 'CLI Module', type: 'module', ... },
  { id: 'core', label: 'Core Engine', type: 'class', ... },
];
```

### 8. Don't Modify the HTML Engine

**Why**: The HTML file contains a tightly-coupled rendering engine with search, tooltips, panels, persistence, and undo. Any modification risks breaking these interconnected features.

```
// ❌ Wrong — editing the HTML to add a feature
// Adding custom CSS, modifying event handlers, changing DOM structure

// ✅ Right — copy verbatim, all customization goes in the data file
// The engine supports: search, tooltips, callChain panel, fieldDetail panel,
// drag persistence, undo, groups, themes — all driven by data alone.
```

### 9. Grid-Aligned Layout Required

**Why**: Scattered or overlapping node placement makes diagrams unreadable. The engine expects consistent column-based positioning.

```js
// ❌ Wrong — random positions, overlapping nodes
{ id: 'A', x: 47, y: 133, w: 280, ... },
{ id: 'B', x: 52, y: 180, w: 280, ... },  // overlaps A

// ✅ Right — grid-aligned columns (30, 350, 670, 990...) with 40px vertical gaps
{ id: 'A', x: 30, y: 60, w: 280, ... },
{ id: 'B', x: 30, y: 300, w: 280, ... },  // same column, proper gap
{ id: 'C', x: 350, y: 60, w: 280, ... },  // next column
```

### 10. Incremental Append — Never Regenerate

**Why**: Users accumulate diagrams across multiple requests. Regenerating the file loses all previous deep-dive diagrams, breaking the append-only contract.

```js
// ❌ Wrong — overwriting the entire data file
var DIAGRAMS = {};  // Wipes all existing diagrams
DIAGRAMS.new_chain = { ... };

// ✅ Right — read existing file, append new diagram entry, write back
// 1. Read existing code_flow_graph_data.js
// 2. Add new DIAGRAMS.new_chain = { ... }; at the end (before UI_LAYOUT_VIEWS if any)
// 3. Write the complete file back
```

## Engine Features (Built-in, No Data-Side Work Needed)

- Ctrl+K global search (fuzzy, cross-diagram)
- Draggable nodes with position persistence (localStorage)
- Bezier connections with gradient direction indication
- Click-to-highlight with related node dimming
- Collapsible children with connection redirect
- Signature tooltips (hover) and call chain detail panel (click)
- Field detail panel for data type nodes
- Click-to-copy function names
- Ctrl+Z undo (up to 50 steps)
- Catppuccin Mocha dark theme with type-based colors
- Group boxes with auto-sizing
- UI Layout widget-tree viewer (for `UI_LAYOUT_VIEWS`)
