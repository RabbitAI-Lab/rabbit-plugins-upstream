/**
 * Code Flow Graph — Data File Skeleton
 *
 * Copy this file as the starting point for a new project's data file.
 * Replace placeholders (marked with <...>) with actual values.
 * Delete sections you don't need (UI_LAYOUT_VIEWS is optional).
 *
 * Usage: Copy to <project>/docs/code_graph/code_flow_graph_data.js
 */

// ============================================================
// DIAGRAMS — Node-graph pages (required)
// ============================================================

var DIAGRAMS = {};
DIAGRAMS._projectTitle = '<ProjectName>';

// --- Overview Diagram (always generate first) ---
DIAGRAMS.overview = {
  title: '<ProjectName> — Module Overview',
  sub: '<root_path>/ — project architecture',
  navLabel: 'Overview',
  navSub: 'Module dependencies',
  NODES: [
    // One node per module/class — NOT per function
    // { id: 'ModuleName', label: 'ModuleName', type: 'module', x: 30, y: 60, w: 280, sections: [...] },
  ],
  CONNECTIONS: [
    // ['source.attr', 'target.attr', '#a6e3a1', false],
  ],
  GROUPS: [
    // { id: 'grp-pkg', label: 'package_name/', nodes: ['Mod1', 'Mod2'], color: '#89b4fa', bg: 'rgba(137,180,250,0.04)' },
  ],
};

// --- Call-Chain Diagram Template ---
// Duplicate this block for each entry-point call chain:
//
// DIAGRAMS.entry_function_name = {
//   title: 'entry_function() — Call Chain',
//   sub: 'path/to/source.py — ClassName',
//   navLabel: '→ entry_function',
//   navSub: 'path/to/source.py',
//   NODES: [...],
//   CONNECTIONS: [...],
//   GROUPS: [...],
// };

// ============================================================
// UI_LAYOUT_VIEWS — Widget hierarchy (optional, UI projects only)
// ============================================================

// var UI_LAYOUT_VIEWS = {};
//
// UI_LAYOUT_VIEWS.main_window = {
//   title: 'MainWindow — Full Layout',
//   sub: 'path/to/main_window.py — QMainWindow',
//   navLabel: '🏠 MainWindow',
//   navSub: 'Main window layout',
//   root: { /* widget tree — see templates/node_patterns.js for widget node format */ },
// };
