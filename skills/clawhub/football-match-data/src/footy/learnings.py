"""Self-improving agent learnings — structured knowledge logs.

Implements the core concepts from self-improving-agent skill:
  .learnings/LEARNINGS.md     — corrections, insights, best practices
  .learnings/ERRORS.md        — command failures, API errors
  .learnings/FEATURE_REQUESTS.md — user-requested capabilities

Each entry gets a unique ID (LRN/ERR/FEAT-YYYYMMDD-NNN), priority,
status, and structured context. Auto-promotes recurring issues.

Integrated with CLI: commands that fail auto-log errors; corrections
from user feedback are captured; feature requests are tracked.
"""
from __future__ import annotations

import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

_LEARNINGS_DIR = Path(__file__).resolve().parent.parent.parent / ".learnings"

_CATEGORIES = {
    "correction": "User corrected the agent",
    "insight": "New insight discovered",
    "knowledge_gap": "Agent knowledge was outdated/wrong",
    "best_practice": "Better way discovered",
    "pattern": "Recurring pattern detected",
}

_PRIORITIES = ["low", "medium", "high", "critical"]
_STATUSES = ["pending", "in_progress", "resolved", "wont_fix", "promoted"]


def _ensure_dir() -> None:
    _LEARNINGS_DIR.mkdir(parents=True, exist_ok=True)


def _next_id(prefix: str, filename: str) -> str:
    """Generate next sequential ID like LRN-20260624-001."""
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    path = _LEARNINGS_DIR / filename
    if not path.exists():
        return f"{prefix}-{today}-001"
    content = path.read_text(encoding="utf-8")
    existing = re.findall(rf"{prefix}-{today}-(\d+)", content)
    if not existing:
        return f"{prefix}-{today}-001"
    next_num = max(int(n) for n in existing) + 1
    return f"{prefix}-{today}-{next_num:03d}"


def _append_entry(filename: str, entry: str) -> None:
    _ensure_dir()
    path = _LEARNINGS_DIR / filename
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        entry = existing.rstrip() + "\n\n" + entry + "\n"
    path.write_text(entry, encoding="utf-8")


def log_learning(
    summary: str,
    category: str = "insight",
    priority: str = "medium",
    details: str = "",
    suggested_action: str = "",
    related_files: str = "",
    tags: str = "",
    source: str = "conversation",
) -> str:
    """Record a learning — correction, insight, or best practice."""
    if category not in _CATEGORIES:
        category = "insight"

    lid = _next_id("LRN", "LEARNINGS.md")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    entry = f"""## [{lid}] {category}
**Logged**: {now}
**Priority**: {priority}
**Status**: pending
### Summary
{summary}
### Details
{details or "—"}
### Suggested Action
{suggested_action or "—"}
### Metadata
- Source: {source}
- Related Files: {related_files or "—"}
- Tags: {tags or "—"}
"""
    _append_entry("LEARNINGS.md", entry)
    return lid


def log_error(
    command: str,
    error_msg: str,
    context: str = "",
    suggested_fix: str = "",
) -> str:
    """Record a command/API/tool failure."""
    err_id = _next_id("ERR", "ERRORS.md")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    entry = f"""## [{err_id}] {command}
**Logged**: {now}
**Priority**: high
**Status**: pending
### Summary
{error_msg[:200]}
### Error
```
{error_msg[:500]}
```
### Context
{context or "—"}
### Suggested Fix
{suggested_fix or "—"}
### Metadata
- Reproducible: unknown
- Related Files: —
"""
    _append_entry("ERRORS.md", entry)
    return err_id


def log_feature_request(
    capability: str,
    user_context: str = "",
    complexity: str = "medium",
    suggested_impl: str = "",
) -> str:
    """Record a user-requested feature."""
    fid = _next_id("FEAT", "FEATURE_REQUESTS.md")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    entry = f"""## [{fid}] {capability}
**Logged**: {now}
**Priority**: medium
**Status**: pending
### Requested Capability
{capability}
### User Context
{user_context or "—"}
### Complexity Estimate
{complexity}
### Suggested Implementation
{suggested_impl or "—"}
### Metadata
- Frequency: once
"""
    _append_entry("FEATURE_REQUESTS.md", entry)
    return fid


def check_recurring(pattern: str, filename: str = "LEARNINGS.md") -> int:
    """Count how many times a pattern appears in the learning log."""
    path = _LEARNINGS_DIR / filename
    if not path.exists():
        return 0
    content = path.read_text(encoding="utf-8")
    return len(re.findall(re.escape(pattern), content))


def pending_count() -> int:
    """Count pending items across all logs."""
    total = 0
    for fn in ["LEARNINGS.md", "ERRORS.md", "FEATURE_REQUESTS.md"]:
        path = _LEARNINGS_DIR / fn
        if path.exists():
            total += len(re.findall(r"Status\*\*:\s*pending", path.read_text(encoding="utf-8")))
    return total


def show_pending() -> list[str]:
    """Return list of pending entry summaries."""
    results = []
    for fn in ["LEARNINGS.md", "ERRORS.md", "FEATURE_REQUESTS.md"]:
        path = _LEARNINGS_DIR / fn
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        # Find all pending entries
        entries = re.split(r"\n## \[", content)
        for entry in entries:
            if "pending" in entry.lower() and "**Status**" in entry:
                # Extract summary line
                summary = entry.split("### Summary")[1].split("\n")[1].strip() if "### Summary" in entry else "—"
                eid = entry.split("]")[0].strip() if "]" in entry else "???"
                results.append(f"[{eid}] {summary[:120]}")
    return results
