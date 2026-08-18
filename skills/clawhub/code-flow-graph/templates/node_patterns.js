/**
 * Code Flow Graph — Node Patterns Reference
 *
 * Composable patterns for the 6 node types, connections, and groups.
 * AI should reference these patterns when generating data, not write from scratch.
 *
 * Each pattern shows the MINIMUM required fields + common optional fields.
 */

// ============================================================
// NODE PATTERNS
// ============================================================

// --- Pattern 1: Entry Node ---
// Use for: main(), CLI commands, API route handlers, pipeline entry points
var ENTRY_NODE = {
  id: 'EntryPoint',
  label: 'EntryPoint',
  type: 'entry',               // Renders: yellow badge "ENTRY"
  x: 30, y: 60, w: 280,
  sections: [
    {
      title: 'Entry',
      attrs: [
        {
          id: 'EntryPoint.main',
          name: 'main()',
          sig: '<span class="sig-name">main</span>(<span class="sig-params">args</span>)\n<span class="sig-return">→ int</span>',
          desc: 'Application entry point',
          detail: 'Initializes config, sets up logging, dispatches to subcommands.',
          callChain: [
            // Recursive call tree for detail panel
            { id: 'EntryPoint.main', name: 'main()', module: 'cli.py', desc: 'Entry point', calls: [
              { id: 'Config.load', name: 'load()', module: 'config.py', desc: 'Load configuration', calls: [] },
            ]},
          ],
        },
      ],
    },
  ],
};

// --- Pattern 2: Class Node ---
// Use for: standard classes with methods
var CLASS_NODE = {
  id: 'ClassName',
  label: 'ClassName',
  type: 'class',               // Renders: blue badge "CLASS"
  x: 350, y: 60, w: 280,
  sections: [
    {
      title: 'Public Methods',
      attrs: [
        {
          id: 'ClassName.method',
          name: 'method(param)',
          val: '→ Result',       // Return type shown on right side
          sig: '<span class="sig-name">method</span>(<span class="sig-params">param: <span class="sig-type">str</span></span>)\n<span class="sig-return">→ Result</span>',
          desc: 'One-line description',
          detail: 'Multi-line explanation:\n- Step 1\n- Step 2\n- Side effects',
          children: [
            // Collapsed sub-functions (expand via ▶ toggle)
            { id: 'ClassName._helper', name: '_helper()', sig: '...' },
          ],
        },
      ],
    },
    {
      title: 'Private Methods',
      attrs: [
        { id: 'ClassName._internal', name: '_internal()' },
      ],
    },
  ],
};

// --- Pattern 3: Module Node ---
// Use for: Python modules, JS files, Go packages (group of free functions)
var MODULE_NODE = {
  id: 'utils',
  label: 'utils',
  type: 'module',              // Renders: green badge "MODULE"
  x: 670, y: 60, w: 260,
  sections: [
    {
      attrs: [
        { id: 'utils.parse', name: 'parse(input)', desc: 'Parse raw input into structured data' },
        { id: 'utils.validate', name: 'validate(data)', desc: 'Validate against schema' },
      ],
    },
  ],
};

// --- Pattern 4: Function Node ---
// Use for: standalone functions, closures, callbacks
var FUNCTION_NODE = {
  id: 'handlers',
  label: 'Event Handlers',
  type: 'function',            // Renders: mauve badge "FUNC"
  x: 350, y: 400, w: 280,
  sections: [
    {
      attrs: [
        { id: 'handlers.on_click', name: 'on_click(event)', desc: 'Handle button click' },
        { id: 'handlers.on_submit', name: 'on_submit(form)', desc: 'Validate and submit form' },
      ],
    },
  ],
};

// --- Pattern 5: Data Node ---
// Use for: dataclasses, models, schemas, state containers
var DATA_NODE = {
  id: 'UserModel',
  label: 'UserModel',
  type: 'data',               // Renders: peach badge "DATA"
  x: 670, y: 400, w: 280,
  sections: [
    {
      title: 'Fields',
      attrs: [
        {
          id: 'UserModel.name',
          name: 'name',
          val: ': str',
          fieldDetail: {
            field: 'name',
            type: 'str',
            summary: 'Display name of the user, set during registration.',
            sources: [
              {
                mode: 'INITIAL',
                fn: 'register()',
                steps: ['Validate input length (2-50 chars)', 'Strip whitespace', 'Store in database'],
              },
              {
                mode: 'ON UPDATE',
                fn: 'update_profile()',
                steps: ['Re-validate', 'Check uniqueness', 'Emit name_changed event'],
              },
            ],
          },
        },
        { id: 'UserModel.email', name: 'email', val: ': str' },
      ],
    },
  ],
};

// --- Pattern 6: Widget Node ---
// Use for: UI components (Qt widgets, React components, Web components)
var WIDGET_NODE = {
  id: 'MainWindow',
  label: 'MainWindow',
  type: 'widget',             // Renders: sapphire badge "UI CLASS"
  x: 30, y: 60, w: 300,
  sections: [
    {
      title: 'Widgets',
      attrs: [
        { id: 'MainWindow.sidebar', name: 'sidebar', val: ': QListWidget' },
        { id: 'MainWindow.content', name: 'content_stack', val: ': QStackedWidget' },
      ],
    },
    {
      title: 'Signals/Slots',
      attrs: [
        { id: 'MainWindow.on_item_clicked', name: 'on_item_clicked(item)', desc: 'Switch content page when sidebar item selected' },
      ],
    },
  ],
};

// ============================================================
// CONNECTION PATTERNS
// ============================================================

var CONNECTION_PATTERNS = {
  // Direct function call (most common)
  call:     ['source.method', 'target.method', '#a6e3a1', false],

  // Inheritance / method override
  inherit:  ['Child.method', 'Parent.method', '#f38ba8', false],

  // Data flow / return value
  data:     ['producer.get', 'consumer.use', '#89b4fa', false],

  // Signal / event / callback (dashed)
  signal:   ['widget.clicked', 'handler.on_click', '#f5c2e7', true],

  // External dependency call
  external: ['local.fetch', 'axios.get', '#fab387', false],

  // Weak reference / optional dependency
  weak:     ['mod.maybe_call', 'other.func', '#6c7086', false],

  // With label (5-element form)
  labelled: ['source.emit', 'target.handle', '#f5c2e7', true, 'event_name'],
};

// ============================================================
// GROUP PATTERN
// ============================================================

var GROUP_PATTERN = {
  id: 'grp-module-name',
  label: 'module_name/ (Package)',
  nodes: ['Node1', 'Node2'],        // Array of node IDs enclosed by this group
  color: '#89b4fa',                  // Border + label color
  bg: 'rgba(137,180,250,0.04)',      // Background fill (very low opacity)
};

// Common group colors:
// - Blue (#89b4fa)   — standard packages/modules
// - Green (#a6e3a1)  — core/domain logic
// - Peach (#fab387)  — external/third-party
// - Mauve (#cba6f7)  — utilities/helpers
// - Pink (#f5c2e7)   — UI layer

// ============================================================
// UI_LAYOUT_VIEWS — Widget Tree Node Pattern
// ============================================================

var WIDGET_TREE_NODE = {
  name: 'widget_name',         // Object name or display text
  obj: 'QWidget',              // Framework class
  color: 'blue',               // Catppuccin color key
  badge: 'FRAME',              // WINDOW/FRAME/PANEL/BTN/TAB/STACK/WIDGET/LIST/etc.
  layout: 'v',                 // 'h' | 'v' | 'hsplit' | 'stack' | 'tab'
  // Optional:
  // note: 'tooltip info',
  // flex: 1,
  // w: 200,
  // h: 40,
  // leaf: true,
  // spacer: true,
  children: [
    // Nested widget nodes...
  ],
};
