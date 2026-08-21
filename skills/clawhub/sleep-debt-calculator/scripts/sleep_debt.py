#!/usr/bin/env python3
"""
Sleep Debt Calculator — track sleep, calculate debt, suggest recovery schedules.
Pure Python stdlib. JSON file database.

Usage:
    python3 sleep_debt.py init                          # Set up profile (age)
    python3 sleep_debt.py log <bedtime> <wake> [quality] [notes]
                                                        # Log a sleep session
    python3 sleep_debt.py debt                          # Show current sleep debt
    python3 sleep_debt.py recovery <hours_per_night>    # Days to recover
    python3 sleep_debt.py optimal                       # Show optimal sleep for your age
    python3 sleep_debt.py streak                        # Show logging consistency streak
    python3 sleep_debt.py report [week|month]           # Weekly/monthly summary
    python3 sleep_debt.py schedule                      # Suggest bedtime tonight
    python3 sleep_debt.py chronotype                    # Detect your chronotype
    python3 sleep_debt.py chart [days]                  # ASCII chart of sleep duration

Time format: "HH:MM" (24-hour). e.g., 23:30, 07:15.
Quality: 1 (terrible) to 5 (excellent). Default 3.
Notes: free text. Mention caffeine/alcohol for impact tracking.

Examples:
    python3 sleep_debt.py init
    python3 sleep_debt.py log 23:30 07:15 4 "slept well, had coffee at 3pm"
    python3 sleep_debt.py debt
    python3 sleep_debt.py recovery 8.5
    python3 sleep_debt.py schedule
    python3 sleep_debt.py chart 14
"""

import json
import os
import sys
import math
from datetime import datetime, date, timedelta, time as dtime

# --- Constants ---

DEFAULT_DB_PATH = os.path.expanduser("~/.sleep_debt.json")

# Age-based optimal sleep durations (hours) — National Sleep Foundation recommendations
AGE_OPTIMAL = {
    "school_age": (6, 13, 9.5),      # 6-13 years: 9-11h, optimal ~9.5
    "teen": (14, 17, 9.0),           # 14-17 years: 8-10h, optimal ~9.0
    "young_adult": (18, 25, 8.0),    # 18-25 years: 7-9h, optimal ~8.0
    "adult": (26, 64, 8.0),          # 26-64 years: 7-9h, optimal ~8.0
    "senior": (65, 120, 7.5),        # 65+: 7-8h, optimal ~7.5
}

QUALITY_WEIGHTS = {
    1: 0.45,   # terrible — only ~45% of time asleep is restorative
    2: 0.65,   # poor
    3: 0.80,   # average
    4: 0.92,   # good
    5: 1.0,    # excellent — fully restorative
}

QUALITY_LABELS = {1: "terrible", 2: "poor", 3: "average", 4: "good", 5: "excellent"}

CAFFEINE_KEYWORDS = ["coffee", "caffeine", "espresso", "energy drink", "tea (black", "pre-workout", "cola", "caffeinated"]
ALCOHOL_KEYWORDS = ["alcohol", "beer", "wine", "whiskey", "vodka", "rum", "cocktail", "drinks", "drunk", "tipsy"]


# --- Database ---

def load_db(path=None):
    path = path or DEFAULT_DB_PATH
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {"profile": {}, "logs": []}


def save_db(db, path=None):
    path = path or DEFAULT_DB_PATH
    with open(path, "w") as f:
        json.dump(db, f, indent=2, default=str)


# --- Sleep Science ---

def get_optimal_for_age(age):
    """Return (min_hours, max_hours, optimal_hours) for a given age."""
    for key, (lo, hi, opt) in AGE_OPTIMAL.items():
        if lo <= age <= hi:
            return opt
    return 8.0  # default adult


def parse_time(t_str):
    """Parse HH:MM into hours (float). Returns None on failure."""
    try:
        parts = t_str.strip().split(":")
        h = int(parts[0])
        m = int(parts[1])
        return h + m / 60.0
    except (ValueError, IndexError, AttributeError):
        return None


def calculate_sleep_duration(bedtime_str, wake_str):
    """Calculate sleep duration in hours from bedtime and wake time strings."""
    bed = parse_time(bedtime_str)
    wake = parse_time(wake_str)
    if bed is None or wake is None:
        return None
    if wake < bed:  # crossed midnight
        duration = (24.0 - bed) + wake
    else:
        duration = wake - bed
    return round(duration, 2)


def quality_weighted_hours(duration, quality):
    """Apply quality weighting: 6h excellent sleep > 8h poor sleep."""
    weight = QUALITY_WEIGHTS.get(quality, 0.80)
    return round(duration * weight, 2)


def detect_substances(notes):
    """Check notes for caffeine/alcohol mentions."""
    notes_lower = (notes or "").lower()
    caffeine = any(k in notes_lower for k in CAFFEINE_KEYWORDS)
    alcohol = any(k in notes_lower for k in ALCOHOL_KEYWORDS)
    return caffeine, alcohol


def get_date_key(offset_days=0):
    """Get date string for today (or offset)."""
    d = date.today() - timedelta(days=offset_days)
    return d.isoformat()


# --- Commands ---

def cmd_init(db, args):
    """Initialize profile with age."""
    if len(args) < 1:
        age_input = input("Enter your age: ")
    else:
        age_input = args[0]
    try:
        age = int(age_input)
    except ValueError:
        print("Error: age must be a number.")
        return
    db["profile"]["age"] = age
    optimal = get_optimal_for_age(age)
    db["profile"]["optimal_hours"] = optimal
    save_db(db)
    print(f"Profile created! Age: {age}, optimal sleep: {optimal}h/night")


def cmd_log(db, args):
    """Log a sleep session."""
    if len(args) < 2:
        print("Usage: log <bedtime> <wake> [quality 1-5] [notes]")
        print('Example: log 23:30 07:15 4 "slept well"')
        return

    bedtime = args[0]
    wake = args[1]
    quality = 3
    notes = ""

    if len(args) >= 3:
        try:
            quality = int(args[2])
            if quality < 1 or quality > 5:
                print("Error: quality must be 1-5")
                return
        except ValueError:
            # Maybe it's notes without quality
            notes = " ".join(args[2:])
            quality = 3

    if len(args) >= 4:
        notes = " ".join(args[3:])

    duration = calculate_sleep_duration(bedtime, wake)
    if duration is None:
        print(f"Error: invalid time format. Use HH:MM (e.g. 23:30, 07:15)")
        return

    age = db.get("profile", {}).get("age")
    if age:
        optimal = get_optimal_for_age(age)
    else:
        optimal = 8.0

    effective = quality_weighted_hours(duration, quality)
    caffeine, alcohol = detect_substances(notes)

    entry = {
        "date": get_date_key(),
        "bedtime": bedtime,
        "wake": wake,
        "duration": duration,
        "quality": quality,
        "effective_hours": effective,
        "notes": notes,
        "caffeine": caffeine,
        "alcohol": alcohol,
    }

    db["logs"].append(entry)
    save_db(db)

    print(f"✓ Logged sleep for {entry['date']}")
    print(f"  Bedtime: {bedtime} → Wake: {wake} = {duration:.1f}h in bed")
    print(f"  Quality: {quality}/5 ({QUALITY_LABELS[quality]})")
    print(f"  Effective sleep: {effective:.1f}h (quality-weighted)")
    print(f"  Optimal: {optimal:.1f}h → {'+' if effective >= optimal else ''}{effective - optimal:.1f}h")
    if caffeine:
        print(f"  ⚠ Caffeine detected in notes — may have reduced sleep quality")
    if alcohol:
        print(f"  ⚠ Alcohol detected in notes — disrupts REM sleep")


def cmd_debt(db, args):
    """Show current accumulated sleep debt."""
    logs = db.get("logs", [])
    if not logs:
        print("No sleep logged yet. Use 'log' to record sleep.")
        return

    age = db.get("profile", {}).get("age")
    optimal = get_optimal_for_age(age) if age else 8.0

    # Calculate debt over all logged days
    total_debt = 0.0
    total_effective = 0.0
    total_raw = 0.0
    for entry in logs:
        effective = entry.get("effective_hours", entry.get("duration", 0))
        deficit = optimal - effective
        total_debt += deficit
        total_effective += effective
        total_raw += entry.get("duration", 0)

    n = len(logs)
    avg_raw = total_raw / n if n else 0
    avg_effective = total_effective / n if n else 0

    print(f"📊 Sleep Debt Summary ({n} days logged)")
    print(f"   Optimal: {optimal:.1f}h/night")
    print(f"   Average raw sleep: {avg_raw:.1f}h")
    print(f"   Average effective sleep: {avg_effective:.1f}h")
    if total_debt > 0:
        print(f"   💰 Total sleep debt: {total_debt:.1f}h")
    else:
        print(f"   ✅ Sleep surplus: {abs(total_debt):.1f}h (well rested!)")
    print()

    # Recent 7-day window
    recent = logs[-7:]
    recent_debt = sum(optimal - e.get("effective_hours", e.get("duration", 0)) for e in recent)
    print(f"   Last {len(recent)} days: {'debt' if recent_debt > 0 else 'surplus'} of {abs(recent_debt):.1f}h")

    # Weekend recovery detection
    weekend_days = [e for e in recent if _is_weekend(e.get("date", ""))]
    weekday_days = [e for e in recent if not _is_weekend(e.get("date", ""))]
    if weekend_days and weekday_days:
        wknd_avg = sum(e.get("duration", 0) for e in weekend_days) / len(weekend_days)
        wkdy_avg = sum(e.get("duration", 0) for e in weekday_days) / len(weekday_days)
        diff = wknd_avg - wkdy_avg
        if diff > 0.5:
            print(f"   🛌 Weekend recovery detected: sleeping {diff:.1f}h more on weekends")
            print(f"      (Weekdays: {wkdy_avg:.1f}h, Weekends: {wknd_avg:.1f}h)")


def _is_weekend(date_str):
    """Check if a date string (YYYY-MM-DD) falls on a weekend."""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
        return d.weekday() >= 5  # Saturday=5, Sunday=6
    except (ValueError, TypeError):
        return False


def cmd_recovery(db, args):
    """Calculate days needed to recover from debt."""
    if len(args) < 1:
        print("Usage: recovery <hours_per_night>")
        print("Example: recovery 8.5")
        return

    try:
        target_hours = float(args[0])
    except ValueError:
        print("Error: hours must be a number (e.g., 8.5)")
        return

    logs = db.get("logs", [])
    if not logs:
        print("No sleep logged yet.")
        return

    age = db.get("profile", {}).get("age")
    optimal = get_optimal_for_age(age) if age else 8.0

    # Calculate current debt (last 14 days for accuracy)
    recent = logs[-14:]
    current_debt = sum(optimal - e.get("effective_hours", e.get("duration", 0)) for e in recent)

    if current_debt <= 0:
        print("✅ You have no sleep debt! You're well rested.")
        return

    surplus_per_night = target_hours - optimal
    if surplus_per_night <= 0:
        print(f"⚠ Your target of {target_hours}h is at or below your optimal of {optimal}h.")
        print(f"  You need to sleep MORE than {optimal}h to recover. Current debt: {current_debt:.1f}h")
        return

    days_needed = math.ceil(current_debt / surplus_per_night)
    print(f"💤 Recovery Plan")
    print(f"   Current debt: {current_debt:.1f}h")
    print(f"   Target: {target_hours}h/night (+{surplus_per_night:.1f}h above optimal)")
    print(f"   → Sleep {target_hours}h for {days_needed} nights to fully recover.")
    print(f"   Full recovery date: {(date.today() + timedelta(days=days_needed)).strftime('%b %d, %Y')}")


def cmd_optimal(db, args):
    """Show optimal sleep duration for the user's age."""
    age = db.get("profile", {}).get("age")
    if not age:
        age_input = input("Enter your age to see optimal sleep: ")
        try:
            age = int(age_input)
        except ValueError:
            print("Error: age must be a number.")
            return

    optimal = get_optimal_for_age(age)
    # Find the range
    range_str = ""
    for key, (lo, hi, opt) in AGE_OPTIMAL.items():
        if lo <= age <= hi:
            range_str = f"{lo}-{hi} years"
            break

    print(f"🌙 Optimal Sleep Duration")
    print(f"   Your age: {age} ({range_str})")
    print(f"   Recommended: {optimal:.1f}h/night")
    print()
    print(f"   Age-based reference table:")
    for key, (lo, hi, opt) in AGE_OPTIMAL.items():
        marker = " ◀ you" if lo <= age <= hi else ""
        print(f"     {lo:3d}-{hi:<3d} years: {opt:.1f}h/night{marker}")


def cmd_streak(db, args):
    """Show logging consistency streak."""
    logs = db.get("logs", [])
    if not logs:
        print("No sleep logged yet.")
        return

    # Get sorted unique dates
    dates_logged = sorted(set(e["date"] for e in logs if "date" in e), reverse=True)

    today = date.today()
    streak = 0
    check_date = today
    for _ in range(len(dates_logged) + 1):
        iso = check_date.isoformat()
        if iso in dates_logged:
            streak += 1
            check_date = check_date - timedelta(days=1)
        elif streak == 0 and iso == today.isoformat():
            # Today not logged yet, check yesterday
            check_date = check_date - timedelta(days=1)
        else:
            break

    print(f"🔥 Consistency Streak: {streak} day{'s' if streak != 1 else ''}")
    total = len(dates_logged)
    print(f"   Total days logged: {total}")
    if streak >= 7:
        print(f"   Great job staying consistent!")
    elif streak >= 3:
        print(f"   Keep it up!")
    elif streak == 0:
        print(f"   Log today's sleep to start a streak!")


def cmd_report(db, args):
    """Weekly or monthly summary."""
    logs = db.get("logs", [])
    if not logs:
        print("No sleep logged yet.")
        return

    period = args[0] if args else "week"
    if period not in ("week", "month"):
        print("Usage: report [week|month]")
        return

    days = 7 if period == "week" else 30
    period_logs = logs[-days:]
    age = db.get("profile", {}).get("age")
    optimal = get_optimal_for_age(age) if age else 8.0

    total_raw = sum(e.get("duration", 0) for e in period_logs)
    total_effective = sum(e.get("effective_hours", e.get("duration", 0)) for e in period_logs)
    avg_raw = total_raw / len(period_logs) if period_logs else 0
    avg_effective = total_effective / len(period_logs) if period_logs else 0
    avg_quality = sum(e.get("quality", 3) for e in period_logs) / len(period_logs) if period_logs else 3
    period_debt = sum(optimal - e.get("effective_hours", e.get("duration", 0)) for e in period_logs)

    best = max(period_logs, key=lambda e: e.get("effective_hours", 0), default=None)
    worst = min(period_logs, key=lambda e: e.get("effective_hours", 0), default=None)

    print(f"📋 {period.capitalize()}ly Sleep Report ({len(period_logs)} days)")
    print(f"{'─' * 45}")
    print(f"   Average raw sleep:      {avg_raw:.1f}h")
    print(f"   Average effective sleep: {avg_effective:.1f}h")
    print(f"   Average quality:        {avg_quality:.1f}/5")
    print(f"   Total sleep debt:       {period_debt:+.1f}h")
    print(f"   Optimal:                {optimal:.1f}h/night")
    if best:
        print(f"   Best night:  {best['date']} — {best.get('effective_hours', 0):.1f}h effective")
    if worst:
        print(f"   Worst night: {worst['date']} — {worst.get('effective_hours', 0):.1f}h effective")

    # Substance impact
    caffeine_days = sum(1 for e in period_logs if e.get("caffeine"))
    alcohol_days = sum(1 for e in period_logs if e.get("alcohol"))
    if caffeine_days:
        print(f"   ☕ Caffeine noted on {caffeine_days} day{'s' if caffeine_days != 1 else ''}")
    if alcohol_days:
        print(f"   🍺 Alcohol noted on {alcohol_days} day{'s' if alcohol_days != 1 else ''}")

    # Quality correlation
    if caffeine_days > 0:
        caf_avg = sum(e.get("quality", 3) for e in period_logs if e.get("caffeine")) / caffeine_days
        no_caf_avg = sum(e.get("quality", 3) for e in period_logs if not e.get("caffeine")) / max(1, len(period_logs) - caffeine_days)
        print(f"   Quality with caffeine: {caf_avg:.1f} vs without: {no_caf_avg:.1f}")

    print(f"{'─' * 45}")

    # Mini ASCII bar chart
    print(f"\n   Daily effective sleep:")
    for entry in period_logs:
        eff = entry.get("effective_hours", entry.get("duration", 0))
        bar_len = int(eff * 2)  # 2 chars per hour
        marker = "✓" if eff >= optimal else "✗"
        bar = "█" * bar_len
        print(f"   {entry['date']} |{bar:<20s}| {eff:.1f}h {marker}")


def cmd_schedule(db, args):
    """Suggest optimal bedtime tonight to minimize debt."""
    logs = db.get("logs", [])
    age = db.get("profile", {}).get("age")
    optimal = get_optimal_for_age(age) if age else 8.0

    if logs:
        recent = logs[-14:]
        current_debt = sum(optimal - e.get("effective_hours", e.get("duration", 0)) for e in recent)
    else:
        current_debt = 0

    print(f"🌙 Tonight's Sleep Schedule Recommendation")
    print(f"{'─' * 50}")

    if current_debt > 0:
        recovery_sleep = optimal + (current_debt / 7)  # spread over a week
        recovery_sleep = min(recovery_sleep, 10.0)  # cap at 10h
        print(f"   Current debt: {current_debt:.1f}h")
        print(f"   Recommended tonight: {recovery_sleep:.1f}h")
        print(f"   (extra {recovery_sleep - optimal:.1f}h to chip away at debt)")
        target_hours = recovery_sleep
    else:
        print(f"   No significant debt — maintain your optimal of {optimal:.1f}h")
        target_hours = optimal

    # Suggest bedtime for common wake times
    print(f"\n   Suggested bedtimes for {target_hours:.1f}h sleep:")
    for wake_h, wake_m in [(6, 0), (6, 30), (7, 0), (7, 30), (8, 0)]:
        wake_minutes = wake_h * 60 + wake_m
        bed_minutes = wake_minutes - int(target_hours * 60) - 15  # 15min to fall asleep
        bed_minutes = bed_minutes % (24 * 60)
        bed_h = bed_minutes // 60
        bed_m = bed_minutes % 60
        print(f"     Wake {wake_h:02d}:{wake_m:02d} → Bed {bed_h:02d}:{bed_m:02d}")

    # Chronotype-aware suggestion
    if logs:
        avg_bed = _average_bedtime(logs[-14:])
        if avg_bed:
            print(f"\n   Your average bedtime: {avg_bed}")
            bed_h = parse_time(avg_bed.split("→")[0].strip()) if "→" in avg_bed else None

    print(f"\n   💡 Tips: Avoid screens 30min before bed, keep the room cool (~18°C)")


def _average_bedtime(logs):
    """Compute average bedtime from logs. Returns a string description."""
    if not logs:
        return None
    bedtimes = []
    for e in logs:
        bt = parse_time(e.get("bedtime", ""))
        if bt is not None:
            if bt < 6.0:  # after midnight
                bt += 24.0
            bedtimes.append(bt)
    if not bedtimes:
        return None
    avg = sum(bedtimes) / len(bedtimes)
    avg = avg % 24.0
    avg_h = int(avg)
    avg_m = int((avg - avg_h) * 60)
    return f"{avg_h:02d}:{avg_m:02d}"


def cmd_chronotype(db, args):
    """Detect chronotype from logged patterns."""
    logs = db.get("logs", [])
    if len(logs) < 3:
        print("Need at least 3 nights of data to detect chronotype.")
        return

    recent = logs[-14:]
    bedtimes_raw = [parse_time(e["bedtime"]) for e in recent if e.get("bedtime")]
    bedtimes_raw = [b for b in bedtimes_raw if b is not None]
    if not bedtimes_raw:
        print("No valid bedtime data found.")
        return

    # Handle midnight-crossing: times before 6:00 are actually late (24+h)
    bedtimes = []
    for b in bedtimes_raw:
        if b < 6.0:  # 00:00-05:59 is after midnight (late bedtime)
            bedtimes.append(b + 24.0)
        else:
            bedtimes.append(b)

    avg_bed = sum(bedtimes) / len(bedtimes)
    avg_bed_normalized = avg_bed % 24.0
    avg_bed_h = int(avg_bed_normalized)
    avg_bed_m = int((avg_bed_normalized - avg_bed_h) * 60)

    print(f"🦉 Chronotype Detection ({len(recent)} nights)")
    print(f"{'─' * 45}")
    print(f"   Average bedtime: {avg_bed_h:02d}:{avg_bed_m:02d}")

    # Use normalized average for chronotype classification
    if avg_bed_normalized < 22.0:
        chronotype = "Early Bird 🐦"
        desc = "You tend to go to bed early and likely function best in the morning."
    elif avg_bed_normalized < 23.5:
        chronotype = "Moderate / Balanced 🌤"
        desc = "Your bedtime pattern is moderate and flexible."
    elif avg_bed_normalized < 24.5:
        chronotype = "Night Owl 🦉"
        desc = "You naturally prefer later bedtimes. Consider adjusting gradually."
    else:
        chronotype = "Extreme Night Owl 🦉🦉"
        desc = "Very late bedtimes detected. This may conflict with typical schedules."

    print(f"   Detected: {chronotype}")
    print(f"   {desc}")

    # Consistency
    if len(bedtimes) > 1:
        variance = sum((b - avg_bed) ** 2 for b in bedtimes) / len(bedtimes)
        std = math.sqrt(variance)
        print(f"\n   Bedtime consistency: σ = {std:.1f}h")
        if std < 1.0:
            print(f"   Very consistent schedule! ✅")
        elif std < 2.0:
            print(f"   Moderately consistent.")
        else:
            print(f"   Irregular schedule — try to standardize your bedtime.")


def cmd_chart(db, args):
    """ASCII chart of sleep duration over time."""
    logs = db.get("logs", [])
    if not logs:
        print("No sleep data to chart. Log some sleep first.")
        return

    days = int(args[0]) if args else min(14, len(logs))
    chart_logs = logs[-days:]
    age = db.get("profile", {}).get("age")
    optimal = get_optimal_for_age(age) if age else 8.0

    print(f"\n  📉 Sleep Duration Chart — Last {len(chart_logs)} days")
    print(f"  Optimal: {optimal:.1f}h/night\n")

    chart_width = 40
    max_hours = 12.0

    # Build the chart
    for entry in chart_logs:
        eff = entry.get("effective_hours", entry.get("duration", 0))
        bar_len = int((eff / max_hours) * chart_width)
        optimal_pos = int((optimal / max_hours) * chart_width)

        bar = ""
        for i in range(chart_width):
            if i < bar_len:
                if i < optimal_pos:
                    bar += "░"  # below optimal
                else:
                    bar += "▓"  # above optimal
            elif i == optimal_pos:
                bar += "|"
            else:
                bar += " "

        marker = "✓" if eff >= optimal else "✗"
        date_short = entry["date"][5:]  # MM-DD
        print(f"  {date_short} │{bar}│ {eff:.1f}h {marker}")

    # Legend
    opt_pos = int((optimal / max_hours) * chart_width)
    legend_line = " " * 18
    for i in range(chart_width):
        if i == opt_pos:
            legend_line += "|"
        else:
            legend_line += " "
    print(f"  {'':>5}  {legend_line}")
    print(f"  Legend: ░ below optimal  ▓ above optimal  | = {optimal:.1f}h optimal")


# --- Main ---

COMMANDS = {
    "init": cmd_init,
    "log": cmd_log,
    "debt": cmd_debt,
    "recovery": cmd_recovery,
    "optimal": cmd_optimal,
    "streak": cmd_streak,
    "report": cmd_report,
    "schedule": cmd_schedule,
    "chronotype": cmd_chronotype,
    "chart": cmd_chart,
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print(__doc__)
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available commands: {', '.join(COMMANDS.keys())}")
        print("Use --help for usage.")
        return

    db = load_db()
    COMMANDS[cmd](db, args)


if __name__ == "__main__":
    main()
