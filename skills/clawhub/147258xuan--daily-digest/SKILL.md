---
name: daily-digest
description: Compile a daily digest from memory files and recent workspace activity. Use when asked for daily summaries, recent activity reports, or memory consolidation.
---

# Daily Digest

Compile a concise daily digest from workspace memory files and evolution state.

## Usage

```bash
node skills/daily-digest/index.js
```

Or import as a module:

```js
const { generateDigest } = require('./skills/daily-digest');
const digest = generateDigest({ days: 1 });
console.log(digest);
```

## Options

- `days`: Number of days to look back (default: 1)

## Output

Returns a markdown string containing:
- Recent memory file previews
- Evolution state summary

## Notes

- Reads from `memory/YYYY-MM-DD.md` files
- Reads from `memory/evolution/evolution_state.json`
- All paths are relative to `WORKSPACE_ROOT` or current working directory
