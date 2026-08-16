# Deep-Dive Diagram Types

This document covers how to generate each type of deep-dive diagram that can be incrementally appended to `code_flow_graph_data.js`.

## General Principles

- **Append only** — Read existing data file, add new `DIAGRAMS.<name>` entries, write back. Never regenerate existing diagrams.
- **Rich tooltips** — Every non-trivial function attr should have `sig` (HTML signature tooltip), `desc` (one-line summary), and `detail` (multi-line explanation covering: core steps, key sub-calls, side effects, error handling).
- **Type-based colors** — Color is auto-assigned by `type`. Don't set manual colors. Use `external: true` for third-party deps (renders dashed border + EXT tag).
- **Grid-aligned** — Follow layout guidelines in `data_format.md`.

## Call-Chain Diagram

Traces the complete call chain of one entry function.

### Structure

- Entry function as the leftmost node (type: `entry`)
- Callees organized left-to-right by execution depth
- Each node represents a class/module with attrs for its methods
- The entry function's attr includes `callChain` array for the interactive detail panel

### Generation Steps

1. Read the entry function's source completely
2. For each called function, apply importance filtering:
   - **Separate node** if high fan-out/fan-in or significant logic
   - **Collapsed `children`** if simple helper but relevant
   - **Exclude** if trivial accessor or generic utility
3. Determine placement:
   - Same-module helpers → attr with `children` or same-group node
   - Cross-module calls → different group, connected
   - Has sub-calls worth showing → recurse
4. Layout: left-to-right by execution depth (entry left, deepest right)
5. Add `callChain` to entry function attr with recursive call tree
6. Ensure `callChain[].id` matches target `attrs[].id` (format: `NodeId.method_name`)
7. Include `desc` for every `callChain` item

### Example `callChain` Format

```js
callChain: [
  {
    id: 'ClassName.method', name: 'method()', module: 'file.py',
    desc: 'What this function does in one line',
    calls: [
      { id: 'Other.func', name: 'func()', module: 'other.py', desc: '...', calls: [...] },
    ],
  },
],
```

## UI Signal/Event Diagram

For UI projects with event-driven architecture (Qt, React, Web, etc.).

### Structure

- One diagram entry per major UI view/window
- Use `widget` type for widget nodes (renders UI CLASS badge + sapphire color)
- Sections: Widgets, Event Handlers, Slots
- Dashed pink connections from event handlers to business logic

### Connections

- Widget → Handler: `#f5c2e7` dashed (signal/event)
- Handler → Business Logic: `#a6e3a1` solid (function call)
- External API: `#fab387` solid

## UI Layout Visualization

Generates `UI_LAYOUT_VIEWS` data for interactive widget hierarchy tree rendering.

### Top-Level Structure

```js
var UI_LAYOUT_VIEWS = {};
UI_LAYOUT_VIEWS.view_name = {
  title: 'ViewName — Full Layout',
  sub: 'path/to/source.py — FrameworkClass',
  navLabel: '🏠 ViewName',
  navSub: 'Description',
  legend: [  // optional
    { color: 'blue', label: 'Containers' },
    { color: 'green', label: 'Content Areas' },
  ],
  root: { /* widget tree */ },
};
```

### Widget Node Format

```js
{
  name: 'widget_name',       // Object name or display text
  obj: 'QWidget',            // Framework class name
  color: 'blue',             // Catppuccin color key
  badge: 'FRAME',            // Short badge (WINDOW/FRAME/PANEL/BTN/TAB/STACK/etc.)
  layout: 'v',              // 'h' | 'v' | 'hsplit' | 'stack' | 'tab'
  note: 'tooltip info',     // Optional hover text
  flex: 1,                  // CSS flex value
  w: 200,                   // Fixed width px
  h: 40,                    // Fixed height px
  leaf: true,               // Terminal widget
  children: [ ... ],
  // For stack: stackTabs + stackPages
  // For tab: tabTabs + tabPages
}
```

### Color Semantics

| Color | Usage |
|-------|-------|
| `blue` / `sapphire` | Containers, frames, windows |
| `green` / `peach` / `pink` / `flamingo` / `mauve` | Functional areas |
| `yellow` | Menus, toolbars |
| `lavender` | QStackedWidget |
| `teal` | Functional widgets |
| `red` | Overlays, floating layers |
| `overlay` | Basic leaf controls |

### Special Features

- `\\n` in names → vertical text (CSS white-space: pre-line)
- `{ spacer: true, name: 'stretch' }` → flex spacer
- `splitWeight` → QSplitter weight for hsplit children

## Data Type Diagram

Visualizes dataclass/model structures and their relationships.

### Structure

- Each data type → node with `type: 'data'`
- Fields as attrs with type in `val` field (e.g., `val: ': User[]'`)
- **Every non-trivial field gets `fieldDetail`** — this enables the right-sidebar computation panel

### `fieldDetail` Format

```js
fieldDetail: {
  field: 'fieldName',
  type: 'FieldType',
  summary: 'What this field represents and how it is managed.',
  sources: [
    {
      mode: 'INITIAL',           // Scenario label
      fn: 'constructor()',        // Source function
      steps: [                    // Ordered computation steps
        'Step 1 — what happens',
        'Step 2 — call someFunction() to process',
      ],
    },
    {
      mode: 'ON UPDATE',
      fn: 'reducer(state, action)',
      steps: [ ... ],
    },
  ],
}
```

Common modes: `INITIAL`, `ON FETCH`, `ON UPDATE`, `ON DELETE`, `ON FILTER`, `COMPUTED`, `ON EVENT`.

### Connections Between Data Nodes

| Color | Meaning |
|-------|---------|
| `#89b4fa` (blue) | Data composition (parent → child state) |
| `#a6e3a1` (green) | Reducer/producer → state field |
| `#f5c2e7` (pink dashed) | Signal/event dispatch → handler |
| `#fab387` (peach) | External API dependency |

## Sidebar Organization

As diagrams accumulate, sidebar order follows:

1. **Overview** (always first)
2. **Call-chain diagrams** — named after entry function
3. **UI diagrams** — widget hierarchy and events
4. **Data Types** — field listings and data flow
5. **🖼️ UI 布局** — separated by visual divider (UI_LAYOUT_VIEWS)
