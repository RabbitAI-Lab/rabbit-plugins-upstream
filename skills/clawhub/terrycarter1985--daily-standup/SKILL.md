---
name: daily-standup
description: Generate structured daily standup summaries from recent activity (git commits, completed tasks, blockers). Use when the user asks for a standup report, daily update, "what did I do yesterday", or needs a formatted summary for a team meeting. Supports markdown and plain-text output.
---

# Daily Standup

Generate a concise standup summary covering three sections: **Done**, **Doing**, **Blockers**.

## Quick Start

1. Gather recent activity: run `scripts/gather_activity.sh` to collect git commits and modified files from the last 24 hours.
2. Draft the summary using the template below.
3. Refine based on user input or additional context.

## Output Template

```markdown
## Daily Standup — <YYYY-MM-DD>

### ✅ Done
- ...

### 🔄 Doing
- ...

### 🚧 Blockers
- ...
```

## Tips

- Keep each bullet to one line.
- If no blockers exist, write "None".
- Use plain past tense for Done items ("Implemented…", "Fixed…").

## Scripts

- `scripts/gather_activity.sh [repo-path]` — prints recent git commits and changed files. Run without arguments to use the current directory.
