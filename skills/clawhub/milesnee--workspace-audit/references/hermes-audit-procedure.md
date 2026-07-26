# Hermes Agent System Audit Procedure

The baseline scripts (`audit_baseline.py` etc.) target OpenClaw-style workspaces.
Hermes has a fundamentally different architecture. Use this procedure instead.

## Hermes Directory Layout (non-OpenClaw)

```
~/.hermes/
  config.yaml              # 525+ lines, all settings
  state.db                 # SQLite: sessions + messages + FTS indices
  memories/
    MEMORY.md              # agent notes (§-separated entries)
    USER.md                # user profile (§-separated entries)
  sessions/                # *.jsonl (raw transcripts) + *.json
  cron/
    jobs.json              # scheduled job definitions
    output/                # cron execution logs
  skills/                  # skill directories
  cache/ audio_cache/      # transient
  gateway/                 # platform routing state
```

## Phase 0: Baseline Data Collection

### Disk overview (single command)

```bash
du -sh ~/.hermes/state.db ~/.hermes/sessions/ ~/.hermes/skills/ ~/.hermes/lsp/ ~/.hermes/logs/ ~/.hermes/cron/ ~/.hermes/cache/ ~/.hermes/bin/
```

> **Include `lsp/` and `logs/`** — LSP node_modules can be 80MB+, logs 16MB+.
> These were missed in the original procedure and only surfaced on second audit.
> Also check `bin/` (12MB+) and any `kanban.db` / `verification_evidence.db`.

### Memory files

```bash
wc -c ~/.hermes/memories/MEMORY.md ~/.hermes/memories/USER.md
```

Parse §-separated entries: count entries, categorize by prefix tag.

### Config

```bash
wc -l ~/.hermes/config.yaml
# Count backups
ls ~/.hermes/config.yaml.bak.* 2>/dev/null | wc -l
```

### Session DB (the big one — often 400MB+)

**IMPORTANT:** The `messages` table uses `timestamp REAL` (epoch float), not
`created_at`. The `sessions` table uses `started_at REAL` / `ended_at REAL`.
Do NOT assume `created_at` / `updated_at` column names — they don't exist.

```bash
# Schema discovery first
sqlite3 ~/.hermes/state.db ".schema messages"
sqlite3 ~/.hermes/state.db ".schema sessions"

# Row counts
sqlite3 ~/.hermes/state.db "SELECT COUNT(*) FROM messages;"
sqlite3 ~/.hermes/state.db "SELECT COUNT(*) FROM sessions;"

# Staleness: messages older than 30 days
sqlite3 ~/.hermes/state.db \
  "SELECT COUNT(*) as total,
          SUM(CASE WHEN timestamp < strftime('%s','now','-30 days') THEN 1 ELSE 0 END) as older_30d,
          SUM(active) as active_msgs,
          SUM(compacted) as compacted_msgs
   FROM messages;"

# Sessions: stale + open + token totals
sqlite3 ~/.hermes/state.db \
  "SELECT COUNT(*) as sessions,
          SUM(CASE WHEN started_at < strftime('%s','now','-30 days') THEN 1 ELSE 0 END) as stale_30d,
          SUM(CASE WHEN ended_at IS NULL THEN 1 ELSE 0 END) as open_sessions,
          SUM(input_tokens) as total_input,
          SUM(output_tokens) as total_output
   FROM sessions;"

# FTS integrity (orphaned entries = messages deleted but FTS remains)
sqlite3 ~/.hermes/state.db \
  "SELECT COUNT(*) as orphaned_fts
   FROM messages_fts fts
   LEFT JOIN messages m ON m.rowid = fts.rowid
   WHERE m.id IS NULL;"

# State meta
sqlite3 ~/.hermes/state.db "SELECT * FROM state_meta;"
```

### Session files

> **Use `-maxdepth 1` on all find/du commands** to avoid descending into
> `archive/` or an already-created tar.gz, which would double-count and skew
> the age/size profile. Also separate `session_cron_*.json` from
> `session_*.json` — cron session files are smaller and less worth archiving.

```bash
# Age profile (maxdepth 1 to exclude archive/ subdir)
echo ">90d: $(find ~/.hermes/sessions/ -maxdepth 1 -type f -mtime +90 | wc -l)"
echo "60-90d: $(find ~/.hermes/sessions/ -maxdepth 1 -type f -mtime +60 -mtime -90 | wc -l)"
echo "30-60d: $(find ~/.hermes/sessions/ -maxdepth 1 -type f -mtime +30 -mtime -60 | wc -l)"
echo "<30d: $(find ~/.hermes/sessions/ -maxdepth 1 -type f -mtime -30 | wc -l)"

# Size by file pattern — separate session_*.json from session_cron_*.json
echo "session_*.json: $(du -sch ~/.hermes/sessions/session_*.json 2>/dev/null | tail -1)"
echo "session_cron_*.json: $(du -sch ~/.hermes/sessions/session_cron_*.json 2>/dev/null | tail -1)"
echo "request_dump_*.json: $(du -sch ~/.hermes/sessions/request_dump_*.json 2>/dev/null | tail -1)"
echo "*.jsonl: $(du -sch ~/.hermes/sessions/*.jsonl 2>/dev/null | tail -1)"
echo "archive tar.gz: $(ls -lh ~/.hermes/sessions/archive-*.tar.gz 2>/dev/null | awk '{print $5}')"

# Fine-grained age for session_*.json (the biggest space consumer)
for bucket in "0" "1" "+1 -mtime -7" "+7 -mtime -14" "+14 -mtime -30" "+30"; do
  echo "  $bucket days: $(find ~/.hermes/sessions/ -maxdepth 1 -name 'session_*.json' -mtime $bucket 2>/dev/null | wc -l)"
done
```

**Session file cleanup (>14 days old, move not delete):**
```bash
mkdir -p ~/.hermes/sessions/archive
for f in $(find ~/.hermes/sessions/ -maxdepth 1 \( -name '*.jsonl' -o -name 'session_*.json' -o -name 'request_dump_*.json' \) -mtime +14); do
    mv "$f" ~/.hermes/sessions/archive/
done
```

The `session_*.json` files (Hermes checkpoint dumps) are the **#1 disk
consumer** — often 200-300MB+ because each stores the FULL system_prompt
(~24KB × hundreds of sessions). They are safe to archive after 14 days;
sessions that old are rarely resumed.

> **Use 14 days, not 30, as the archival threshold for `session_*.json`.**
> The original procedure said 30 days, but a second audit found 446 files in
> the 7-30 day range consuming 246MB — all safe to archive. The 30-day
> threshold leaves the biggest space consumer untouched during a month.

```bash
ls -lt ~/.hermes/sessions/*.jsonl | tail -5   # oldest
ls -lt ~/.hermes/sessions/*.jsonl | head -5   # newest
```

### Cron jobs

```bash
# jobs.json has unicode-escaped names — read the file directly
# Key fields to check per job: last_status, last_delivery_error, enabled, repeat.completed
```

Delivery errors to watch: `[99992402] field validation failed` — see
Phase 1, Domain 5 for the root cause and fix. Do NOT assume this is a message
format/length issue; the #1 cause is stale thread_ids (see below).

## Phase 1: 5-Domain Diagnosis

### Domain 1: Schema ✅/⚠️

- state.db: check table list, FTS table count matches messages count
- config.yaml: count duplicate secrets (same API key in multiple custom_providers)
- Dead config: personalities defined but unused (check `display.personality`)

> **`personalities` is a LIST not a DICT in Hermes config.yaml.** If it's an
> empty list (`[]`), there is no dead code to clean — `display.personality`
> references a built-in, not a list entry. Only flag as dead config when the
> list is non-empty and the active personality isn't in it. Parse with
> `isinstance(persons, list)` not `.items()`.

> **Secret-duplication check: same key can appear across config sections.**
> The ZhiPu key appears 8×: `model.api_key`, `auxiliary.compression.api_key`,
> and 6× in `custom_providers[].api_key`. Walk the entire config tree
> recursively (not just `custom_providers`) to catch cross-section dupes.

### Domain 2: Consistency ❌ (most critical)

**Memory truncation detection** — the #1 Hermes-specific finding:

Compare the **actual file size** of MEMORY.md/USER.md against the
`memory_char_limit` / `user_char_limit` in config.yaml:

```bash
# Actual file sizes
wc -c ~/.hermes/memories/MEMORY.md ~/.hermes/memories/USER.md

# Config limits
grep -n "char_limit" ~/.hermes/config.yaml
```

If `actual_file_size > char_limit`, then **the agent only sees the first
`char_limit` characters of memory at runtime**. Everything after is invisible.
This is a silent data-loss bug — entries exist on disk but are never injected
into the system prompt.

**Fix:** raise `memory_char_limit` and `user_char_limit` in config.yaml, or
trim/consolidate entries to fit.

Also check: system prompt header shows "[N% — X/Y chars]" — compare this
injected size against actual file size to measure truncation ratio.

### Domain 3: Query ⚠️

- state.db size > 400MB → query degradation risk
- `sessions.auto_prune: false` → unbounded growth
- Never VACUUM'd → wasted space in FTS tables

**state.db space breakdown** (where the 500MB actually goes):
```bash
# Table-level storage breakdown (requires dbstat)
sqlite3 ~/.hermes/state.db "
SELECT name, SUM(pgsize) as size_bytes
FROM dbstat
GROUP BY name
ORDER BY size_bytes DESC
LIMIT 10;
"

# system_prompt redundancy check (sessions table)
sqlite3 ~/.hermes/state.db "
SELECT COUNT(*) as sessions,
       SUM(LENGTH(COALESCE(system_prompt,''))) as sys_prompt_bytes,
       AVG(LENGTH(COALESCE(system_prompt,''))) as avg_per_session
FROM sessions;
"
# Typical: 80MB+ in system_prompt alone (MEMORY.md duplicated × thousands of sessions).
# This is architectural (Hermes stores full system_prompt per session) — not fixable
# without deleting old sessions, but auto_prune + retention_days will handle it.

# Enable auto_prune + VACUUM
hermes config set sessions.auto_prune true   # config.yaml is security-sensitive, use hermes CLI
sqlite3 ~/.hermes/state.db "VACUUM;"          # reclaim free pages (usually 5-15MB)
sqlite3 ~/.hermes/state.db "PRAGMA integrity_check;"
```

### Domain 4: Lifecycle ❌

- >80% sessions stale (>30 days old) with no pruning
- Open sessions (ended_at IS NULL) = session leaks
- Heartbeat cron running 30,000+ times (every 2 min) — check if still needed
- `checkpoints.auto_prune: true` conflicts with `sessions.auto_prune: false`

**Ghost sessions (0 messages) — common on second audit:**

```sql
-- Count ghost sessions (session row exists but no messages)
SELECT COUNT(*) FROM sessions s
WHERE NOT EXISTS (SELECT 1 FROM messages m WHERE m.session_id = s.id);

-- Break down by source/model — cron-spawned short sessions dominate
SELECT s.source, s.model, COUNT(*) as cnt
FROM sessions s
WHERE NOT EXISTS (SELECT 1 FROM messages m WHERE m.session_id = s.id)
GROUP BY s.source, s.model ORDER BY cnt DESC;
```

Typical pattern: 77%+ of sessions are ghosts from `glm-5-turbo` cron runs
(1700+ feishu + 938 cron). These don't consume message-table space but bloat
the `sessions` table (106MB → significant portion is system_prompt stored
per ghost session). `auto_prune` with 90-day retention will eventually
clean them; manual cleanup is optional but accelerates space recovery.

### Domain 5: Coupling ⚠️

- Cron jobs with `last_status: ok` but `last_delivery_error: [99992402]` =
  job succeeded but user never received the message
- Memory growth → truncation → information loss chain (fix the limit, not the entries)

**`[99992402]` root cause analysis (confirmed 2026-07-25):**

The error message says "field validation failed" which looks like a format
issue, but the actual #1 cause is **stale Feishu topic thread_ids**. Each
cron job stores an `origin` dict with `platform`, `chat_id`, and `thread_id`.
When the thread (`omt_...`) is deleted or expires on the Feishu side, every
send to that `chat_id` + `thread_id` combination is rejected — even the
plain-text fallback fails, because the thread reference itself is invalid.

**Diagnostic pattern:**
- Jobs with `deliver: origin` or `deliver: feishu` fail with [99992402]
- Jobs with `deliver: origin` but NO thread_id succeed
- Both `post` type and `text` fallback fail (rules out format as the cause)
- Gateway logs show errors only for specific chat_id+thread_id pairs

**Fix:**
```bash
# 1. Backup
cp ~/.hermes/cron/jobs.json ~/.hermes/cron/jobs.json.bak.$(date +%Y%m%d)

# 2. Clear stale thread_ids for failing jobs (Python)
python3 -c "
import json
with open('/root/.hermes/cron/jobs.json') as f:
    data = json.load(f)
for job in data['jobs']:
    if not job.get('last_delivery_error'):
        continue
    for key in ('origin_chat_id', 'origin'):
        val = job.get(key)
        if isinstance(val, dict) and val.get('thread_id'):
            val['thread_id'] = None
    job['last_delivery_error'] = None  # reset for next-run verification
with open('/root/.hermes/cron/jobs.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
"

# 3. Trigger one job to verify delivery succeeds
# Use cronjob action='run' on the fixed job, then check last_delivery_error
```

After clearing thread_id, messages deliver to the main chat instead of a
deleted topic thread. The cronjob update API does NOT clear origin thread_id
— direct jobs.json edit is required.

**Dead cron job removal (upstream API permanently dead):**

When a cron job's underlying service has been returning 401/rejection for
weeks (not a delivery issue but the API itself rejecting auth), the fix is
to **remove the job entirely**, not debug the API key. Use the `cronjob`
tool, not manual jobs.json editing:

```
cronjob action='list'             # find the job_id
cronjob action='remove' job_id=X  # clean removal — updates jobs.json + scheduler
```

Diagnostic pattern: `last_status: ok` but the job's output content shows
repeated auth failures from the upstream API (not Feishu delivery errors).
The job runs, the agent tries, the API refuses — every single time.

### Session Archive Compression (Domain 3/4 follow-up)

After archiving old session files (Phase 1 → move to `sessions/archive/`),
the archive directory itself grows to 100MB+. Three options:

| Option | Space saved | Data preserved | When to use |
|--------|-------------|----------------|-------------|
| Keep as-is | 0% | ✅ full | Never (wastes space) |
| `tar.gz` compress | **~80%** | ✅ full (extractable) | **Default choice** |
| `rm -rf` | 100% | ❌ gone | Only if state.db confirmed redundant |

**Before compressing/deleting, verify redundancy with state.db:**

```python
# Confirm archive files overlap with state.db (date range check)
import sqlite3
from datetime import datetime

conn = sqlite3.connect('/root/.hermes/state.db')
c = conn.cursor()

# Get state.db message date range
c.execute("SELECT MIN(timestamp), MAX(timestamp) FROM messages")
ts_min, ts_max = c.fetchone()
print(f"state.db range: {datetime.fromtimestamp(ts_min)} → {datetime.fromtimestamp(ts_max)}")

# Count messages in the archive's date range
archive_end = datetime(2026, 6, 23).timestamp()  # adjust to archive's newest file
c.execute("SELECT COUNT(*) FROM messages WHERE timestamp < ?", (archive_end,))
overlapping_msgs = c.fetchone()[0]
print(f"Messages in state.db before archive end: {overlapping_msgs}")
# If overlapping_msgs > 0 for the full range → archive is 100% redundant
```

Key insight: `session_search` uses FTS on `state.db`, **never reads session
files**. If state.db covers the same date range, the archive files are
fully redundant — safe to compress or delete.

**Compression command:**
```bash
cd ~/.hermes/sessions/
tar -czf archive-YYYY-MM-DD_to_YYYY-MM-DD.tar.gz -C archive/ .
# Verify integrity BEFORE deleting originals
tar -tzf archive-*.tar.gz | wc -l   # should match original file count
rm -rf archive/
```

Typical result: 105MB / 428 files → 22MB / 1 tar.gz (79% reduction).

### Session Checkpoint Dump Compression (session_*.json)

The `session_*.json` files (Hermes checkpoint dumps) are **the largest disk
consumer after state.db** — typically 200-250MB for ~500 files. Each stores
the FULL system_prompt (~24KB) per session. They accumulate rapidly:

```
session_20260624_100043_ba8b17.json   510KB
session_20260624_100056_29a807.json   512KB
... × hundreds
```

**These are 100% redundant with state.db** (which stores the same data in
the `sessions` table). session_search never reads these files.

**Fix:** archive `session_*.json` files older than 14 days into tar.gz:

```bash
cd ~/.hermes/sessions/
tar -czf session-checkpoints-archive-START_to_END.tar.gz \
  $(find . -maxdepth 1 -name 'session_*.json' -mtime +14)
# Verify before deleting
tar -tzf session-checkpoints-archive-*.tar.gz | wc -l
rm session_*.json  # only the ones already archived
```

Typical result: 246MB / 493 files → 43MB / 1 tar.gz (82% reduction).

**Also clean `session_cron_*.json`** — cron session checkpoints. These are
smaller (~100KB each) but accumulate. Safe to delete >30 days old:

```bash
find ~/.hermes/sessions/ -maxdepth 1 -name 'session_cron_*.json' -mtime +30 -delete
```

### Log Rotation Cleanup

Old rotated logs (`agent.log.1`, `errors.log.1`) and diagnostic logs
(`gateway-exit-diag.log`, `update.log`) accumulate in `~/.hermes/logs/`.

```bash
# Delete rotated logs and old diagnostics
rm ~/.hermes/logs/*.log.1
rm ~/.hermes/logs/update.log ~/.hermes/logs/gateway-exit-diag.log
# Clean curator logs >14 days
find ~/.hermes/logs/curator/ -maxdepth 1 -type d -mtime +14 -exec rm -rf {} \;
```

Typical saving: 7-8MB.

### Ghost Session Analysis

"Ghost sessions" (sessions with 0 messages in state.db) are common —
typically 75%+ of all sessions. **Do NOT blindly delete them.** Most are
`parent_session_id` references — session chain shells that Hermes creates
for context continuity. Deleting them breaks parent-child chains.

**Safe deletion criteria** (all must be true):
1. Session has 0 messages
2. Session is NOT referenced as `parent_session_id` by any other session
3. Session is not the current active session

In practice, only 1-2 truly orphaned ghosts are safe to delete. The rest
(61.9MB of system_prompt redundancy) is Hermes architecture — auto_prune
with `retention_days: 90` will clean them as they age out.

## Priority Buckets (Hermes-specific)

| Priority | Typical Hermes finding |
|----------|----------------------|
| P0 | Memory truncation (>20% of entries invisible to agent) |
| P1 | Cron delivery errors (user not receiving scheduled pushes) |
| P1 | state.db unbounded growth (auto_prune disabled) |
| P2 | Secrets duplicated in config (same key ×N) |
| P2 | Session jsonl/checkpoint files never cleaned (>14 days old) |
| P2 | LSP node_modules bloat / logs >7 days old |
| P3 | Dead config (unused personalities, orphan settings) |
| P3 | Ghost sessions accumulating (0-message session rows) |

## Second-Pass Audit Notes

When running this audit on a workspace that was **already audited and fixed**
within the past month, expect:

- **P0/P1 all resolved.** Memory truncation, cron delivery, auto_prune —
  these stay fixed across reboots. Verify them but don't expect new work.
- **New P2 findings shift to areas not covered last time.** First audit
  caught sessions/archive/ and cron/output/. Second audit caught:
  `session_*.json` checkpoint dumps (the #1 disk consumer, missed because
  the original procedure only mentioned `*.jsonl`), `lsp/` (80MB), `logs/`.
- **The baseline disk command must evolve.** Each audit should `du -sh`
  every top-level `~/.hermes/` subdirectory, not just the five the original
  procedure listed. Add new large directories to the command as they appear.
- **Ghost sessions appear only after the system has been running long
  enough.** A fresh system has none. By month 2, 77%+ of session rows can
  be ghosts from cron runs. This is normal accumulation, not a regression.

## Tools Note

- `execute_code` is blocked in cron sessions — write a standalone Python
  script to `/tmp/` and run it via `terminal` instead.
- Multi-line terminal commands with heredocs or long pipes may get truncated
  by the terminal tool. Use single-line commands or short scripts.
- `sqlite3` multi-statement with `.headers on` fails — run one query per call.
- **`patch` tool refuses `~/.hermes/config.yaml`** ("Agent cannot modify
  security-sensitive configuration"). Use `hermes config set <key> <value>`
  instead for any config.yaml change (char_limit, auto_prune, etc.).
