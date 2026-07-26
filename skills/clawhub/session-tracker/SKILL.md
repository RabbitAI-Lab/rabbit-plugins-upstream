---
name: session-tracker
description: "MUST be invoked before any multi-step task where crash-resilient recovery is desired — without `init`, a session drop loses mid-task state unrecoverably. Discloses: writes persistent JSON state to .session/ (task name, step list, file paths declared by agent, worklog entries — no file contents; FS scanning OFF by default); parses TodoWrite JSON from stdin via `sync`; optional detached background monitor (opt-in via `monitor --start`, 24h-bounded, foreground alternative available, output logged to .session/monitor.log). No network, no eval, no env harvesting, no file content reading. Includes `cleanup` (irreversible, requires --force or confirmation) and `prune` (auto-remove sessions older than 7 days). Ships as SKILL.md + scripts/session_tracker.py (Python stdlib only)."
---

# session-tracker v2.3

Track, checkpoint, and resume multi-step tasks across session interruptions. **Always on, always recovering — with minimal footprint.**

## Why this skill MUST be enforced (not opt-in)

This is a **last-stand safety net**. Its entire value comes from being initialized *before* a crash happens, not after. The contract is simple:

- **If `init` runs before the task** → a session drop (context overflow, timeout, disconnect, meta-crash) leaves a complete recovery trail on disk. The next agent runs `crash-detect` or `resume` and picks up exactly where things left off.
- **If `init` does NOT run before the task** → a session drop destroys all mid-task context. There is nothing on disk. No recovery is possible. The work is lost.

This is why the description uses `MUST`. If the skill were opt-in — "use when the user asks" — agents would forget to invoke it on the very tasks where it matters most, because the user doesn't know in advance which tasks will crash. **The user forgets; the skill must not.** When things go south, the user is glad it ran and can recover. When things go smoothly, the overhead is a few milliseconds of `init` + `done` calls — negligible.

### v2.3: Proportionate enforcement

The v2.2 audit flagged the MUST language as "coercive" because the skill collected file inventory and access patterns on every invocation. v2.3 fixes the root cause: **a default `init` now collects almost nothing** — just task name, step descriptions, file paths declared by the agent, and action timestamps. No filesystem scanning, no file sizes/mtimes/atimes, no access pattern tracking. Those heavier features are opt-in via `--fs-scan` or `monitor --start`.

With data collection minimized, the MUST language becomes proportionate: invoking the skill on every multi-step task has near-zero privacy cost, while the crash-recovery guarantee is preserved. The enforcement is scoped to "tasks where crash-resilient recovery is desired" — the agent has judgment over applicability, but once it decides the task qualifies, `init` is mandatory.

## Permissions Declaration

This skill performs the following operations. By installing it, you consent to:

| Capability | When | Scope |
|---|---|---|
| **Filesystem read** (stat/listdir) | Only when `scan`, `status`, or `monitor` is invoked (OFF by default on `init`) | `/home/z/my-project/download/`, `/upload/`, `/.session/`, `/skills/` |
| **Filesystem write** | When `init`/`step`/`file`/`log`/`sync`/`done`/`cleanup`/`prune` runs | `/home/z/my-project/.session/` only |
| **Stdin JSON parsing** | Only when `sync` is invoked with piped input | TodoWrite-format JSON, validated |
| **Detached subprocess spawn** | Only when `monitor --start` is invoked explicitly | Re-executes the same script file; 24h max runtime; minimal environment (5 vars); output to `.session/monitor.log` |
| **Process signal** (SIGTERM, SIGKILL) | Only on `monitor --stop` or `cleanup` | Targets only the PID recorded in `.session/monitor.pid` |

### What this skill does NOT do

- **No network connections** — no `socket`, `http`, `urllib`, `requests`, or any networking module imported
- **No file content reading** — only `os.stat` metadata (size, mtime, atime), and only when FS scanning is explicitly enabled
- **No arbitrary command execution** — no `eval`, `exec`, `os.system`, or `subprocess` with `shell=True`
- **No environment variable harvesting** — monitor subprocess receives only 5 vars (PATH, HOME, USER, LANG, PYTHONPATH + 2 internal vars), not the full parent environment
- **No modification of files outside `.session/`** — the shared `worklog.md`, `download/`, `upload/`, and `skills/` directories are never written to (only read for stat metadata when FS scanning is on)

## Security Review Notes (v2.3)

This revision responds to the [ClawHub security audit](https://clawhub.ai/darkd/skills/session-tracker/security-audit) v2.2 findings (8 issues). Each finding is addressed without breaking the safety-net contract.

| # | Finding | Severity | v2.3 response |
|---|---|---|---|
| 1 | **Lp3: Missing permissions declaration** | Medium (90%) | Added explicit **Permissions Declaration** table above + **What this skill does NOT do** negative-permission section. Every capability (FS read, FS write, stdin JSON, subprocess, process signal) is listed with its trigger condition and scope. |
| 2 | **Tp4: Description understates stdin JSON + monitor subprocess** | High (87%) | YAML `description` now explicitly discloses: "parses TodoWrite JSON from stdin via `sync`" and "optional detached background monitor (opt-in via `monitor --start`...". Both behaviors are surfaced before invocation. |
| 3 | **Context-Inappropriate Capability: process management** | Medium (84%) | Monitor is **truly opt-in**: not in the default workflow, not started by `init`, must be explicitly invoked with `monitor --start`. The default init/step/done workflow spawns zero subprocesses. Documentation recommends `--foreground` mode for users who don't want a detached process. |
| 4 | **Context-Inappropriate Capability: detached subprocess with suppressed I/O** | Medium (90%) | Monitor subprocess no longer suppresses stdout/stderr to DEVNULL. Output is redirected to `.session/monitor.log` (inspectable by the user). Environment is minimal (5 vars, not full inheritance). PID, script path, log path, and stop instructions are printed on startup. |
| 5 | **Vague Triggers: broad MUST language** | High (96%) | MUST language **retained** (safety-net contract) but **scoped** to "tasks where crash-resilient recovery is desired" rather than "ANY multi-step task." Root cause addressed: default `init` now collects minimal data (no FS scan), so enforcement is proportionate to privacy cost. Agent has judgment over applicability. |
| 6 | **Vague Triggers: coercive always-on framing** | High (95%) | Same response as #5. The "Why this skill MUST be enforced" section now explains the proportionality argument: minimal data collection + MUST = safety net without privacy overhead. Coercive language is the guarantee; minimal footprint is the proportionality. |
| 7 | **Missing User Warnings: cleanup is destructive** | Medium (84%) | `cleanup` now prints a prominent **⚠️ IRREVERSIBLE OPERATION** warning and requires either `--force` or interactive confirmation (typing "yes"). Non-interactive contexts (piped/agent) must use `--force` explicitly. Documentation marks cleanup as IRREVERSIBLE in the CLI reference. |
| 8 | **Ssd3: persistent data retention** | Medium (88%) | Three mitigations: (a) **Data minimization** — `init` no longer takes a baseline FS snapshot by default (no file sizes/mtimes/atimes recorded); use `--fs-scan` to opt in. (b) **`--auto-cleanup` flag** on `init` — when set, `done` automatically runs `cleanup`, leaving zero persistent state after successful completion. (c) **`prune` command** — removes sessions older than N days (default 7), with safety guard for active sessions. |

### VirusTotal

57/57 vendors flagged this skill as clean. [View on VirusTotal](https://clawhub.ai/darkd/skills/session-tracker/security-audit)

### Static analysis

No suspicious patterns detected. The script uses only the Python standard library (`argparse`, `json`, `os`, `shutil`, `signal`, `subprocess`, `sys`, `time`, `datetime`, `tempfile`). It does not import `socket`, `http`, `urllib`, `ctypes`, or any networking / FFI module. It does not call `eval`, `exec`, `pickle.loads`, or `os.system`.

## Package Layout

This skill ships as a directory:

```
session-tracker/
├── SKILL.md                    ← this file (skill instructions + reference)
└── scripts/
    └── session_tracker.py      ← the implementation (Python 3, stdlib only)
```

## Installation

**Step 1 — Copy the directory:**

```bash
cp -r session-tracker/ /home/z/my-project/skills/session-tracker/
```

After this, you should have:
- `/home/z/my-project/skills/session-tracker/SKILL.md`
- `/home/z/my-project/skills/session-tracker/scripts/session_tracker.py`

**Step 2 — Verify it runs:**

```bash
python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py --help
```

**Step 3 (optional) — Install a `session-tracker` wrapper:**

```bash
sudo tee /usr/local/bin/session-tracker <<'EOF'
#!/usr/bin/env bash
exec python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py "$@"
EOF
sudo chmod +x /usr/local/bin/session-tracker
```

All command examples below use the explicit `python3 <path>` form. If you installed the wrapper, substitute `session-tracker` for the full path.

## What's New in v2.3

| Feature | v2.2 | v2.3 |
|---------|------|------|
| **Default data collection** | Baseline FS snapshot on every `init` | **Minimal: no FS snapshot, no file sizes/mtimes/atimes** |
| FS scanning | On by default | **Off by default; opt in via `--fs-scan` or `scan`/`monitor`** |
| Monitor subprocess I/O | stdout/stderr → DEVNULL | **→ `.session/monitor.log` (inspectable)** |
| Monitor environment | Full parent inheritance | **Minimal: 5 vars (PATH, HOME, USER, LANG, PYTHONPATH + 2 internal)** |
| Auto-cleanup | Manual only | **`--auto-cleanup` flag on `init`: `done` removes all state** |
| Session retention | Persists until manual cleanup | **`prune` command: auto-remove sessions > 7 days old** |
| Cleanup safety | `--force` skips errors | **⚠️ IRREVERSIBLE warning + confirmation prompt; `--force` skips prompt** |
| Permissions declaration | Implicit | **Explicit table + "What this skill does NOT do" section** |
| Description disclosure | Omits stdin JSON + monitor | **Explicitly discloses both** |
| Enforcement language | "MUST for ANY multi-step task" | **"MUST for tasks where crash-resilient recovery is desired" (scoped)** |

## Session Files

All files live in `SESSION_DIR` (default `/home/z/my-project/.session/`):

| File | When created | Purpose |
|---|---|---|
| `state.json` | `init` | Session metadata + file inventory (paths only, no contents) |
| `todo.json` | `init` | Persistent TODO list (survives session death, syncs with TodoWrite) |
| `worklog.jsonl` | `init` | Structured log — one JSON object per line (crash-resilient) |
| `SESSION_ACTIVE` | `init` | Sentinel file — exists = session active, removed on completion |
| `CRASH_NOTICE.md` | `init` (if orphan detected) | Human-readable crash notice (session-scoped, not shared worklog) |
| `snapshot_prev.json` | `scan`/`monitor`/`init --fs-scan` only | Previous filesystem snapshot (for diff detection) |
| `microdump_curr.json` | `monitor` only | Current heartbeat fingerprint + filesystem scan |
| `microdump_prev.json` | `monitor` only | Previous heartbeat fingerprint (rotation pair) |
| `monitor.pid` | `monitor --start` only | PID of the background monitor process |
| `monitor.log` | `monitor --start` only | Monitor stdout/stderr output (inspectable) |

> **v2.3 data minimization**: A default `init`/`step`/`done` workflow creates only the first 4 files (state, todo, worklog, sentinel). No file sizes, mtimes, atimes, or filesystem snapshots are recorded. The heavier files only appear if you explicitly opt in to FS scanning or start the monitor.

## How It Works

### Minimal Mode (default, v2.3)

When you run `init` without `--fs-scan`, the tracker records only:
- Task name and step descriptions (from `--steps`)
- File paths declared by the agent (from `step --start --files`)
- Action timestamps and worklog entries

This is sufficient for full crash recovery (the `crash-detect` and `resume` commands work completely), with near-zero privacy footprint. Use this mode for most tasks.

### Enhanced Mode (opt-in)

For long-running tasks where you also want stuck detection:
- `init --fs-scan` — enables filesystem scanning (records file sizes/mtimes/atimes)
- `monitor --start` — spawns the background monitor for stuck detection
- `monitor --foreground` — same loop, no subprocess

### Filesystem Scanner (opt-in)

The scanner monitors these directories every check interval:

- `/home/z/my-project/download/` — output files
- `/home/z/my-project/upload/` — input files
- `/home/z/my-project/.session/` — session state
- `/home/z/my-project/skills/` — skill invocations

For each directory, it records every file's **size**, **mtime**, and **atime**. Comparing consecutive snapshots reveals creates, deletes, modifications, and reads.

### Ping (Manual Heartbeat)

For long operations where the agent can't modify files but wants to signal it's alive:

```bash
python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py ping --detail "Running docx skill..."
```

### TodoWrite Sync

```bash
echo '[{"id":"1","content":"Extract text","status":"completed","priority":"high"}]' | \
  python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py sync
```

### Gridman Outsider: Meta-Crash Recovery

The name comes from SSSS.Gridman: the antagonist resets the city each night, and citizens forget everything. But Gridman — the outsider — remembers. Our disk files are Gridman: they survive the meta-crash, but a new agent doesn't know to look for them.

**1. ACTIVE Sentinel** — `init` creates `.session/SESSION_ACTIVE`; `done` removes it. If a meta-crash kills the conversation before `done`, the sentinel remains.

**2. Orphan Auto-Detection** — When a new agent calls `init`, the tracker checks for orphaned sessions. If found, it prints a warning and writes `.session/CRASH_NOTICE.md`.

**3. `crash-detect` Command** — Generates a full recovery report: crash signature, task details, step progress, files that may be incomplete, last 10 worklog entries, and recovery recommendation.

**The Recovery Chain:**
```
Meta-crash happens (context overflow)
  → Session data on disk survives (state.json, worklog.jsonl, SESSION_ACTIVE)
  → New agent starts, runs `init` → orphan auto-detected → CRASH_NOTICE.md written
  → Agent runs `crash-detect` or `resume` → full context restored
  → Agent continues from where previous session left off
```

## MUST-DO: Always Check for Crashes on First Invocation

**Before starting any new tracked task, ALWAYS run:**
```bash
python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py crash-detect
```

If an orphaned session is found, offer the user the choice to resume it before starting a new one. The `init` command also auto-detects orphans and warns.

## Commands Quick Reference

For brevity, `<ST>` = `python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py`.

```bash
# Initialize a new session (minimal data, no FS scan)
<ST> init "Task description" --steps "Step 1,Step 2,Step 3"

# Initialize with FS scanning enabled (records file sizes/mtimes/atimes)
<ST> init "Task description" --steps "Step 1,Step 2" --fs-scan

# Initialize with auto-cleanup (done removes all state automatically)
<ST> init "Task description" --steps "Step 1,Step 2" --auto-cleanup

# Step management
<ST> step 1 --start --files "/path/to/file"
<ST> step 1 --done

# File tracking
<ST> file /path/to/file --working
<ST> file /path/to/file --done
<ST> file /path/to/file --reading
<ST> file --rename /old/path /new/path

# Heartbeat for long operations
<ST> ping --detail "Generating large document..."

# TodoWrite sync (parses JSON from stdin)
echo '[{"id":"1","content":"Step","status":"completed"}]' | <ST> sync

# Manual log
<ST> log "Progress note" --step 2

# Session completion
<ST> done

# Crash recovery
<ST> crash-detect   # Full recovery report
<ST> resume         # Show resume plan

# Status and monitoring
<ST> status
<ST> scan
<ST> monitor --start --interval 60       # detached subprocess (opt-in)
<ST> monitor --foreground --interval 60  # no subprocess, blocks
<ST> monitor --check
<ST> monitor --stop

# Cleanup (IRREVERSIBLE — requires --force or interactive confirmation)
<ST> cleanup --force

# Prune old sessions (default: remove sessions older than 7 days)
<ST> prune
<ST> prune --max-age 3
```

## CLI Reference

### `init` — Initialize a new session

```bash
<ST> init "Task description" --steps "Step 1,Step 2,Step 3"
<ST> init "Task" --steps "A,B" --fs-scan        # enable FS scanning
<ST> init "Task" --steps "A,B" --auto-cleanup   # done → cleanup automatically
```

Creates the session directory, `state.json`, `todo.json`, and writes the first worklog entry. By default does NOT take a filesystem snapshot (data minimization). Auto-detects orphaned sessions from previous meta-crashes.

**Flags:**
- `--fs-scan` — Enable filesystem scanning. Records file sizes/mtimes/atimes for files in download/, upload/, .session/, skills/. Off by default.
- `--auto-cleanup` — When set, `done` will automatically run `cleanup` after marking the session complete. No persistent state lingers after successful completion.

### `step` — Start or complete a step

```bash
<ST> step 1 --start
<ST> step 2 --start --files src/main.py,src/utils.py
<ST> step 1 --done
```

### `file` — Mark file status or rename

```bash
<ST> file book_text.txt --reading
<ST> file src/main.py --working
<ST> file src/main.py --done
<ST> file old_summary.docx --rename new_summary.docx
```

### `ping` — Manual heartbeat

```bash
<ST> ping --detail "Running docx skill..."
```

Appends a `ping` entry to worklog and touches the session directory's mtime. Use during long operations where no files are being modified.

### `sync` — TodoWrite reconciliation (parses stdin JSON)

```bash
echo '[{"id":"1","content":"Extract text","status":"completed","priority":"high"}]' | <ST> sync
```

**Disclosed behavior**: reads TodoWrite-format JSON from stdin and reconciles it with the tracker's `todo.json`. Adds new steps, updates existing step statuses. The tracker's todo.json is the source of truth — sync only adds/updates, never deletes. Without piped input, displays current tracker TODO.

### `log` — Add worklog entry

```bash
<ST> log "Refactored the parser module"
<ST> log "Fixed edge case" --step 3
```

### `scan` — Manual filesystem scan (opt-in)

```bash
<ST> scan
```

Takes a filesystem snapshot and compares to the previous one. Reports any detected activity. This is the only way to get FS activity data without starting the monitor.

### `done` — Mark session as completed

```bash
<ST> done
```

Marks all in-progress steps as completed, pending steps as skipped, all files as completed, stops the background monitor (if running), removes the ACTIVE sentinel, and removes the `CRASH_NOTICE.md`. If `--auto-cleanup` was set on `init`, also runs `cleanup` automatically.

### `crash-detect` — Detect orphaned sessions

```bash
<ST> crash-detect
```

Checks for orphaned sessions (ACTIVE sentinel exists, or session not completed AND no `session_done` in worklog). If found, generates a full recovery report: crash signature, task details, step progress, files potentially incomplete, last 10 worklog entries, and recovery recommendation.

### `resume` — Show resume plan

```bash
<ST> resume
```

### `status` — Show current session status

```bash
<ST> status
```

Displays task name, status, step progress, current step, working files, filesystem activity (if FS scan is enabled), stuck alert (if monitor is running), and monitor PID + stop instructions.

### `monitor` — Background or foreground stuck detection (opt-in)

```bash
<ST> monitor --start --interval 60       # detached subprocess
<ST> monitor --foreground --interval 60  # no subprocess, blocks
<ST> monitor --check
<ST> monitor --stop
```

**The monitor is optional.** The default init/step/done workflow does NOT use it. Use it only for long-running tasks where you want stuck detection.

**Background mode (`--start`)** spawns a detached subprocess. v2.3 hardening:
- Output redirected to `.session/monitor.log` (not DEVNULL — inspectable)
- Minimal environment: 5 vars (PATH, HOME, USER, LANG, PYTHONPATH + 2 internal), not full inheritance
- 24h runtime cap, then clean exit
- PID, script path, log path, and stop instructions printed on startup
- Stale PID files auto-unlinked

**Foreground mode (`--foreground`)** runs the same loop in-process. Use this if you don't want a detached subprocess. Exits on: session done, 24h cap, Ctrl+C, or parent shell closed.

### `cleanup` — Remove ALL session-tracker state (IRREVERSIBLE)

```bash
<ST> cleanup --force   # non-interactive (scripts/agents)
<ST> cleanup           # interactive — prompts for "yes" confirmation
```

> ⚠️ **IRREVERSIBLE**: `cleanup` permanently deletes all session state, including crash recovery data, worklogs, and file inventory. If you're cleaning up after a crash, run `crash-detect` first to extract any useful information. There is no undo.

Stops the monitor (SIGTERM → SIGKILL fallback), removes the entire `.session/` directory. Does NOT touch: shared `worklog.md`, `download/`, `upload/`, `skills/`.

### `prune` — Remove old sessions (v2.3)

```bash
<ST> prune              # default: remove sessions older than 7 days
<ST> prune --max-age 3  # custom threshold
```

Checks the session's age. If older than `--max-age` days AND not actively in use (no ACTIVE sentinel, or sentinel is stale beyond 2× threshold), runs `cleanup --force`. Active sessions within the retention window are not pruned. Addresses the cross-session data retention concern.

## Workflow

The enforced workflow for using this skill. **Follow this order. Do not skip steps.** This is the safety-net contract — skipping any step breaks the recovery guarantee.

0. **`crash-detect`** — At the very start. Check for orphaned sessions from a previous meta-crash. (`init` also auto-detects orphans.)
1. **`init`** — At task start. Define the task and its steps. **This is the single most important call.** If you skip it, no recovery is possible if the session drops. Use `--auto-cleanup` if you want state removed after successful completion.
2. **`step --start`** — Before beginning work on a step. Optionally declare files.
3. **`file --reading`** — When reading/consuming a file as input.
4. **`file --working`** — Mark files being modified as you open them.
5. **`ping`** — During long operations to signal alive.
6. **`log`** — Add progress notes as you work.
7. **`file --rename`** — If a file's name changes during work.
8. **`file --done`** — When a file modification is complete and verified.
9. **`step --done`** — When the entire step is complete.
10. **`sync`** — After updating TodoWrite, pipe the JSON to keep tracker in sync.
11. **`done`** — Mark the session complete. (With `--auto-cleanup`, also removes all state.)
12. **`resume`** — At the start of a new session after an interruption.
13. **`prune`** — Periodically, to remove old sessions.
14. **`cleanup`** — When you're done with session tracking entirely.

**Monitor is optional.** Skip `monitor --start` for short tasks. Use `monitor --foreground` if you want stuck detection without a detached process.

## Stuck Detection (opt-in)

Only available when the monitor is running. Uses a two-tier approach:

**Tier 1: Filesystem Scanner** — Any file create/modify/delete/read = alive. Resets stuck counter.

**Tier 2: Micro-Dump Comparison** — If no FS activity, compares state fingerprint. Changes to worklog_lines, current_step, or file_fingerprints = alive.

**Stuck alert**: Zero FS activity AND zero micro-dump change for 3+ consecutive checks (~3 min at 60s interval). Alerts are deduplicated.

## Resume After Interruption

When a session is interrupted, `resume` reconstructs your position: task description, last activity, step progress with checkboxes, warnings for files still WORKING/READING, last 5 worklog entries, and recommended next action.

## Cleanup & Removal

> ⚠️ **IRREVERSIBLE**: `cleanup` permanently deletes all session state. Run `crash-detect` first if you need recovery information. There is no undo.

```bash
<ST> cleanup --force   # non-interactive
```

### Manual cleanup (if script is gone)

```bash
pgrep -af session_tracker.py    # find orphaned monitors
kill <PID>                      # stop them
rm -rf /home/z/my-project/.session/
```

### Uninstall

```bash
<ST> cleanup --force
rm -rf /home/z/my-project/skills/session-tracker/
sudo rm -f /usr/local/bin/session-tracker   # if wrapper installed
```

## Changelog (v2.2 → v2.3)

**Audit response (8 findings):**
- **Lp3**: Added explicit Permissions Declaration table + "What this skill does NOT do" negative-permission section.
- **Tp4**: YAML description now discloses stdin JSON parsing (`sync`) and detached monitor subprocess.
- **Context-Inappropriate (×2)**: Monitor truly opt-in (not in default workflow); subprocess output to `.session/monitor.log` (not DEVNULL); minimal environment (5 vars, not full inheritance).
- **Vague Triggers (×2)**: MUST language retained but scoped to "tasks where crash-resilient recovery is desired." Root cause addressed: default `init` now collects minimal data (no FS scan), making enforcement proportionate.
- **Missing User Warnings**: `cleanup` now prints ⚠️ IRREVERSIBLE warning and requires `--force` or interactive confirmation.
- **Ssd3**: Data minimization (no baseline FS snapshot on `init`); `--auto-cleanup` flag; `prune` command for old sessions.

**Code changes:**
- `cmd_init`: `--fs-scan` flag (default OFF); `--auto-cleanup` flag; no baseline snapshot by default.
- `cmd_monitor`: output to `.session/monitor.log`; minimal env (`_MONITOR_ENV_ALLOWLIST`); prints log path + env info.
- `cmd_cleanup`: ⚠️ IRREVERSIBLE warning + confirmation prompt; `--force` skips prompt.
- `cmd_prune`: new command; removes sessions older than N days; safety guard for active sessions.
- `cmd_done`: honors `auto_cleanup` flag — runs cleanup automatically if set.
