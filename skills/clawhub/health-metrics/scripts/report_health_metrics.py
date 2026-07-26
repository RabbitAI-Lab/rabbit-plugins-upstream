#!/usr/bin/env python3
"""Generate daily / weekly / rolling-4-week HTML health dashboards from the
DuckDB store built by ingest_health_metrics.py. Self-contained output: inline CSS + inline
SVG charts, no network dependencies, no extra Python packages.
"""
import argparse
import sys
from datetime import date, timedelta
from pathlib import Path
from statistics import mean, pstdev

sys.path.insert(0, str(Path(__file__).parent))
from lib.query import query
from lib.metrics import QTY_METRICS, HR_METRICS, ALL_QTY, CUMULATIVE_METRICS
from lib import svg

REPORTS_DIR = Path(__file__).parent / "reports"

UNIT_LABEL = {
    "count": "", "min": " min", "km": " km", "kJ": " kJ", "%": "%",
    "count/min": " bpm", "ms": " ms", "degC": "°C", "m/s": " m/s",
    "km/hr": " km/h", "cm": " cm", "dBASPL": " dB", "ml/(kg·min)": " ml/kg/min",
    "kcal/hr·kg": "",
}

DISPLAY_NAME = {
    "step_count": "Steps", "walking_running_distance": "Walk+Run Distance",
    "cycling_distance": "Cycling Distance", "flights_climbed": "Flights Climbed",
    "active_energy": "Active Energy", "basal_energy_burned": "Resting Energy",
    "apple_exercise_time": "Exercise Time", "apple_stand_time": "Stand Time",
    "apple_stand_hour": "Stand Hours", "resting_heart_rate": "Resting HR",
    "walking_heart_rate_average": "Walking HR", "heart_rate_variability": "HRV",
    "respiratory_rate": "Respiratory Rate", "blood_oxygen_saturation": "Blood Oxygen",
    "apple_sleeping_wrist_temperature": "Wrist Temp", "vo2_max": "VO2 Max",
    "cardio_recovery": "Cardio Recovery", "heart_rate": "Heart Rate",
    "walking_speed": "Walking Speed", "walking_step_length": "Step Length",
    "walking_asymmetry_percentage": "Walking Asymmetry",
    "walking_double_support_percentage": "Double Support",
    "stair_speed_up": "Stair Speed Up", "stair_speed_down": "Stair Speed Down",
    "six_minute_walking_test_distance": "6-Min Walk Test",
    "environmental_audio_exposure": "Ambient Audio", "headphone_audio_exposure": "Headphone Audio",
    "time_in_daylight": "Time in Daylight", "physical_effort": "Physical Effort",
    "running_power": "Running Power", "running_speed": "Running Speed",
    "running_stride_length": "Stride Length", "running_vertical_oscillation": "Vertical Oscillation",
    "running_ground_contact_time": "Ground Contact Time",
}


def date_list(start, end):
    days, d = [], start
    while d <= end:
        days.append(d.isoformat())
        d += timedelta(days=1)
    return days


def daily_range(d):
    return dict(start=d, end=d, prev_start=d - timedelta(days=1), prev_end=d - timedelta(days=1),
                label=d.isoformat(), slug=f"daily-{d.isoformat()}")


def weekly_range(d):
    iso_year, iso_week, iso_wd = d.isocalendar()
    monday = d - timedelta(days=iso_wd - 1)
    sunday = monday + timedelta(days=6)
    end = min(sunday, d)
    return dict(start=monday, end=end, prev_start=monday - timedelta(days=7),
                prev_end=sunday - timedelta(days=7),
                label=f"{iso_year}-W{iso_week:02d}", slug=f"weekly-{iso_year}-W{iso_week:02d}")


def monthly_range(d):
    start = d - timedelta(days=27)
    prev_end = start - timedelta(days=1)
    prev_start = prev_end - timedelta(days=27)
    return dict(start=start, end=d, prev_start=prev_start, prev_end=prev_end,
                label=f"{start.isoformat()} to {d.isoformat()} (trailing 28d)",
                slug=f"monthly-{d.isoformat()}")


def qty_series(metric, start, end):
    cumulative = metric in CUMULATIVE_METRICS
    agg = "SUM(qty)" if cumulative else "AVG(qty)"
    rows = query(f"SELECT date::VARCHAR AS d, {agg} AS v FROM samples_qty "
                 f"WHERE metric='{metric}' AND date BETWEEN DATE '{start}' AND DATE '{end}' "
                 f"GROUP BY date ORDER BY date")
    return {r["d"]: r["v"] for r in rows}


def hr_series(metric, start, end):
    rows = query(f"SELECT date::VARCHAR AS d, AVG(avg) AS avg, MIN(min) AS lo, MAX(max) AS hi "
                 f"FROM samples_hr WHERE metric='{metric}' AND date BETWEEN DATE '{start}' AND DATE '{end}' "
                 f"GROUP BY date ORDER BY date")
    return {r["d"]: r for r in rows}


def sleep_series(start, end):
    rows = query(f"SELECT date::VARCHAR AS d, total_sleep, core, deep, rem, awake, "
                 f"sleep_start::VARCHAR AS sleep_start FROM sleep_sessions "
                 f"WHERE date BETWEEN DATE '{start}' AND DATE '{end}' ORDER BY date")
    return {r["d"]: r for r in rows}


def period_value(metric, series):
    vals = [v for v in series.values() if v is not None]
    if not vals:
        return None
    return sum(vals) if metric in CUMULATIVE_METRICS else mean(vals)


def pct_change(cur, prev):
    if cur is None or prev is None or prev == 0:
        return None
    return (cur - prev) / prev * 100


def baseline(metric, kind, end_date, window=28):
    start = end_date - timedelta(days=window - 1)
    if kind == "hr":
        rows = query(f"SELECT avg AS v FROM samples_hr WHERE metric='{metric}' "
                     f"AND date BETWEEN DATE '{start}' AND DATE '{end_date}'")
    else:
        rows = query(f"SELECT qty AS v FROM samples_qty WHERE metric='{metric}' "
                     f"AND date BETWEEN DATE '{start}' AND DATE '{end_date}'")
    vals = [r["v"] for r in rows if r["v"] is not None]
    if len(vals) < 3:
        return None, None
    return mean(vals), pstdev(vals)


def fmt(v, unit="", digits=1):
    if v is None:
        return "–"
    return f"{v:,.{digits}f}{unit}"


def trend_arrow(pct):
    if pct is None:
        return ""
    arrow = "▲" if pct > 0 else ("▼" if pct < 0 else "▶")
    cls = "up" if pct > 0 else ("down" if pct < 0 else "flat")
    return f'<span class="trend {cls}">{arrow} {abs(pct):.0f}%</span>'


def days_covered(start, end):
    rows = query("SELECT DISTINCT date::VARCHAR AS d FROM ("
                 f"SELECT date FROM samples_qty WHERE date BETWEEN DATE '{start}' AND DATE '{end}' "
                 f"UNION SELECT date FROM samples_hr WHERE date BETWEEN DATE '{start}' AND DATE '{end}' "
                 f"UNION SELECT date FROM sleep_sessions WHERE date BETWEEN DATE '{start}' AND DATE '{end}'"
                 ") ORDER BY d")
    return [r["d"] for r in rows]


def build_metric_stat(metric, kind, start, end, prev_start, prev_end, end_date_for_baseline):
    series = hr_series(metric, start, end) if kind == "hr" else qty_series(metric, start, end)
    prev_series = hr_series(metric, prev_start, prev_end) if kind == "hr" else qty_series(metric, prev_start, prev_end)
    if kind == "hr":
        flat = {d: r["avg"] for d, r in series.items()}
        cur = period_value(metric, flat)
        prev = period_value(metric, {d: r["avg"] for d, r in prev_series.items()})
    else:
        cur = period_value(metric, series)
        prev = period_value(metric, prev_series)
    base_mean, base_std = baseline(metric, kind, end_date_for_baseline)
    return dict(metric=metric, series=series, cur=cur, prev=prev,
                pct=pct_change(cur, prev), base_mean=base_mean, base_std=base_std)


HTML_HEAD = """<!doctype html>
<html><head><meta charset="utf-8"><title>Health — {title}</title>
<style>
  :root {{ color-scheme: dark; }}
  body {{ background:#10121a; color:#e6e9f0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
          margin:0; padding:24px; }}
  h1 {{ font-size:20px; margin:0 0 4px; }}
  .sub {{ color:#8890a0; font-size:13px; margin-bottom:20px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:16px; }}
  .card {{ background:#181b24; border:1px solid #2a2f3a; border-radius:10px; padding:16px; }}
  .card h2 {{ font-size:14px; text-transform:uppercase; letter-spacing:.05em; color:#8890a0; margin:0 0 12px; }}
  .headline {{ display:flex; flex-wrap:wrap; gap:20px; margin-bottom:20px; }}
  .stat {{ min-width:110px; }}
  .stat .v {{ font-size:22px; font-weight:600; }}
  .stat .l {{ font-size:11px; color:#8890a0; text-transform:uppercase; }}
  .trend.up {{ color:#f87171; }} .trend.down {{ color:#5ec8f8; }} .trend.flat {{ color:#8890a0; }}
  .tiles {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(150px,1fr)); gap:10px; }}
  .tile {{ background:#10121a; border-radius:8px; padding:8px; }}
  .tile .l {{ font-size:11px; color:#8890a0; }}
  .tile .v {{ font-size:14px; font-weight:600; margin-bottom:4px; }}
  ul.insights {{ margin:0; padding-left:18px; line-height:1.7; font-size:13.5px; }}
  .note {{ color:#8890a0; font-size:12px; margin-top:8px; }}
</style></head><body>
<h1>Health Dashboard — {title}</h1>
<div class="sub">{sub}</div>
"""


def render(period, ref_date, out_dir=None):
    out = Path(out_dir) if out_dir else REPORTS_DIR
    r = {"daily": daily_range, "weekly": weekly_range, "monthly": monthly_range}[period](ref_date)
    start, end, prev_start, prev_end = r["start"], r["end"], r["prev_start"], r["prev_end"]
    covered = days_covered(start, end)
    all_days = date_list(start, end)

    # --- Activity ---
    activity_stats = {}
    for m in sorted(QTY_METRICS["activity"]):
        activity_stats[m] = build_metric_stat(m, "qty", start, end, prev_start, prev_end, end)
    steps_by_day = qty_series("step_count", start, end)

    # --- Sleep ---
    sleep_days = sleep_series(start, end)
    prev_sleep_days = sleep_series(prev_start, prev_end)
    total_sleep_cur = period_value("total_sleep", {d: v["total_sleep"] for d, v in sleep_days.items()})
    total_sleep_prev = period_value("total_sleep", {d: v["total_sleep"] for d, v in prev_sleep_days.items()})
    stage_series = {stage: [sleep_days.get(d, {}).get(stage) for d in all_days]
                    for stage in ("core", "deep", "rem", "awake")}
    weekday_sleep, weekend_sleep = [], []
    for d_str, v in sleep_days.items():
        if v["total_sleep"] is None:
            continue
        wd = date.fromisoformat(d_str).weekday()
        (weekend_sleep if wd >= 5 else weekday_sleep).append(v["total_sleep"])
    sleep_start_minutes = []
    for v in sleep_days.values():
        if v["sleep_start"]:
            hh, mm = v["sleep_start"][11:13], v["sleep_start"][14:16]
            minutes = int(hh) * 60 + int(mm)
            if minutes < 720:  # after-midnight bedtime, normalize onto the same clock scale
                minutes += 1440
            sleep_start_minutes.append(minutes)
    sleep_consistency = pstdev(sleep_start_minutes) if len(sleep_start_minutes) >= 2 else None

    # --- Vitals ---
    vitals_stats = {}
    for m in sorted(QTY_METRICS["vitals"]):
        vitals_stats[m] = build_metric_stat(m, "qty", start, end, prev_start, prev_end, end)
    vitals_stats["heart_rate"] = build_metric_stat("heart_rate", "hr", start, end, prev_start, prev_end, end)

    # --- Other actively-tracked ---
    other_stats = {}
    for m in sorted(QTY_METRICS["other"]):
        s = build_metric_stat(m, "qty", start, end, prev_start, prev_end, end)
        if s["cur"] is not None:
            other_stats[m] = s

    # --- Insights ---
    insights = []
    if len(covered) < len(all_days):
        insights.append(f"Data covers {len(covered)} of {len(all_days)} day(s) in this period — "
                         f"the rest will fill in as new daily exports arrive.")

    rhr = vitals_stats["resting_heart_rate"]
    if rhr["cur"] is not None and rhr["base_mean"]:
        z = (rhr["cur"] - rhr["base_mean"]) / rhr["base_std"] if rhr["base_std"] else 0
        if z > 1.5:
            insights.append(f"Resting heart rate ({rhr['cur']:.0f} bpm) is notably elevated vs. your "
                             f"28-day baseline ({rhr['base_mean']:.0f} bpm) — possible stress, illness, or under-recovery.")
        elif z < -1.5:
            insights.append(f"Resting heart rate ({rhr['cur']:.0f} bpm) is notably below your 28-day "
                             f"baseline ({rhr['base_mean']:.0f} bpm) — a good recovery/fitness sign.")

    hrv = vitals_stats["heart_rate_variability"]
    if hrv["cur"] is not None and hrv["base_mean"]:
        z = (hrv["cur"] - hrv["base_mean"]) / hrv["base_std"] if hrv["base_std"] else 0
        if z < -1.5:
            insights.append(f"HRV ({hrv['cur']:.0f} ms) is notably below your 28-day baseline "
                             f"({hrv['base_mean']:.0f} ms) — a common marker of accumulated fatigue or stress.")
        elif z > 1.5:
            insights.append(f"HRV ({hrv['cur']:.0f} ms) is notably above your 28-day baseline "
                             f"({hrv['base_mean']:.0f} ms) — looks like a well-recovered stretch.")

    if total_sleep_cur is not None:
        if total_sleep_cur < 7:
            insights.append(f"Average sleep is {total_sleep_cur:.1f}h/night, below the common 7–8h target.")
        if weekday_sleep and weekend_sleep:
            gap = mean(weekend_sleep) - mean(weekday_sleep)
            if abs(gap) >= 0.5:
                insights.append(f"Weekend sleep runs {abs(gap):.1f}h "
                                 f"{'longer' if gap > 0 else 'shorter'} than weekday sleep on average.")
    if sleep_consistency is not None and sleep_consistency > 60:
        insights.append(f"Bedtime varies by about {sleep_consistency/60:.1f}h night-to-night — "
                         f"less consistent than ideal for sleep quality.")

    ex = activity_stats["apple_exercise_time"]
    if ex["cur"] is not None:
        goal_days = sum(1 for v in ex["series"].values() if v and v >= 30)
        if len(covered) > 0:
            insights.append(f"Hit 30+ exercise minutes on {goal_days}/{len(covered)} tracked day(s).")

    if not insights:
        insights.append("Nothing stands out vs. baseline — metrics look steady.")

    # --- Render ---
    html = [HTML_HEAD.format(title=r["label"], sub=f"{start} → {end}")]
    html.append('<div class="headline">')
    for m, label in (("step_count", "Steps"), ("active_energy", "Active kcal")):
        s = activity_stats[m]
        v = s["cur"] * (1 / 4.184 if m == "active_energy" else 1) if s["cur"] is not None else None
        html.append(f'<div class="stat"><div class="v">{fmt(v, digits=0)}</div>'
                     f'<div class="l">{label} {trend_arrow(s["pct"])}</div></div>')
    html.append(f'<div class="stat"><div class="v">{fmt(total_sleep_cur, "h")}</div>'
                f'<div class="l">Sleep {trend_arrow(pct_change(total_sleep_cur, total_sleep_prev))}</div></div>')
    rhr_s = vitals_stats["resting_heart_rate"]
    html.append(f'<div class="stat"><div class="v">{fmt(rhr_s["cur"], " bpm", 0)}</div>'
                f'<div class="l">Resting HR {trend_arrow(rhr_s["pct"])}</div></div>')
    html.append("</div>")

    html.append('<div class="grid">')

    # Activity card
    html.append('<div class="card"><h2>Activity</h2>')
    html.append(svg.calendar_heatmap({d: steps_by_day.get(d) for d in all_days}, all_days))
    html.append('<div class="tiles">')
    for m in ("step_count", "walking_running_distance", "cycling_distance", "flights_climbed",
              "active_energy", "apple_exercise_time", "apple_stand_time", "apple_stand_hour"):
        s = activity_stats[m]
        digits = 1 if m in ("walking_running_distance", "cycling_distance") else 0
        html.append(f'<div class="tile"><div class="v">{fmt(s["cur"], digits=digits)}</div>'
                     f'<div class="l">{DISPLAY_NAME[m]} {trend_arrow(s["pct"])}</div></div>')
    html.append('</div></div>')

    # Sleep card
    html.append('<div class="card"><h2>Sleep</h2>')
    html.append(svg.stacked_bar(all_days, stage_series,
                colors={"core": "#5ec8f8", "deep": "#3a6ea5", "rem": "#a78bfa", "awake": "#f87171"}))
    html.append(f'<div class="tiles">'
                f'<div class="tile"><div class="v">{fmt(total_sleep_cur, "h")}</div><div class="l">Avg Total Sleep</div></div>'
                f'<div class="tile"><div class="v">{fmt(sleep_consistency/60 if sleep_consistency else None, "h")}</div>'
                f'<div class="l">Bedtime Variability</div></div>')
    if weekday_sleep:
        html.append(f'<div class="tile"><div class="v">{fmt(mean(weekday_sleep), "h")}</div><div class="l">Weekday Avg</div></div>')
    if weekend_sleep:
        html.append(f'<div class="tile"><div class="v">{fmt(mean(weekend_sleep), "h")}</div><div class="l">Weekend Avg</div></div>')
    html.append('</div></div>')

    # Vitals card
    html.append('<div class="card"><h2>Vitals</h2>')
    hr = vitals_stats["heart_rate"]
    hr_vals = [(d[5:], hr["series"].get(d, {}).get("avg")) for d in all_days]
    html.append(svg.line_chart(hr_vals, color=svg.PALETTE["accent2"]))
    html.append('<div class="tiles">')
    for m in ("resting_heart_rate", "walking_heart_rate_average", "heart_rate_variability",
              "respiratory_rate", "blood_oxygen_saturation", "apple_sleeping_wrist_temperature",
              "vo2_max", "cardio_recovery"):
        s = vitals_stats[m]
        if s["cur"] is None:
            continue
        html.append(f'<div class="tile">{svg.sparkline([v for v in s["series"].values() if v is not None] or [0])}'
                     f'<div class="v">{fmt(s["cur"], UNIT_LABEL.get("count/min" if "heart_rate" in m or m=="respiratory_rate" or m=="cardio_recovery" else "", ""), 1)}</div>'
                     f'<div class="l">{DISPLAY_NAME[m]} {trend_arrow(s["pct"])}</div></div>')
    html.append('</div></div>')

    # Other tracked card
    if other_stats:
        html.append('<div class="card"><h2>Other Tracked</h2><div class="tiles">')
        for m, s in other_stats.items():
            html.append(f'<div class="tile">{svg.sparkline([v for v in s["series"].values() if v is not None])}'
                         f'<div class="v">{fmt(s["cur"], digits=1)}</div>'
                         f'<div class="l">{DISPLAY_NAME.get(m, m)} {trend_arrow(s["pct"])}</div></div>')
        html.append('</div></div>')

    # Insights card
    html.append('<div class="card"><h2>Insights</h2><ul class="insights">')
    for line in insights:
        html.append(f"<li>{line}</li>")
    html.append('</ul></div>')

    html.append('</div></body></html>')

    out.mkdir(parents=True, exist_ok=True)
    out_path = out / f"{r['slug']}.html"
    out_path.write_text("".join(html))
    return out_path


def main(period="all", ref_date=None, out_dir=None):
    d = ref_date or date.today()
    periods = ["daily", "weekly", "monthly"] if period == "all" else [period]
    for p in periods:
        path = render(p, d, out_dir)
        print(f"wrote {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", choices=["daily", "weekly", "monthly", "all"], default="all")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--out-dir", "-o", help="Directory to write summary HTML into (default: reports/)")
    args = ap.parse_args()
    main(args.period, date.fromisoformat(args.date), args.out_dir)
