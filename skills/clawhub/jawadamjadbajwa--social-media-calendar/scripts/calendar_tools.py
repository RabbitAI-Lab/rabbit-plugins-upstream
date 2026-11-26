#!/usr/bin/env python3
"""Plan, check and export a social media calendar (standard library only; Python 3.9+).

Commands
  skeleton PLAN.json [--out PLAN.json]   fill empty slots from the cadence and pillar targets (keeps existing items)
  check    PLAN.json [--json out.json]   cadence, pillar mix, gaps, clashes, blackouts, missing fields, overdue items
  export   PLAN.json --out DIR           calendar.csv, calendar.ics and calendar.md
  shift    PLAN.json --days N [--from YYYY-MM-DD] [--platform NAME]   move later items (delays, schedule changes)

Plan format
  {"brand": "Botvee", "timezone": "Asia/Karachi", "start": "2026-12-01", "weeks": 4,
   "platforms": {"instagram": {"per_week": 4, "days": ["Mon","Wed","Fri","Sun"], "times": ["19:00"]},
                 "linkedin":  {"per_week": 2, "days": ["Tue","Thu"], "times": ["10:00"]}},
   "pillars": {"Educate": 40, "Proof": 20, "Story": 20, "Offer": 10, "Community": 10},
   "blackout": ["2026-12-25"],
   "events": [{"date": "2026-12-15", "name": "Product launch", "note": ""}],
   "items": [{"date": "2026-12-01", "time": "19:00", "platform": "instagram", "pillar": "Educate", "format": "carousel",
              "title": "3 mistakes", "brief": "", "cta": "", "status": "idea", "owner": "", "notes": ""}]}

Days and times in the plan are assumptions until real audience data (analytics) supports them. The tool does not know holidays
or religious dates: put them in "events" or "blackout" after checking current sources (lunar dates move each year).
"""
import argparse
import csv
import datetime as dt
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
STATUSES = ["idea", "draft", "review", "approved", "scheduled", "posted", "skipped"]


class Fail(RuntimeError):
    pass


def load(path):
    try:
        p = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as e:
        raise Fail(f"Cannot read plan: {e}") from None
    for k in ("start", "weeks", "platforms"):
        if k not in p:
            raise Fail(f"Plan needs '{k}'.")
    try:
        p["_start"] = dt.date.fromisoformat(p["start"])
    except ValueError:
        raise Fail("'start' must be YYYY-MM-DD.") from None
    if p["_start"].weekday() != 0:
        p["_warn_start"] = f"start {p['start']} is a {DAYS[p['_start'].weekday()]}; weeks are counted from it."
    p.setdefault("items", [])
    p.setdefault("pillars", {})
    p.setdefault("blackout", [])
    p.setdefault("events", [])
    p.setdefault("timezone", "UTC")
    if ZoneInfo:
        try:
            ZoneInfo(p["timezone"])
        except Exception:
            raise Fail(f"Unknown timezone '{p['timezone']}'. Use an IANA name like Asia/Karachi (Windows may need `pip install tzdata`).") from None
    return p


def save(plan, path):
    out = {k: v for k, v in plan.items() if not k.startswith("_")}
    Path(path).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")


def pdate(s):
    try:
        return dt.date.fromisoformat(s)
    except (ValueError, TypeError):
        return None


def end_date(plan):
    return plan["_start"] + dt.timedelta(days=7 * int(plan["weeks"]) - 1)


# ---- skeleton ----------------------------------------------------------------
def pillar_sequence(pillars, n):
    """Smooth weighted round-robin so pillars are spread out, not clumped."""
    if not pillars:
        return [""] * n
    total = sum(pillars.values())
    cur = {k: 0.0 for k in pillars}
    out = []
    for _ in range(n):
        for k, w in pillars.items():
            cur[k] += w
        best = max(cur, key=lambda k: cur[k])
        cur[best] -= total
        out.append(best)
    return out


def cmd_skeleton(a):
    plan = load(a.plan)
    existing = {(i.get("date"), i.get("platform"), i.get("time")) for i in plan["items"]}
    black = set(plan["blackout"])
    slots = []
    for w in range(int(plan["weeks"])):
        for plat, cfg in plan["platforms"].items():
            days = cfg.get("days") or []
            if not days:
                raise Fail(f"Platform '{plat}' needs 'days'.")
            times = cfg.get("times") or ["12:00"]
            for j, d in enumerate(days):
                if d not in DAYS:
                    raise Fail(f"Unknown day '{d}' for {plat}; use {', '.join(DAYS)}.")
                ws = plan["_start"] + dt.timedelta(days=7 * w)
                date = ws + dt.timedelta(days=(DAYS.index(d) - ws.weekday()) % 7)
                if date > end_date(plan) or date.isoformat() in black:
                    continue
                slots.append((date, times[j % len(times)], plat))
    slots = sorted(set(slots))
    seq = pillar_sequence(plan["pillars"], len(slots))
    added = 0
    for (date, t, plat), pil in zip(slots, seq):
        if (date.isoformat(), plat, t) in existing:
            continue
        plan["items"].append({"date": date.isoformat(), "time": t, "platform": plat, "pillar": pil, "format": "",
                              "title": "", "brief": "", "cta": "", "status": "idea", "owner": "", "notes": ""})
        added += 1
    plan["items"].sort(key=lambda i: (i.get("date", ""), i.get("time", ""), i.get("platform", "")))
    save(plan, a.out or a.plan)
    print(f"Added {added} empty slots ({len(plan['items'])} items total). Fill title, format, brief and CTA, then run check.")
    if black:
        print(f"Skipped {len(black)} blackout date(s).")


# ---- check -------------------------------------------------------------------
def cmd_check(a):
    plan = load(a.plan)
    res = []

    def add(level, msg):
        res.append({"level": level, "text": msg})

    if plan.get("_warn_start"):
        add("INFO", plan["_warn_start"])
    items = plan["items"]
    if not items:
        raise Fail("No items. Run skeleton first or add items.")
    start, end = plan["_start"], end_date(plan)
    today = dt.date.today()
    black = set(plan["blackout"])
    by_week = defaultdict(Counter)
    pillars = Counter()
    dates_by_plat = defaultdict(list)
    seen = Counter()
    for it in items:
        d = pdate(it.get("date"))
        pf = it.get("platform", "")
        if not d:
            add("FAIL", f"Bad date in item '{it.get('title') or pf}': {it.get('date')!r}.")
            continue
        if pf not in plan["platforms"]:
            add("WARN", f"{it['date']} item uses platform '{pf}' that is not in the plan's platforms.")
        if not (start <= d <= end):
            add("INFO", f"{it['date']} {pf} is outside the plan window {start} to {end}.")
        if it["date"] in black:
            add("FAIL", f"{it['date']} {pf} is on a blackout date.")
        if it.get("status") not in STATUSES:
            add("WARN", f"{it['date']} {pf}: status {it.get('status')!r} not one of {', '.join(STATUSES)}.")
        wk = (d - start).days // 7
        by_week[wk][pf] += 1
        if it.get("pillar"):
            pillars[it["pillar"]] += 1
        dates_by_plat[pf].append(d)
        if it.get("title"):
            seen[(it["title"].strip().lower(), pf)] += 1
        filled = it.get("title") and it.get("format")
        if it.get("status") in ("approved", "scheduled") and not (filled and it.get("brief") or filled and it.get("cta")):
            add("WARN", f"{it['date']} {pf} is '{it['status']}' but title/format/brief or CTA is missing.")
        if d < today and it.get("status") in ("idea", "draft", "review", "approved", "scheduled"):
            add("WARN", f"{it['date']} {pf} is in the past but status is '{it['status']}'.")
        if it.get("time"):
            try:
                dt.time.fromisoformat(it["time"])
            except ValueError:
                add("FAIL", f"{it['date']} {pf}: time {it['time']!r} is not HH:MM.")
    for (t, pf), n in seen.items():
        if n > 1:
            add("WARN", f"Title '{t}' appears {n} times on {pf}.")
    for pf, cfg in plan["platforms"].items():
        want = cfg.get("per_week")
        if want:
            for w in range(int(plan["weeks"])):
                have = by_week[w][pf]
                if have != want:
                    add("WARN", f"Week {w + 1} {pf}: {have} items, plan says {want} per week.")
        ds = sorted(set(dates_by_plat[pf]))
        for x, y in zip(ds, ds[1:]):
            if (y - x).days > 5:
                add("WARN", f"{pf}: {(y - x).days}-day gap between {x} and {y}.")
    total = sum(pillars.values())
    for k, target in plan["pillars"].items():
        share = pillars.get(k, 0) * 100 / total if total else 0
        if abs(share - target) > 10:
            add("WARN", f"Pillar '{k}': {share:.0f}% of items vs target {target}%.")
    extra = [k for k in pillars if k not in plan["pillars"]]
    if extra and plan["pillars"]:
        add("INFO", f"Pillars not in the target list: {', '.join(extra)}.")
    per_day = Counter(it["date"] for it in items)
    for d, n in per_day.items():
        if n >= 4:
            add("INFO", f"{d} has {n} posts across platforms; check the team can produce them.")
    ev = {e["date"]: e["name"] for e in plan["events"] if e.get("date")}
    for d, name in ev.items():
        if per_day.get(d, 0) == 0 and start <= (pdate(d) or start) <= end:
            add("INFO", f"Event '{name}' on {d} has no post planned.")
    statuses = Counter(i.get("status") for i in items)
    add("INFO", "Status: " + ", ".join(f"{k} {v}" for k, v in statuses.items()))
    if total:
        add("INFO", "Pillar mix: " + ", ".join(f"{k} {v * 100 / total:.0f}%" for k, v in pillars.most_common()))
    for r in res:
        print(f"[{r['level']}] {r['text']}")
    fails = sum(1 for r in res if r["level"] == "FAIL")
    warns = sum(1 for r in res if r["level"] == "WARN")
    print(f"\n{len(items)} items: {fails} fail, {warns} warn. Days, times and cadence are assumptions until audience data supports them.")
    if a.json:
        Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if fails else 0


# ---- export ------------------------------------------------------------------
def local_dt(plan, it):
    d = pdate(it.get("date"))
    t = dt.time.fromisoformat(it.get("time") or "09:00")
    x = dt.datetime.combine(d, t)
    return x.replace(tzinfo=ZoneInfo(plan["timezone"])) if ZoneInfo else x


def ics_escape(s):
    return (s or "").replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def cmd_export(a):
    plan = load(a.plan)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    items = sorted(plan["items"], key=lambda i: (i.get("date", ""), i.get("time", ""), i.get("platform", "")))
    cols = ["date", "time", "weekday", "platform", "pillar", "format", "title", "brief", "cta", "status", "owner", "notes"]
    with open(out / "calendar.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(cols + ["timezone"])
        for it in items:
            d = pdate(it.get("date"))
            w.writerow([it.get("date"), it.get("time", ""), DAYS[d.weekday()] if d else ""] + [it.get(c, "") for c in cols[3:]] + [plan["timezone"]])
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//social-media-calendar//EN", "CALSCALE:GREGORIAN"]
    for n, it in enumerate(items, 1):
        if not pdate(it.get("date")):
            continue
        s = local_dt(plan, it)
        e = s + dt.timedelta(minutes=30)
        su = s.astimezone(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") if s.tzinfo else s.strftime("%Y%m%dT%H%M%S")
        eu = e.astimezone(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") if e.tzinfo else e.strftime("%Y%m%dT%H%M%S")
        title = f"[{it.get('platform', '')}] {it.get('title') or it.get('pillar') or 'TBD'}"
        desc = "\n".join(x for x in (f"Format: {it.get('format', '')}", f"Pillar: {it.get('pillar', '')}", f"Status: {it.get('status', '')}",
                                     f"CTA: {it.get('cta', '')}", it.get("brief", ""), it.get("notes", "")) if x.split(": ")[-1])
        lines += ["BEGIN:VEVENT", f"UID:smc-{plan['start']}-{n}-{abs(hash(title)) % 10**8}@local", f"DTSTAMP:{stamp}",
                  f"DTSTART:{su}", f"DTEND:{eu}", f"SUMMARY:{ics_escape(title)}", f"DESCRIPTION:{ics_escape(desc)}", "END:VEVENT"]
    lines.append("END:VCALENDAR")
    (out / "calendar.ics").write_text("\r\n".join(lines) + "\r\n", encoding="utf-8")
    md = [f"# Content calendar: {plan.get('brand', '')}", f"Timezone: {plan['timezone']}. Window: {plan['start']} to {end_date(plan)}.", ""]
    for w in range(int(plan["weeks"])):
        ws = plan["_start"] + dt.timedelta(days=7 * w)
        we = ws + dt.timedelta(days=6)
        md += [f"## Week {w + 1} ({ws} to {we})", "", "| Date | Time | Platform | Pillar | Format | Title | Status |", "|---|---|---|---|---|---|---|"]
        for it in items:
            d = pdate(it.get("date"))
            if d and ws <= d <= we:
                md.append(f"| {DAYS[d.weekday()]} {it['date']} | {it.get('time', '')} | {it.get('platform', '')} | {it.get('pillar', '')} | "
                          f"{it.get('format', '')} | {(it.get('title') or '').replace('|', '/')} | {it.get('status', '')} |")
        md.append("")
    (out / "calendar.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote calendar.csv, calendar.ics and calendar.md to {out} ({len(items)} items). The ICS uses UTC times; import it into any calendar app.")


def cmd_shift(a):
    plan = load(a.plan)
    frm = pdate(a.from_date) if a.from_date else plan["_start"]
    if not frm:
        raise Fail("--from must be YYYY-MM-DD.")
    n = 0
    for it in plan["items"]:
        d = pdate(it.get("date"))
        if d and d >= frm and (not a.platform or it.get("platform") == a.platform) and it.get("status") != "posted":
            it["date"] = (d + dt.timedelta(days=a.days)).isoformat()
            n += 1
    plan["items"].sort(key=lambda i: (i.get("date", ""), i.get("time", ""), i.get("platform", "")))
    save(plan, a.plan)
    print(f"Moved {n} item(s) by {a.days} day(s). Posted items were left alone. Run check for blackout or gap problems.")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("skeleton")
    s.add_argument("plan")
    s.add_argument("--out")
    s.set_defaults(fn=cmd_skeleton)
    c = sub.add_parser("check")
    c.add_argument("plan")
    c.add_argument("--json")
    c.set_defaults(fn=cmd_check)
    e = sub.add_parser("export")
    e.add_argument("plan")
    e.add_argument("--out", required=True)
    e.set_defaults(fn=cmd_export)
    h = sub.add_parser("shift")
    h.add_argument("plan")
    h.add_argument("--days", type=int, required=True)
    h.add_argument("--from", dest="from_date")
    h.add_argument("--platform")
    h.set_defaults(fn=cmd_shift)
    a = p.parse_args(argv)
    try:
        return a.fn(a) or 0
    except Fail as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
