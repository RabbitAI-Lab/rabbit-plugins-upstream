#!/usr/bin/env node
/**
 * Validates a code_flow_graph_data.js file for common errors.
 * Usage: node validate_data.js <path_to_data_file>
 *
 * Checks (5-point verification):
 * 1. Syntax — File is valid JavaScript (no syntax errors)
 * 2. ID Consistency — All connection/callChain IDs reference existing attrs
 * 3. Orphan Detection — Nodes not in any connection or group
 * 4. Completeness — Required fields present, callChain coverage
 * 5. Visual Hint — Reminds to open in browser for visual verification
 */

const fs = require('fs');
const vm = require('vm');
const path = require('path');

const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: node validate_data.js <path_to_data_file>');
  process.exit(1);
}

const code = fs.readFileSync(path.resolve(filePath), 'utf-8');
const errors = [];
const warnings = [];

// ============================================================
// Check 1: SYNTAX — Valid JS
// ============================================================
let context;
try {
  context = {};
  vm.runInNewContext(code, context);
} catch (e) {
  errors.push(`[SYNTAX] ${e.message}`);
  console.log('\n=== Validation: ' + filePath + ' ===\n');
  console.log(`❌ ${errors.length} error(s):\n`);
  errors.forEach(e => console.log(`  • ${e}`));
  process.exit(1);
}

// ============================================================
// Check 2 & 3 & 4: ID Consistency, Orphans, Completeness
// ============================================================
if (!context.DIAGRAMS) {
  errors.push('[COMPLETENESS] Missing global `DIAGRAMS` object');
} else {
  const diagrams = context.DIAGRAMS;
  const diagramKeys = Object.keys(diagrams).filter(k => k !== '_projectTitle');

  if (diagramKeys.length === 0) {
    errors.push('[COMPLETENESS] DIAGRAMS has no diagram entries (only _projectTitle found)');
  }

  for (const key of diagramKeys) {
    const d = diagrams[key];
    const prefix = `DIAGRAMS.${key}`;

    // Completeness: required diagram fields
    if (!d.title) warnings.push(`[COMPLETENESS] ${prefix}: missing 'title'`);
    if (!d.navLabel) warnings.push(`[COMPLETENESS] ${prefix}: missing 'navLabel'`);
    if (!d.NODES || !Array.isArray(d.NODES)) {
      errors.push(`[COMPLETENESS] ${prefix}: missing or invalid 'NODES' array`);
      continue;
    }

    // Collect all IDs
    const attrIds = new Set();
    const nodeIds = new Set();
    const connectedAttrIds = new Set();
    const groupedNodeIds = new Set();

    for (const node of d.NODES) {
      // Completeness: required node fields
      if (!node.id) { errors.push(`[COMPLETENESS] ${prefix}: node missing 'id'`); continue; }
      if (!node.label) warnings.push(`[COMPLETENESS] ${prefix}: node '${node.id}' missing 'label'`);
      if (!node.type) warnings.push(`[COMPLETENESS] ${prefix}: node '${node.id}' missing 'type'`);
      if (node.x === undefined) warnings.push(`[COMPLETENESS] ${prefix}: node '${node.id}' missing 'x'`);
      if (node.y === undefined) warnings.push(`[COMPLETENESS] ${prefix}: node '${node.id}' missing 'y'`);

      if (nodeIds.has(node.id)) {
        errors.push(`[ID] ${prefix}: duplicate node id '${node.id}'`);
      }
      nodeIds.add(node.id);

      if (node.sections) {
        for (const sec of node.sections) {
          if (sec.attrs) {
            for (const attr of sec.attrs) {
              if (!attr.id) { warnings.push(`[COMPLETENESS] ${prefix}: attr in '${node.id}' missing 'id'`); continue; }
              if (attrIds.has(attr.id)) {
                errors.push(`[ID] ${prefix}: duplicate attr id '${attr.id}'`);
              }
              attrIds.add(attr.id);

              // Collect children IDs
              if (attr.children) {
                for (const child of attr.children) {
                  if (child.id) attrIds.add(child.id);
                }
              }
            }
          }
        }
      }
    }

    // Check 2: ID Consistency — Connections reference valid attrs
    if (d.CONNECTIONS && Array.isArray(d.CONNECTIONS)) {
      for (const conn of d.CONNECTIONS) {
        if (!Array.isArray(conn) || conn.length < 4) {
          errors.push(`[ID] ${prefix}: invalid connection format (expected 4-5 element array)`);
          continue;
        }
        if (!attrIds.has(conn[0])) {
          errors.push(`[ID] ${prefix}: connection source '${conn[0]}' not found in attrs`);
        }
        if (!attrIds.has(conn[1])) {
          errors.push(`[ID] ${prefix}: connection target '${conn[1]}' not found in attrs`);
        }
        connectedAttrIds.add(conn[0]);
        connectedAttrIds.add(conn[1]);
      }
    }

    // Check 2: ID Consistency — callChain IDs reference existing attrs
    for (const node of d.NODES) {
      if (!node.sections) continue;
      for (const sec of node.sections) {
        if (!sec.attrs) continue;
        for (const attr of sec.attrs) {
          if (attr.callChain) {
            validateCallChainIds(attr.callChain, attrIds, prefix);
          }
        }
      }
    }

    // Check 3: Orphan Detection — nodes not in any connection or group
    if (d.GROUPS && Array.isArray(d.GROUPS)) {
      for (const grp of d.GROUPS) {
        if (grp.nodes) {
          for (const nid of grp.nodes) {
            if (!nodeIds.has(nid)) {
              warnings.push(`[ID] ${prefix}: group '${grp.id}' references unknown node '${nid}'`);
            }
            groupedNodeIds.add(nid);
          }
        }
      }
    }

    // Find nodes whose attrs are never referenced in connections AND not in any group
    for (const node of d.NODES) {
      const nodeHasConnection = node.sections && node.sections.some(sec =>
        sec.attrs && sec.attrs.some(attr => connectedAttrIds.has(attr.id))
      );
      const nodeInGroup = groupedNodeIds.has(node.id);

      if (!nodeHasConnection && !nodeInGroup && d.NODES.length > 1) {
        warnings.push(`[ORPHAN] ${prefix}: node '${node.id}' has no connections and is not in any group`);
      }
    }
  }
}

// Check UI_LAYOUT_VIEWS if present
if (context.UI_LAYOUT_VIEWS) {
  const views = context.UI_LAYOUT_VIEWS;
  for (const key of Object.keys(views)) {
    const v = views[key];
    if (!v.title) warnings.push(`[COMPLETENESS] UI_LAYOUT_VIEWS.${key}: missing 'title'`);
    if (!v.root) errors.push(`[COMPLETENESS] UI_LAYOUT_VIEWS.${key}: missing 'root' widget tree`);
  }
}

function validateCallChainIds(items, attrIds, prefix) {
  if (!Array.isArray(items)) return;
  for (const item of items) {
    if (item.id && !attrIds.has(item.id) && !item.external) {
      warnings.push(`[ID] ${prefix}: callChain id '${item.id}' not found in diagram attrs (click-to-highlight won't work)`);
    }
    if (item.calls) {
      validateCallChainIds(item.calls, attrIds, prefix);
    }
  }
}

// ============================================================
// Output Results
// ============================================================
console.log(`\n=== Validation: ${filePath} ===\n`);

if (errors.length === 0 && warnings.length === 0) {
  console.log('✅ All 5 checks passed!\n');
  console.log('  1. [SYNTAX]       ✓ Valid JavaScript');
  console.log('  2. [ID]           ✓ All IDs consistent');
  console.log('  3. [ORPHAN]       ✓ No orphan nodes');
  console.log('  4. [COMPLETENESS] ✓ Required fields present');
  console.log('  5. [VISUAL]       → Open the HTML in a browser to verify visual rendering\n');
  process.exit(0);
}

if (errors.length > 0) {
  console.log(`❌ ${errors.length} error(s):\n`);
  errors.forEach(e => console.log(`  • ${e}`));
}

if (warnings.length > 0) {
  console.log(`\n⚠️  ${warnings.length} warning(s):\n`);
  warnings.forEach(w => console.log(`  • ${w}`));
}

console.log('\n---');
console.log('Checklist:');
console.log(`  1. [SYNTAX]       ${errors.some(e => e.startsWith('[SYNTAX]')) ? '✗' : '✓'}`);
console.log(`  2. [ID]           ${errors.some(e => e.startsWith('[ID]')) ? '✗' : (warnings.some(w => w.startsWith('[ID]')) ? '⚠' : '✓')}`);
console.log(`  3. [ORPHAN]       ${warnings.some(w => w.startsWith('[ORPHAN]')) ? '⚠' : '✓'}`);
console.log(`  4. [COMPLETENESS] ${errors.some(e => e.startsWith('[COMPLETENESS]')) ? '✗' : (warnings.some(w => w.startsWith('[COMPLETENESS]')) ? '⚠' : '✓')}`);
console.log(`  5. [VISUAL]       → Open the HTML in a browser to verify visual rendering`);

process.exit(errors.length > 0 ? 1 : 0);
