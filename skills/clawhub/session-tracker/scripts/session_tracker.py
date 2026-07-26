#!/usr/bin/env python3
"""
Session Tracker v2.3.0
======================
Track, checkpoint, and resume multi-step tasks across session interruptions.

v2.3 changes (second security audit response):
  - **Data minimization**: `init` no longer takes a baseline filesystem
    snapshot by default. The FS scanner only runs when `scan`, `status`,
    or `monitor` is explicitly invoked. A minimal init/step/done workflow
    now collects ONLY: task name, step descriptions, file paths (declared
    by the agent, not scanned), timestamps, and action worklog entries.
    No file sizes, mtimes, or atimes are recorded unless the user opts in
    to FS scanning via `--fs-scan` on init or by running `scan`/`monitor`.
  - **Monitor hardening**: background monitor subprocess no longer suppresses
    stdout/stderr to DEVNULL. Instead, output is redirected to
    `.session/monitor.log` so the user can inspect what the monitor is doing.
    Environment passed to the subprocess is now minimal (only the two
    _SESSION_TRACKER_LOOP_* vars + PATH/HOME/PYTHONPATH), not full inheritance.
  - **Auto-cleanup**: new `--auto-cleanup` flag on `init`. When set, `done`
    automatically runs `cleanup` after marking the session complete, so no
    persistent state lingers after a successfully completed task.
  - **Prune command**: new `prune` command removes sessions older than N days
    (default 7). Addresses the cross-session retention concern.
  - **Cleanup warning**: `cleanup` command now prints a prominent IRREVERSIBLE
    warning and requires either `--force` or interactive confirmation.
  - **Permissions declaration**: the skill markdown now includes an explicit
    Permissions Declaration section and a "What this skill does NOT do"
    negative-permission section.
  - **Description disclosure**: the YAML description now explicitly discloses
    stdin JSON parsing (`sync`), detached subprocess (`monitor --start`),
    and persistent local state — addressing the Tool Poisoning finding.
  - **Enforcement scoping**: the MUST language is retained (safety-net
    contract) but scoped to "tasks where crash-resilient recovery is desired"
    rather than "ANY multi-step task," giving the agent judgment over
    applicability while preserving the init-before-task guarantee.

v2.2 changes (first security review response):
  - All command examples use the explicit `python3 <path>/session_tracker.py` form.
  - New `cleanup` command: stops monitor, removes session dir + crash notice.
  - New `monitor --foreground` mode: runs the loop in the foreground.
  - Monitor loop is bounded: max 24h runtime, exits cleanly on session_done.
  - PID file hygiene: stale PID files (process dead) are unlinked automatically.
  - Crash notices are written to .session/CRASH_NOTICE.md, NOT to the shared
    project worklog.md.

v2.1 changes (Gridman Outsider):
  - ACTIVE sentinel file (SESSION_ACTIVE): crash detection across meta-resets
  - `crash-detect` command: full recovery report from orphaned sessions
  - Orphan auto-detection in `init`: warns about previous crashed sessions
  - Crash marker: any new agent sees the crash notice
  - Disk state survives meta-crashes (context overflow)

v2.0 changes:
  - Filesystem scanner: auto-detects file creates/edits/deletes/renames
  - `ping` command: manual heartbeat for long operations
  - `sync` command: bidirectional TodoWrite sync
  - `file --rename OLD NEW`: track file renames, update all references
  - `file --reading`: track files being read (not just written)
  - Enhanced monitor: uses filesystem activity as PRIMARY alive signal,
    micro-dump as fallback. Eliminates false "stuck" on slow-but-busy tasks.
  - Activity log: scanner auto-logs detected filesystem events to worklog

Files (all in SESSION_DIR, default /home/z/my-project/.session/):
  state.json          - Session metadata + file inventory
  todo.json           - Persistent TODO list (survives session death)
  worklog.jsonl       - Structured log, one JSON per line (crash-resilient)
  microdump_curr.json - Current micro-dump (heartbeat check)
  microdump_prev.json - Previous micro-dump (rotation pair)
  snapshot_prev.json  - Previous filesystem snapshot (for diff detection)
  monitor.pid         - PID of the background monitor process
  SESSION_ACTIVE      - Sentinel file: exists = session active, removed on completion
  CRASH_NOTICE.md     - Human-readable crash notice (shown by `init` when orphan found)

Commands:
  python3 session_tracker.py init "Task description" --steps "Step 1,Step 2,Step 3"
  python3 session_tracker.py step <id> --start [--files f1,f2]
  python3 session_tracker.py step <id> --done
  python3 session_tracker.py file <path> --working|--done|--reading
  python3 session_tracker.py file --rename <old_path> <new_path>
  python3 session_tracker.py ping [--detail "optional note"]
  python3 session_tracker.py sync
  python3 session_tracker.py log "Message"
  python3 session_tracker.py done
  python3 session_tracker.py resume
  python3 session_tracker.py crash-detect
  python3 session_tracker.py status
  python3 session_tracker.py scan
  python3 session_tracker.py monitor --start [--interval 60]
  python3 session_tracker.py monitor --foreground [--interval 60]
  python3 session_tracker.py monitor --stop
  python3 session_tracker.py monitor --check
  python3 session_tracker.py cleanup [--force]
"""

import argparse
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone

DEFAULT_DIR = "/home/z/my-project/.session"
PROJECT_ROOT = "/home/z/my-project"

STATE_FILE = "state.json"
TODO_FILE = "todo.json"
WORKLOG_FILE = "worklog.jsonl"
MICRODUMP_CURR = "microdump_curr.json"
MICRODUMP_PREV = "microdump_prev.json"
SNAPSHOT_PREV = "snapshot_prev.json"
MONITOR_PID_FILE = "monitor.pid"
ACTIVE_SENTINEL = "SESSION_ACTIVE"  # Created on init, removed on done — crash detector
CRASH_NOTICE = "CRASH_NOTICE.md"    # Human-readable crash notice (session-scoped)

STUCK_THRESHOLD = 3  # consecutive checks with zero activity = stuck
MAX_MONITOR_RUNTIME_S = 24 * 3600  # 24h hard cap; monitor exits after this
ORPHAN_IDLE_THRESHOLD_S = 30 * 60  # 30 min: status() only flags orphan if silent longer than this
DEFAULT_PRUNE_AGE_DAYS = 7  # prune removes sessions older than this

# Monitor log file (replaces stdout=DEVNULL so monitor output is inspectable)
MONITOR_LOG = "monitor.log"

# Minimal environment passed to the monitor subprocess (not full inheritance)
# Addresses the "inherited environment" concern from the audit.
_MONITOR_ENV_ALLOWLIST = (
    "PATH", "HOME", "USER", "LANG", "LC_ALL", "PYTHONPATH",
    "_SESSION_TRACKER_LOOP_DIR", "_SESSION_TRACKER_LOOP_INTERVAL",
)

# Directories the filesystem scanner monitors
SCAN_DIRS = [
    os.path.join(PROJECT_ROOT, "download"),
    os.path.join(PROJECT_ROOT, "upload"),
    os.path.join(PROJECT_ROOT, ".session"),
    os.path.join(PROJECT_ROOT, "skills"),
]

# Max files per directory to stat (prevents slowdown on huge dirs)
MAX_FILES_PER_DIR = 500


# ── Helpers ──────────────────────────────────────────────────────────────────

def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _path(session_dir, filename):
    return os.path.join(session_dir, filename)


def read_json(path, default=None):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def write_json(path, data):
    """Atomic write: temp file + os.replace()."""
    parent = os.path.dirname(path) or "."
    fd, tmp = tempfile_safe(parent, ".st_", ".tmp")
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def tempfile_safe(parent, prefix, suffix):
    """Create temp file, return (fd, path)."""
    import tempfile as _tf
    fd, path = _tf.mkstemp(dir=parent, prefix=prefix, suffix=suffix)
    return fd, path


def append_jsonl(path, data):
    """Append a JSON line. Crash-resilient: partial line at worst."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")
        f.flush()


def read_jsonl(path):
    """Read all complete JSON lines from a JSONL file."""
    if not os.path.exists(path):
        return []
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                lines.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return lines


# ── State Management ─────────────────────────────────────────────────────────

def load_state(session_dir):
    return read_json(_path(session_dir, STATE_FILE), {})


def save_state(session_dir, state):
    state["updated_at"] = now_iso()
    write_json(_path(session_dir, STATE_FILE), state)


def load_todo(session_dir):
    return read_json(_path(session_dir, TODO_FILE), [])


def save_todo(session_dir, todo):
    write_json(_path(session_dir, TODO_FILE), todo)


# ── Filesystem Scanner ───────────────────────────────────────────────────────

def take_snapshot(session_dir):
    """
    Scan project directories and build a filesystem fingerprint.
    Returns a dict: {dir_path: {filename: {size, mtime, atime}}}
    """
    snapshot = {}
    for scan_dir in SCAN_DIRS:
        if not os.path.isdir(scan_dir):
            continue
        dir_files = {}
        count = 0
        try:
            for entry in sorted(os.listdir(scan_dir)):
                if count >= MAX_FILES_PER_DIR:
                    dir_files["__truncated__"] = True
                    break
                fpath = os.path.join(scan_dir, entry)
                try:
                    st = os.stat(fpath)
                    dir_files[entry] = {
                        "s": st.st_size,
                        "m": int(st.st_mtime),
                        "a": int(st.st_atime),
                    }
                    count += 1
                except OSError:
                    pass
        except OSError:
            pass
        snapshot[scan_dir] = dir_files
    return snapshot


def diff_snapshots(prev, curr):
    """
    Compare two snapshots. Returns a dict of detected events:
      {dir: {"created": [...], "deleted": [...], "modified": [...], "read": [...]}}
    """
    result = {}
    all_dirs = set(list(prev.keys()) + list(curr.keys()))

    for d in all_dirs:
        prev_files = prev.get(d, {})
        curr_files = curr.get(d, {})
        if prev_files.get("__truncated__") or curr_files.get("__truncated__"):
            continue

        events = {"created": [], "deleted": [], "modified": [], "read": []}

        prev_names = set(k for k in prev_files if k != "__truncated__")
        curr_names = set(k for k in curr_files if k != "__truncated__")

        # New files
        for name in sorted(curr_names - prev_names):
            events["created"].append(name)

        # Deleted files
        for name in sorted(prev_names - curr_names):
            events["deleted"].append(name)

        # Modified or read files
        for name in sorted(prev_names & curr_names):
            pf = prev_files[name]
            cf = curr_files[name]
            if cf["s"] != pf["s"] or cf["m"] != pf["m"]:
                events["modified"].append(name)
            elif cf["a"] > pf["a"] and cf["a"] > cf["m"]:
                # atime newer than mtime suggests a read (relatime semantics)
                events["read"].append(name)

        if any(events.values()):
            result[d] = events

    return result


def has_activity(diff):
    """Check if a snapshot diff shows any filesystem activity."""
    for d, events in diff.items():
        for evt_type, items in events.items():
            if items:
                return True
    return False


def cmd_scan(session_dir):
    """Take a filesystem snapshot and compare to previous. Report activity."""
    curr = take_snapshot(session_dir)
    prev = read_json(_path(session_dir, SNAPSHOT_PREV))

    if prev is None:
        # First scan, just save baseline
        write_json(_path(session_dir, SNAPSHOT_PREV), curr)
        print("Baseline snapshot taken (no previous to compare)")
        return

    diff = diff_snapshots(prev, curr)
    activity = has_activity(diff)

    if not activity:
        print("No filesystem activity detected")
    else:
        print("Filesystem activity detected:")
        for d, events in diff.items():
            dirname = os.path.basename(d)
            for evt_type, items in events.items():
                if items:
                    print(f"  {dirname}/{evt_type}: {', '.join(items)}")

    # Save current snapshot for next comparison
    write_json(_path(session_dir, SNAPSHOT_PREV), curr)

    return diff


# ── Commands ─────────────────────────────────────────────────────────────────

def cmd_init(session_dir, task, steps_str, fs_scan=False, auto_cleanup=False):
    """Initialize a new session.

    v2.3: By default does NOT take a baseline filesystem snapshot (data
    minimization). Pass fs_scan=True to enable FS scanning, or run
    `scan` / `monitor --start` later to opt in.

    v2.3: If auto_cleanup=True, stores a flag in state so that `done`
    will automatically run `cleanup` after marking the session complete.
    """
    os.makedirs(session_dir, exist_ok=True)

    existing = load_state(session_dir)
    if existing.get("task"):
        print(f"Warning: session already exists with task: {existing['task']}")
        print("Use 'resume' to continue, or 'cleanup' to remove and start fresh.")

    steps = [s.strip() for s in steps_str.split(",") if s.strip()]
    todo = [
        {"id": str(i + 1), "content": s, "status": "pending", "priority": "high"}
        for i, s in enumerate(steps)
    ]

    state = {
        "session_id": "",
        "task": task,
        "status": "in_progress",
        "current_step_id": None,
        "current_files": [],
        "files": {},
        "started_at": now_iso(),
        "updated_at": now_iso(),
        "auto_cleanup": auto_cleanup,  # v2.3: done → cleanup automatically
        "fs_scan_enabled": fs_scan,     # v2.3: whether FS scanning is enabled
    }

    # ── Check for orphaned sessions (Gridman outsider) ──
    orphan = detect_orphan(session_dir)
    if orphan:
        print("=" * 60)
        print("  ORPHANED SESSION DETECTED (meta-crash survivor)")
        print("=" * 60)
        print(f"  Previous task: {orphan['task']}")
        print(f"  Status: {orphan['status']}")
        print(f"  Last activity: {orphan['last_activity']}")
        print(f"  Progress: {orphan['completed_steps']}/{orphan['total_steps']} steps done")
        if orphan.get('working_files'):
            print(f"  Files in progress: {', '.join(orphan['working_files'])}")
        if orphan.get('next_step'):
            print(f"  Was working on: step {orphan['next_step']['id']} - {orphan['next_step']['content']}")
        print()
        print("  Run 'crash-detect' for full recovery report.")
        print("  Run 'resume' to continue the orphaned session.")
        print("  Run 'cleanup' to delete the orphan and start fresh.")
        print("=" * 60)
        print()

        # Write crash notice to a SESSION-SCOPED file (not shared worklog.md)
        _write_crash_marker(session_dir, orphan)

    save_state(session_dir, state)
    save_todo(session_dir, todo)

    # Write ACTIVE sentinel (crash detection flag)
    sentinel_path = _path(session_dir, ACTIVE_SENTINEL)
    with open(sentinel_path, "w", encoding="utf-8") as f:
        f.write(f"{task}\ninitialized: {now_iso()}\n")

    # v2.3: Only take baseline filesystem snapshot if --fs-scan was passed.
    # This minimizes data collection: a default init/step/done workflow
    # now records NO file sizes, mtimes, or atimes — only task name, step
    # descriptions, and file paths declared by the agent.
    if fs_scan:
        snapshot = take_snapshot(session_dir)
        write_json(_path(session_dir, SNAPSHOT_PREV), snapshot)
        print("  FS scanning: ENABLED (baseline snapshot taken)")
    else:
        print("  FS scanning: disabled (use --fs-scan to enable, or run scan/monitor)")

    append_jsonl(_path(session_dir, WORKLOG_FILE), {
        "ts": now_iso(), "action": "init",
        "detail": f"Task: {task}", "steps": len(steps),
        "fs_scan": fs_scan, "auto_cleanup": auto_cleanup,
    })

    print(f"Session initialized: {task}")
    print(f"Steps: {len(steps)}")
    print(f"Session dir: {session_dir}")
    if auto_cleanup:
        print("  Auto-cleanup: ENABLED (done will remove all state after completion)")


def cmd_step(session_dir, step_id, action, files_str=None):
    """Start or complete a step."""
    state = load_state(session_dir)
    todo = load_todo(session_dir)
    if not state.get("task"):
        print("Error: no active session. Run 'init' first.", file=sys.stderr)
        sys.exit(1)

    step = None
    for item in todo:
        if item["id"] == step_id:
            step = item
            break
    if not step:
        print(f"Error: step '{step_id}' not found.", file=sys.stderr)
        sys.exit(1)

    files = [f.strip() for f in files_str.split(",") if f.strip()] if files_str else []

    if action == "start":
        step["status"] = "in_progress"
        if files:
            step["files"] = files
        state["current_step_id"] = step_id
        state["current_files"] = files

        for f in files:
            state["files"][f] = {"purpose": step["content"], "status": "working"}

        # Reset micro-dumps on step start
        for mf in [MICRODUMP_CURR, MICRODUMP_PREV]:
            mp = _path(session_dir, mf)
            if os.path.exists(mp):
                os.unlink(mp)

        append_jsonl(_path(session_dir, WORKLOG_FILE), {
            "ts": now_iso(), "action": "step_start",
            "step_id": step_id, "step": step["content"],
            "files": files
        })
        print(f"Step {step_id} started: {step['content']}")
        if files:
            print(f"  Working on: {', '.join(files)}")

    elif action == "done":
        step["status"] = "completed"
        if state.get("current_step_id") == step_id:
            state["current_step_id"] = None
            state["current_files"] = []
            for f in step.get("files", []):
                if f in state["files"]:
                    state["files"][f]["status"] = "completed"

        append_jsonl(_path(session_dir, WORKLOG_FILE), {
            "ts": now_iso(), "action": "step_done",
            "step_id": step_id, "step": step["content"]
        })
        print(f"Step {step_id} completed: {step['content']}")

    save_state(session_dir, state)
    save_todo(session_dir, todo)


def cmd_file(session_dir, filepath, action, rename_to=None):
    """Mark a file as working, done, reading, or rename it."""
    state = load_state(session_dir)
    if not state.get("task"):
        print("Error: no active session.", file=sys.stderr)
        sys.exit(1)

    if action == "rename":
        old_path = os.path.abspath(filepath)
        new_path = os.path.abspath(rename_to)

        # Update state.files
        if old_path in state["files"]:
            info = state["files"].pop(old_path)
            state["files"][new_path] = info

        # Update current_files
        if old_path in state.get("current_files", []):
            idx = state["current_files"].index(old_path)
            state["current_files"][idx] = new_path

        # Update todo items that reference the old path
        todo = load_todo(session_dir)
        for item in todo:
            if "files" in item:
                item["files"] = [
                    new_path if f == old_path else f for f in item["files"]
                ]
        save_todo(session_dir, todo)

        append_jsonl(_path(session_dir, WORKLOG_FILE), {
            "ts": now_iso(), "action": "file_rename",
            "old_path": old_path, "new_path": new_path
        })
        print(f"File renamed: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")

        save_state(session_dir, state)
        return

    filepath = os.path.abspath(filepath)

    if action == "working":
        state["files"][filepath] = state["files"].get(filepath, {})
        state["files"][filepath]["status"] = "working"
        if filepath not in state["current_files"]:
            state["current_files"].append(filepath)
        append_jsonl(_path(session_dir, WORKLOG_FILE), {
            "ts": now_iso(), "action": "file_working", "file": filepath
        })
        print(f"File marked WORKING: {filepath}")

    elif action == "done":
        if filepath in state["files"]:
            state["files"][filepath]["status"] = "completed"
        if filepath in state.get("current_files", []):
            state["current_files"].remove(filepath)
        append_jsonl(_path(session_dir, WORKLOG_FILE), {
            "ts": now_iso(), "action": "file_done", "file": filepath
        })
        print(f"File marked DONE: {filepath}")

    elif action == "reading":
        state["files"][filepath] = state["files"].get(filepath, {})
        state["files"][filepath]["status"] = "reading"
        if filepath not in state["current_files"]:
            state["current_files"].append(filepath)
        append_jsonl(_path(session_dir, WORKLOG_FILE), {
            "ts": now_iso(), "action": "file_reading", "file": filepath
        })
        print(f"File marked READING: {filepath}")

    save_state(session_dir, state)


def cmd_ping(session_dir, detail=None):
    """Manual heartbeat — signals 'I'm alive but busy'. Resets stuck counter."""
    entry = {"ts": now_iso(), "action": "ping"}
    if detail:
        entry["detail"] = detail
    append_jsonl(_path(session_dir, WORKLOG_FILE), entry)

    # Also touch the session dir's mtime as a physical heartbeat signal
    try:
        os.utime(session_dir, None)
    except OSError:
        pass

    print(f"Ping{': ' + detail if detail else ''}")


def cmd_sync(session_dir):
    """
    Bidirectional sync with TodoWrite.
    Reads tracker todo, reads TodoWrite-format from stdin or args,
    reconciles differences.
    """
    state = load_state(session_dir)
    tracker_todo = load_todo(session_dir)

    if not state.get("task"):
        print("Error: no active session. Run 'init' first.", file=sys.stderr)
        sys.exit(1)

    # Build a lookup of current tracker steps by content
    tracker_by_content = {item["content"]: item for item in tracker_todo}

    # Try to read TodoWrite format from stdin (piped in)
    import_selective = []
    if not sys.stdin.isatty():
        try:
            piped = json.load(sys.stdin)
            if isinstance(piped, list):
                import_selective = piped
        except (json.JSONDecodeError, EOFError):
            pass

    if not import_selective:
        # No piped input — just display current sync status
        print("Tracker TODO (source of truth):")
        for item in tracker_todo:
            icon = {"completed": "[x]", "in_progress": "[~]", "pending": "[ ]"}.get(
                item["status"], "[?]"
            )
            print(f"  {icon} {item['id']}. {item['content']}")
        print()
        print("To sync, pipe TodoWrite JSON:")
        print("  echo '[...]' | python3 session_tracker.py sync")
        return

    # Reconcile: import new items, update existing ones
    new_items = []
    max_id = max((int(item["id"]) for item in tracker_todo), default=0)
    content_to_id = {item["content"]: item["id"] for item in tracker_todo}

    for tw_item in import_selective:
        content = tw_item.get("content", "").strip()
        if not content:
            continue
        tw_status = tw_item.get("status", "pending")

        if content in content_to_id:
            # Update existing step's status if it changed
            step_id = content_to_id[content]
            for t_item in tracker_todo:
                if t_item["id"] == step_id and t_item["status"] != tw_status:
                    old_status = t_item["status"]
                    t_item["status"] = tw_status
                    append_jsonl(_path(session_dir, WORKLOG_FILE), {
                        "ts": now_iso(), "action": "sync_update",
                        "step_id": step_id, "content": content,
                        "old_status": old_status, "new_status": tw_status
                    })
        else:
            # New item not in tracker
            max_id += 1
            new_step = {
                "id": str(max_id),
                "content": content,
                "status": tw_status,
                "priority": tw_item.get("priority", "high"),
            }
            tracker_todo.append(new_step)
            new_items.append(new_step)
            append_jsonl(_path(session_dir, WORKLOG_FILE), {
                "ts": now_iso(), "action": "sync_add",
                "step_id": str(max_id), "content": content
            })

    save_todo(session_dir, tracker_todo)

    if new_items:
        print(f"Synced: {len(new_items)} new step(s) added from TodoWrite")
    else:
        print("Synced: no new steps (existing statuses updated)")


def cmd_log(session_dir, message, step_id=None):
    """Add a worklog entry."""
    entry = {"ts": now_iso(), "action": "log", "detail": message}
    if step_id:
        entry["step_id"] = step_id
    append_jsonl(_path(session_dir, WORKLOG_FILE), entry)
    print(f"Logged: {message}")


def cmd_done(session_dir):
    """Mark session as completed, stop monitor."""
    state = load_state(session_dir)
    todo = load_todo(session_dir)

    state["status"] = "completed"
    state["current_step_id"] = None
    state["current_files"] = []
    state["completed_at"] = now_iso()

    for item in todo:
        if item["status"] == "in_progress":
            item["status"] = "completed"
        elif item["status"] == "pending":
            item["status"] = "skipped"

    for f in state["files"]:
        state["files"][f]["status"] = "completed"

    save_state(session_dir, state)
    save_todo(session_dir, todo)

    # Remove ACTIVE sentinel (clean completion — no crash)
    sentinel_path = _path(session_dir, ACTIVE_SENTINEL)
    if os.path.exists(sentinel_path):
        os.unlink(sentinel_path)

    append_jsonl(_path(session_dir, WORKLOG_FILE), {
        "ts": now_iso(), "action": "session_done",
        "detail": "Session completed"
    })

    # Stop monitor if running (best-effort; ignore if not running)
    cmd_monitor(session_dir, "stop")

    # Remove crash notice (no longer relevant once session is done)
    notice_path = _path(session_dir, CRASH_NOTICE)
    if os.path.exists(notice_path):
        try:
            os.unlink(notice_path)
        except OSError:
            pass

    print("Session marked as COMPLETED.")

    # v2.3: If --auto-cleanup was set on init, remove all session state now.
    # This addresses the cross-session retention concern: tasks that completed
    # successfully leave no persistent data behind.
    if state.get("auto_cleanup"):
        print("  Auto-cleanup enabled — removing session state...")
        cmd_cleanup(session_dir, force=True)


# ── Gridman Outsider: Crash Detection & Recovery ────────────────────────────

def detect_orphan(session_dir, idle_threshold_s=None):
    """
    Detect an orphaned session — one that was initialized but never completed.
    This is the 'outsider who remembers' — survives meta-crashes.

    Detection signals (any one is sufficient):
      1. SESSION_ACTIVE sentinel exists (init was called, done was not)
      2. state.json exists with status != 'completed' and no session_done in worklog

    If `idle_threshold_s` is provided, additionally require that the session's
    `updated_at` is older than `idle_threshold_s` seconds ago. This prevents
    false-positive orphan warnings during normal active use of `status`.

    Use idle_threshold_s=None (default) for the strict check in `init` —
    any unfinished session from a previous run is suspicious.

    Use idle_threshold_s=ORPHAN_IDLE_THRESHOLD_S for `status` — only flag
    orphans if the session has actually been silent for a while.
    """
    if not os.path.isdir(session_dir):
        return None

    state = load_state(session_dir)
    if not state.get("task"):
        return None

    # Signal 1: ACTIVE sentinel file exists
    sentinel_exists = os.path.exists(_path(session_dir, ACTIVE_SENTINEL))

    # Signal 2: Session not completed
    status = state.get("status", "unknown")
    not_completed = status != "completed"

    # Signal 3: No session_done entry in worklog
    worklog = read_jsonl(_path(session_dir, WORKLOG_FILE))
    has_done_entry = any(e.get("action") == "session_done" for e in worklog)

    # Orphan if: sentinel exists OR (session not completed AND no done entry)
    is_orphan = sentinel_exists or (not_completed and not has_done_entry)

    if not is_orphan:
        return None

    # Idle threshold check (used by `status` to avoid false positives)
    if idle_threshold_s is not None:
        updated_at = state.get("updated_at")
        if not updated_at:
            return None  # No timestamp — can't confirm idle, don't false-positive
        try:
            last_ts = datetime.fromisoformat(updated_at)
            if last_ts.tzinfo is None:
                last_ts = last_ts.replace(tzinfo=timezone.utc)
            age_s = (datetime.now(timezone.utc) - last_ts).total_seconds()
            if age_s < idle_threshold_s:
                return None  # Recently active — not an orphan
        except (ValueError, TypeError):
            return None  # Bad timestamp — don't false-positive

    todo = load_todo(session_dir)
    completed = sum(1 for s in todo if s["status"] == "completed")
    total = len(todo)

    # Find next step
    next_step = None
    for step in todo:
        if step["status"] == "in_progress":
            next_step = {"id": step["id"], "content": step["content"], "status": step["status"]}
            break
    if not next_step:
        for step in todo:
            if step["status"] == "pending":
                next_step = {"id": step["id"], "content": step["content"], "status": step["status"]}
                break

    # Working files (may be incomplete after crash)
    working_files = []
    for f, info in state.get("files", {}).items():
        if info["status"] in ("working", "reading"):
            working_files.append(os.path.basename(f))

    # Last worklog entries for context
    last_entries = worklog[-5:] if worklog else []

    return {
        "task": state["task"],
        "status": status,
        "last_activity": state.get("updated_at", "unknown"),
        "completed_steps": completed,
        "total_steps": total,
        "next_step": next_step,
        "working_files": working_files,
        "last_log_entries": last_entries,
        "sentinel_exists": sentinel_exists,
    }


def _write_crash_marker(session_dir, orphan_info):
    """
    Write a crash recovery notice to SESSION_DIR/CRASH_NOTICE.md.

    v2.2: This is SESSION-SCOPED — it does NOT touch the shared project
    worklog.md. The shared worklog is reserved for user/agent content;
    session-tracker state belongs under .session/.
    """
    os.makedirs(session_dir, exist_ok=True)
    notice_path = _path(session_dir, CRASH_NOTICE)

    marker_lines = [
        "# META-CRASH DETECTED",
        "",
        "A previous session was interrupted (context overflow / timeout / disconnect).",
        "The session-tracker has preserved the session state. A new agent can resume.",
        "",
        f"- **Task**: {orphan_info['task']}",
        f"- **Last activity**: {orphan_info['last_activity']}",
        f"- **Progress**: {orphan_info['completed_steps']}/{orphan_info['total_steps']} steps completed",
    ]

    if orphan_info.get('next_step'):
        ns = orphan_info['next_step']
        marker_lines.append(f"- **Was working on**: step {ns['id']} — {ns['content']}")
    if orphan_info.get('working_files'):
        marker_lines.append(f"- **Files in progress**: {', '.join(orphan_info['working_files'])}")

    marker_lines.extend([
        "",
        "**To resume**: `python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py resume`",
        "**For full report**: `python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py crash-detect`",
        "**To discard**: `python3 /home/z/my-project/skills/session-tracker/scripts/session_tracker.py cleanup`",
        "",
    ])

    # Overwrite (not prepend) — crash notice is always about the most recent orphan
    with open(notice_path, "w", encoding="utf-8") as f:
        f.write("\n".join(marker_lines))


def cmd_crash_detect(session_dir):
    """
    Generate a full crash recovery report from an orphaned session.
    This is the Gridman outsider revealing what the kaiju destroyed.
    """
    orphan = detect_orphan(session_dir)
    if not orphan:
        print("No orphaned session detected. All sessions completed cleanly.")
        return

    state = load_state(session_dir)
    todo = load_todo(session_dir)
    worklog = read_jsonl(_path(session_dir, WORKLOG_FILE))

    print()
    print("=" * 64)
    print("  META-CRASH RECOVERY REPORT")
    print("  (Gridman Outsider — Restoring Lost Memory)")
    print("=" * 64)
    print()

    # Crash signature
    print("  CRASH SIGNATURE:")
    print(f"    ACTIVE sentinel: {'EXISTS (session never completed)' if orphan['sentinel_exists'] else 'missing'}")
    print(f"    Session status: {orphan['status']}")
    print(f"    session_done in worklog: {'NO (crash confirmed)' if not any(e.get('action') == 'session_done' for e in worklog) else 'YES (contradicts status — possible corruption)'}")
    print()

    # What was happening
    print("  TASK:")
    print(f"    {orphan['task']}")
    print(f"    Started: {state.get('started_at', 'unknown')}")
    print(f"    Last activity: {orphan['last_activity']}")
    print()

    # Step-by-step progress
    print("  STEPS:")
    for step in todo:
        icon = {"completed": "[x]", "in_progress": "[~]", "pending": "[ ]", "skipped": "[-]"}.get(
            step["status"], "[?]"
        )
        files_str = ""
        if step.get("files"):
            files_str = f"  ({', '.join(os.path.basename(f) for f in step['files'])})"
        print(f"    {icon} {step['id']}. {step['content']}{files_str}")
    print()

    # Files that may be incomplete
    working_files = [
        (f, info) for f, info in state.get("files", {}).items()
        if info["status"] in ("working", "reading")
    ]
    if working_files:
        print("  FILES POTENTIALLY INCOMPLETE (verify before using):")
        for f, info in working_files:
            exists = "exists" if os.path.exists(f) else "MISSING"
            size_str = ""
            if os.path.exists(f):
                try:
                    size_str = f" ({os.path.getsize(f)} bytes)"
                except OSError:
                    pass
            print(f"    ! [{info['status'].upper()}] {f} ({exists}){size_str}")
        print()

    # Last worklog entries — what happened right before the crash
    if worklog:
        print(f"  LAST {min(10, len(worklog))} WORKLOG ENTRIES (what happened before crash):")
        for entry in worklog[-10:]:
            ts = entry.get("ts", "?")[-8:]
            action = entry.get("action", "?")
            detail = entry.get("detail", entry.get("file", entry.get("step", "")))
            print(f"    {ts} {action}: {detail}")
        print()

    # Recovery recommendation
    next_step = orphan.get('next_step')
    print("  RECOVERY RECOMMENDATION:")
    if next_step:
        if next_step['status'] == 'in_progress':
            print(f"    1. Verify output of step {next_step['id']} ({next_step['content']})")
            print(f"    2. If incomplete, redo step {next_step['id']}")
            print(f"    3. Continue with remaining steps")
        else:
            print(f"    1. Begin step {next_step['id']} ({next_step['content']})")
            print(f"    2. Continue with remaining steps")
        print(f"    Run: python3 session_tracker.py step {next_step['id']} --start")
    print()
    print("  To archive this orphan and start fresh:")
    print(f"    python3 session_tracker.py cleanup")
    print()
    print("=" * 64)
    print()


def cmd_resume(session_dir):
    """Show resume plan from last session state."""
    state = load_state(session_dir)
    todo = load_todo(session_dir)

    if not state.get("task"):
        print("No session found. Run 'init' to start one.", file=sys.stderr)
        sys.exit(1)

    if state["status"] == "completed":
        print("Session already completed. Start a new one with 'init'.")
        return

    # Check if this is a crash recovery (not just a manual resume)
    orphan = detect_orphan(session_dir)

    completed = sum(1 for s in todo if s["status"] == "completed")
    total = len(todo)

    print()
    print("=" * 56)
    print("  SESSION RESUME")
    if orphan:
        print("  ** META-CRASH RECOVERY **")
    print("=" * 56)
    print(f"  Task: {state['task']}")
    if orphan:
        print(f"  Status: IN_PROGRESS (META-CRASH — previous session was killed)")
    else:
        print(f"  Status: IN_PROGRESS (interrupted)")
    print(f"  Last activity: {state.get('updated_at', 'unknown')}")
    print(f"  Progress: {completed}/{total} steps completed")
    print()

    for step in todo:
        icon = {"completed": "[x]", "in_progress": "[~]", "pending": "[ ]"}.get(
            step["status"], "[?]"
        )
        files_str = ""
        if step.get("files"):
            files_str = f"  ({', '.join(os.path.basename(f) for f in step['files'])})"
        print(f"  {icon} {step['id']}. {step['content']}{files_str}")

    working_files = [
        (f, info) for f, info in state.get("files", {}).items()
        if info["status"] in ("working", "reading")
    ]
    if working_files:
        print()
        print("  WARNING - Files still in progress (may be incomplete):")
        for f, info in working_files:
            status_tag = info["status"].upper()
            print(f"    ! [{status_tag}] {f}")

    # Show last few worklog entries for context
    worklog = read_jsonl(_path(session_dir, WORKLOG_FILE))
    if worklog:
        print()
        print(f"  Last {min(5, len(worklog))} log entries:")
        for entry in worklog[-5:]:
            ts = entry.get("ts", "?")[-8:]
            action = entry.get("action", "?")
            detail = entry.get("detail", entry.get("file", entry.get("step", "")))
            print(f"    {ts} {action}: {detail}")

    next_step = None
    for step in todo:
        if step["status"] == "in_progress":
            next_step = step
            break
    if not next_step:
        for step in todo:
            if step["status"] == "pending":
                next_step = step
                break

    print()
    if next_step:
        print(f"  Resume from: step {next_step['id']} ({next_step['content']})")
        if next_step["status"] == "in_progress":
            print(f"  Action: Verify step {next_step['id']} work, then continue or redo")
        else:
            print(f"  Action: Begin step {next_step['id']}")
    print("=" * 56)
    print()


def cmd_status(session_dir):
    """Show current session status with activity info."""
    state = load_state(session_dir)
    todo = load_todo(session_dir)

    if not state.get("task"):
        print("No active session.", file=sys.stderr)
        sys.exit(1)

    completed = sum(1 for s in todo if s["status"] == "completed")
    in_progress = sum(1 for s in todo if s["status"] == "in_progress")
    pending = sum(1 for s in todo if s["status"] == "pending")

    # Check for orphaned session (meta-crash detection).
    # Use the idle-gated check so we don't false-positive on active sessions
    # that simply haven't called `done` yet. Only flag as orphan if the
    # session has been silent for > ORPHAN_IDLE_THRESHOLD_S.
    orphan = detect_orphan(session_dir, idle_threshold_s=ORPHAN_IDLE_THRESHOLD_S)
    if orphan:
        print("!! META-CRASH DETECTED: This session was killed before completion !!")

    print(f"Task: {state['task']}")
    print(f"Status: {state['status']}{' (ORPHANED — previous agent crashed)' if orphan else ''}")
    print(f"Progress: {completed}/{len(todo)} done, {in_progress} active, {pending} pending")
    print(f"Last update: {state.get('updated_at', 'unknown')}")

    if state.get("current_step_id"):
        print(f"Current step: {state['current_step_id']}")
    if state.get("current_files"):
        print(f"Working files: {', '.join(os.path.basename(f) for f in state['current_files'])}")

    # Check filesystem activity
    curr = take_snapshot(session_dir)
    prev = read_json(_path(session_dir, SNAPSHOT_PREV))
    if prev:
        diff = diff_snapshots(prev, curr)
        if has_activity(diff):
            print("FS Activity: YES (changes detected since last scan)")
            for d, events in diff.items():
                dirname = os.path.basename(d)
                for evt_type, items in events.items():
                    if items:
                        print(f"  {dirname}/{evt_type}: {', '.join(items[:5])}")
        else:
            print("FS Activity: None since last scan")

    # Check stuck status
    stuck = _check_stuck(session_dir)
    if stuck:
        print(f"ALERT: Task appears STUCK ({stuck} consecutive checks with no activity)")

    # Show monitor status
    pid = _read_alive_pid(_path(session_dir, MONITOR_PID_FILE))
    if pid:
        print(f"Monitor: running (PID {pid})")
    else:
        print("Monitor: not running")


# ── Micro-dump & Monitor ────────────────────────────────────────────────────

def take_microdump(session_dir):
    """Capture current state fingerprint + filesystem scan."""
    state = load_state(session_dir)
    todo = load_todo(session_dir)
    worklog_path = _path(session_dir, WORKLOG_FILE)

    worklog_lines = 0
    if os.path.exists(worklog_path):
        with open(worklog_path, "r") as f:
            worklog_lines = sum(1 for _ in f)

    file_fingerprints = {}
    for fpath, info in state.get("files", {}).items():
        if info["status"] in ("working", "reading") and os.path.exists(fpath):
            try:
                st = os.stat(fpath)
                file_fingerprints[fpath] = {"size": st.st_size, "mtime": int(st.st_mtime)}
            except OSError:
                pass

    current_steps = [
        {"id": s["id"], "status": s["status"]}
        for s in todo if s["status"] == "in_progress"
    ]

    # Filesystem scan — compact summary for comparison
    fs_scan = take_snapshot(session_dir)

    return {
        "current_step_id": state.get("current_step_id"),
        "current_files": state.get("current_files", []),
        "current_steps": current_steps,
        "file_fingerprints": file_fingerprints,
        "worklog_lines": worklog_lines,
        "fs_scan": fs_scan,
        "ts": now_iso(),
    }


def cmd_monitor(session_dir, action, interval=60):
    """Start, stop, foreground, or check the background monitor."""

    if action == "start":
        pid_path = _path(session_dir, MONITOR_PID_FILE)

        existing_pid = _read_alive_pid(pid_path)
        if existing_pid:
            print(f"Monitor already running (PID {existing_pid})")
            return

        # v2.3: Minimal environment — don't inherit the full parent environment.
        # Only pass PATH, HOME, etc. plus the two _SESSION_TRACKER_LOOP_* vars
        # the monitor loop needs. This addresses the "inherited environment"
        # concern from the audit.
        env = {}
        for key in _MONITOR_ENV_ALLOWLIST:
            if key in os.environ:
                env[key] = os.environ[key]
        env["_SESSION_TRACKER_LOOP_DIR"] = session_dir
        env["_SESSION_TRACKER_LOOP_INTERVAL"] = str(interval)

        # Pass the script path explicitly so the subprocess runs the SAME file
        # the user invoked — not whatever `session-tracker` might be in PATH.
        script_path = os.path.abspath(__file__)
        cmd = [sys.executable, script_path]

        # v2.3: Redirect stdout/stderr to .session/monitor.log instead of
        # DEVNULL. The monitor's output is now inspectable by the user,
        # addressing the "suppressed stdout/stderr" concern from the audit.
        log_path = _path(session_dir, MONITOR_LOG)
        log_fd = open(log_path, "a", encoding="utf-8")

        proc = subprocess.Popen(
            cmd,
            env=env,
            stdout=log_fd,
            stderr=log_fd,
            start_new_session=True,
        )
        # Close our copy of the fd; the child has inherited it.
        log_fd.close()

        write_json(pid_path, {"pid": proc.pid, "started_at": now_iso(),
                              "script": script_path, "interval": interval,
                              "log": log_path})
        print(f"Monitor started (PID {proc.pid}, interval {interval}s)")
        print(f"  Script: {script_path}")
        print(f"  PID file: {pid_path}")
        print(f"  Log file: {log_path}")
        print(f"  Stop with: python3 {script_path} monitor --stop")
        print(f"  Bounded to {MAX_MONITOR_RUNTIME_S // 3600}h max runtime.")
        print(f"  Environment: minimal ({len(env)} vars, no full inheritance)")

    elif action == "foreground":
        # Run monitor loop in the foreground (no subprocess). Useful for users
        # who don't want a detached background process. Blocks until session
        # done, stuck for too long, or Ctrl+C.
        pid_path = _path(session_dir, MONITOR_PID_FILE)
        existing_pid = _read_alive_pid(pid_path)
        if existing_pid:
            print(f"Background monitor already running (PID {existing_pid}). Stop it first.")
            return
        print(f"Monitor running in FOREGROUND (interval={interval}s, "
              f"max runtime {MAX_MONITOR_RUNTIME_S // 3600}h).")
        print("Press Ctrl+C to stop.")
        try:
            _monitor_loop(session_dir, interval)
        except KeyboardInterrupt:
            print("\nMonitor stopped by user.")
        print("Foreground monitor exited.")

    elif action == "stop":
        pid_path = _path(session_dir, MONITOR_PID_FILE)
        existing_pid = _read_alive_pid(pid_path)
        if existing_pid:
            try:
                os.kill(existing_pid, signal.SIGTERM)
                print(f"Monitor stopped (PID {existing_pid})")
            except ProcessLookupError:
                print("Monitor process not found (already stopped)")
            except PermissionError:
                print(f"Permission denied stopping PID {existing_pid} "
                      f"(not owned by you?). Try: kill {existing_pid}")
                return
            try:
                os.unlink(pid_path)
            except OSError:
                pass
        else:
            print("No monitor running")

    elif action == "check":
        stuck = _check_stuck(session_dir)
        if stuck:
            print(f"STUCK: {stuck} consecutive checks with no activity")
        else:
            state = load_state(session_dir)
            if state.get("status") == "completed":
                print("Session completed")
            else:
                print("Session active (activity detected or too soon to tell)")
        return stuck


def _read_alive_pid(pid_path):
    """
    Read a PID from `pid_path`. Returns the PID if the file exists AND the
    process is alive. If the process is dead, unlinks the stale PID file and
    returns None.
    """
    data = read_json(pid_path)
    if not data:
        return None
    pid = data.get("pid")
    if not pid:
        return None
    if not _is_process_alive(pid):
        try:
            os.unlink(pid_path)
        except OSError:
            pass
        return None
    return pid


def _is_process_alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


def _check_stuck(session_dir):
    """Check stuck status. Returns stuck count or None."""
    curr = read_json(_path(session_dir, MICRODUMP_CURR))
    prev = read_json(_path(session_dir, MICRODUMP_PREV))

    if not curr or not prev:
        return None

    # Compare ignoring internal fields and timestamps
    skip_keys = {"ts", "_stuck_count"}
    clean_curr = {k: v for k, v in curr.items() if k not in skip_keys}
    clean_prev = {k: v for k, v in prev.items() if k not in skip_keys}

    if clean_curr == clean_prev:
        count = curr.get("_stuck_count", 2)
        return count + 2 if count >= 1 else 2

    return None


def _monitor_loop(session_dir, interval):
    """
    Internal: run as background monitor loop.

    v2.2: Bounded by MAX_MONITOR_RUNTIME_S. Exits cleanly when session is
    completed or when runtime cap is hit.

    Stuck detection strategy:
    1. Take filesystem snapshot + micro-dump each interval
    2. Compare current dump to previous dump
    3. If filesystem shows activity (new/modified/read files) → ALIVE, reset counter
    4. If no filesystem activity AND no micro-dump change → increment stuck counter
    5. If stuck counter >= STUCK_THRESHOLD → fire stuck_alert
    """
    stuck_count = 0
    last_alert_count = 0  # avoid duplicate alerts at same count
    start_time = time.time()

    while True:
        state = load_state(session_dir)

        if state.get("status") == "completed":
            break

        # Hard runtime cap — prevent zombie monitor processes
        if time.time() - start_time > MAX_MONITOR_RUNTIME_S:
            append_jsonl(_path(session_dir, WORKLOG_FILE), {
                "ts": now_iso(), "action": "monitor_timeout",
                "detail": f"Monitor hit {MAX_MONITOR_RUNTIME_S // 3600}h runtime cap and exited."
            })
            break

        dump = take_microdump(session_dir)

        # Check filesystem activity from the scan inside the dump
        prev_snapshot = read_json(_path(session_dir, SNAPSHOT_PREV))
        curr_snapshot = dump.get("fs_scan", {})
        fs_activity = False

        if prev_snapshot:
            diff = diff_snapshots(prev_snapshot, curr_snapshot)
            fs_activity = has_activity(diff)

            # Auto-log filesystem events to worklog (throttled: max 1 per interval)
            if fs_activity:
                events_summary = []
                for d, events in diff.items():
                    dirname = os.path.basename(d)
                    for evt_type, items in events.items():
                        if items:
                            events_summary.append(
                                f"{dirname}/{evt_type}:{len(items)}"
                            )
                if events_summary:
                    append_jsonl(_path(session_dir, WORKLOG_FILE), {
                        "ts": now_iso(), "action": "fs_activity",
                        "detail": "; ".join(events_summary),
                    })

        # Save current snapshot for next iteration
        write_json(_path(session_dir, SNAPSHOT_PREV), curr_snapshot)

        # Determine alive vs stuck
        prev_curr = read_json(_path(session_dir, MICRODUMP_CURR))

        if fs_activity:
            # Filesystem activity detected → definitely alive
            stuck_count = 0
        elif prev_curr:
            # No filesystem activity — check micro-dump changes as fallback
            skip = {"ts", "_stuck_count", "fs_scan"}
            clean_prev = {k: v for k, v in prev_curr.items() if k not in skip}
            clean_dump = {k: v for k, v in dump.items() if k not in skip}

            if clean_dump == clean_prev:
                # No change at all → possibly stuck
                stuck_count += 1
            else:
                # Micro-dump changed (e.g., new worklog entry from ping/log)
                stuck_count = 0
        else:
            # First check, no previous to compare
            stuck_count = 0

        dump["_stuck_count"] = stuck_count

        # Rotate: current → previous, new → current
        curr_path = _path(session_dir, MICRODUMP_CURR)
        prev_path = _path(session_dir, MICRODUMP_PREV)

        if os.path.exists(curr_path):
            os.replace(curr_path, prev_path)

        write_json(curr_path, dump)

        if stuck_count >= STUCK_THRESHOLD and stuck_count != last_alert_count:
            total_stuck = stuck_count + 2
            last_alert_count = stuck_count
            append_jsonl(_path(session_dir, WORKLOG_FILE), {
                "ts": now_iso(), "action": "stuck_alert",
                "detail": (
                    f"Task stuck for {total_stuck} consecutive checks "
                    f"({total_stuck * interval}s) — no filesystem or state activity"
                ),
                "stuck_count": total_stuck,
            })

        time.sleep(interval)

    # Clean up PID file on exit (only if this is the background subprocess)
    pid_path = _path(session_dir, MONITOR_PID_FILE)
    if os.environ.get("_SESSION_TRACKER_LOOP_DIR"):
        try:
            os.unlink(pid_path)
        except OSError:
            pass


# ── Cleanup ─────────────────────────────────────────────────────────────────

def cmd_cleanup(session_dir, force=False):
    """
    Remove ALL session-tracker state for this project:
      - Stop and kill the background monitor (if running)
      - Remove the entire SESSION_DIR (state, todo, worklog, snapshots, etc.)
      - Remove the CRASH_NOTICE.md

    v2.3: This operation is IRREVERSIBLE. All crash recovery data, worklogs,
    and file inventory are permanently deleted. If force=False and stdin is
    a TTY, the user is prompted for confirmation. Use --force to skip the
    prompt (for scripts/agents).

    Use this when you're done with session tracking, or when an orphaned
    session is no longer needed and you want a clean slate.
    """
    if not os.path.isdir(session_dir):
        print(f"Session dir does not exist: {session_dir}")
        print("Nothing to clean up.")
        return

    # v2.3: Prominent IRREVERSIBLE warning + confirmation prompt.
    # Addresses the "Missing User Warnings" finding from the audit.
    if not force:
        print("=" * 64)
        print("  ⚠️  IRREVERSIBLE OPERATION  ⚠️")
        print("=" * 64)
        print("  cleanup will PERMANENTLY DELETE:")
        print(f"    {session_dir}/")
        print("  including: state.json, todo.json, worklog.jsonl,")
        print("             snapshots, crash notices, monitor log")
        print()
        print("  All crash recovery data will be lost. There is no undo.")
        print("  Run 'crash-detect' first if you need to extract information.")
        print("=" * 64)
        print()

        # If stdin is a TTY, prompt for confirmation.
        # If stdin is not a TTY (piped/closed), require --force.
        if sys.stdin.isatty():
            response = input("  Type 'yes' to confirm deletion: ").strip().lower()
            if response != "yes":
                print("  Cleanup cancelled.")
                return
        else:
            print("  ERROR: Non-interactive context. Use --force to skip this prompt.")
            print("  (e.g. python3 session_tracker.py cleanup --force)")
            sys.exit(1)

    # 1. Stop the background monitor (best-effort)
    pid_path = _path(session_dir, MONITOR_PID_FILE)
    pid = _read_alive_pid(pid_path)
    if pid:
        try:
            os.kill(pid, signal.SIGTERM)
            print(f"Stopped monitor (PID {pid})")
            # Give it a moment to exit cleanly
            time.sleep(0.5)
            if _is_process_alive(pid):
                os.kill(pid, signal.SIGKILL)
                print(f"Force-killed monitor (PID {pid})")
        except (ProcessLookupError, PermissionError) as e:
            print(f"Could not stop monitor PID {pid}: {e}")
    else:
        # Also check for stale PID file (process dead but file lingers)
        if os.path.exists(pid_path):
            try:
                os.unlink(pid_path)
                print("Removed stale monitor PID file")
            except OSError:
                pass

    # 2. Remove the session directory
    try:
        shutil.rmtree(session_dir)
        print(f"Removed session directory: {session_dir}")
    except OSError as e:
        print(f"Error removing {session_dir}: {e}", file=sys.stderr)
        if not force:
            print("Use --force to attempt removal anyway.")
            sys.exit(1)
        try:
            shutil.rmtree(session_dir, ignore_errors=True)
            print(f"Force-removed session directory: {session_dir}")
        except Exception as e2:
            print(f"Force removal also failed: {e2}", file=sys.stderr)
            sys.exit(1)

    print()
    print("Cleanup complete. No session-tracker state remains in:")
    print(f"  {session_dir}")
    print()
    print("Note: This does NOT remove any project worklog.md or other")
    print("user/agent content — only session-tracker's own files.")


# ── Prune ────────────────────────────────────────────────────────────────────

def cmd_prune(session_dir, max_age_days=DEFAULT_PRUNE_AGE_DAYS):
    """
    v2.3: Remove the session if it's older than max_age_days.

    Addresses the Ssd3 audit finding: "persistently records ... across
    sessions, which can capture sensitive user data or behavioral metadata
    beyond what is necessary for many tasks."

    Usage:
      python3 session_tracker.py prune              # default 7 days
      python3 session_tracker.py prune --max-age 3  # custom threshold

    If the session is older than max_age_days AND is not currently active
    (no ACTIVE sentinel or sentinel is stale), it is removed via cleanup.
    Active sessions (sentinel exists and recently updated) are NOT pruned.
    """
    if not os.path.isdir(session_dir):
        print(f"Session dir does not exist: {session_dir}")
        print("Nothing to prune.")
        return

    state = load_state(session_dir)
    if not state.get("task"):
        print(f"Session dir exists but has no task: {session_dir}")
        print("Removing empty/invalid session dir.")
        cmd_cleanup(session_dir, force=True)
        return

    updated_at = state.get("updated_at", "")
    if not updated_at:
        print("Cannot determine session age (no updated_at field). Skipping.")
        return

    try:
        last_ts = datetime.fromisoformat(updated_at)
        if last_ts.tzinfo is None:
            last_ts = last_ts.replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        print(f"Cannot parse updated_at: {updated_at}. Skipping.")
        return

    age_days = (datetime.now(timezone.utc) - last_ts).total_seconds() / 86400

    if age_days < max_age_days:
        print(f"Session is {age_days:.1f} days old (threshold: {max_age_days} days).")
        print("Not pruning — session is within retention window.")
        return

    # Check if session is still active (sentinel exists and recently updated)
    sentinel_exists = os.path.exists(_path(session_dir, ACTIVE_SENTINEL))
    if sentinel_exists and age_days < max_age_days * 2:
        # Sentinel exists but session is past retention — could be a long-running task.
        # Don't auto-prune; warn the user.
        print(f"Session is {age_days:.1f} days old with ACTIVE sentinel present.")
        print("This may be a long-running task. Not auto-pruning.")
        print("Run 'cleanup --force' manually if you want to remove it.")
        return

    print(f"Session is {age_days:.1f} days old (threshold: {max_age_days} days).")
    print(f"  Task: {state.get('task', 'unknown')}")
    print(f"  Status: {state.get('status', 'unknown')}")
    print(f"  Last activity: {updated_at}")
    print()
    print("Pruning (running cleanup --force)...")
    cmd_cleanup(session_dir, force=True)


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    # Internal monitor loop mode — triggered via env var, not CLI arg.
    # The background subprocess re-invokes the SAME script file with this
    # env var set (see cmd_monitor "start"), so the loop runs the exact
    # code the user invoked — not whatever `session-tracker` might be in PATH.
    _loop_dir = os.environ.get("_SESSION_TRACKER_LOOP_DIR")
    _loop_interval = os.environ.get("_SESSION_TRACKER_LOOP_INTERVAL", "60")
    if _loop_dir:
        _monitor_loop(_loop_dir, int(_loop_interval))
        return

    parser = argparse.ArgumentParser(
        description="Session tracker v2.3: checkpoint, monitor, and resume multi-step tasks.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--dir", default=DEFAULT_DIR,
                        help=f"Session directory (default: {DEFAULT_DIR})")

    sub = parser.add_subparsers(dest="command")

    p_init = sub.add_parser("init", help="Initialize a new session")
    p_init.add_argument("task", help="Task description")
    p_init.add_argument("--steps", required=True, help="Comma-separated step descriptions")
    p_init.add_argument("--fs-scan", action="store_true",
                        help="Enable filesystem scanning (records file sizes/mtimes/atimes). "
                             "Default: OFF (data minimization). Use scan/monitor to enable later.")
    p_init.add_argument("--auto-cleanup", action="store_true",
                        help="Automatically run cleanup after done (no persistent state lingers). "
                             "Addresses data retention concern.")

    p_step = sub.add_parser("step", help="Start or complete a step")
    p_step.add_argument("id", help="Step ID")
    p_step.add_argument("--start", action="store_true", help="Mark step as started")
    p_step.add_argument("--done", action="store_true", help="Mark step as completed")
    p_step.add_argument("--files", help="Comma-separated file paths being worked on")

    p_file = sub.add_parser("file", help="Mark file status or rename")
    p_file.add_argument("path", help="File path")
    p_file.add_argument("--working", action="store_true", help="Mark as being worked on")
    p_file.add_argument("--done", action="store_true", help="Mark as completed")
    p_file.add_argument("--reading", action="store_true", help="Mark as being read")
    p_file.add_argument("--rename", metavar="NEW_PATH", help="Rename file to NEW_PATH")

    p_ping = sub.add_parser("ping", help="Manual heartbeat — signals alive")
    p_ping.add_argument("--detail", help="Optional note about what's happening")

    p_log = sub.add_parser("log", help="Add worklog entry")
    p_log.add_argument("message", help="Log message")
    p_log.add_argument("--step", help="Associated step ID")

    sub.add_parser("sync", help="Sync with TodoWrite (pipe JSON to stdin)")
    sub.add_parser("done", help="Mark session as completed")
    sub.add_parser("resume", help="Show resume plan from last session")
    sub.add_parser("crash-detect", help="Detect orphaned sessions from meta-crashes")
    sub.add_parser("status", help="Show current session status")
    sub.add_parser("scan", help="Take filesystem snapshot and check activity")

    p_mon = sub.add_parser("monitor", help="Background monitor (opt-in)")
    p_mon.add_argument("--start", action="store_true", help="Start monitor (detached subprocess)")
    p_mon.add_argument("--foreground", action="store_true",
                       help="Run monitor in foreground (no subprocess; blocks)")
    p_mon.add_argument("--stop", action="store_true", help="Stop monitor")
    p_mon.add_argument("--check", action="store_true", help="Check stuck status")
    p_mon.add_argument("--interval", type=int, default=60, help="Check interval in seconds")

    p_clean = sub.add_parser("cleanup",
                             help="Remove ALL session-tracker state (IRREVERSIBLE)")
    p_clean.add_argument("--force", action="store_true",
                         help="Skip confirmation prompt (for scripts/agents)")

    p_prune = sub.add_parser("prune",
                              help="Remove sessions older than N days (default: 7)")
    p_prune.add_argument("--max-age", type=int, default=DEFAULT_PRUNE_AGE_DAYS,
                         help=f"Max session age in days (default: {DEFAULT_PRUNE_AGE_DAYS})")

    args = parser.parse_args()
    session_dir = args.dir

    if args.command == "init":
        cmd_init(session_dir, args.task, args.steps,
                 fs_scan=args.fs_scan, auto_cleanup=args.auto_cleanup)
    elif args.command == "step":
        if args.start:
            cmd_step(session_dir, args.id, "start", args.files)
        elif args.done:
            cmd_step(session_dir, args.id, "done")
        else:
            print("Error: specify --start or --done", file=sys.stderr)
            sys.exit(1)
    elif args.command == "file":
        if args.rename:
            cmd_file(session_dir, args.path, "rename", rename_to=args.rename)
        elif args.working:
            cmd_file(session_dir, args.path, "working")
        elif args.done:
            cmd_file(session_dir, args.path, "done")
        elif args.reading:
            cmd_file(session_dir, args.path, "reading")
        else:
            print("Error: specify --working, --done, --reading, or --rename", file=sys.stderr)
            sys.exit(1)
    elif args.command == "ping":
        cmd_ping(session_dir, args.detail)
    elif args.command == "sync":
        cmd_sync(session_dir)
    elif args.command == "log":
        cmd_log(session_dir, args.message, args.step)
    elif args.command == "done":
        cmd_done(session_dir)
    elif args.command == "resume":
        cmd_resume(session_dir)
    elif args.command == "crash-detect":
        cmd_crash_detect(session_dir)
    elif args.command == "status":
        cmd_status(session_dir)
    elif args.command == "scan":
        cmd_scan(session_dir)
    elif args.command == "monitor":
        if args.start:
            cmd_monitor(session_dir, "start", args.interval)
        elif args.foreground:
            cmd_monitor(session_dir, "foreground", args.interval)
        elif args.stop:
            cmd_monitor(session_dir, "stop")
        elif args.check:
            cmd_monitor(session_dir, "check")
        else:
            print("Error: specify --start, --foreground, --stop, or --check", file=sys.stderr)
            sys.exit(1)
    elif args.command == "cleanup":
        cmd_cleanup(session_dir, args.force)
    elif args.command == "prune":
        cmd_prune(session_dir, args.max_age)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
