---
name: session-cleanup
description: Lightweight session cleanup tool for OpenClaw. Removes old session backups, checkpoints, and trajectory files to prevent disk bloat.
metadata:
  {
    "openclaw":
      {
        "emoji": "🧹",
        "requires": { "bins": ["jq"] },
        "install":
          [
            {
              "id": "brew-jq",
              "kind": "brew",
              "formula": "jq",
              "bins": ["jq"],
              "label": "Install jq (brew)",
            },
          ],
      },
  }
---

# session-cleanup

Clean up OpenClaw session artifacts to prevent disk bloat.

## What It Cleans

| Pattern | Description | Default Retention |
|---------|-------------|-------------------|
| `.jsonl.reset.*` | Session backups from `/new` or `/reset` | 7 days |
| `.checkpoint.*.jsonl` | Auto-save checkpoints | 7 days |
| `.trajectory.jsonl` | Trajectory/thinking logs | 3 days |
| `.trajectory-path.json` | Trajectory index files | 3 days |
| `.jsonl.lock` | Stale lock files | 1 day |

## Usage

```bash
# Dry run - see what would be deleted
~/.openclaw/workspace/skills/session-cleanup/cleanup.sh --dry-run

# Clean with defaults (7d for backups, 3d for trajectories)
~/.openclaw/workspace/skills/session-cleanup/cleanup.sh

# Aggressive clean - keep only last 3 days of everything
~/.openclaw/workspace/skills/session-cleanup/cleanup.sh --backup-days 3 --trajectory-days 1

# Report only - show disk usage by session
~/.openclaw/workspace/skills/session-cleanup/cleanup.sh --report
```

## Cron Setup

Add to your crontab for weekly cleanup:

```cron
# Weekly session cleanup, Sunday 3:06 AM
6 3 * * 0 ~/.openclaw/workspace/skills/session-cleanup/cleanup.sh >> ~/.openclaw/logs/session-cleanup.log 2>&1
```

Or use OpenClaw cron:

```bash
openclaw cron add --name "session-cleanup" --schedule "0 3 * * 0" --command "~/.openclaw/workspace/skills/session-cleanup/cleanup.sh"
```

## Safety

- **Never deletes active sessions** (checks `.jsonl.lock` and recent modification time)
- **Moves to `.trash/` first** instead of permanent deletion (recoverable for 30 days)
- **Logs all actions** to `~/.openclaw/logs/session-cleanup.log`
