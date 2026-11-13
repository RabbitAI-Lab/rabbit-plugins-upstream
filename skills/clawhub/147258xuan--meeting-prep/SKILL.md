---
name: meeting-prep
description: Auto-summarize recent workspace memory into a meeting prep brief. Use when asked for meeting context, daily standup notes, or recent activity summary.
---

# Meeting Prep

Auto-summarize recent memory files into a concise meeting prep brief.

## Usage

```bash
node skills/meeting-prep/index.js
```

Or from Node:

```js
const { main } = require('./skills/meeting-prep');
console.log(main());
```

## Behavior

- Reads memory files modified in the last 3 days
- Reads `.learnings/` files modified in the last 7 days
- Extracts high-priority lines
- Outputs a brief with top context, open items, and recent learnings
- Skips markdown headings, HTML comments, and promotion markers
