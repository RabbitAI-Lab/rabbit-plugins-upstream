#!/usr/bin/env python3
"""Generate a per-day Markdown health summary aimed at *AI/LLM* readers (not
humans looking at charts). One file per day -> reports/summary/YYYY-MM-DD.md.

Each file is self-contained: it deep-dives the target day (normally "yesterday")
and embeds 7-day / 28-day / 90-day-vs-prior-year trend context, so an LLM can
reason about both short- and long-term change from a single document.

Layout mirrors the three insight tiers we designed:
  Tier 1  Progress / controllable   (rings, steps, training load)
  Tier 2  Readiness / state         (sleep, vitals vs personal baseline)
  Tier 3  Long-term trajectory      (last-90d vs prior-12mo baseline)

It deliberately reuses the existing engines rather than re-deriving them:
  - TRIMP / EWMA training load  <- report_training_load
  - Activity-ring goals + logic <- report_rings
  - metric display names        <- report_health_metrics
so the markdown numbers always match the HTML dashboards.

Per the design decision, Tier 3 uses a FIXED year-vs-90d model everywhere; where
history is too short (health metrics currently only reach ~5 weeks) it prints an
honest "insufficient history" line that will fill in as exports accumulate.
"""
import argparse
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from statistics import mean, pstdev

sys.path.insert(0, str(Path(__file__).parent))
from lib.query import query
from lib.metrics import CUMULATIVE_METRICS

# Reuse the exact engines behind the HTML dashboards so numbers never drift.
from report_training_load import (
    MAX_HR, resting_hr_by_date, workouts_with_hr, workout_load,
    ewma_series, zone_for, date_list,
)
from report_rings import (
    MOVE_GOAL_KCAL, EXERCISE_GOAL_MIN, STAND_GOAL_HR, KJ_PER_KCAL,
    daily_activity, fracs_for,
)
from report_health_metrics import DISPLAY_NAME

REPORTS_DIR = Path(__file__).parent / "reports" / "summary"

TREND_DAYS = 90          # "emerging trend" = last 3 months
BASELINE_DAYS = 365      # "baseline" = the 12 months immediately before the trend window

# Population reference ranges for at-a-glance flagging (in addition to the
# personal baseline). (low_ok, high_ok, unit). None = judge on personal baseline only.
REFERENCE = {
    "resting_heart_rate": (40, 100, "bpm"),
    "respiratory_rate": (12, 20, "/min"),
    "blood_oxygen_saturation": (95, 100, "%"),
    "vo2_max": (35, 60, "mL/kg·min"),
    "heart_rate_variability": None,   # SDNN is highly individual; personal baseline only
}

# Vitals surfaced in the Tier-2 readiness section (all live in samples_qty).
READINESS_VITALS = [
    "resting_heart_rate", "heart_rate_variability", "respiratory_rate",
    "blood_oxygen_saturation", "apple_sleeping_wrist_temperature",
    "walking_heart_rate_average",
]

# (metric, cumulative?) surfaced in the Tier-3 long-term trend table.
TREND_METRICS = [
    ("vo2_max", False),
    ("step_count", True),
    ("walking_running_distance", True),
    ("cycling_distance", True),
    ("active_energy", True),
    ("apple_exercise_time", True),
    ("apple_stand_time", True),
    ("resting_heart_rate", False),
    ("heart_rate_variability", False),
    ("walking_speed", False),
    ("walking_step_length", False),
    ("walking_asymmetry_percentage", False),
    ("walking_double_support_percentage", False),
]


# ---------------------------------------------------------------------------
# small formatting helpers
# ---------------------------------------------------------------------------
def fmt(v, unit="", d=1):
    if v is None:
        return "n/a"
    return f"{v:,.{d}f}{unit}"


def pct_change(cur, base):
    if cur is None or base in (None, 0):
        return None
    return (cur - base) / base * 100


def arrow(pct):
    if pct is None:
        return ""
    if pct > 1:
        return f"▲ {abs(pct):.0f}%"
    if pct < -1:
        return f"▼ {abs(pct):.0f}%"
    return "→ flat"


def zscore(cur, m, s):
    if cur is None or m is None or not s:
        return None
    return (cur - m) / s


def zstr(z):
    if z is None:
        return ""
    return f"{z:+.1f}σ"


# ---------------------------------------------------------------------------
# data access
# ---------------------------------------------------------------------------
def latest_data_date():
    rows = query(
        "SELECT MAX(d)::VARCHAR AS d FROM ("
        "SELECT MAX(date) d FROM samples_qty "
        "UNION ALL SELECT MAX(date) FROM samples_hr "
        "UNION ALL SELECT MAX(date) FROM sleep_sessions "
        "UNION ALL SELECT MAX(date) FROM workouts)"
    )
    return rows[0]["d"] if rows and rows[0]["d"] else None


def qty_day(metric, day, cumulative):
    """Single-day value for a samples_qty metric (SUM if cumulative else AVG)."""
    agg = "SUM(qty)" if cumulative else "AVG(qty)"
    rows = query(f"SELECT {agg} AS v FROM samples_qty "
                 f"WHERE metric='{metric}' AND date = DATE '{day}'")
    return rows[0]["v"] if rows else None


def coverage_days(start, end):
    """Calendar days in the window that actually received an export (any metric).
    Used as the denominator for cumulative per-day averages so a day with an
    export but no cycling/etc. counts as a genuine zero, while days with no
    export at all (missing data) don't drag the average down."""
    rows = query("SELECT COUNT(DISTINCT date) AS n FROM samples_qty "
                 f"WHERE date BETWEEN DATE '{start}' AND DATE '{end}'")
    return (rows[0]["n"] if rows else 0) or 0


def qty_window(metric, start, end, cumulative):
    """Return (representative value, n_days) over a window.
    Cumulative metrics -> total / covered calendar days (true per-day rate,
    counting export days with no activity as zero). Rate metrics -> mean sample.
    n_days reports the days the metric itself had data (for insufficiency checks)."""
    if cumulative:
        rows = query(
            f"SELECT SUM(qty) AS total, COUNT(DISTINCT date) AS n FROM samples_qty "
            f"WHERE metric='{metric}' AND date BETWEEN DATE '{start}' AND DATE '{end}'")
        r = rows[0] if rows else {}
        cov = coverage_days(start, end)
        value = (r.get("total") / cov) if (r.get("total") is not None and cov) else None
        return value, (r.get("n") or 0)
    rows = query(
        f"SELECT AVG(qty) AS v, COUNT(DISTINCT date) AS n FROM samples_qty "
        f"WHERE metric='{metric}' AND date BETWEEN DATE '{start}' AND DATE '{end}'")
    r = rows[0] if rows else {}
    return r.get("v"), (r.get("n") or 0)


def qty_baseline(metric, end_day, window=28):
    """Per-sample mean/std over a trailing window, for z-score comparison."""
    start = (date.fromisoformat(end_day) - timedelta(days=window - 1)).isoformat()
    rows = query(f"SELECT qty AS v FROM samples_qty WHERE metric='{metric}' "
                 f"AND date BETWEEN DATE '{start}' AND DATE '{end_day}'")
    vals = [r["v"] for r in rows if r["v"] is not None]
    if len(vals) < 3:
        return None, None, len(vals)
    return mean(vals), pstdev(vals), len(vals)


def sleep_row(day):
    rows = query("SELECT total_sleep, core, deep, rem, awake, "
                 "sleep_start::VARCHAR AS sleep_start, sleep_end::VARCHAR AS sleep_end, "
                 "in_bed_start::VARCHAR AS in_bed_start "
                 f"FROM sleep_sessions WHERE date = DATE '{day}' ORDER BY total_sleep DESC LIMIT 1")
    return rows[0] if rows else None


def sleep_window(start, end):
    rows = query("SELECT date::VARCHAR AS d, total_sleep, "
                 "sleep_start::VARCHAR AS sleep_start FROM sleep_sessions "
                 f"WHERE date BETWEEN DATE '{start}' AND DATE '{end}' ORDER BY date")
    return rows


def workouts_on(day):
    return query(
        "SELECT id, name, ROUND(duration_s/60.0,1) AS min, distance_km, avg_hr, max_hr, "
        "min_hr, avg_speed, active_energy_kj, total_energy_kj, elevation_up_m, is_indoor, "
        "location, temperature_c, step_cadence, flights_climbed, start::VARCHAR AS start "
        f"FROM workouts WHERE date = DATE '{day}' ORDER BY start")


def clock(ts):
    """'2026-07-04 21:27:06+02' -> '21:27'."""
    if not ts:
        return "n/a"
    return ts[11:16]


# ---------------------------------------------------------------------------
# training load (reuse report_training_load engine)
# ---------------------------------------------------------------------------
def compute_load(target):
    resting_by_date, resting_fallback = resting_hr_by_date()
    workouts, hr_by_workout = workouts_with_hr()
    if not workouts:
        return None
    per_workout = {}
    daily = {}
    for w in workouts:
        resting = resting_by_date.get(w["date"], resting_fallback)
        load = workout_load(w, hr_by_workout.get(w["id"], []), resting)
        per_workout[w["id"]] = load
        daily[w["date"]] = daily.get(w["date"], 0.0) + load

    first = date.fromisoformat(workouts[0]["date"])
    all_days = date_list(first, date.fromisoformat(target))
    series = [daily.get(d, 0.0) for d in all_days]
    idx = len(all_days) - 1

    def rolling(i, window):
        return sum(series[max(0, i - window + 1):i + 1])

    acute = rolling(idx, 7)
    chronic_weekly = ewma_series(series, tau=28)[idx] * 7
    acwr = acute / chronic_weekly if chronic_weekly > 0 else None
    zone = zone_for(acwr)[0] if acwr is not None else None
    return dict(today=daily.get(target, 0.0), acute=acute, chronic=chronic_weekly,
                acwr=acwr, zone=zone, per_workout=per_workout,
                hr_by_workout=hr_by_workout, resting=resting_fallback)


def hr_zone_minutes(hr_series):
    """Approx minutes in %-max-HR zones from a per-minute avg-HR series."""
    zones = {"Z1 (<60%)": 0, "Z2 (60-70%)": 0, "Z3 (70-80%)": 0,
             "Z4 (80-90%)": 0, "Z5 (>90%)": 0}
    for _, hr in hr_series:
        if hr is None:
            continue
        frac = hr / MAX_HR
        if frac < 0.6:
            zones["Z1 (<60%)"] += 1
        elif frac < 0.7:
            zones["Z2 (60-70%)"] += 1
        elif frac < 0.8:
            zones["Z3 (70-80%)"] += 1
        elif frac < 0.9:
            zones["Z4 (80-90%)"] += 1
        else:
            zones["Z5 (>90%)"] += 1
    return zones


def typical_for(name, end_day):
    """Averages for same-named workouts over the prior 12 months, for comparison."""
    start = (date.fromisoformat(end_day) - timedelta(days=BASELINE_DAYS)).isoformat()
    name_esc = name.replace("'", "''")
    rows = query(
        "SELECT COUNT(*) AS n, AVG(duration_s/60.0) AS min, AVG(distance_km) AS km, "
        "AVG(avg_hr) AS avg_hr, AVG(active_energy_kj) AS kj FROM workouts "
        f"WHERE name='{name_esc}' AND date BETWEEN DATE '{start}' AND DATE '{end_day}'")
    return rows[0] if rows else {}


# ---------------------------------------------------------------------------
# section builders
# ---------------------------------------------------------------------------
def build_tier1(target, load):
    """Progress / controllable: rings, steps & distance, training load."""
    L = []
    # Rings — pull a wide window so we can compute streak + 28d baseline in one go.
    wide_start = (date.fromisoformat(target) - timedelta(days=400)).isoformat()
    move, exercise, stand = daily_activity(wide_start, target)
    win28 = date_list(date.fromisoformat(target) - timedelta(days=27),
                      date.fromisoformat(target))

    def base_avg(series):
        vals = [series[d] for d in win28 if series.get(d)]
        return mean(vals) if vals else None

    mv, ex, sd = move.get(target, 0), exercise.get(target, 0), stand.get(target, 0)
    mv_b, ex_b, sd_b = base_avg(move), base_avg(exercise), base_avg(stand)

    L.append("## Tier 1 — Progress (things you control)\n")
    L.append("### Activity Rings\n")
    L.append(f"- **Move**: {mv:.0f} / {MOVE_GOAL_KCAL} kcal "
             f"({'closed ✓' if mv >= MOVE_GOAL_KCAL else 'open'}) · "
             f"28d avg {fmt(mv_b, ' kcal', 0)} {arrow(pct_change(mv, mv_b))}")
    L.append(f"- **Exercise**: {ex:.0f} / {EXERCISE_GOAL_MIN} min "
             f"({'closed ✓' if ex >= EXERCISE_GOAL_MIN else 'open'}) · "
             f"28d avg {fmt(ex_b, ' min', 0)} {arrow(pct_change(ex, ex_b))}")
    L.append(f"- **Stand**: {sd:.0f} / {STAND_GOAL_HR} hr "
             f"({'closed ✓' if sd >= STAND_GOAL_HR else 'open'}) · "
             f"28d avg {fmt(sd_b, ' hr', 0)} {arrow(pct_change(sd, sd_b))}")

    # streak of all-3-closed days ending today
    streak, d = 0, date.fromisoformat(target)
    while all(f >= 1 for f in fracs_for(d.isoformat(), move, exercise, stand)):
        streak += 1
        d -= timedelta(days=1)
    week = date_list(date.fromisoformat(target) - timedelta(days=6),
                     date.fromisoformat(target))
    week_closed = sum(1 for x in week if all(f >= 1 for f in fracs_for(x, move, exercise, stand)))
    all_three = all(f >= 1 for f in fracs_for(target, move, exercise, stand))
    L.append(f"- All three closed today: {'yes' if all_three else 'no'} · "
             f"current streak {streak} day(s) · {week_closed}/7 closed this week\n")

    # Steps & distance
    L.append("### Steps & Distance\n")
    for m, unit, d0 in (("step_count", " steps", 0),
                        ("walking_running_distance", " km", 2),
                        ("cycling_distance", " km", 2),
                        ("flights_climbed", " flights", 0)):
        cum = m in CUMULATIVE_METRICS
        cur = qty_day(m, target, cum)
        b7, _ = qty_window(m, (date.fromisoformat(target) - timedelta(days=7)).isoformat(),
                           (date.fromisoformat(target) - timedelta(days=1)).isoformat(), cum)
        if cur is None and not b7:
            continue
        L.append(f"- **{DISPLAY_NAME.get(m, m)}**: {fmt(cur, unit, d0)} "
                 f"(prior-7d avg/day {fmt(b7, unit, d0)} {arrow(pct_change(cur, b7))})")
    L.append("")

    # Training load
    L.append("### Training Load (TRIMP)\n")
    if load:
        acwr = f"{load['acwr']:.2f}" if load["acwr"] is not None else "n/a"
        L.append(f"- Yesterday's load: **{load['today']:.0f}**")
        L.append(f"- 7-day acute load: **{load['acute']:.0f}**")
        L.append(f"- 28-day chronic load (weekly-equiv): **{load['chronic']:.0f}**")
        L.append(f"- Acute:Chronic ratio: **{acwr}** — zone: **{load['zone'] or 'n/a'}** "
                 f"(Optimal ≈ 0.8–1.3; >1.5 = spike risk)\n")
    else:
        L.append("- No workout history yet to compute training load.\n")
    return "\n".join(L), (move, exercise, stand, mv, ex, sd, streak, week_closed)


def build_tier2(target):
    """Readiness / state: sleep + vitals vs 28-day personal baseline."""
    L = ["## Tier 2 — Readiness (things that shape your day)\n"]
    signals, flags = [], []

    # --- Sleep ---
    L.append("### Sleep\n")
    s = sleep_row(target)
    if s and s["total_sleep"]:
        total = s["total_sleep"]
        L.append(f"- Total sleep: **{total:.1f} h** "
                 f"(bed {clock(s['sleep_start'])} → wake {clock(s['sleep_end'])})")
        L.append(f"- Stages: core {fmt(s['core'],'h')} · deep {fmt(s['deep'],'h')} · "
                 f"REM {fmt(s['rem'],'h')} · awake {fmt(s['awake'],'h')}")
        # 28d context + bedtime consistency
        sw = sleep_window((date.fromisoformat(target) - timedelta(days=27)).isoformat(), target)
        tots = [r["total_sleep"] for r in sw if r["total_sleep"]]
        if tots:
            L.append(f"- 28-day avg: {mean(tots):.1f} h/night {arrow(pct_change(total, mean(tots)))}")
        starts = []
        for r in sw:
            if r["sleep_start"]:
                mnt = int(r["sleep_start"][11:13]) * 60 + int(r["sleep_start"][14:16])
                if mnt < 720:
                    mnt += 1440
                starts.append(mnt)
        if len(starts) >= 2:
            L.append(f"- Bedtime consistency: ±{pstdev(starts)/60:.1f} h night-to-night")
        if total < 7:
            signals.append("short sleep (<7h)")
            flags.append("sleep_short")
    else:
        L.append("- No sleep session recorded for this night.")
    L.append("")

    # --- Vitals ---
    L.append("### Vitals (vs 28-day personal baseline)\n")
    L.append("| Metric | Value | 28d baseline | Deviation | Range |")
    L.append("|---|---|---|---|---|")
    for m in READINESS_VITALS:
        cur = qty_day(m, target, cumulative=False)
        bmean, bstd, n = qty_baseline(m, target)
        z = zscore(cur, bmean, bstd)
        # population range flag
        ref = REFERENCE.get(m)
        flag = "—"
        if ref and cur is not None:
            lo, hi, _u = ref
            flag = "low" if cur < lo else ("high" if cur > hi else "normal")
        base_txt = fmt(bmean, "", 1) if bmean is not None else f"insufficient ({n} pts)"
        L.append(f"| {DISPLAY_NAME.get(m, m)} | {fmt(cur, '', 1)} | {base_txt} | "
                 f"{zstr(z) or '—'} | {flag} |")

        # readiness signals
        if m == "resting_heart_rate" and z is not None and z >= 1.0:
            signals.append(f"resting HR elevated ({zstr(z)})")
            flags.append("rhr_elevated")
        if m == "heart_rate_variability" and z is not None and z <= -1.0:
            signals.append(f"HRV suppressed ({zstr(z)})")
            flags.append("hrv_low")
        if m == "respiratory_rate" and z is not None and z >= 1.5:
            signals.append(f"respiratory rate elevated ({zstr(z)})")
            flags.append("resp_elevated")
        if m == "blood_oxygen_saturation" and cur is not None and cur < 95:
            signals.append(f"blood oxygen low ({cur:.0f}%)")
            flags.append("spo2_low")
    L.append("")

    # --- Readiness read ---
    if len(signals) >= 3:
        verdict = "under-recovered"
    elif signals:
        verdict = "normal"
    else:
        verdict = "well-recovered"
    L.append("### Readiness read\n")
    if signals:
        L.append(f"**{verdict.capitalize()}.** Notable signals: " + "; ".join(signals) + ".")
    else:
        L.append(f"**{verdict.capitalize()}.** Sleep and vitals sit near your personal baseline; "
                 "nothing flags as elevated stress or under-recovery.")
    L.append("")
    return "\n".join(L), verdict, flags


def build_tier3(target):
    """Long-term trajectory: last-90d vs prior-12mo baseline (fixed model)."""
    d = date.fromisoformat(target)
    trend_start = (d - timedelta(days=TREND_DAYS - 1)).isoformat()
    base_end = (d - timedelta(days=TREND_DAYS)).isoformat()
    base_start = (d - timedelta(days=TREND_DAYS + BASELINE_DAYS - 1)).isoformat()

    L = ["## Tier 3 — Long-term Trends (last 90 days vs prior 12 months)\n"]
    L.append(f"*Baseline window: {base_start} → {base_end}. "
             f"Trend window: {trend_start} → {target}.*\n")

    # Metric trend table
    L.append("| Metric | Baseline (12mo) | Last 90d | Change | Data |")
    L.append("|---|---|---|---|---|")
    for m, cum in TREND_METRICS:
        base_v, base_n = qty_window(m, base_start, base_end, cum)
        trend_v, trend_n = qty_window(m, trend_start, target, cum)
        if trend_n == 0 and base_n == 0:
            continue
        # honest "insufficient history" — health metrics only reach ~5 weeks today
        if base_n < 5:
            change = "insufficient history"
        else:
            change = arrow(pct_change(trend_v, base_v)) or "→ flat"
        unit = " km" if "distance" in m else ""
        d0 = 2 if "distance" in m or "speed" in m else 1
        L.append(f"| {DISPLAY_NAME.get(m, m)} | {fmt(base_v, unit, d0)} | "
                 f"{fmt(trend_v, unit, d0)} | {change} | {trend_n}d/{base_n}d |")
    L.append("")

    # Workout patterns (workouts have ~18mo history, so these are meaningful)
    L.append("### Workout patterns\n")
    base_wk = query("SELECT COUNT(*) AS n, COUNT(DISTINCT date) AS days FROM workouts "
                    f"WHERE date BETWEEN DATE '{base_start}' AND DATE '{base_end}'")[0]
    trend_wk = query("SELECT COUNT(*) AS n FROM workouts "
                     f"WHERE date BETWEEN DATE '{trend_start}' AND DATE '{target}'")[0]
    base_per_wk = (base_wk["n"] or 0) / (BASELINE_DAYS / 7)
    trend_per_wk = (trend_wk["n"] or 0) / (TREND_DAYS / 7)
    L.append(f"- Frequency: **{trend_per_wk:.1f}/week** last 90d vs "
             f"**{base_per_wk:.1f}/week** baseline {arrow(pct_change(trend_per_wk, base_per_wk))}")
    mix = query("SELECT name, COUNT(*) AS n FROM workouts "
                f"WHERE date BETWEEN DATE '{trend_start}' AND DATE '{target}' "
                "GROUP BY name ORDER BY n DESC LIMIT 4")
    if mix:
        L.append("- Top workout types (last 90d): "
                 + ", ".join(f"{r['name']} ×{r['n']}" for r in mix))

    # Running pace + cycling distance trend
    run = query("SELECT AVG(avg_speed) AS spd, AVG(distance_km) AS km, COUNT(*) AS n FROM workouts "
                f"WHERE name='Outdoor Run' AND date BETWEEN DATE '{trend_start}' AND DATE '{target}'")[0]
    run_b = query("SELECT AVG(avg_speed) AS spd, AVG(distance_km) AS km FROM workouts "
                  f"WHERE name='Outdoor Run' AND date BETWEEN DATE '{base_start}' AND DATE '{base_end}'")[0]
    if run["n"]:
        def pace(spd):  # km/h -> min/km
            return 60 / spd if spd else None
        L.append(f"- Running (last 90d, {run['n']} runs): avg {fmt(run['km'],' km',1)} @ "
                 f"{fmt(pace(run['spd']),' min/km',1)} pace "
                 f"(baseline pace {fmt(pace(run_b['spd']),' min/km',1)})")
    L.append("")
    return "\n".join(L)


def build_workouts(target, load):
    L = ["## Yesterday's Workout(s)\n"]
    ws = workouts_on(target)
    if not ws:
        L.append("No workouts recorded.\n")
        return "\n".join(L)
    hr_by_workout = load["hr_by_workout"] if load else {}
    per_workout = load["per_workout"] if load else {}
    for w in ws:
        L.append(f"### {w['name']} — {w['min']:.0f} min\n")
        bits = []
        if w["distance_km"]:
            bits.append(f"distance {w['distance_km']:.2f} km")
        if w["avg_hr"]:
            bits.append(f"HR {w['avg_hr']:.0f} avg / {fmt(w['max_hr'],'',0)} max")
        if w["active_energy_kj"]:
            bits.append(f"active energy {w['active_energy_kj']/KJ_PER_KCAL:.0f} kcal")
        if w["elevation_up_m"]:
            bits.append(f"ascent {w['elevation_up_m']:.0f} m")
        if w["id"] in per_workout:
            bits.append(f"TRIMP load {per_workout[w['id']]:.0f}")
        L.append("- " + " · ".join(bits) if bits else "- (limited metrics)")

        # HR zone breakdown
        hs = hr_by_workout.get(w["id"], [])
        if hs:
            zones = hr_zone_minutes(hs)
            active = [f"{k} {v}m" for k, v in zones.items() if v]
            if active:
                L.append("- HR zones (approx min): " + " · ".join(active))

        # comparison to your typical session of this type
        typ = typical_for(w["name"], target)
        if typ and typ.get("n") and typ["n"] > 1:
            cmp = []
            if typ.get("min"):
                cmp.append(f"duration {arrow(pct_change(w['min'], typ['min']))} vs {typ['min']:.0f} min typical")
            if w["distance_km"] and typ.get("km"):
                cmp.append(f"distance {arrow(pct_change(w['distance_km'], typ['km']))}")
            if w["avg_hr"] and typ.get("avg_hr"):
                cmp.append(f"avg HR {arrow(pct_change(w['avg_hr'], typ['avg_hr']))}")
            if cmp:
                L.append(f"- vs your typical {w['name']} ({typ['n']} in prior 12mo): " + "; ".join(cmp))
        L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------------------
# assembly
# ---------------------------------------------------------------------------
def render(target, generated=None, out_dir=None):
    generated = generated or date.today().isoformat()
    d = date.fromisoformat(target)

    load = compute_load(target)
    tier1, _ = build_tier1(target, load)
    tier2, verdict, flags = build_tier2(target)
    tier3 = build_tier3(target)
    workouts_md = build_workouts(target, load)

    # completeness snapshot
    has_metrics = bool(query(f"SELECT 1 FROM samples_qty WHERE date=DATE '{target}' LIMIT 1"))
    has_sleep = bool(sleep_row(target))
    n_workouts = len(workouts_on(target))

    fm = [
        "---",
        f"date: {target}",
        f"generated: {generated}",
        f"weekday: {d.strftime('%A')}",
        "data_completeness:",
        f"  health_metrics: {'present' if has_metrics else 'missing'}",
        f"  sleep: {'present' if has_sleep else 'missing'}",
        f"  workouts: {n_workouts}",
        "baseline_windows:",
        "  readiness: 28d",
        f"  trend: {TREND_DAYS}d vs prior {BASELINE_DAYS}d",
        f"readiness: {verdict}",
        f"flags: [{', '.join(flags)}]",
        "---",
        "",
    ]

    tldr = (f"On {d.strftime('%A, %B %-d, %Y')} you logged {n_workouts} workout(s). "
            f"Readiness reads **{verdict}**"
            + (f" ({', '.join(flags)})." if flags else ".")
            + " See tiers below for controllable progress, overnight readiness, and long-term trajectory.")

    body = [
        f"# Daily Health Summary — {d.strftime('%A, %Y-%m-%d')}",
        "",
        "## TL;DR",
        tldr,
        "",
        tier1,
        tier2,
        tier3,
        workouts_md,
        "## Data Notes",
        "- Health-metric baselines (Tier 2) use a trailing 28-day personal window.",
        "- Tier 3 uses a fixed last-90d vs prior-12mo model; rows show "
        "'insufficient history' until enough days accumulate (health metrics began 2026-06-01).",
        "- Training load is estimated TRIMP (Banister), not Apple's own score.",
        "",
    ]

    out = "\n".join(fm) + "\n".join(body)
    base = Path(out_dir) if out_dir else REPORTS_DIR
    base.mkdir(parents=True, exist_ok=True)
    out_path = base / f"{target}.md"
    out_path.write_text(out)
    return out_path


def main(target=None, out_dir=None):
    target = target or latest_data_date()
    if not target:
        print("No data ingested yet.")
        return
    path = render(target, out_dir=out_dir)
    print(f"wrote {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate a per-day Markdown health summary for AI readers.")
    ap.add_argument("--date", help="target day YYYY-MM-DD (default: latest day with data)")
    ap.add_argument("--out-dir", "-o", help="Directory to write the .md summary into (default: reports/summary/)")
    args = ap.parse_args()
    main(args.date, args.out_dir)
