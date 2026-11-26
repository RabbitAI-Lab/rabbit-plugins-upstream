#!/usr/bin/env python3
"""Social media analytics from platform CSV exports (standard library only; Python 3.9+).

Commands
  normalize EXPORT.csv --platform NAME [--map field=Column ...] [--tz Asia/Karachi] [--date-format FMT] --out clean.csv
  summary   clean.csv [--by platform|format|pillar|weekday] [--min-n 3]
  top       clean.csv [--metric er|views|reach|likes|saves|shares|comments|clicks|ctr] [--n 5] [--bottom] [--platform P]
  trend     clean.csv [--metric views] [--period 4] [--platform P]      last N weeks vs the N weeks before
  times     clean.csv [--metric er] [--min-n 3] [--platform P]          weekday x 3-hour slots, with sample sizes
  abtest    --a-clicks N --a-impressions N --b-clicks N --b-impressions N   two-proportion test for CTR or similar rates
  merge     A.csv B.csv ... --out all.csv                               combine normalized files
  report    clean.csv --out report.md [--min-n 3]

Standard fields: platform, post_id, posted_at, format, pillar, title, impressions, views, reach, likes, comments,
shares, saves, clicks, avg_watch_seconds, followers_gained, ctr_reported. Missing is kept as missing (not zero).
Derived: interactions = likes+comments+shares+saves (only the parts present); er = interactions / (reach, else views,
else impressions); ctr = clicks / impressions (else views), or the platform's own CTR % (ctr_reported, e.g. YouTube's
"Impressions click-through rate (%)") when there is no clicks column.

Dates: slash dates are checked across the whole column. If any first part is over 12 the column is day-first, if any
second part is over 12 it is month-first; if every value fits both (e.g. 03/04/2026), normalize stops and asks for
--date-format instead of guessing. Durations such as 4:07 or 0:04:07 are converted to seconds.

Statistics here are descriptive. With few posts, differences are mostly noise: groups under --min-n are flagged and the
report never states a "winner" from a small sample.
"""
import argparse
import csv
import datetime as dt
import json
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None

NUM = ["impressions", "views", "reach", "likes", "comments", "shares", "saves", "clicks", "avg_watch_seconds", "followers_gained",
       "ctr_reported"]
DURATION = {"avg_watch_seconds"}
FIELDS = ["platform", "post_id", "posted_at", "format", "pillar", "title"] + NUM
ALIASES = {
    "post_id": ["post id", "id", "video id", "media id", "post_id", "permalink", "post link", "url", "link", "content"],
    "posted_at": ["publish time", "published at", "posted_at", "date", "created time", "post time", "publish date",
                  "timestamp", "video publish time", "created_at"],
    "format": ["format", "type", "post type", "media type", "content type"],
    "pillar": ["pillar", "topic", "category"],
    "title": ["title", "caption", "post", "text", "description", "video title", "post message"],
    "impressions": ["impressions", "video impressions"],
    "views": ["views", "video views", "plays", "video_views", "total views"],
    "reach": ["reach", "accounts reached", "unique reach"],
    "likes": ["likes", "reactions", "like count"],
    "comments": ["comments", "comment count"],
    "shares": ["shares", "reposts", "retweets", "share count"],
    "saves": ["saves", "saved", "bookmarks"],
    "clicks": ["clicks", "link clicks", "url clicks", "post clicks"],
    "avg_watch_seconds": ["avg_watch_seconds", "average view duration (seconds)", "average view duration",
                          "average watch time", "avg watch time (s)", "average time watched"],
    "followers_gained": ["follows", "new followers", "subscribers gained", "followers gained", "followers_gained"],
    "ctr_reported": ["impressions click-through rate (%)", "click-through rate (%)", "ctr (%)", "ctr", "ctr_reported"],
    "platform": ["platform", "network"],
}
DATE_FORMATS = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ",
                "%m/%d/%Y %H:%M", "%d/%m/%Y %H:%M", "%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%d", "%b %d, %Y", "%d %b %Y"]


class Fail(RuntimeError):
    pass


def num(s):
    if s is None:
        return None
    s = str(s).strip().replace(",", "").replace("%", "")
    if s in ("", "-", "—", "n/a", "N/A", "NA", "null", "None"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def dur(s):
    """Seconds from '247', '4:07' or '0:04:07'. None when empty or unreadable."""
    s = (str(s) if s is not None else "").strip()
    if ":" not in s:
        return num(s)
    parts = s.split(":")
    try:
        vals = [float(p) for p in parts]
    except ValueError:
        return None
    if len(vals) not in (2, 3):
        return None
    secs = 0.0
    for v in vals:
        secs = secs * 60 + v
    return secs


SLASH = __import__("re").compile(r"^\s*(\d{1,2})/(\d{1,2})/(\d{2,4})\b")


def slash_order(values):
    """'dmy', 'mdy', 'ambiguous' or None (no slash dates). Decided from the whole column, never from one value."""
    firsts, seconds = [], []
    for v in values:
        m = SLASH.match(v or "")
        if m:
            firsts.append(int(m.group(1)))
            seconds.append(int(m.group(2)))
    if not firsts:
        return None
    day_first, month_first = max(firsts) > 12, max(seconds) > 12
    if day_first and month_first:
        raise Fail("The date column mixes day-first and month-first values; pass --date-format.")
    return "dmy" if day_first else "mdy" if month_first else "ambiguous"


def parse_date(s, fmt, tz, order=None):
    s = (s or "").strip()
    if not s:
        return None
    fmts = [fmt] if fmt else DATE_FORMATS
    if not fmt and order == "dmy":
        fmts = [f for f in DATE_FORMATS if not f.startswith("%m/")]
    elif not fmt and order == "mdy":
        fmts = [f for f in DATE_FORMATS if not f.startswith("%d/")]
    for f in fmts:
        try:
            d = dt.datetime.strptime(s, f)
            break
        except ValueError:
            d = None
    if d is None:
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    if tz and ZoneInfo:
        d = d.astimezone(ZoneInfo(tz)) if d.tzinfo else d.replace(tzinfo=ZoneInfo(tz))
    return d


# ---- normalize ---------------------------------------------------------------
def cmd_normalize(a):
    try:
        with open(a.export, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        raise Fail(f"Cannot read {a.export}: {e}") from None
    if not rows:
        raise Fail("The export has no rows.")
    headers = {h.strip().lower(): h for h in rows[0].keys() if h}
    mapping = {}
    for fld, names in ALIASES.items():
        for n in names:
            if n in headers:
                mapping[fld] = headers[n]
                break
    for m in a.map or []:
        k, _, v = m.partition("=")
        if k not in FIELDS or v not in rows[0]:
            raise Fail(f"--map {m!r}: field must be one of {', '.join(FIELDS)} and the column must exist ({', '.join(rows[0].keys())}).")
        mapping[k] = v
    print("Column mapping: " + ", ".join(f"{k}<-{v}" for k, v in mapping.items()))
    missing = [k for k in ("posted_at",) if k not in mapping]
    if missing:
        print(f"[WARN] No column found for: {', '.join(missing)}. Use --map posted_at=\"Your column\".")
    order = None
    if "posted_at" in mapping and not a.date_format:
        order = slash_order([r.get(mapping["posted_at"], "") for r in rows])
        if order == "ambiguous":
            raise Fail("Every date in the column fits both day/month and month/day (for example 03/04/2026), so "
                       "it cannot be read safely. Check one known post, then pass --date-format \"%d/%m/%Y %H:%M\" "
                       "(day first) or \"%m/%d/%Y %H:%M\" (month first).")
        if order:
            print(f"[NOTE] Slash dates read as {'day/month/year' if order == 'dmy' else 'month/day/year'} "
                  "(decided from the whole column). Pass --date-format to override.")
    out, bad_dates, bad_dur = [], 0, 0
    for r in rows:
        o = {k: "" for k in FIELDS}
        o["platform"] = a.platform
        for k, col in mapping.items():
            v = r.get(col, "")
            if k in NUM:
                x = dur(v) if k in DURATION else num(v)
                if x is None and str(v).strip() not in ("", "-", "—"):
                    bad_dur += k in DURATION
                o[k] = "" if x is None else (int(x) if x == int(x) else round(x, 2))
            elif k == "posted_at":
                d = parse_date(v, a.date_format, a.tz, order)
                if d is None and v.strip():
                    bad_dates += 1
                o[k] = d.isoformat() if d else ""
            elif k != "platform":
                o[k] = (v or "").strip()
        out.append(o)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out)
    print(f"Wrote {a.out}: {len(out)} rows" + (f", {bad_dates} unreadable dates (pass --date-format)" if bad_dates else "")
          + (f", {bad_dur} unreadable durations (left blank)" if bad_dur else "") + ".")
    if not a.tz:
        print("[NOTE] No --tz given: dates keep the export's own time zone (often the account's or UTC). Posting-time analysis depends on this.")
    absent = [k for k in NUM if k not in mapping]
    print(f"Fields not present in this export: {', '.join(absent) or 'none'}. Metrics that need them are skipped, never assumed zero.")


# ---- load and derive -----------------------------------------------------------
def load(path, platform=None):
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        raise Fail(f"Cannot read {path}: {e}") from None
    out = []
    for r in rows:
        if platform and r.get("platform") != platform:
            continue
        o = dict(r)
        for k in NUM:
            o[k] = num(r.get(k))
        d = None
        if r.get("posted_at"):
            try:
                d = dt.datetime.fromisoformat(r["posted_at"]).replace(tzinfo=None)  # wall-clock time, comparable across files
            except ValueError:
                d = None
        o["_dt"] = d
        parts = [o[k] for k in ("likes", "comments", "shares", "saves") if o[k] is not None]
        o["interactions"] = sum(parts) if parts else None
        denom = next((o[k] for k in ("reach", "views", "impressions") if o[k]), None)
        o["er"] = o["interactions"] / denom * 100 if o["interactions"] is not None and denom else None
        d2 = next((o[k] for k in ("impressions", "views") if o[k]), None)
        o["ctr"] = o["clicks"] / d2 * 100 if o["clicks"] is not None and d2 else o.get("ctr_reported")
        out.append(o)
    if not out:
        raise Fail("No rows match.")
    return out


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None


def fmt(x, d=1):
    return "-" if x is None else (f"{x:,.{d}f}" if isinstance(x, float) and x != int(x) else f"{int(x):,}")


def group_key(o, by):
    if by == "weekday":
        return o["_dt"].strftime("%a") if o["_dt"] else "unknown"
    return o.get(by) or "unknown"


def cmd_summary(a):
    rows = load(a.clean)
    keys = ["views", "reach", "likes", "comments", "shares", "saves", "er"]
    groups = defaultdict(list)
    for o in rows:
        groups[group_key(o, a.by)].append(o)
    print(f"{len(rows)} posts. Grouped by {a.by}. Medians (less sensitive to one viral post than averages).")
    print(f"{'group':18}{'n':>4}" + "".join(f"{k:>10}" for k in keys))
    for g, rs in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        line = f"{g[:17]:18}{len(rs):>4}" + "".join(f"{fmt(med([o[k] for o in rs])):>10}" for k in keys)
        print(line + ("   <- small sample" if len(rs) < a.min_n else ""))
    print("\ner = interactions / reach (else views, else impressions), in %. Compare ER only within one platform; definitions differ.")
    if any(len(v) < a.min_n for v in groups.values()):
        print(f"Groups under {a.min_n} posts are anecdotes, not evidence.")


def cmd_top(a):
    rows = [o for o in load(a.clean, a.platform) if o.get(a.metric) is not None]
    if not rows:
        raise Fail(f"No posts have '{a.metric}'. Is it present in the export?")
    m = med([o[a.metric] for o in rows])
    rows.sort(key=lambda o: o[a.metric], reverse=not a.bottom)
    print(f"{'Bottom' if a.bottom else 'Top'} {a.n} by {a.metric} (median {fmt(m)}, {len(rows)} posts):")
    for o in rows[:a.n]:
        x = o[a.metric] / m if m else None
        d = o["_dt"].strftime("%Y-%m-%d") if o["_dt"] else "?"
        print(f"  {fmt(o[a.metric]):>10}  {(f'{x:.1f}x median') if x else '':>14}  {d}  {o.get('format', ''):10} {(o.get('title') or o.get('post_id') or '')[:60]}")
    print("Look for what the top posts share (hook, format, topic, timing) and test it; one post is not a pattern.")


def week_index(o, origin):
    return (o["_dt"].date() - origin).days // 7


def cmd_trend(a):
    rows = [o for o in load(a.clean, a.platform) if o["_dt"] and o.get(a.metric) is not None]
    if len(rows) < 4:
        raise Fail("Need at least 4 dated posts with this metric.")
    last = max(o["_dt"] for o in rows).date()
    P = a.period
    cur_start = last - dt.timedelta(days=7 * P - 1)
    prev_start = cur_start - dt.timedelta(days=7 * P)
    cur = [o[a.metric] for o in rows if cur_start <= o["_dt"].date() <= last]
    prev = [o[a.metric] for o in rows if prev_start <= o["_dt"].date() < cur_start]
    print(f"Metric {a.metric}. Last {P} weeks ({cur_start} to {last}) vs previous {P} weeks ({prev_start} to {cur_start - dt.timedelta(days=1)}).")
    print(f"  current : n={len(cur)} median={fmt(med(cur))}  total={fmt(sum(cur)) if cur else '-'}")
    print(f"  previous: n={len(prev)} median={fmt(med(prev))}  total={fmt(sum(prev)) if prev else '-'}")
    if cur and prev and med(prev):
        ch = (med(cur) - med(prev)) / med(prev) * 100
        print(f"  median change: {ch:+.0f}%")
    if min(len(cur), len(prev)) < 5:
        print("  [NOTE] Fewer than 5 posts in a window: treat the change as a hint, not a finding. Posting mix and one viral post can move it.")


def cmd_times(a):
    rows = [o for o in load(a.clean, a.platform) if o["_dt"] and o.get(a.metric) is not None]
    if not rows:
        raise Fail("No dated posts with this metric.")
    b = defaultdict(list)
    for o in rows:
        b[(o["_dt"].strftime("%a"), o["_dt"].hour // 3 * 3)].append(o[a.metric])
    base = med([o[a.metric] for o in rows])
    print(f"Metric {a.metric}; overall median {fmt(base)}; {len(rows)} posts. Slots are weekday + 3-hour block, in the time zone of the clean file.")
    ok = [(k, v) for k, v in b.items() if len(v) >= a.min_n]
    for (day, h), v in sorted(ok, key=lambda kv: -med(kv[1])):
        print(f"  {day} {h:02d}-{h + 3:02d}h  n={len(v):<3} median={fmt(med(v)):>9}  ({med(v) / base:.1f}x overall)" if base else "")
    small = len(b) - len(ok)
    print(f"{small} slot(s) hidden for having under {a.min_n} posts.")
    print("[CAUTION] Time effects are confounded with topic, format and promotion. Use this to choose 2 or 3 slots to test, not as proof.")


def cmd_abtest(a):
    ca, ia, cb, ib = a.a_clicks, a.a_impressions, a.b_clicks, a.b_impressions
    if min(ia, ib) <= 0 or ca > ia or cb > ib or min(ca, cb) < 0:
        raise Fail("Counts must be positive and clicks cannot exceed impressions.")
    pa, pb = ca / ia, cb / ib
    p = (ca + cb) / (ia + ib)
    se = math.sqrt(p * (1 - p) * (1 / ia + 1 / ib))
    z = (pb - pa) / se if se else 0.0
    pv = math.erfc(abs(z) / math.sqrt(2))
    se_d = math.sqrt(pa * (1 - pa) / ia + pb * (1 - pb) / ib)
    lo, hi = pb - pa - 1.96 * se_d, pb - pa + 1.96 * se_d
    print(f"A: {ca}/{ia} = {pa * 100:.2f}%   B: {cb}/{ib} = {pb * 100:.2f}%")
    print(f"Difference B-A: {(pb - pa) * 100:+.2f} points (95% CI {lo * 100:+.2f} to {hi * 100:+.2f}); z={z:.2f}, two-sided p={pv:.3f}")
    if min(ca, cb, ia - ca, ib - cb) < 10:
        print("[WARN] Fewer than 10 events in some cell: the normal approximation is unreliable. Collect more data.")
    if pv < 0.05:
        print("The difference is unlikely to be chance under this simple model, but check the groups were comparable (same time, audience, no other change).")
    else:
        print("No reliable difference detected. That is not proof they are equal; more impressions may be needed.")
    print("Do not stop a test the moment p dips below 0.05 (repeated peeking inflates false positives); decide the sample size in advance.")


def cmd_merge(a):
    rows = []
    for f in a.files:
        try:
            with open(f, newline="", encoding="utf-8-sig") as fh:
                rows += list(csv.DictReader(fh))
        except OSError as e:
            raise Fail(f"Cannot read {f}: {e}") from None
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows({k: r.get(k, "") for k in FIELDS} for r in rows)
    print(f"Wrote {a.out}: {len(rows)} rows from {len(a.files)} file(s).")


def cmd_report(a):
    rows = load(a.clean)
    dated = [o for o in rows if o["_dt"]]
    L = [f"# Social media performance report", ""]
    if dated:
        L.append(f"Window: {min(o['_dt'] for o in dated).date()} to {max(o['_dt'] for o in dated).date()} ({len(rows)} posts).")
    else:
        L.append(f"{len(rows)} posts (no usable dates).")
    L += ["", "## Headline numbers (medians per post)", "",
          "| Platform | Posts | Views | Reach | ER % | Saves | Shares | Clicks | CTR % | Avg watch (s) |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    by_p = defaultdict(list)
    for o in rows:
        by_p[o.get("platform") or "unknown"].append(o)
    for p, rs in by_p.items():
        L.append(f"| {p} | {len(rs)} | " + " | ".join(fmt(med([o[k] for o in rs])) for k in
                                                     ("views", "reach", "er", "saves", "shares", "clicks", "ctr",
                                                      "avg_watch_seconds")) + " |")
    for by in ("format", "pillar"):
        gs = defaultdict(list)
        for o in rows:
            gs[group_key(o, by)].append(o)
        if len(gs) > 1 or "unknown" not in gs:
            L += ["", f"## By {by}", "", f"| {by} | Posts | Views | ER % | Saves | Note |", "|---|---|---|---|---|---|"]
            for g, rs in sorted(gs.items(), key=lambda kv: -len(kv[1])):
                note = "small sample" if len(rs) < a.min_n else ""
                L.append(f"| {g} | {len(rs)} | {fmt(med([o['views'] for o in rs]))} | {fmt(med([o['er'] for o in rs]))} | {fmt(med([o['saves'] for o in rs]))} | {note} |")
    ranked = sorted([o for o in rows if o["er"] is not None], key=lambda o: o["er"], reverse=True)
    if ranked:
        L += ["", "## Top and bottom posts by engagement rate", ""]
        for label, sel in (("Top", ranked[:3]), ("Bottom", ranked[-3:])):
            L.append(f"**{label}**")
            for o in sel:
                L.append(f"- {o['er']:.1f}% ER, {fmt(o['views'])} views: {(o.get('title') or o.get('post_id') or '')[:70]} ({o.get('platform')}, {o.get('format')})")
            L.append("")
    L += ["## Caveats", "",
          "- Engagement rate is computed from the fields present in each export; definitions differ by platform, so compare within a platform.",
          f"- Groups under {a.min_n} posts are flagged. Differences between small groups are not evidence.",
          "- Missing metrics are blank, not zero. Platform data can lag and may be revised.",
          "- Correlation only: topic, format, timing and promotion are mixed together.", "",
          "## What to decide next", "",
          "Pick one thing to repeat, one to stop, and one test (change a single variable, set the sample size first). Fill these in from the numbers above; do not invent reasons the data does not show.", ""]
    Path(a.out).write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote {a.out}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("normalize")
    n.add_argument("export")
    n.add_argument("--platform", required=True)
    n.add_argument("--map", action="append")
    n.add_argument("--tz")
    n.add_argument("--date-format")
    n.add_argument("--out", required=True)
    n.set_defaults(fn=cmd_normalize)
    s = sub.add_parser("summary")
    s.add_argument("clean")
    s.add_argument("--by", choices=["platform", "format", "pillar", "weekday"], default="format")
    s.add_argument("--min-n", type=int, default=3)
    s.set_defaults(fn=cmd_summary)
    t = sub.add_parser("top")
    t.add_argument("clean")
    t.add_argument("--metric", default="er")
    t.add_argument("--n", type=int, default=5)
    t.add_argument("--bottom", action="store_true")
    t.add_argument("--platform")
    t.set_defaults(fn=cmd_top)
    tr = sub.add_parser("trend")
    tr.add_argument("clean")
    tr.add_argument("--metric", default="views")
    tr.add_argument("--period", type=int, default=4)
    tr.add_argument("--platform")
    tr.set_defaults(fn=cmd_trend)
    ti = sub.add_parser("times")
    ti.add_argument("clean")
    ti.add_argument("--metric", default="er")
    ti.add_argument("--min-n", type=int, default=3)
    ti.add_argument("--platform")
    ti.set_defaults(fn=cmd_times)
    ab = sub.add_parser("abtest")
    for k in ("a-clicks", "a-impressions", "b-clicks", "b-impressions"):
        ab.add_argument(f"--{k}", type=int, required=True)
    ab.set_defaults(fn=cmd_abtest)
    mg = sub.add_parser("merge")
    mg.add_argument("files", nargs="+")
    mg.add_argument("--out", required=True)
    mg.set_defaults(fn=cmd_merge)
    r = sub.add_parser("report")
    r.add_argument("clean")
    r.add_argument("--out", required=True)
    r.add_argument("--min-n", type=int, default=3)
    r.set_defaults(fn=cmd_report)
    a = p.parse_args(argv)
    try:
        return a.fn(a) or 0
    except Fail as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
