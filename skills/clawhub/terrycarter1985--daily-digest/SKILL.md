---
name: daily-digest
description: Generate a daily digest summarizing workspace activity, memory entries, and completed tasks. Use at end of day to produce a readable summary of what happened in the workspace.
metadata:
  openclaw:
    emoji: "📋"
---

# Daily Digest

Produce a structured daily digest from workspace artifacts.

## When to Use

- End-of-day review
- Weekly retrospectives
- Handover summaries
- Personal productivity logs

## What It Does

1. Scans `memory/` directory for today's entries
2. Reads `MEMORY.md` for long-term context changes
3. Summarizes completed TODOs and ongoing work
4. Outputs a clean markdown digest

## Prerequisites

- `memory/` directory exists in workspace
- Read access to workspace files

## Steps

1. List files in `memory/` matching today's date pattern (`YYYY-MM-DD.md`)
2. If no daily file exists, note "No daily log for today"
3. Read the daily file(s) and extract:
   - Key events
   - Decisions made
   - Files created/modified
   - Pending items
4. Check `MEMORY.md` for recent additions
5. Format output as a structured digest

## Output Template

```markdown
# 📋 Daily Digest — YYYY-MM-DD

## Key Events
- ...

## Decisions
- ...

## Files Touched
- ...

## Still Open
- ...

## Memory Updates
- ...
```

## Notes

- This is read-only; it never modifies workspace files
- Run it at end of day for best results
- Multiple runs in one day produce the same digest
