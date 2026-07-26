#!/usr/bin/env python3
"""Generate an Apple-Fitness-style Activity Rings dashboard (Move/Exercise/
Stand) from the daily health-metrics data. Self-contained HTML, inline SVG,
no network dependency. Trend charts are rendered client-side (interactive,
hoverable) by lib/ichart.py's small JS runtime.
"""
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.query import query
from lib import svg, ichart

REPORTS_DIR = Path(__file__).parent / "reports"

MOVE_GOAL_KCAL = 1000
EXERCISE_GOAL_MIN = 75
STAND_GOAL_HR = 12
KJ_PER_KCAL = 4.184

HTML_HEAD = """<!doctype html>
<html><head><meta charset="utf-8"><title>Activity Rings</title>
<style>
  :root { color-scheme: dark; }
  body { background:#000; color:#fff; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
          margin:0; padding:32px; display:flex; flex-direction:column; align-items:center; }
  .wrap { width:100%; max-width:640px; }
  h1 { font-size:22px; margin:0 0 4px; text-align:center; }
  .sub { color:#8e8e93; font-size:14px; margin-bottom:28px; text-align:center; }
  .hero { display:flex; align-items:center; justify-content:center; gap:36px; flex-wrap:wrap; margin-bottom:32px; }
  .hero svg { width:180px; height:180px; flex:none; }
  .legend { display:flex; flex-direction:column; gap:14px; }
  .legend .row { display:flex; align-items:baseline; gap:8px; }
  .legend .dot { width:11px; height:11px; border-radius:50%; display:inline-block; margin-right:2px; }
  .legend .label { font-size:13px; color:#8e8e93; text-transform:uppercase; letter-spacing:.03em; width:64px; }
  .legend .val { font-size:20px; font-weight:700; }
  .legend .goal { font-size:13px; color:#8e8e93; }
  .week { display:flex; justify-content:space-between; margin-bottom:28px; }
  .week .day { display:flex; flex-direction:column; align-items:center; gap:6px; }
  .week .day svg { width:52px; height:52px; }
  .week .day .l { font-size:11px; color:#8e8e93; }
  .cards { display:flex; flex-direction:column; gap:16px; }
  .card { background:#1c1c1e; border-radius:14px; padding:16px; }
  .card h2 { font-size:13px; text-transform:uppercase; letter-spacing:.05em; color:#8e8e93; margin:0 0 10px; }
  .insights { margin:0; padding-left:18px; line-height:1.7; font-size:13.5px; }
  .tiles { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; text-align:center; }
  .tiles .v { font-size:20px; font-weight:700; }
  .tiles .l { font-size:11px; color:#8e8e93; }
__ICHART_STYLE__
</style></head><body>
<script>__ICHART_SCRIPT__</script>
<div class="wrap">
<h1>Activity</h1>
<div class="sub">__SUB__</div>
""".replace("__ICHART_STYLE__", ichart.ICHART_STYLE).replace("__ICHART_SCRIPT__", ichart.ICHART_SCRIPT)


def daily_activity(start, end):
    move = {r["d"]: r["v"] / KJ_PER_KCAL for r in query(
        f"SELECT date::VARCHAR AS d, SUM(qty) AS v FROM samples_qty WHERE metric='active_energy' "
        f"AND date BETWEEN DATE '{start}' AND DATE '{end}' GROUP BY date")}
    exercise = {r["d"]: r["v"] for r in query(
        f"SELECT date::VARCHAR AS d, SUM(qty) AS v FROM samples_qty WHERE metric='apple_exercise_time' "
        f"AND date BETWEEN DATE '{start}' AND DATE '{end}' GROUP BY date")}
    stand = {r["d"]: r["v"] for r in query(
        f"SELECT date::VARCHAR AS d, SUM(qty) AS v FROM samples_qty WHERE metric='apple_stand_hour' "
        f"AND date BETWEEN DATE '{start}' AND DATE '{end}' GROUP BY date")}
    return move, exercise, stand


def fracs_for(day, move, exercise, stand):
    return (
        move.get(day, 0) / MOVE_GOAL_KCAL,
        exercise.get(day, 0) / EXERCISE_GOAL_MIN,
        stand.get(day, 0) / STAND_GOAL_HR,
    )


def date_list(start, end):
    days, d = [], start
    while d <= end:
        days.append(d.isoformat())
        d += timedelta(days=1)
    return days


def render(out_dir=None):
    out = Path(out_dir) if out_dir else REPORTS_DIR
    latest_rows = query("SELECT max(date)::VARCHAR AS d FROM samples_qty "
                        "WHERE metric IN ('active_energy','apple_exercise_time','apple_stand_hour')")
    if not latest_rows or not latest_rows[0]["d"]:
        print("No activity data ingested yet.")
        return
    latest = date.fromisoformat(latest_rows[0]["d"])
    start = latest - timedelta(days=27)
    move, exercise, stand = daily_activity(start, latest)
    all_days = date_list(start, latest)

    mv, ex, sd = fracs_for(latest.isoformat(), move, exercise, stand)

    html = [HTML_HEAD.replace("__SUB__", latest.strftime("%A, %B %-d"))]

    # Hero rings + legend
    html.append('<div class="hero">')
    html.append(svg.activity_rings(mv, ex, sd, size=180, stroke=16))
    html.append('<div class="legend">')
    move_c = svg.RING_COLORS["move"][0]
    ex_c = svg.RING_COLORS["exercise"][0]
    stand_c = svg.RING_COLORS["stand"][0]
    html.append(f'<div class="row"><span class="dot" style="background:{move_c}"></span>'
                f'<div><div class="val">{move.get(latest.isoformat(), 0):.0f}<span class="goal">/{MOVE_GOAL_KCAL} CAL</span></div>'
                f'<div class="label">Move</div></div></div>')
    html.append(f'<div class="row"><span class="dot" style="background:{ex_c}"></span>'
                f'<div><div class="val">{exercise.get(latest.isoformat(), 0):.0f}<span class="goal">/{EXERCISE_GOAL_MIN} MIN</span></div>'
                f'<div class="label">Exercise</div></div></div>')
    html.append(f'<div class="row"><span class="dot" style="background:{stand_c}"></span>'
                f'<div><div class="val">{stand.get(latest.isoformat(), 0):.0f}<span class="goal">/{STAND_GOAL_HR} HRS</span></div>'
                f'<div class="label">Stand</div></div></div>')
    html.append('</div></div>')

    # Last 7 days mini rings
    week_days = all_days[-7:]
    html.append('<div class="week">')
    for d in week_days:
        wm, we, ws = fracs_for(d, move, exercise, stand)
        wd_label = date.fromisoformat(d).strftime("%a")[0]
        html.append(f'<div class="day">{svg.mini_rings(wm, we, ws, size=52, stroke=6, gap=2)}<div class="l">{wd_label}</div></div>')
    html.append('</div>')

    # Streak + insights
    closed_days = 0
    d = latest
    while True:
        m, e, s = fracs_for(d.isoformat(), move, exercise, stand)
        if m >= 1 and e >= 1 and s >= 1:
            closed_days += 1
            d -= timedelta(days=1)
        else:
            break
    week_closed = sum(1 for d in week_days if all(f >= 1 for f in fracs_for(d, move, exercise, stand)))

    html.append('<div class="cards">')
    html.append('<div class="card"><h2>Streaks</h2><div class="tiles">')
    html.append(f'<div><div class="v">{closed_days}</div><div class="l">Day Streak (all rings)</div></div>')
    html.append(f'<div><div class="v">{week_closed}/7</div><div class="l">Closed This Week</div></div>')
    total_days = len(all_days)
    total_closed = sum(1 for d in all_days if all(f >= 1 for f in fracs_for(d, move, exercise, stand)))
    html.append(f'<div><div class="v">{total_closed}/{total_days}</div><div class="l">Closed (28d)</div></div>')
    html.append('</div></div>')

    # Trends (interactive)
    day_labels = [d[5:] for d in all_days]
    html.append('<div class="card"><h2>Move (28 days)</h2>')
    html.append(ichart.chart("chart-move", day_labels,
                             [{"name": "Move", "color": move_c, "values": [move.get(d) for d in all_days]}],
                             goal=MOVE_GOAL_KCAL, legend=False))
    html.append('</div>')
    html.append('<div class="card"><h2>Exercise (28 days)</h2>')
    html.append(ichart.chart("chart-exercise", day_labels,
                             [{"name": "Exercise", "color": ex_c, "values": [exercise.get(d) for d in all_days]}],
                             goal=EXERCISE_GOAL_MIN, legend=False))
    html.append('</div>')
    html.append('<div class="card"><h2>Stand (28 days)</h2>')
    html.append(ichart.chart("chart-stand", day_labels,
                             [{"name": "Stand", "color": stand_c, "values": [stand.get(d) for d in all_days]}],
                             goal=STAND_GOAL_HR, legend=False))
    html.append('</div>')

    html.append('</div></div>')
    html.append('</body></html>')

    out.mkdir(parents=True, exist_ok=True)
    out_path = out / "rings.html"
    out_path.write_text("".join(html))
    return out_path


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", "-o", help="Directory to write rings.html into (default: reports/)")
    args = ap.parse_args()
    path = render(args.out_dir)
    if path:
        print(f"wrote {path}")
