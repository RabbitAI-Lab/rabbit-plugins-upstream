#!/usr/bin/env python3
"""agent-bom-scan self_improve — durable feedback loop for the skill.

Stdlib only. Local-only (feedback.jsonl is never uploaded).

  bom_improve.py log --event E [--area A] [--context C]
  bom_improve.py learn [--area A] [--limit N]
  bom_improve.py report [--out FILE]
  bom_improve.py reset --yes

Event vocabulary (closed list; extend via report review, not ad hoc):
  false_positive  missed_vuln  db_gap  parser_gap  perf_issue  doc_stale
  user_confusion  online_error
Areas: scan | db | parser | online | skill | report
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
EVENT_RE = re.compile(r"^[a-z0-9_]{2,48}$")
FORBIDDEN = re.compile(
    r"(?i)(api[_-]?key|token|password|secret|cookie|bearer\s+[a-z0-9._-]{8,}|AKIA[0-9A-Z]{16})")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def cmd_log(a):
    if not EVENT_RE.match(a.event):
        print("error=invalid_event value=%s" % a.event, file=sys.stderr)
        return 2
    entry = {"ts": now(), "event": a.event, "area": a.area or "skill", "context": a.context or ""}
    blob = json.dumps(entry, ensure_ascii=False)
    if FORBIDDEN.search(blob):
        print("error=context_rejected reason=possible_secret_or_credential", file=sys.stderr)
        return 2
    FEEDBACK.parent.mkdir(parents=True, exist_ok=True)
    with FEEDBACK.open("a", encoding="utf-8") as fh:
        fh.write(blob + "\n")
    print("logged=%s file=%s" % (a.event, FEEDBACK))
    return 0


def read_entries(path):
    out = []
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
            if isinstance(o, dict) and "event" in o:
                out.append(o)
        except json.JSONDecodeError:
            continue
    return out


def cmd_learn(a):
    entries = read_entries(a.feedback)
    if a.area:
        entries = [e for e in entries if e.get("area") == a.area]
    tail = entries[-a.limit:] if a.limit and a.limit > 0 else entries
    if not tail:
        print("learn=empty area=%s" % (a.area or "all"))
        return 0
    for e in tail:
        print("ts=%s area=%s event=%s context=%s" % (
            e.get("ts", "?"), e.get("area", "?"), e.get("event", "?"),
            (e.get("context") or "").replace("\n", " ")))
    return 0


def cmd_report(a):
    entries = read_entries(a.feedback)
    by_event = Counter(e.get("event", "?") for e in entries)
    by_area = Counter(e.get("area", "?") for e in entries)
    rows = "\n".join(
        "- %s · %s · %s · %s" % (e.get("ts", "?"), e.get("area", "?"),
                                 e.get("event", "?"), (e.get("context") or "")[:200])
        for e in entries[-10:]) or "- (none)"
    events = ", ".join("%s x%d" % kv for kv in sorted(by_event.items(), key=lambda kv: -kv[1])) or "(none)"
    areas = ", ".join("%s x%d" % kv for kv in sorted(by_area.items(), key=lambda kv: -kv[1])) or "(none)"
    out = (f"# BOM Scan Improvement Report\n\n- generated: {now()}\n"
           f"- total events: {len(entries)}\n- by event: {events}\n- by area: {areas}\n\n"
           f"## Recent\n\n{rows}\n\n## Suggested actions\n\n"
           "- db_gap / missed_vuln -> verify against OSV.dev, add records per references/advisories_format.md\n"
           "- false_positive -> re-check the range; never silently delete a record; annotate instead\n"
           "- parser_gap -> extend the parser + add a fixture in tools/fixtures/\n")
    dest = Path(a.out)
    dest.write_text(out, encoding="utf-8")
    print("report=%s events=%d" % (dest, len(entries)))
    return 0


def cmd_reset(a):
    if not a.yes:
        print("error=confirmation_required hint=pass --yes", file=sys.stderr)
        return 2
    if FEEDBACK.exists():
        FEEDBACK.unlink()
    print("reset=done")
    return 0


def main():
    p = argparse.ArgumentParser(prog="bom_improve.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    pl = sub.add_parser("log"); pl.add_argument("--event", required=True)
    pl.add_argument("--area"); pl.add_argument("--context"); pl.set_defaults(fn=cmd_log)
    plr = sub.add_parser("learn"); plr.add_argument("--area"); plr.add_argument("--limit", type=int, default=20)
    plr.add_argument("--feedback", type=Path, default=FEEDBACK); plr.set_defaults(fn=cmd_learn)
    pr = sub.add_parser("report"); pr.add_argument("--out", default=str(ROOT / "improvement_report.md"))
    pr.add_argument("--feedback", type=Path, default=FEEDBACK); pr.set_defaults(fn=cmd_report)
    prs = sub.add_parser("reset"); prs.add_argument("--yes", action="store_true"); prs.set_defaults(fn=cmd_reset)
    a = p.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
