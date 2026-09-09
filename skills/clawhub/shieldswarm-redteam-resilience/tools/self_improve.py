#!/usr/bin/env python3
"""ShieldSwarm self_improve.py — durable feedback loop for the skill.

Stdlib only. No network. Local-only (feedback.jsonl is never uploaded).

Contract (machine-readable):
  self_improve.py log --event EVENT [--area AREA] [--context TEXT]
      -> appends one JSONL line to feedback.jsonl (skill root)
         stdout: logged=<event> file=<path>
      exit: 0 ok, 2 usage
  self_improve.py learn [--area AREA] [--limit N]
      -> prints the most recent matching feedback entries (newest last)
      exit: 0 ok (even if empty), 2 usage
  self_improve.py report [--out FILE] [--feedback FILE]
      -> renders templates/arena_improvement_report.md with live counts
         default out: improvement_report.md
      exit: 0 ok, 1 template missing, 2 usage
  self_improve.py reset --yes
      -> removes feedback.jsonl (guarded)
Areas: validate|approval|floor|mode|skill|incident (free text allowed)
Events: any snake_case token; recommended closed list lives in
references/self_improvement.md.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FEEDBACK = ROOT / "feedback.jsonl"
TEMPLATE = ROOT / "templates" / "arena_improvement_report.md"
EVENT_RE = re.compile(r"^[a-z0-9_]{2,64}$")
FORBIDDEN = re.compile(
    r"(?i)(api[_-]?key|token|password|secret|cookie|bearer\s+[a-z0-9._-]{8,}|AKIA[0-9A-Z]{16})"
)


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cmd_log(args: argparse.Namespace) -> int:
    if not EVENT_RE.match(args.event):
        print("error=invalid_event value=%s" % args.event, file=sys.stderr)
        return 2
    entry = {
        "ts": now(),
        "event": args.event,
        "area": args.area or "skill",
        "context": args.context or "",
    }
    blob = json.dumps(entry, ensure_ascii=False)
    if FORBIDDEN.search(blob):
        print("error=context_rejected reason=possible_secret_or_credential", file=sys.stderr)
        return 2
    FEEDBACK.parent.mkdir(parents=True, exist_ok=True)
    with FEEDBACK.open("a", encoding="utf-8") as fh:
        fh.write(blob + "\n")
    print("logged=%s file=%s" % (args.event, FEEDBACK))
    return 0


def read_entries(path: Path):
    entries = []
    if not path.exists():
        return entries
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            if isinstance(obj, dict) and "event" in obj:
                entries.append(obj)
        except json.JSONDecodeError:
            continue
    return entries


def cmd_learn(args: argparse.Namespace) -> int:
    entries = read_entries(args.feedback)
    if args.area:
        entries = [e for e in entries if e.get("area") == args.area]
    tail = entries[-args.limit:] if args.limit and args.limit > 0 else entries
    if not tail:
        print("learn=empty area=%s" % (args.area or "all"))
        return 0
    for e in tail:
        ctx = (e.get("context") or "").replace("\n", " ")
        print("ts=%s area=%s event=%s context=%s" % (e.get("ts", "?"), e.get("area", "?"), e.get("event", "?"), ctx))
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    if not TEMPLATE.exists():
        print("error=template_missing file=%s" % TEMPLATE, file=sys.stderr)
        return 1
    entries = read_entries(args.feedback)
    by_event = Counter(e.get("event", "?") for e in entries)
    by_area = Counter(e.get("area", "?") for e in entries)
    recent = entries[-10:]
    rows = "\n".join(
        "- %s · %s · %s · %s"
        % (e.get("ts", "?"), e.get("area", "?"), e.get("event", "?"), (e.get("context") or "")[:200])
        for e in recent
    ) or "- (none)"
    events = ", ".join("%s x%d" % (k, v) for k, v in sorted(by_event.items(), key=lambda kv: -kv[1])) or "(none)"
    areas = ", ".join("%s x%d" % (k, v) for k, v in sorted(by_area.items(), key=lambda kv: -kv[1])) or "(none)"
    out = TEMPLATE.read_text(encoding="utf-8")
    out = out.replace("{{GENERATED_AT}}", now())
    out = out.replace("{{TOTAL_EVENTS}}", str(len(entries)))
    out = out.replace("{{EVENT_COUNTS}}", events)
    out = out.replace("{{AREA_COUNTS}}", areas)
    out = out.replace("{{RECENT_EVENTS}}", rows)
    dest = Path(args.out)
    dest.write_text(out, encoding="utf-8")
    print("report=%s events=%d" % (dest, len(entries)))
    return 0


def cmd_reset(args: argparse.Namespace) -> int:
    if not args.yes:
        print("error=confirmation_required hint=pass --yes", file=sys.stderr)
        return 2
    if FEEDBACK.exists():
        FEEDBACK.unlink()
    print("reset=done")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(prog="self_improve.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    pl = sub.add_parser("log", help="append one feedback event")
    pl.add_argument("--event", required=True)
    pl.add_argument("--area", default=None)
    pl.add_argument("--context", default=None)
    pl.set_defaults(fn=cmd_log)
    plr = sub.add_parser("learn", help="print recent feedback entries")
    plr.add_argument("--area", default=None)
    plr.add_argument("--limit", type=int, default=20)
    plr.add_argument("--feedback", type=Path, default=FEEDBACK)
    plr.set_defaults(fn=cmd_learn)
    pr = sub.add_parser("report", help="render the improvement report")
    pr.add_argument("--out", default=str(ROOT / "improvement_report.md"))
    pr.add_argument("--feedback", type=Path, default=FEEDBACK)
    pr.set_defaults(fn=cmd_report)
    prs = sub.add_parser("reset", help="delete feedback.jsonl")
    prs.add_argument("--yes", action="store_true")
    prs.set_defaults(fn=cmd_reset)
    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
