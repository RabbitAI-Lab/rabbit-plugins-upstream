---
name: todo-manager
description: Scan workspace files for TODO/FIXME/HACK comments, list them with context, and optionally sync to a local task file. Use when you need to track code TODOs or audit outstanding work.
---

# Todo Manager

Scans workspace source files for `TODO`, `FIXME`, `HACK`, and `XXX` comments and presents them as a structured task list.

## Usage

```js
const { scanTodos, formatReport, getSummary, filterByTag } = require('./skills/todo-manager');
const todos = scanTodos('.');
console.log(formatReport(todos));
console.log(getSummary(todos));
const onlyTodos = filterByTag(todos, 'TODO');
```

## Integration

Can be combined with `quick-healthcheck` for a full system audit:
```js
const healthcheck = require('./skills/quick-healthcheck');
const todoManager = require('./skills/todo-manager');

const health = healthcheck.quick();
const todos = todoManager.scanTodos('.');

console.log('=== SYSTEM AUDIT ===');
console.log(health);
console.log(todoManager.getSummary(todos));
```

## Functions

### `scanTodos(rootDir, options)`
- `rootDir` — directory to scan (default: `.`)
- `options.extensions` — file extensions to scan (default: `['.js', '.ts', '.py', '.md', '.json']`)
- `options.ignore` — directories to skip (default: `['node_modules', '.git', 'dist']`)
- Returns array of `{ file, line, column, tag, text, context }`

### `formatReport(todos)`
- Returns a formatted string report grouped by tag (TODO/FIXME/HACK/XXX)

### `getSummary(todos)`
- Returns `{ total, byTag }` summary object

### `filterByTag(todos, tag)`
- Returns array filtered to only include the specified tag (e.g. `'TODO'`, `'FIXME'`)

### `saveTodos(todos, outputPath)`
- Saves todos as JSON to `outputPath` (default: `memory/todos.json`)

## CLI

```bash
node skills/todo-manager/scripts/scan.js [directory]
```
