"""
Shared utilities for Homebase.
"""
import contextlib
import fcntl
import json
import os
import re
import tempfile
import time as _time
from typing import Any


# ─── Atomic JSON writes ─────────────────────────────────────────────────────
#
# Every state file write goes through this. Reason: a naked
# ``open(path, "w") + json.dump`` will leave a truncated/empty file behind if
# the process is killed mid-write (cron timeout, OOM, sigkill, disk full).
# The next run then crashes on JSONDecodeError. For a skill that runs
# unattended for weeks, that single failure mode is the difference between
# "self-heals" and "wakes you up Saturday morning".
#
# How to apply: replace
#     with open(path, "w") as f:
#         json.dump(data, f, indent=2)
# with
#     write_json_atomic(path, data)

def write_json_atomic(path: str, data: Any, indent: int = 2) -> None:
    """Write JSON to ``path`` atomically: tempfile in same dir → fsync → rename."""
    dir_path = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(dir_path, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=".tmp.", suffix=".json", dir=dir_path)
    try:
        with os.fdopen(fd, "w") as tmp:
            json.dump(data, tmp, indent=indent, default=str)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(tmp_path, path)
    except Exception:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

# ─── Cross-process file lock ────────────────────────────────────────────────
#
# write_json_atomic prevents a *corrupt* file from a crash mid-write, but it
# does nothing to prevent a *lost update*: two processes that each load a
# JSON file, mutate their own in-memory copy, and call write_json_atomic
# will race on the final os.replace(), and whichever finishes last silently
# discards the other's change. Locking your own freshly-created temp file
# (as a couple of call sites used to) doesn't help — no other process can
# ever see or contend for that file.
#
# Callers must hold this lock for the *entire* read-modify-write critical
# section (reload from disk, mutate, save) — locking only the final write
# still loses updates if two processes both loaded stale data first.

@contextlib.contextmanager
def locked_file(path: str):
    """Exclusive cross-process lock scoped to ``path``, via a sibling
    ``<path>.lock`` file."""
    dir_path = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(dir_path, exist_ok=True)
    lock_path = path + ".lock"
    with open(lock_path, "a") as lock_f:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)


# Note: All LLM interactions have been removed from this skill.
# Python tools must return raw or structured data to the OpenClaw agent,
# which uses whichever model OpenClaw is configured with to reason about the data.


# ─── Retry helper ───────────────────────────────────────────────────────────

def retry_with_backoff(fn, retries: int = 3, delays: tuple = (1, 2, 4)):
    """
    Retry a function call up to `retries` times with specified delays between attempts.
    No delay before first attempt. Raises the last exception if all retries fail.

    Usage:
        response = retry_with_backoff(lambda: fn(...), retries=3, delays=(1, 2, 4))
    """
    last_error = None
    for attempt in range(retries):
        if attempt > 0:
            delay = delays[attempt - 1] if attempt - 1 < len(delays) else delays[-1]
            import time
            time.sleep(delay)
        try:
            return fn()
        except Exception as e:
            last_error = e
    raise last_error


# ─── Think tag cleaner ──────────────────────────────────────────────────────

def clean_think_tags(text: str) -> str:
    """
    Remove <think>...</think> tags and their content from a string.
    Also handles some variations like *thought* tags.
    Returns cleaned text with surrounding whitespace stripped.
    """
    cleaned = re.sub(r'<think>[^*]*\*\/?[^>]*\*\/?>', '', text, flags=re.DOTALL)
    cleaned = re.sub(r'<think>[\s\S]*?</think>', '', cleaned)
    return cleaned.strip()
