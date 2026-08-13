#!/usr/bin/env python3
"""
Failure Forensics — log parser, categorizer, and post-mortem report generator.

Part of the 'failure-forensics' skill. Analyzes tool-call logs to build a failure
timeline, categorizes failures, and generates post-mortem reports.

Usage:
    python3 failure_forensics.py analyze --log session.jsonl [--format jsonl|json] [--output timeline.md]
    python3 failure_forensics.py categorize --error "error message text"
    python3 failure_forensics.py report --log session.jsonl --title "Title" [--author "name"]

Requires: Python 3.8+, stdlib only.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# Failure Taxonomy — signature patterns for auto-categorization
# ============================================================================

# Each category maps to a list of (regex, description) tuples.
# Patterns are matched case-insensitively against the error string.
# Order matters: more specific categories are checked first.
TAXONOMY: Dict[str, List[Tuple[str, str]]] = {
    "resource": [
        (r"out of memory|oomkilled|memoryerror|cannot allocate memory", "memory exhaustion"),
        (r"no space left on device|enospc|disk full", "disk full"),
        (r"too many open files|emfile|enfile", "file descriptor limit"),
        (r"429|too many requests|rate limit|rate.?limit", "API rate limit"),
        (r"quota exceeded", "cloud quota exceeded"),
        (r"sigkill|exit code 137|exit.?137", "process killed (often OOM)"),
    ],
    "permissions": [
        (r"\b401\b|unauthorized|invalid.?token|token.?expired|invalid_grant", "auth rejected"),
        (r"\b403\b|forbidden|access.?denied|insufficient.?privileges", "authorization denied"),
        (r"permission.?denied|eacces|permissionerror", "filesystem permission denied"),
    ],
    "network": [
        (r"connection.?refused|connectionrefusederror", "connection refused"),
        (r"connection.?timed.?out|etimedout|connection.?timeout", "connection timeout"),
        (r"name or service not known|nxdomain|dns|name.?resolution", "DNS resolution failure"),
        (r"ssl.?certificate|cert.?verify|tls.?handshake", "TLS/certificate failure"),
        (r"\b502\b|bad gateway|503|service unavailable|504|gateway timeout", "server-side failure"),
        (r"econnreset|connection.?reset", "connection reset"),
        (r"failed to connect", "connection failure"),
    ],
    "dependency": [
        (r"modulenotfounderror|importerror|no module named", "Python module not found"),
        (r"cannot find module|module_not_found", "Node.js module not found"),
        (r"noclassdeffounderror|classnotfoundexception", "Java class not found"),
        (r"unresolved dependency|version.?conflict|incompatible.?version", "version conflict"),
        (r"abi.?mismatch|undefined symbol", "ABI/symbol mismatch"),
        (r"package.*not found|no package available", "package not available"),
    ],
    "environment": [
        (r"command not found|no such file or directory|command.*not found", "binary not found"),
        (r"env:.*no such file|environment variable.*not set|var.*not defined", "missing env var"),
        (r"wrong version|incorrect version|version.?mismatch", "wrong version"),
        (r"executable file not found|exec format error", "binary format/arch issue"),
    ],
    "logic": [
        (r"assertionerror|assertion.?failed", "assertion violated"),
        (r"typeerror|valueerror|keyerror|attributeerror", "data shape/type error"),
        (r"indexerror", "index out of bounds"),
        (r"unexpected.*none|null.?pointer|nullreference", "null/unexpected None"),
    ],
}


def categorize_error(error_text: str) -> str:
    """
    Categorize an error message string.

    Returns the category name (e.g., 'network', 'permissions', 'logic',
    'environment', 'dependency', 'resource', or 'uncategorized').
    """
    if not error_text:
        return "uncategorized"
    lowered = error_text.lower()
    for category, patterns in TAXONOMY.items():
        for regex, _desc in patterns:
            if re.search(regex, lowered):
                return category
    return "uncategorized"


def describe_category_match(error_text: str) -> Optional[str]:
    """Return the human-readable description for the matched pattern, if any."""
    if not error_text:
        return None
    lowered = error_text.lower()
    for category, patterns in TAXONOMY.items():
        for regex, desc in patterns:
            if re.search(regex, lowered):
                return f"{category}: {desc}"
    return None


# ============================================================================
# Log Parsing
# ============================================================================

@dataclass
class ToolCall:
    """Represents a single tool call from the log."""
    timestamp: Optional[datetime] = None
    tool: str = "unknown"
    args: Dict[str, Any] = field(default_factory=dict)
    result: Optional[Dict[str, Any]] = None
    duration_ms: Optional[float] = None
    raw: Dict[str, Any] = field(default_factory=dict)

    @property
    def success(self) -> bool:
        if self.result is None:
            return True  # assume success if no result recorded
        if isinstance(self.result, dict):
            return self.result.get("success", True) and "error" not in self.result
        return True

    @property
    def error(self) -> Optional[str]:
        if self.result and isinstance(self.result, dict):
            return self.result.get("error")
        return None

    @property
    def is_failure(self) -> bool:
        return not self.success

    @property
    def category(self) -> str:
        return categorize_error(self.error) if self.error else "none"


def _parse_timestamp(ts: Any) -> Optional[datetime]:
    """Parse a timestamp from various formats into a datetime object."""
    if ts is None:
        return None
    if isinstance(ts, datetime):
        return ts
    if isinstance(ts, (int, float)):
        return datetime.fromtimestamp(ts, tz=timezone.utc)
    if isinstance(ts, str):
        # Try ISO 8601 first
        for fmt in (None,):  # None means fromisoformat
            try:
                if fmt is None:
                    # Handle trailing Z
                    cleaned = ts.replace("Z", "+00:00") if ts.endswith("Z") else ts
                    return datetime.fromisoformat(cleaned)
            except (ValueError, TypeError):
                pass
        # Try common alternative formats
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S"):
            try:
                return datetime.strptime(ts, fmt).replace(tzinfo=timezone.utc)
            except (ValueError, TypeError):
                pass
    return None


def parse_log_entry(entry: Dict[str, Any]) -> ToolCall:
    """Parse a single JSON log entry into a ToolCall."""
    return ToolCall(
        timestamp=_parse_timestamp(entry.get("timestamp")),
        tool=str(entry.get("tool", entry.get("name", "unknown"))),
        args=entry.get("args", {}),
        result=entry.get("result"),
        duration_ms=entry.get("duration_ms", entry.get("duration")),
        raw=entry,
    )


def load_log(path: str, fmt: str = "auto") -> List[ToolCall]:
    """
    Load a log file and return a list of ToolCall objects.

    Args:
        path: Path to the log file.
        fmt: 'jsonl', 'json', or 'auto' (detect from content).
    """
    log_path = Path(path)
    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")

    content = log_path.read_text(encoding="utf-8").strip()

    if not content:
        return []

    # Auto-detect format
    if fmt == "auto":
        if content.startswith("["):
            fmt = "json"
        else:
            fmt = "jsonl"

    entries: List[Dict[str, Any]] = []

    if fmt == "jsonl":
        for line_num, line in enumerate(content.splitlines(), 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Warning: skipping invalid JSON on line {line_num}: {e}", file=sys.stderr)
    elif fmt == "json":
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                entries = parsed
            elif isinstance(parsed, dict):
                # Maybe wrapped in a key like {"calls": [...]}
                for key in ("calls", "events", "log", "tool_calls", "entries"):
                    if key in parsed and isinstance(parsed[key], list):
                        entries = parsed[key]
                        break
                else:
                    entries = [parsed]  # single entry
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {path}: {e}")
    else:
        raise ValueError(f"Unknown format: {fmt}")

    calls = [parse_log_entry(e) for e in entries]

    # Sort by timestamp if available (stable sort preserves order for missing ts)
    calls.sort(key=lambda c: c.timestamp or datetime.max.replace(tzinfo=timezone.utc))

    return calls


# ============================================================================
# Timeline Analysis
# ============================================================================

@dataclass
class FailureAnalysis:
    """Results of analyzing a log for failures."""
    total_calls: int = 0
    failed_calls: int = 0
    first_failure: Optional[ToolCall] = None
    failures: List[ToolCall] = field(default_factory=list)
    timeline: List[ToolCall] = field(default_factory=list)
    categories: Dict[str, int] = field(default_factory=dict)

    def summary(self) -> Dict[str, Any]:
        return {
            "total_calls": self.total_calls,
            "failed_calls": self.failed_calls,
            "failure_rate": f"{self.failed_calls}/{self.total_calls}" if self.total_calls else "N/A",
            "first_failure_tool": self.first_failure.tool if self.first_failure else None,
            "first_failure_error": self.first_failure.error if self.first_failure else None,
            "first_failure_category": self.first_failure.category if self.first_failure else None,
            "category_distribution": self.categories,
        }


def analyze_calls(calls: List[ToolCall]) -> FailureAnalysis:
    """Analyze a list of tool calls for failures."""
    analysis = FailureAnalysis()
    analysis.total_calls = len(calls)
    analysis.timeline = calls

    for call in calls:
        if call.is_failure:
            analysis.failed_calls += 1
            analysis.failures.append(call)
            cat = call.category
            analysis.categories[cat] = analysis.categories.get(cat, 0) + 1
            if analysis.first_failure is None:
                analysis.first_failure = call

    return analysis


def format_timeline_markdown(analysis: FailureAnalysis) -> str:
    """Format the analysis as a Markdown timeline."""
    lines: List[str] = []
    lines.append("# Failure Timeline")
    lines.append("")

    summary = analysis.summary()
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Total tool calls:** {summary['total_calls']}")
    lines.append(f"- **Failed calls:** {summary['failed_calls']}")
    if summary["total_calls"] > 0:
        rate = (summary["failed_calls"] / summary["total_calls"]) * 100
        lines.append(f"- **Failure rate:** {rate:.1f}%")
    lines.append("")

    if summary["first_failure_tool"]:
        lines.append("## First Failure")
        lines.append("")
        lines.append(f"- **Tool:** `{summary['first_failure_tool']}`")
        lines.append(f"- **Error:** `{summary['first_failure_error']}`")
        lines.append(f"- **Category:** `{summary['first_failure_category']}`")
        lines.append("")

    if summary["category_distribution"]:
        lines.append("## Failure Category Distribution")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("|---|---|")
        for cat, count in sorted(summary["category_distribution"].items(),
                                  key=lambda x: -x[1]):
            lines.append(f"| {cat} | {count} |")
        lines.append("")

    lines.append("## Timeline")
    lines.append("")
    lines.append("| # | Timestamp | Tool | Outcome | Duration | Category |")
    lines.append("|---|---|---|---|---|---|")

    for i, call in enumerate(analysis.timeline, 1):
        ts = call.timestamp.strftime("%Y-%m-%d %H:%M:%S") if call.timestamp else "—"
        outcome = "❌ **FAILURE**" if call.is_failure else "✅ success"
        if call.error:
            outcome += f"\n\n`{call.error[:120]}`"
        dur = f"{call.duration_ms:.0f}ms" if call.duration_ms else "—"
        cat = call.category if call.is_failure else "—"
        lines.append(f"| {i} | {ts} | `{call.tool}` | {outcome} | {dur} | {cat} |")

    lines.append("")
    return "\n".join(lines)


# ============================================================================
# Post-Mortem Report Generation
# ============================================================================

POST_MORTEM_TEMPLATE = """\
# Post-Mortem: {title}

**Date:** {date}
**Author:** {author}
**Task:** [one-line description of what the agent was trying to do]
**Status:** Failed

## Summary

[One paragraph, plain language. Describe what happened, not just that it failed.]

**Failure category:** {primary_category}

## Auto-Generated Analysis

This section was generated by `failure_forensics.py`. Edit and expand it.

- **Total tool calls:** {total_calls}
- **Failed calls:** {failed_calls}
- **First failure tool:** `{first_failure_tool}`
- **First failure error:** `{first_failure_error}`
- **First failure category:** `{first_failure_category}`

## Timeline

{timeline_table}

## Impact

- **What was affected:** [fill in]
- **Severity:** [low / medium / high / critical]
- **Data loss:** [yes/no]

## Root Cause

[The terminal link of the causal chain. State plainly and specifically.]

## Causal Chain

[Trace backward from the failure. See references/post-mortem-template.md for format.]

## Contributing Factors

[Factors that didn't cause the failure but made it worse or harder to diagnose.]

## Action Items

| # | Action | Owner | Verification | Priority |
|---|---|---|---|---|
| 1 | [fill in] | [owner] | [how to verify] | [priority] |

## Lessons Learned

[Generalizable insights — the durable output of this post-mortem.]
"""


def generate_post_mortem(
    analysis: FailureAnalysis,
    title: str = "Untitled Incident",
    author: str = "agent",
) -> str:
    """Generate a pre-filled post-mortem report from analysis results."""
    summary = analysis.summary()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Build compact timeline table for the report
    timeline_rows: List[str] = []
    for i, call in enumerate(analysis.timeline, 1):
        ts = call.timestamp.strftime("%H:%M:%S") if call.timestamp else "—"
        outcome = "❌ FAILURE" if call.is_failure else "✅"
        err = call.error[:80] + "..." if call.error and len(call.error) > 80 else (call.error or "")
        timeline_rows.append(f"| {i} | {ts} | `{call.tool}` | {outcome} | {err} |")

    timeline_table = "| # | Time | Tool | Outcome | Error |\n|---|---|---|---|---|\n"
    timeline_table += "\n".join(timeline_rows) if timeline_rows else "| — | — | — | — | — |"

    primary_category = summary["first_failure_category"] or "uncategorized"

    return POST_MORTEM_TEMPLATE.format(
        title=title,
        date=now,
        author=author,
        primary_category=primary_category,
        total_calls=summary["total_calls"],
        failed_calls=summary["failed_calls"],
        first_failure_tool=summary["first_failure_tool"] or "N/A",
        first_failure_error=(summary["first_failure_error"] or "N/A")[:200],
        first_failure_category=summary["first_failure_category"] or "uncategorized",
        timeline_table=timeline_table,
    )


# ============================================================================
# CLI
# ============================================================================

def cmd_analyze(args: argparse.Namespace) -> int:
    """Analyze a log file and output a timeline."""
    try:
        calls = load_log(args.log, args.format)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not calls:
        print("No tool calls found in log.", file=sys.stderr)
        return 1

    analysis = analyze_calls(calls)
    output = format_timeline_markdown(analysis)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Timeline written to {args.output}", file=sys.stderr)
    else:
        print(output)

    return 0


def cmd_categorize(args: argparse.Namespace) -> int:
    """Categorize an error message."""
    category = categorize_error(args.error)
    description = describe_category_match(args.error)
    print(category)
    if args.verbose and description:
        print(f"Match: {description}", file=sys.stderr)
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    """Generate a post-mortem report from a log file."""
    try:
        calls = load_log(args.log, args.format)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    analysis = analyze_calls(calls)
    report = generate_post_mortem(analysis, title=args.title, author=args.author)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(report)

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="failure_forensics",
        description="Failure Forensics — log parser, categorizer, and post-mortem generator.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # analyze
    p_analyze = subparsers.add_parser("analyze", help="Analyze a log file and output a timeline.")
    p_analyze.add_argument("--log", required=True, help="Path to the log file (JSONL or JSON).")
    p_analyze.add_argument("--format", default="auto", choices=["auto", "jsonl", "json"],
                           help="Log format (default: auto-detect).")
    p_analyze.add_argument("--output", "-o", help="Write output to this file instead of stdout.")
    p_analyze.set_defaults(func=cmd_analyze)

    # categorize
    p_cat = subparsers.add_parser("categorize", help="Categorize an error message.")
    p_cat.add_argument("--error", required=True, help="The error message text to categorize.")
    p_cat.add_argument("--verbose", "-v", action="store_true", help="Print match description.")
    p_cat.set_defaults(func=cmd_categorize)

    # report
    p_report = subparsers.add_parser("report", help="Generate a post-mortem report from a log file.")
    p_report.add_argument("--log", required=True, help="Path to the log file (JSONL or JSON).")
    p_report.add_argument("--format", default="auto", choices=["auto", "jsonl", "json"],
                          help="Log format (default: auto-detect).")
    p_report.add_argument("--title", default="Untitled Incident", help="Report title.")
    p_report.add_argument("--author", default="agent", help="Report author.")
    p_report.add_argument("--output", "-o", help="Write report to this file instead of stdout.")
    p_report.set_defaults(func=cmd_report)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
