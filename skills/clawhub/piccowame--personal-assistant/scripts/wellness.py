#!/usr/bin/env python3
"""Wellness engine for admin-assistant.

Drives the two health guardrails:
  * drink water every N minutes          (default 35)
  * stretch / muscle-relax every N minutes (default 60, i.e. after 1h of work)

The reminder jobs call `remind <kind>`; the script prints the reminder text and
exits 0. Outside the configured working window it prints the single token
`SILENT`, and the job must not notify the user.

Commands
--------
  remind {water|stretch}     print next reminder text (rotating) or SILENT
  status                     show config + today's counters + next due times
  set key=value [...]        update config (stretch_min water_min work_start
                             work_end enabled)
  log                        show today's reminder log
  reset-today                clear today's counters

Config lives in $ADMIN_ASSIST_HOME/wellness.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import (  # noqa: E402
    append_log, data_home, fail, fpath, iso, load, now, out, parse_time, read_log, save,
)

CONFIG_FILE = "wellness.json"
LOG_FILE = "wellness-log.jsonl"

DEFAULTS = {
    "enabled": True,
    "stretch_min": 60,      # every 1 hour of continuous work
    "water_min": 35,        # every 35 minutes
    "work_start": "09:00",  # quiet hours start (local tz)
    "work_end": "22:00",    # quiet hours end
    "weekends": True,       # also remind on Sat/Sun
}

WATER = [
    "💧 Water break — drink 200–300 ml (about a glass).",
    "💧 Hydration check — refill your bottle and take 5 slow sips.",
    "💧 Time to drink water. Small sips, no gulping — your kidneys say thanks.",
    "💧 Water + posture: shoulders down, jaw unclenched, drink a glass now.",
    "💧 Dehydration sneaks up as fatigue. Drink water before you feel thirsty.",
    "💧 60% of you is water. Top the tank up — one glass, right now.",
]

STRETCH = [
    "🧘 Stretch break (1h of work!) — 2 min: neck rolls, shoulder shrugs ×10, "
    "stand and reach for the ceiling.",
    "🧘 Muscle-relax — 3 min: cat-cow on the chair, wrist circles ×10 each way, "
    "look at something 20 m away for 20 s.",
    "🧘 Move break — stand up, 10 bodyweight squats, 30 s chest-opener doorway stretch, "
    "roll your ankles.",
    "🧘 Eye + back reset — 20-20-20 rule (20 ft / 20 s), then seated spinal twist 30 s each side.",
    "🧘 Micro-yoga — forward fold 30 s, thread-the-needle 30 s each side, "
    "3 deep diaphragmatic breaths (4-in / 6-out).",
    "🧘 Tension scan — unclench jaw, drop shoulders, shake out hands for 20 s, "
    "then 10 slow neck tilts each side.",
]


def cfg() -> dict:
    c = dict(DEFAULTS)
    c.update(load(CONFIG_FILE, {}))
    return c


def save_cfg(c: dict) -> None:
    save(CONFIG_FILE, c)


def _within_hours(c: dict) -> bool:
    n = now()
    if not c.get("enabled", True):
        return False
    if not c.get("weekends", True) and n.weekday() >= 5:
        return False
    start = parse_time(c["work_start"])
    end = parse_time(c["work_end"])
    cur = n.time().replace(tzinfo=None)
    if start <= end:
        return start <= cur <= end
    return cur >= start or cur <= end  # overnight window


def _count_today(kind: str) -> int:
    day = now().date().isoformat()
    return sum(1 for r in read_log(LOG_FILE) if r.get("kind") == kind and r.get("at", "")[:10] == day)


def _next_due(kind: str, c: dict) -> datetime:
    minutes = c[f"{kind}_min"]
    entries = [r for r in read_log(LOG_FILE) if r.get("kind") == kind]
    base = datetime.fromisoformat(entries[-1]["at"]) if entries else now()
    return base + timedelta(minutes=minutes)


def cmd_remind(args) -> int:
    c = cfg()
    kind = args.kind
    if not _within_hours(c):
        print("SILENT")
        return 0
    bucket = WATER if kind == "water" else STRETCH
    idx = _count_today(kind) % len(bucket)
    text = bucket[idx]
    append_log(LOG_FILE, {"kind": kind, "at": iso(now()), "index": idx})
    print(text)
    return 0


def cmd_status(_args) -> int:
    c = cfg()
    n = now()
    out("🌿 WELLNESS ENGINE")
    out(f"   Data home    : {data_home()}")
    out(f"   Now          : {n.strftime('%Y-%m-%d %H:%M %A')}")
    out(f"   Enabled      : {c['enabled']}   Weekends: {c['weekends']}")
    out(f"   Working hours: {c['work_start']} – {c['work_end']}")
    out(f"   Water every  : {c['water_min']} min   → {_next_due('water', c).strftime('%H:%M')}"
        f"   (drank reminders today: {_count_today('water')})")
    out(f"   Stretch every: {c['stretch_min']} min → {_next_due('stretch', c).strftime('%H:%M')}"
        f"   (stretch reminders today: {_count_today('stretch')})")
    out(f"   In working window: {_within_hours(c)}")
    return 0


def cmd_set(args) -> int:
    c = cfg()
    if not args.pairs:
        fail("set requires key=value pairs")
    for pair in args.pairs:
        if "=" not in pair:
            fail(f"bad pair {pair!r}, expected key=value")
        k, v = pair.split("=", 1)
        k = k.strip()
        if k not in DEFAULTS:
            fail(f"unknown key {k!r}; valid: {', '.join(DEFAULTS)}")
        if k in ("stretch_min", "water_min"):
            try:
                c[k] = max(1, int(v))
            except ValueError:
                fail(f"{k} must be an integer number of minutes")
        elif k in ("work_start", "work_end"):
            parse_time(v)
            c[k] = v.strip()
        else:
            c[k] = str(v).strip().lower() in {"1", "true", "yes", "on"}
    save_cfg(c)
    out("✔ wellness config updated:")
    out(json.dumps(c, ensure_ascii=False, indent=2))
    out("")
    out("NOTE: re-register the wellness cron jobs if you changed the intervals.")
    return 0


def cmd_log(_args) -> int:
    day = now().date().isoformat()
    rows = [r for r in read_log(LOG_FILE) if r.get("at", "")[:10] == day]
    if not rows:
        out("No wellness reminders logged today.")
        return 0
    for r in rows:
        out(f"  {r.get('at')}  {r.get('kind')}")
    out(f"\n{len(rows)} reminder(s) today.")
    return 0


def cmd_reset(_args) -> int:
    rows = read_log(LOG_FILE)
    day = now().date().isoformat()
    keep = [r for r in rows if r.get("at", "")[:10] != day]
    with open(fpath(LOG_FILE), "w", encoding="utf-8") as fh:
        for r in keep:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    out(f"✔ cleared {len(rows) - len(keep)} log entries from today")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="wellness.py")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("remind")
    r.add_argument("kind", choices=["water", "stretch"])
    r.set_defaults(func=cmd_remind)
    sub.add_parser("status").set_defaults(func=cmd_status)
    s = sub.add_parser("set")
    s.add_argument("pairs", nargs="*")
    s.set_defaults(func=cmd_set)
    sub.add_parser("log").set_defaults(func=cmd_log)
    sub.add_parser("reset-today").set_defaults(func=cmd_reset)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
