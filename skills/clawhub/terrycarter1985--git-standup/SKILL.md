---
name: git-standup
description: Generate a daily standup report from git commit history. Groups commits by author, lists what was done yesterday, what's planned today, and highlights any blockers. Use at the start of the workday or before a standup meeting.
metadata:
  openclaw:
    emoji: "📋"
    requires:
      bins: ["git"]
---

# Git Standup

Generate a concise standup report from recent git activity in a repository.

## Quick Start

```bash
# Standup for the last 24 hours
bash scripts/standup.sh /path/to/repo

# Custom hours
bash scripts/standup.sh /path/to/repo --hours 48

# Specific author
bash scripts/standup.sh /path/to/repo --author "Jane"
```

## Output Format

```
📋 Standup Report — 2026-08-17

Yesterday:
  ✅ Fixed login bug (#342)
  ✅ Updated API rate limiting
  ✅ Added unit tests for auth module

Today:
  ⬜ Code review for PR #345
  ⬜ Implement password reset flow

Blockers:
  ⚠️ Waiting on design specs for dashboard redesign
```

## Use Cases

- **Daily standup** — run at standup time to auto-generate talking points
- **Weekly review** — use `--hours 168` to summarize a week's work
- **Manager overview** — combine with `--author` to filter by team member
- **Remote teams** — run as part of a cron job for async standups

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--hours` | 24 | Lookback window in hours |
| `--author` | all | Filter commits by author (fuzzy match) |
| `--format` | text | Output format: text or json |
| `--repo` | cwd | Path to git repository |

## Prerequisites

- git ≥ 2.0
- bash ≥ 4.0
- A git repository with commit history
