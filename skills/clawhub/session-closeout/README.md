# openclaw-session-closeout

A read-only end-of-session closeout skill for [OpenClaw](https://github.com/openclaw/openclaw). Catches loose ends before your context resets, and writes exactly one thing: a closeout block in today's daily memory file.

## What it does

- **Repo hygiene.** Lists git repos with uncommitted changes. Never commits or discards.
- **Task hygiene.** Reports whether `MASTER_TODO.md` is fresh, stale, or missing. Never rebuilds it.
- **Project-doc hygiene** (optional). With `CLOSEOUT_PROJECTS="a|b"`, warns when a project's `STATUS.md`, `DECISIONS.md`, `PROJECT.md`, or `BACKLOG.md` was not updated today.
- **Automation hygiene.** Reports `not_verified` so you check cron health by hand.
- **Memory.** Computes the real `ok` / `warning` / `error` status first, then appends the block.

## 1.1.0: security-first refresh

- Removed automatic execution of `scripts/build-master-todo.py` and sourcing of `scripts/closeout-hooks.sh`. The script no longer discovers and runs anything in your workspace.
- Fixed the status bug: memory used to record `Status: ok` before checks were evaluated.
- Trigger narrowed to explicit closeout requests.
- Implemented the `CLOSEOUT_PROJECTS` check that the docs previously described.
- Portable `stat` (GNU and BSD).

## Install

```bash
clawhub install session-closeout
```

Or copy `SKILL.md` and `scripts/` into `skills/session-closeout/` in your workspace.

## Usage

```bash
CLOSEOUT_OUTCOMES="Shipped auth flow|Fixed login bug" \
CLOSEOUT_BLOCKERS="Waiting on DNS propagation" \
CLOSEOUT_NEXT="Deploy to prod" \
CLOSEOUT_PROJECTS="nyh|mission-control-ops" \
bash skills/session-closeout/scripts/session-closeout.sh
```

Output is `key=value` lines (`CLOSEOUT_STATUS`, `MASTER_TODO_STATUS`, `DIRTY_REPO_COUNT`, `PROJECT_DOC_WARNINGS`, `EXCEPTION_n`, `MEMORY_FILE`). See `SKILL.md` for the full table.

## Configuration

| Item | Default | Override |
|---|---|---|
| Workspace root | `$OPENCLAW_WORKSPACE` or cwd | env var |
| Daily memory | `$ROOT/memory/YYYY-MM-DD.md` | none |
| Master TODO | `$ROOT/MASTER_TODO.md` | none |
| Stale threshold | 24 hours | `CLOSEOUT_TODO_STALE_HOURS` |
| Projects dir | `$ROOT/projects` | `CLOSEOUT_PROJECTS_DIR` |

## Requirements

Bash 4+ and git.

## License

MIT
