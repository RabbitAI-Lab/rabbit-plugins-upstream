#!/usr/bin/env python3
"""
Tool Economy — Session Analyzer
==============================

Analyze an agent session log and report tool-call efficiency metrics:

  - total / redundant calls
  - serializable-but-parallel (missed batching) calls
  - estimated overhead (extra round-trips x latency)
  - a tool economy score (0-100)

Usage:
    python3 analyze_session.py <session.json>
    python3 analyze_session.py <session.json> --window 10 --latency 300
    python3 analyze_session.py --help

Session log format (JSON array of records):
    [
      {
        "turn": 1,                       # optional: turn index
        "tool": "read_file",             # required
        "args": {"path": "src/main.py"}, # required (dict or string)
        "calls_in_turn": 1               # optional: how many calls this turn had
      },
      ...
    ]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ToolCall:
    """A single tool invocation extracted from the session log."""
    index: int
    tool: str
    args: dict[str, Any] | str
    turn: int | None = None
    calls_in_turn: int | None = None

    @property
    def signature(self) -> str:
        """Stable string identity of this call for duplicate detection."""
        # Sort dict keys so {"a":1,"b":2} == {"b":2,"a":1}.
        if isinstance(self.args, dict):
            blob = json.dumps(self.args, sort_keys=True, default=str)
        else:
            blob = str(self.args)
        return f"{self.tool}::{blob}"

    @property
    def digest(self) -> str:
        """Short hash of the signature, for compact dedup."""
        return hashlib.sha1(self.signature.encode()).hexdigest()[:12]


@dataclass
class WasteItem:
    """One detected inefficiency."""
    kind: str
    weight: float          # how many wasted round-trips this represents
    detail: str
    calls: list[int] = field(default_factory=list)  # indices of involved calls


@dataclass
class Report:
    """Aggregated efficiency report."""
    total_calls: int = 0
    redundant_calls: list[WasteItem] = field(default_factory=list)
    missed_parallel: list[WasteItem] = field(default_factory=list)
    latency_ms: int = 300           # cost per extra round-trip

    @property
    def redundant_count(self) -> int:
        return sum(max(0, round(w.weight)) for w in self.redundant_calls)

    @property
    def missed_parallel_count(self) -> int:
        return sum(max(0, round(w.weight)) for w in self.missed_parallel)

    @property
    def extra_round_trips(self) -> int:
        return self.redundant_count + self.missed_parallel_count

    @property
    def overhead_ms(self) -> int:
        return self.extra_round_trips * self.latency_ms

    @property
    def score(self) -> int:
        """Economy score in [0, 100]. 100 = zero waste."""
        if self.total_calls == 0:
            return 100
        # Each wasted round-trip costs ~6 points, scaled by call volume so a
        # large session isn't penalised as harshly per incident.
        penalty = min(100, self.extra_round_trips * 6 * (10 / max(self.total_calls, 1)) * 10)
        return max(0, min(100, round(100 - penalty)))

    @property
    def score_band(self) -> str:
        s = self.score
        if s >= 90:
            return "Excellent"
        if s >= 70:
            return "Good"
        if s >= 50:
            return "Fair"
        return "Poor"


# ---------------------------------------------------------------------------
# Detection logic
# ---------------------------------------------------------------------------

# Tools that are "read-only / side-effect free" and thus always safe to batch
# with any other independent call. Used to avoid flagging false parallelism
# between calls that actually mutate shared state.
READONLY_TOOLS = {
    "read_file", "search_files", "web_search", "web_extract",
    "browser_get_images", "browser_snapshot", "browser_vision",
    "git_status", "git_log", "git_diff", "ls", "cat", "head", "tail",
    "grep", "find", "wc", "session_search", "skill_view", "skills_list",
}

# Tools that are "powerful" — a single call replaces a chain. Using the weak
# alternatives counts as a separate anti-pattern we surface as a hint.
WEAK_TO_STRONG = {
    "cat": "read_file",
    "head": "read_file (offset/limit)",
    "tail": "read_file (offset/limit)",
    "grep": "search_files (content)",
    "find": "search_files (files)",
    "ls": "search_files (files)",
    "wc": "search_files (count)",
}


def detect_redundant(calls: list[ToolCall], window: int) -> list[WasteItem]:
    """Find duplicate calls within a sliding window."""
    waste: list[WasteItem] = []
    for i, c in enumerate(calls):
        # Look back within the window for the same signature.
        start = max(0, i - window)
        for j in range(start, i):
            if calls[j].signature == c.signature:
                waste.append(WasteItem(
                    kind="redundant_call",
                    weight=1.0,
                    detail=f"{c.tool}({c._short_args()}) repeated (call #{j+1} == #{i+1})",
                    calls=[j, i],
                ))
                break  # one prior match is enough
    return waste


def detect_missed_parallel(calls: list[ToolCall]) -> list[WasteItem]:
    """Find independent calls issued serially that could have been batched.

    Heuristic: consecutive calls in *separate turns* that are read-only and
    share no argument overlap are candidates. If `calls_in_turn` is provided,
    a turn with exactly 1 call when the next turn also has 1 read-only call is
    flagged.
    """
    waste: list[WasteItem] = []
    i = 0
    while i < len(calls) - 1:
        chain: list[int] = []
        # Walk forward collecting a chain of serial singleton read-only calls.
        j = i
        while j < len(calls) - 1:
            cur, nxt = calls[j], calls[j + 1]
            cur_singleton = (cur.calls_in_turn or 1) == 1
            nxt_singleton = (nxt.calls_in_turn or 1) == 1
            consecutive = (cur.turn is not None and nxt.turn is not None
                           and nxt.turn == cur.turn + 1)
            if (cur_singleton and nxt_singleton and consecutive
                    and cur.tool in READONLY_TOOLS
                    and nxt.tool in READONLY_TOOLS
                    and not _args_overlap(cur.args, nxt.args)):
                if not chain:
                    chain.append(j)
                chain.append(j + 1)
                j += 1
            else:
                break
        if len(chain) >= 2:
            # A chain of N serial calls could be 1 batched turn → N-1 saved.
            saved = len(chain) - 1
            waste.append(WasteItem(
                kind="missed_batching",
                weight=float(saved),
                detail=(
                    f"{len(chain)} serial read-only calls (turns "
                    f"{calls[chain[0]].turn}\u2013{calls[chain[-1]].turn}) "
                    f"could be 1 batched turn"
                ),
                calls=chain,
            ))
            i = chain[-1] + 1
        else:
            i += 1
    return waste


def detect_weak_chains(calls: list[ToolCall]) -> list[WasteItem]:
    """Surface use of weak commands that have a powerful equivalent."""
    waste: list[WasteItem] = []
    for i, c in enumerate(calls):
        if c.tool in WEAK_TO_STRONG:
            strong = WEAK_TO_STRONG[c.tool]
            waste.append(WasteItem(
                kind="weak_command",
                weight=0.5,
                detail=f"{c.tool}() could be replaced by {strong}",
                calls=[i],
            ))
    return waste


def _args_overlap(a: Any, b: Any) -> bool:
    """True if two calls clearly target the same resource (so batching may
    still be fine, but we avoid flagging near-identical serial reads as
    'missed parallel' — those are caught by redundant detection instead)."""
    if isinstance(a, dict) and isinstance(b, dict):
        return _norm(a) == _norm(b)
    return str(a) == str(b)


def _norm(d: dict) -> str:
    return json.dumps(d, sort_keys=True, default=str)


# Small helper attached to ToolCall for nice detail strings.
def _short_args(self) -> str:
    s = json.dumps(self.args, default=str) if isinstance(self.args, dict) else str(self.args)
    return s if len(s) <= 60 else s[:57] + "..."

ToolCall._short_args = _short_args  # type: ignore[attr-defined]


# ---------------------------------------------------------------------------
# Parsing & reporting
# ---------------------------------------------------------------------------

def parse_session(path: Path) -> list[ToolCall]:
    data = json.loads(path.read_text())
    if isinstance(data, dict) and "calls" in data:
        data = data["calls"]
    if not isinstance(data, list):
        raise ValueError("Session log must be a JSON array of call records.")
    calls: list[ToolCall] = []
    for idx, rec in enumerate(data):
        if not isinstance(rec, dict) or "tool" not in rec:
            raise ValueError(f"Record #{idx} missing required 'tool' field.")
        calls.append(ToolCall(
            index=idx,
            tool=str(rec["tool"]),
            args=rec.get("args", {}),
            turn=rec.get("turn"),
            calls_in_turn=rec.get("calls_in_turn"),
        ))
    return calls


def build_report(calls: list[ToolCall], window: int, latency_ms: int) -> Report:
    r = Report(total_calls=len(calls), latency_ms=latency_ms)
    r.redundant_calls = detect_redundant(calls, window)
    r.missed_parallel = detect_missed_parallel(calls)
    return r


def render_report(r: Report, weak: list[WasteItem]) -> str:
    lines: list[str] = []
    lines.append("Tool Economy Report")
    lines.append("===================")
    lines.append(f"Total tool calls              : {r.total_calls}")
    lines.append(f"Redundant calls               : {r.redundant_count}")
    lines.append(f"Missed parallel opportunities : {r.missed_parallel_count}")
    lines.append(f"Estimated extra round-trips   : {r.extra_round_trips}")
    lines.append(f"Estimated overhead            : {r.overhead_ms} ms")
    lines.append(
        f"Tool economy score            : {r.score}/100  [{r.score_band}]"
    )
    lines.append("")

    items: list[tuple[int, str, int]] = []  # (rank, label, ms)
    if r.redundant_count:
        items.append((1, f"redundant_call      x{r.redundant_count}",
                      r.redundant_count * r.latency_ms))
    if r.missed_parallel_count:
        items.append((1, f"missed_batching     x{r.missed_parallel_count}",
                      r.missed_parallel_count * r.latency_ms))
    if weak:
        w = sum(max(0, round(w.weight)) for w in weak)
        items.append((1, f"weak_command        x{w}", round(w * r.latency_ms * 0.5)))

    if items:
        lines.append("Top waste sources:")
        for i, (_, label, ms) in enumerate(items, 1):
            lines.append(f"  {i}. {label}   (~{ms} ms)")
    else:
        lines.append("No significant waste detected. Nice work.")

    if weak:
        lines.append("")
        lines.append("Weak-command hints (not scored, just suggestions):")
        for w in weak[:8]:
            lines.append(f"  - {w.detail}")

    lines.append("")
    detail = r.redundant_calls + r.missed_parallel
    if detail:
        lines.append("Detail:")
        for d in detail[:15]:
            lines.append(f"  - [{d.kind}] {d.detail}")
        if len(detail) > 15:
            lines.append(f"  ... and {len(detail) - 15} more")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Analyze an agent session log for tool-call efficiency.")
    p.add_argument("session", type=Path,
                   help="Path to session log JSON.")
    p.add_argument("--window", type=int, default=10,
                   help="Sliding window (in calls) for redundant-call "
                        "detection. Default: 10")
    p.add_argument("--latency", type=int, default=300,
                   help="Assumed per-round-trip latency in ms. Default: 300")
    p.add_argument("--json", action="store_true",
                   help="Emit the report as JSON instead of text.")
    args = p.parse_args(argv)

    if not args.session.is_file():
        print(f"error: session file not found: {args.session}", file=sys.stderr)
        return 2

    try:
        calls = parse_session(args.session)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"error: could not parse session: {e}", file=sys.stderr)
        return 2

    report = build_report(calls, args.window, args.latency)
    weak = detect_weak_chains(calls)

    if args.json:
        out = {
            "total_calls": report.total_calls,
            "redundant_calls": report.redundant_count,
            "missed_parallel": report.missed_parallel_count,
            "extra_round_trips": report.extra_round_trips,
            "overhead_ms": report.overhead_ms,
            "score": report.score,
            "score_band": report.score_band,
            "weak_commands": [
                {"detail": w.detail, "calls": w.calls} for w in weak
            ],
            "details": [
                {"kind": w.kind, "detail": w.detail, "calls": w.calls}
                for w in (report.redundant_calls + report.missed_parallel)
            ],
        }
        print(json.dumps(out, indent=2))
    else:
        print(render_report(report, weak))
    return 0


if __name__ == "__main__":
    sys.exit(main())
