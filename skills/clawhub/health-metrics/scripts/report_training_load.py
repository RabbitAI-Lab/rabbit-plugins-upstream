#!/usr/bin/env python3
"""Generate a Training Load dashboard approximating Apple Fitness's "Training
Load" feature. Apple's exact per-workout effort score isn't exposed by Auto
Export, so this uses the standard sports-science TRIMP (Training Impulse)
formula from each workout's HR series against your resting/max HR, then
compares a 7-day rolling load to a 28-day rolling load (Acute:Chronic
Workload Ratio) -- the same two windows Apple's own feature is built around.
"""
import math
import sys
from datetime import date, timedelta
from pathlib import Path
from statistics import mean

sys.path.insert(0, str(Path(__file__).parent))
from lib.query import query
from lib import svg, ichart

REPORTS_DIR = Path(__file__).parent / "reports"

MAX_HR = 185
DEFAULT_RESTING_HR = 55
FALLBACK_DELTA_MIN = 1.0  # assumed spacing when HR samples aren't ~1/min apart
MAX_GAP_MIN = 5.0  # cap any single HR-sample gap so a dropped sensor reading doesn't inflate load

ZONES = [
    (0.0, 0.8, "Low", "#5ec8f8"),
    (0.8, 1.3, "Optimal", "#92e82a"),
    (1.3, 1.5, "High", "#f8b95e"),
    (1.5, 2.0, "Very High", "#fa114f"),
]

WEEKLY_COLOR = "#5ec8f8"
MONTHLY_COLOR = "#92e82a"

HTML_HEAD = """<!doctype html>
<html><head><meta charset="utf-8"><title>Training Load</title>
<style>
  :root { color-scheme: dark; }
  body { background:#000; color:#fff; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
          margin:0; padding:32px; display:flex; flex-direction:column; align-items:center; }
  .wrap { width:100%; max-width:640px; }
  h1 { font-size:22px; margin:0 0 4px; text-align:center; }
  .sub { color:#8e8e93; font-size:14px; margin-bottom:24px; text-align:center; }
  .cards { display:flex; flex-direction:column; gap:16px; }
  .card { background:#1c1c1e; border-radius:14px; padding:16px; }
  .card h2 { font-size:13px; text-transform:uppercase; letter-spacing:.05em; color:#8e8e93; margin:0 0 10px; }
  .headline { font-size:16px; text-align:center; margin-bottom:6px; }
  .headline b { font-size:20px; }
  .note { color:#8e8e93; font-size:12px; margin-top:8px; }
  table { width:100%; border-collapse:collapse; font-size:13px; }
  th, td { text-align:left; padding:6px 8px; border-bottom:1px solid #2c2c2e; }
  th { color:#8e8e93; font-weight:500; text-transform:uppercase; font-size:11px; }
  .tiles { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; text-align:center; }
  .tiles .v { font-size:20px; font-weight:700; }
  .tiles .l { font-size:11px; color:#8e8e93; }
__ICHART_STYLE__
</style></head><body>
<script>__ICHART_SCRIPT__</script>
<div class="wrap">
<h1>Training Load</h1>
<div class="sub">Estimated from heart-rate strain (TRIMP) -- not Apple's own score</div>
<div class="cards">
""".replace("__ICHART_STYLE__", ichart.ICHART_STYLE).replace("__ICHART_SCRIPT__", ichart.ICHART_SCRIPT)


def resting_hr_by_date():
    rows = query("SELECT date::VARCHAR AS d, qty FROM samples_qty WHERE metric='resting_heart_rate'")
    by_date = {r["d"]: r["qty"] for r in rows}
    fallback = mean(by_date.values()) if by_date else DEFAULT_RESTING_HR
    return by_date, fallback


def workouts_with_hr():
    workouts = query("SELECT id, date::VARCHAR AS date, name, duration_s, avg_hr FROM workouts ORDER BY date")
    hr_rows = query("SELECT workout_id, epoch(ts) AS t, avg FROM workout_hr ORDER BY workout_id, t")
    by_workout = {}
    for r in hr_rows:
        by_workout.setdefault(r["workout_id"], []).append((r["t"], r["avg"]))
    return workouts, by_workout


def trimp(hr_r):
    """Banister TRIMP exponential weighting for one HR-reserve fraction (0..1)."""
    return 0.64 * math.exp(1.92 * hr_r)


def workout_load(w, hr_series, resting):
    hrr_range = MAX_HR - resting
    if hrr_range <= 0:
        return 0.0
    if len(hr_series) >= 2:
        total = 0.0
        for (t0, hr0), (t1, hr1) in zip(hr_series, hr_series[1:]):
            delta_min = min(max((t1 - t0) / 60.0, 0.0), MAX_GAP_MIN) or FALLBACK_DELTA_MIN
            hr_mid = (hr0 + hr1) / 2
            r = max(0.0, min(1.0, (hr_mid - resting) / hrr_range))
            total += delta_min * r * trimp(r)
        return total
    if w["avg_hr"] and w["duration_s"]:
        r = max(0.0, min(1.0, (w["avg_hr"] - resting) / hrr_range))
        return (w["duration_s"] / 60.0) * r * trimp(r)
    return 0.0


def date_list(start, end):
    days, d = [], start
    while d <= end:
        days.append(d.isoformat())
        d += timedelta(days=1)
    return days


def zone_for(value):
    for lo, hi, label, color in ZONES:
        if lo <= value < hi or (hi == ZONES[-1][1] and value >= lo):
            return label, color
    return ZONES[-1][2], ZONES[-1][3]


def ewma_series(daily_series, tau):
    """Exponentially-weighted moving average with time constant `tau` (days).
    Unlike a rolling sum, an EWMA changes smoothly every day instead of
    jumping whenever a big workout enters/exits a fixed window -- and using
    the same alpha-blend recurrence as Coggan's CTL (Chronic Training Load)
    makes it a natural "lagging" trend line."""
    alpha = 2 / (tau + 1)
    out, prev = [], None
    for v in daily_series:
        prev = v if prev is None else alpha * v + (1 - alpha) * prev
        out.append(prev)
    return out


def trend_chart_html(chart_id, title, all_days, weekly_load, monthly_load, window_days):
    days = all_days[-window_days:]
    weekly = weekly_load[-window_days:]
    monthly = monthly_load[-window_days:]
    if window_days <= 31:
        labels = [d[5:] for d in days]  # MM-DD
    else:
        labels = [d[5:7] + "/" + d[8:10] for d in days]
    html = [f'<div class="card"><h2>{title}</h2>']
    html.append(ichart.chart(chart_id, labels, [
        {"name": "Weekly load", "color": WEEKLY_COLOR, "values": weekly},
        {"name": "Monthly trend (smoothed)", "color": MONTHLY_COLOR, "values": monthly, "dashed": True},
    ], height=170))
    html.append('</div>')
    return "".join(html)


def render(out_dir=None):
    out = Path(out_dir) if out_dir else REPORTS_DIR
    resting_by_date, resting_fallback = resting_hr_by_date()
    workouts, hr_by_workout = workouts_with_hr()
    if not workouts:
        print("No workouts ingested yet.")
        return

    loads = []
    for w in workouts:
        resting = resting_by_date.get(w["date"], resting_fallback)
        load = workout_load(w, hr_by_workout.get(w["id"], []), resting)
        loads.append((w, load))

    daily_load = {}
    for w, load in loads:
        daily_load[w["date"]] = daily_load.get(w["date"], 0.0) + load

    start = date.fromisoformat(workouts[0]["date"])
    end = date.fromisoformat(workouts[-1]["date"])
    all_days = date_list(start, end)
    series = [daily_load.get(d, 0.0) for d in all_days]

    def rolling_sum(i, window):
        lo = max(0, i - window + 1)
        return sum(series[lo:i + 1])

    # Weekly load: a plain 7-day rolling sum -- responsive, moves with recent activity.
    acute = [rolling_sum(i, 7) for i in range(len(series))]
    # Monthly trend: an EWMA of daily load (tau=28d) scaled to weekly-equivalent units
    # so it's directly comparable to the weekly line, and smoothed/lagging rather than
    # jumping whenever a single hard day enters or exits a fixed 28-day window.
    chronic_weekly = [v * 7 for v in ewma_series(series, tau=28)]
    acwr = [a / c if c > 0 else None for a, c in zip(acute, chronic_weekly)]

    cur_acwr = acwr[-1]
    cur_acute = acute[-1]
    cur_chronic = chronic_weekly[-1]

    html = [HTML_HEAD]

    html.append('<div class="card">')
    if cur_acwr is not None:
        label, color = zone_for(cur_acwr)
        html.append(f'<div class="headline">Your training load is <b style="color:{color}">{label}</b> '
                    f'compared to your last 28 days</div>')
        gauge_vmax = max(2.0, cur_acwr + 0.3)
        gauge_zones = ZONES[:-1] + [(ZONES[-1][0], gauge_vmax, ZONES[-1][2], ZONES[-1][3])]
        html.append(svg.zone_gauge(cur_acwr, gauge_zones, vmax=gauge_vmax))
    else:
        html.append('<div class="headline">Not enough history yet to compare 7-day vs. 28-day load</div>')
    ratio_str = f"{cur_acwr:.2f}" if cur_acwr is not None else "–"
    html.append(f'<div class="tiles">'
                f'<div><div class="v">{cur_acute:.0f}</div><div class="l">7-Day Load</div></div>'
                f'<div><div class="v">{cur_chronic:.0f}</div><div class="l">28-Day Avg (weekly)</div></div>'
                f'<div><div class="v">{ratio_str}</div><div class="l">Ratio</div></div>'
                f'</div>')
    html.append('<div class="note">Load = TRIMP, integrated minute-by-minute over each workout\'s heart-rate '
                f'series against resting HR (~{resting_fallback:.0f} bpm avg) and max HR ({MAX_HR} bpm) -- '
                'longer or harder sessions score higher, not just faster ones.</div>')
    html.append('</div>')

    html.append(trend_chart_html("chart-load-30", "Weekly vs. Monthly Load -- Last Month", all_days, acute, chronic_weekly, 30))
    html.append(trend_chart_html("chart-load-90", "Weekly vs. Monthly Load -- Last 3 Months", all_days, acute, chronic_weekly, 90))
    html.append(trend_chart_html("chart-load-180", "Weekly vs. Monthly Load -- Last 6 Months", all_days, acute, chronic_weekly, 180))

    html.append('<div class="card"><h2>Recent Workouts</h2><table>'
                '<tr><th>Date</th><th>Workout</th><th>Duration</th><th>Avg HR</th><th>Load</th></tr>')
    for w, load in list(reversed(loads))[:20]:
        dur_min = (w["duration_s"] or 0) / 60
        avg_hr_str = f'{w["avg_hr"]:.0f}' if w["avg_hr"] else "–"
        html.append(f'<tr><td>{w["date"]}</td><td>{w["name"]}</td><td>{dur_min:.0f} min</td>'
                    f'<td>{avg_hr_str}</td><td>{load:.0f}</td></tr>')
    html.append('</table></div>')

    html.append('</div></div>')
    html.append('</body></html>')

    out.mkdir(parents=True, exist_ok=True)
    out_path = out / "training-load.html"
    out_path.write_text("".join(html))
    return out_path


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", "-o", help="Directory to write training-load.html into (default: reports/)")
    args = ap.parse_args()
    path = render(args.out_dir)
    if path:
        print(f"wrote {path}")
