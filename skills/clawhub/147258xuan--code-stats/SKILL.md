---
name: code-stats
description: Analyze workspace code complexity — file counts by type, line counts, language breakdown, git commit frequency, and TODO/FIXME density. Use when you need to understand repo health or complexity metrics.
---

# Code Stats Skill

Analyzes a workspace directory for code complexity metrics.

## Usage

```js
const { analyze, report } = require('./skills/code-stats');

// Analyze current workspace
const stats = analyze(process.cwd());
console.log(report(stats));
```

## CLI

```bash
node skills/code-stats/scripts/stats.js [directory]
```

## Exports

- `analyze(dir)` — Returns stats object with file counts, line counts, language breakdown
- `report(stats)` — Returns human-readable formatted report string
- `countTodos(dir)` — Scans for TODO/FIXME/HACK/XXX comments

## Output Fields

- `filesByExt` — File count grouped by extension
- `linesByExt` — Line count grouped by extension
- `totalFiles` — Total file count (excludes node_modules, .git)
- `totalLines` — Total lines of code
- `todoCount` — TODO/FIXME/HACK/XXX comment count
- `languageBreakdown` — Percentage breakdown by language
