---
name: session-closeout
description: Run a read-only end-of-session closeout for an OpenClaw workspace and append one closeout block to today's daily memory file. Checks for dirty git repos, MASTER_TODO.md freshness, and (optionally) whether named project docs were updated today. Use only when the user explicitly asks to run closeout, end the session, or invokes /closeout. Runs no builders, hooks, or workspace scripts.
license: MIT
---

# Session Closeout

Read-only checklist for the end of a work session, plus one intentional write: a closeout block appended to `memory/YYYY-MM-DD.md`. It never commits, deletes, or runs other scripts.

## Run it

From the workspace root, with the outcomes of this session as pipe-delimited inputs:

```bash
CLOSEOUT_OUTCOMES="Shipped feature X|Fixed bug Y" \
CLOSEOUT_BLOCKERS="Waiting on API key" \
CLOSEOUT_NEXT="Deploy to prod" \
bash skills/session-closeout/scripts/session-closeout.sh
```

Optional: `CLOSEOUT_PROJECTS="slug-a|slug-b"` checks whether `STATUS.md`, `DECISIONS.md`, `PROJECT.md`, or `BACKLOG.md` under `projects/<slug>/` were touched today. Warn only.

## What it checks

1. **Repo hygiene.** Finds git repos up to 4 levels below the workspace and lists the ones with uncommitted changes. Reports only.
2. **Task hygiene.** Reports whether `MASTER_TODO.md` is fresh, stale (older than `CLOSEOUT_TODO_STALE_HOURS`, default 24), or missing. It never rebuilds the file. If it is stale and you keep a builder, run that builder yourself as a separate, reviewed step, then rerun closeout.
3. **Project-doc hygiene** (only with `CLOSEOUT_PROJECTS`). Flags projects whose core docs were not updated today.
4. **Automation hygiene.** Always reports `not_verified`; check cron and automation health by hand.
5. **Memory.** Computes the final status first, then appends one block with status, findings, outcomes, blockers, and next-start items.

## Read the output

The script prints `key=value` lines. Summarize these for the user:

| Key | Values |
|---|---|
| `CLOSEOUT_STATUS` | `ok`, `warning` (dirty repos, stale todo, stale project docs), `error` (`MASTER_TODO.md` missing) |
| `MASTER_TODO_STATUS` | `fresh`, `stale`, `missing` |
| `DIRTY_REPO_COUNT`, `DIRTY_REPOS:` | repos to review; never auto-commit or discard |
| `PROJECT_DOC_WARNINGS` | count of projects with no core doc updated today |
| `EXCEPTION_n` | `severity|finding|suggested action` |
| `MEMORY_FILE` | where the block was appended |

The status written to memory is the same one printed, so a failed check is never recorded as `ok`.

## Paths

| Item | Default | Override |
|---|---|---|
| Workspace root | `$OPENCLAW_WORKSPACE`, else cwd | env var |
| Daily memory | `$ROOT/memory/YYYY-MM-DD.md` | none |
| Master TODO | `$ROOT/MASTER_TODO.md` | none |
| Projects dir | `$ROOT/projects` | `CLOSEOUT_PROJECTS_DIR` |

## Boundaries

- Runs nothing it discovers in the workspace: no builders, no `closeout-hooks.sh`, no plugins.
- Extra checks belong in a separate command you review and run yourself, not in this script.
- Do not invoke it on a timer or as a "wrap up" reflex; it is for explicit closeout requests.
