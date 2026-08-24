# Session Rewind (Soft Rewind)

Provides instructions and guidance for rewinding conversation context without reverting local workspace code modifications.

## Problem Statement

In AI Coding assistants (such as `antigravity` / `agy` CLI or Claude Code), native rewind / checkpoint rollback often automatically performs `git revert` or restores source code files to the checkpoint state. 

However, users frequently want to **discard recent conversation context or faulty prompt trajectories while keeping all local code changes intact** (soft-rewind / keep-code rewind).

## Rewind Modes

| Rewind Type | Conversation Context | Local Code Files | Method / Command |
|-------------|----------------------|------------------|------------------|
| **Hard Rewind** (Default UI/CLI) | Rollback to step N | Reverted to step N state | Native Checkpoint Rollback / UI Rewind |
| **Soft Rewind** (Keep-Code) | Truncate / Rollback steps | **Preserved 100% (No revert)** | Stash → Rewind → Pop (or SQLite Step Truncation) |

## Soft Rewind Workflows (Code-Preserving)

### Method 1: Git Stash Bridge (Recommended for agy CLI & Claude Code)

Before triggering a native UI or CLI rewind command that reverts files:

```bash
# 1. Stash all uncommitted local code changes & untracked files
git stash save -u "agy-soft-rewind-keep-code-$(date +%Y%m%d_%H%M%S)"

# 2. Perform native conversation rewind in agy CLI / IDE to the desired checkpoint step
# (e.g. agy --conversation=<uuid> or UI rewind)

# 3. Restore all local code changes without conflict
git stash pop
```

### Method 2: agy SQLite Step Truncation (Advanced CLI Direct Edit)

To truncate conversation turns directly in `antigravity-cli` without touching working directory files:

```bash
# 1. Locate session DB
SESSION_DB="$HOME/.gemini/antigravity-cli/conversations/<conversation_id>.db"

# 2. Backup DB before modification
cp "$SESSION_DB" "${SESSION_DB}.bak"

# 3. Delete steps after target step index (e.g., target step 150)
sqlite3 "$SESSION_DB" "DELETE FROM steps WHERE idx > 150;"

# 4. Update step count in conversation_summaries.db index
sqlite3 "$HOME/.gemini/antigravity-cli/conversation_summaries.db" \
  "UPDATE conversation_summaries SET step_count=(SELECT COUNT(*) FROM steps WHERE conversation_id='<conversation_id>') WHERE conversation_id='<conversation_id>';"
```

## Best Practices

- Always use **Method 1 (Git Stash Bridge)** for safe interaction with CLI flags or UI controls.
- When committing code during soft-rewind workflows, ensure `commit-tidy` is called to verify staged hunks.
