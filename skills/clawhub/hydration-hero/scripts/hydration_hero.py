#!/usr/bin/env python3
"""
Hydration Hero — smart water intake tracking based on body weight, weather,
and activity level. Gamified streaks, dynamic targets, drinking schedules.
Pure Python stdlib. JSON file database.

Usage:
    python3 hydration_hero.py init
    python3 hydration_hero.py log <ml> [--oz]
    python3 hydration_hero.py status
    python3 hydration_hero.py target
    python3 hydration_hero.py activity --exercise <min> --intensity <level>
    python3 hydration_hero.py weather --temp <C> --humidity <percent>
    python3 hydration_hero.py caffeine --cups <N>
    python3 hydration_hero.py alcohol --drinks <N>
    python3 hydration_hero.py schedule
    python3 hydration_hero.py streak
    python3 hydration_hero.py report [week|month]
    python3 hydration_hero.py color-check
    python3 hydration_hero.py remind

Examples:
    python3 hydration_hero.py init
    python3 hydration_hero.py log 250
    python3 hydration_hero.py log 500
    python3 hydration_hero.py activity --exercise 30 --intensity moderate
    python3 hydration_hero.py status
    python3 hydration_hero.py schedule
"""

import json
import os
import sys
from datetime import datetime, date, timedelta

DB_PATH = os.path.expanduser("~/.hydration_hero.json")

# Exercise intensity additions (ml per 30 min)
EXERCISE_ML = {
    "light": 350,
    "moderate": 500,
    "high": 700,
    "intense": 700,
}

# Urine color chart
URINE_CHART = [
    (1, "Very pale / nearly clear", "🟢 Overhydrated", "Reduce intake slightly"),
    (2, "Pale yellow", "✅ Well hydrated", "Maintain current intake"),
    (3, "Light yellow", "✅ Well hydrated", "Good"),
    (4, "Yellow", "🟡 Adequately hydrated", "Drink a glass"),
    (5, "Dark yellow", "🟡 Mildly dehydrated", "Drink 2 glasses"),
    (6, "Amber / honey", "🔴 Dehydrated", "Drink immediately"),
    (7, "Brown / cola", "⚠️  Severely dehydrated", "Seek medical attention"),
    (8, "Pink / red (not food)", "⚠️  Possible blood", "See a doctor"),
]


# --- Database ---

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            return json.load(f)
    return {
        "profile": {},
        "daily": {},  # date -> {intake_ml, adjustments: [...], entries: [...]}
    }

def save_db(db):
    with open(DB_PATH, "w") as f:
        json.dump(db, f, indent=2, default=str)

def today_str():
    return date.today().isoformat()

def get_day(db, d=None):
    d = d or today_str()
    if d not in db["daily"]:
        db["daily"][d] = {
            "intake": 0,
            "adjustments": [],
            "entries": [],
        }
    return db["daily"][d]


# --- Target Calculation ---

def calculate_target(db):
    """Calculate personalized daily hydration target in ml."""
    profile = db.get("profile", {})
    weight = profile.get("weight_kg", 70)

    # Base formula: weight × 35ml
    base = weight * 35
    target = base

    # Today's adjustments
    day = db["daily"].get(today_str(), {})
    for adj in day.get("adjustments", []):
        target += adj.get("ml", 0)

    return int(target)


# --- Parsing ---

def parse_flags(args):
    positional = []
    flags = {}
    i = 0
    while i < len(args):
        if args[i].startswith("--"):
            key = args[i][2:]
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                flags[key] = args[i + 1]
                i += 2
            else:
                flags[key] = True
                i += 1
        else:
            positional.append(args[i])
            i += 1
    return positional, flags


# --- Commands ---

def cmd_init(db, args):
    print("💧 Hydration Hero — Setup")
    print()
    weight_input = input("Your weight in kg (or lbs): ").strip()
    if weight_input:
        try:
            weight = float(weight_input)
            if weight > 100:  # probably lbs
                weight = weight / 2.205
                print(f"   (Detected lbs → {weight:.1f} kg)")
            db["profile"]["weight_kg"] = weight
        except ValueError:
            pass
    activity = input("Daily activity level (sedentary/light/moderate/active): ").strip().lower()
    db["profile"]["activity_level"] = activity or "moderate"
    climate = input("Climate (cool/temperate/hot): ").strip().lower()
    db["profile"]["climate"] = climate or "temperate"
    wake = input("Wake time (HH:MM, e.g. 07:00): ").strip()
    db["profile"]["wake_time"] = wake or "07:00"
    sleep = input("Sleep time (HH:MM, e.g. 23:00): ").strip()
    db["profile"]["sleep_time"] = sleep or "23:00"
    db["profile"]["created"] = today_str()
    target = calculate_target(db)
    save_db(db)
    print()
    print(f"✓ Profile created!")
    print(f"   Weight: {db['profile'].get('weight_kg', 70):.1f} kg")
    print(f"   Daily hydration target: {target} ml ({target/1000:.1f}L)")
    print(f"\n   Start logging: python3 hydration_hero.py log 250")


def cmd_log(db, args):
    if not args:
        print("Usage: log <ml> [--oz]")
        return
    _, flags = parse_flags(args)
    try:
        amount = float(args[0])
    except ValueError:
        print(f"Error: amount must be a number")
        return
    if flags.get("oz"):
        amount = amount * 29.5735  # fl oz to ml

    amount = int(amount)
    day = get_day(db)
    day["intake"] += amount
    day["entries"].append({
        "time": datetime.now().strftime("%H:%M"),
        "amount": amount,
    })
    save_db(db)

    target = calculate_target(db)
    pct = day["intake"] / target * 100 if target else 0
    bar_len = min(int(pct / 5), 20)
    bar = "█" * bar_len + "░" * (20 - bar_len)
    print(f"💧 +{amount} ml logged at {datetime.now().strftime('%H:%M')}")
    print(f"   {day['intake']}/{target} ml ({pct:.0f}%)")
    print(f"   |{bar}|")
    remaining = target - day["intake"]
    if remaining > 0:
        print(f"   {remaining} ml to go — about {remaining/250:.0f} more glasses")
    else:
        print(f"   🎉 Goal achieved! {abs(remaining)} ml over target")


def cmd_status(db, args):
    day = get_day(db)
    target = calculate_target(db)
    intake = day.get("intake", 0)
    pct = intake / target * 100 if target else 0
    remaining = target - intake
    print(f"💧 Hydration Status — {today_str()}")
    print(f"{'═' * 50}")
    bar_len = min(int(pct / 5), 20)
    bar = "█" * bar_len + "░" * (20 - bar_len)
    print(f"   Intake: {intake} ml / {target} ml ({pct:.0f}%)")
    print(f"   |{bar}|")
    if remaining > 0:
        glasses = remaining / 250
        print(f"   Need: {remaining} ml more ({glasses:.0f} × 250ml glasses)")
    else:
        print(f"   🎉 Goal achieved! You're {abs(remaining)} ml over.")
    print()
    # Today's entries
    entries = day.get("entries", [])
    if entries:
        print(f"   Today's intake log:")
        for e in entries[-8:]:  # show last 8
            print(f"      {e['time']}  +{e['amount']} ml")
        if len(entries) > 8:
            print(f"      ... and {len(entries) - 8} more")
    # Adjustments
    adjustments = day.get("adjustments", [])
    if adjustments:
        print(f"\n   Today's adjustments:")
        total_adj = sum(a.get("ml", 0) for a in adjustments)
        print(f"      Base target: {target - total_adj} ml")
        for a in adjustments:
            print(f"      {a['icon']} {a['reason']}: {'+' if a['ml'] >= 0 else ''}{a['ml']} ml")
        print(f"      Adjusted target: {target} ml")
    print(f"\n{'═' * 50}")


def cmd_target(db, args):
    target = calculate_target(db)
    weight = db.get("profile", {}).get("weight_kg", 70)
    base = int(weight * 35)
    print(f"🎯 Daily Hydration Target")
    print(f"{'═' * 50}")
    print(f"   Base formula: {weight:.1f} kg × 35 ml = {base} ml")
    day = db["daily"].get(today_str(), {})
    adjustments = day.get("adjustments", [])
    if adjustments:
        for a in adjustments:
            sign = "+" if a["ml"] >= 0 else ""
            print(f"   {a['icon']} {a['reason']}: {sign}{a['ml']} ml")
        print(f"   {'─' * 45}")
    print(f"   Total target: {target} ml ({target/1000:.1f}L)")
    print(f"   ≈ {target/250:.0f} glasses (250ml) or {target/500:.0f} bottles (500ml)")
    print(f"\n{'═' * 50}")


def cmd_activity(db, args):
    _, flags = parse_flags(args)
    exercise_str = flags.get("exercise", "30")
    intensity = flags.get("intensity", "moderate").lower()
    try:
        minutes = int(exercise_str)
    except ValueError:
        print("Error: --exercise must be a number (minutes)")
        return
    if intensity not in EXERCISE_ML:
        print(f"Error: intensity must be one of: {', '.join(EXERCISE_ML.keys())}")
        return
    # Calculate addition: (minutes / 30) × base_per_30min
    ml = int((minutes / 30) * EXERCISE_ML[intensity])
    day = get_day(db)
    day["adjustments"].append({
        "type": "exercise",
        "ml": ml,
        "reason": f"Exercise: {minutes} min {intensity}",
        "icon": "🏃",
    })
    save_db(db)
    new_target = calculate_target(db)
    print(f"🏃 Exercise logged: {minutes} min {intensity}")
    print(f"   +{ml} ml added to today's target")
    print(f"   New target: {new_target} ml")


def cmd_weather(db, args):
    _, flags = parse_flags(args)
    temp_str = flags.get("temp", "20")
    humidity_str = flags.get("humidity", "50")
    try:
        temp = float(temp_str)
        humidity = float(humidity_str)
    except ValueError:
        print("Error: --temp and --humidity must be numbers")
        return
    day = get_day(db)
    # Heat adjustment: +500ml per 5°C above 20°C
    heat_ml = 0
    if temp > 20:
        heat_ml = int(((temp - 20) / 5) * 500)
        if heat_ml > 0:
            day["adjustments"].append({
                "type": "heat",
                "ml": heat_ml,
                "reason": f"Hot weather: {temp:.0f}°C",
                "icon": "🌡️",
            })
    # Humidity adjustment: +300ml if >70%
    hum_ml = 0
    if humidity > 70:
        hum_ml = 300
        day["adjustments"].append({
            "type": "humidity",
            "ml": hum_ml,
            "reason": f"High humidity: {humidity:.0f}%",
            "icon": "💦",
        })
    total = heat_ml + hum_ml
    save_db(db)
    new_target = calculate_target(db)
    print(f"🌡️ Weather logged: {temp:.0f}°C, {humidity:.0f}% humidity")
    if total > 0:
        print(f"   +{total} ml added to today's target")
    else:
        print(f"   No adjustment needed for this weather")
    print(f"   New target: {new_target} ml")


def cmd_caffeine(db, args):
    _, flags = parse_flags(args)
    cups_str = flags.get("cups", "1")
    try:
        cups = int(cups_str)
    except ValueError:
        print("Error: --cups must be a number")
        return
    ml = cups * 150
    day = get_day(db)
    day["adjustments"].append({
        "type": "caffeine",
        "ml": ml,
        "reason": f"Caffeine: {cups} cup{'s' if cups != 1 else ''}",
        "icon": "☕",
    })
    save_db(db)
    new_target = calculate_target(db)
    print(f"☕ Caffeine logged: {cups} cup{'s' if cups != 1 else ''}")
    print(f"   +{ml} ml compensatory water added")
    print(f"   New target: {new_target} ml")
    print(f"   💡 Drink an extra glass of water per cup of coffee")


def cmd_alcohol(db, args):
    _, flags = parse_flags(args)
    drinks_str = flags.get("drinks", "1")
    try:
        drinks = int(drinks_str)
    except ValueError:
        print("Error: --drinks must be a number")
        return
    ml = drinks * 400
    day = get_day(db)
    day["adjustments"].append({
        "type": "alcohol",
        "ml": ml,
        "reason": f"Alcohol: {drinks} drink{'s' if drinks != 1 else ''}",
        "icon": "🍺",
    })
    save_db(db)
    new_target = calculate_target(db)
    print(f"🍺 Alcohol logged: {drinks} drink{'s' if drinks != 1 else ''}")
    print(f"   +{ml} ml recovery water added")
    print(f"   New target: {new_target} ml")
    print(f"   💡 Drink 1 glass of water per alcoholic drink + 500ml before bed")


def cmd_schedule(db, args):
    target = calculate_target(db)
    profile = db.get("profile", {})
    wake = profile.get("wake_time", "07:00")
    sleep = profile.get("sleep_time", "23:00")
    # Parse times
    try:
        wake_h, wake_m = map(int, wake.split(":"))
        sleep_h, sleep_m = map(int, sleep.split(":"))
    except (ValueError, AttributeError):
        wake_h, wake_m = 7, 0
        sleep_h, sleep_m = 23, 0
    wake_total = wake_h * 60 + wake_m
    sleep_total = sleep_h * 60 + sleep_m
    if sleep_total <= wake_total:
        sleep_total += 24 * 60  # next day
    awake_min = sleep_total - wake_total
    # Schedule: drink every 90 minutes, front-loaded
    num_drinks = max(8, awake_min // 90)
    per_drink = target // num_drinks
    remainder = target % num_drinks
    # Front-load: morning drink is larger
    schedule = []
    for i in range(num_drinks):
        amount = per_drink + (remainder if i == 0 else 0)
        if i == 0:
            amount = int(amount * 1.5)  # morning drink 50% larger
        elif i == num_drinks - 1:
            amount = int(amount * 0.6)  # last drink smaller
        drink_time = wake_total + i * (awake_min // num_drinks)
        dh, dm = divmod(drink_time, 60)
        dh = dh % 24
        schedule.append((dh, dm, amount))
    # Normalize
    total = sum(s[2] for s in schedule)
    scale = target / total if total else 1
    schedule = [(h, m, int(a * scale)) for h, m, a in schedule]
    print(f"📅 Hydration Schedule ({target} ml target)")
    print(f"{'═' * 55}")
    cumulative = 0
    for i, (h, m, amount) in enumerate(schedule):
        cumulative += amount
        pct = cumulative / target * 100
        labels = {
            0: "🌅 Wake up drink (most important!)",
            1: "🥣 Breakfast",
        }
        if i == len(schedule) - 1:
            labels[i] = "🌙 Evening (limit after this)"
        label = labels.get(i, f"💧 Drink #{i+1}")
        print(f"   {h:02d}:{m:02d}  {label}")
        print(f"          {amount} ml  (cumulative: {cumulative}/{target} ml, {pct:.0f}%)")
    print(f"\n{'═' * 55}")
    print(f"   💡 Tips:")
    print(f"      • Keep a bottle visible at your desk")
    print(f"      • Set phone reminders for each time slot")
    print(f"      • Morning drink is largest — you wake up dehydrated")


def cmd_streak(db, args):
    daily = db.get("daily", {})
    today = date.today()
    streak = 0
    for i in range(365):
        d = (today - timedelta(days=i)).isoformat()
        day = daily.get(d)
        if day and day.get("intake", 0) > 0:
            # Check if they hit at least 80% of target
            target = sum([db.get("profile", {}).get("weight_kg", 70) * 35] +
                        [a.get("ml", 0) for a in day.get("adjustments", [])])
            if target > 0 and day["intake"] / target >= 0.8:
                streak += 1
            elif i == 0:
                # Today might not be done yet
                continue
            else:
                break
        elif i == 0:
            continue
        else:
            break
    # Total goal-hit days
    total_days = 0
    for d, day in daily.items():
        target = sum([db.get("profile", {}).get("weight_kg", 70) * 35] +
                    [a.get("ml", 0) for a in day.get("adjustments", [])])
        if target > 0 and day.get("intake", 0) / target >= 0.8:
            total_days += 1
    print(f"🔥 Hydration Streak: {streak} day{'s' if streak != 1 else ''}")
    print(f"   Total goal-hit days: {total_days}")
    if streak >= 7:
        print(f"   🎉 A full week! Amazing consistency!")
    elif streak >= 3:
        print(f"   Keep it up!")
    elif streak == 0:
        print(f"   Log water and hit your goal to start a streak!")
    # Weekly achievement
    week_hit = 0
    for i in range(7):
        d = (today - timedelta(days=i)).isoformat()
        day = daily.get(d)
        if day:
            target = sum([db.get("profile", {}).get("weight_kg", 70) * 35] +
                        [a.get("ml", 0) for a in day.get("adjustments", [])])
            if target > 0 and day.get("intake", 0) / target >= 0.8:
                week_hit += 1
    if week_hit >= 7:
        print(f"   🏆 This week: GOLD (7/7 days)")
    elif week_hit >= 6:
        print(f"   🥈 This week: SILVER ({week_hit}/7 days)")
    elif week_hit >= 5:
        print(f"   🥉 This week: BRONZE ({week_hit}/7 days)")
    else:
        print(f"   This week: {week_hit}/7 days — aim for 5+ for Bronze")


def cmd_report(db, args):
    period = args[0] if args else "week"
    days = 7 if period == "week" else 30
    today = date.today()
    base_target = db.get("profile", {}).get("weight_kg", 70) * 35
    print(f"📊 {period.capitalize()}ly Hydration Report")
    print(f"{'═' * 55}")
    total_intake = 0
    total_target = 0
    goal_hits = 0
    active_days = 0
    for i in range(days):
        d = (today - timedelta(days=i)).isoformat()
        day = db.get("daily", {}).get(d)
        if not day or day.get("intake", 0) == 0:
            continue
        active_days += 1
        intake = day.get("intake", 0)
        day_target = base_target + sum(a.get("ml", 0) for a in day.get("adjustments", []))
        total_intake += intake
        total_target += day_target
        if day_target > 0 and intake / day_target >= 0.8:
            goal_hits += 1
    avg_intake = total_intake / active_days if active_days else 0
    avg_target = total_target / active_days if active_days else base_target
    consistency = goal_hits / days * 100
    print(f"\n   Active days: {active_days}/{days}")
    print(f"   Goal-hit days: {goal_hits}/{days} ({consistency:.0f}%)")
    print(f"   Average intake: {avg_intake:.0f} ml/day")
    print(f"   Average target: {avg_target:.0f} ml/day")
    print(f"   Average achievement: {(avg_intake/avg_target*100 if avg_target else 0):.0f}%")
    # Daily chart
    print(f"\n   Daily intake chart:")
    for i in range(days - 1, -1, -1):
        d = (today - timedelta(days=i)).isoformat()
        day = db.get("daily", {}).get(d)
        intake = day.get("intake", 0) if day else 0
        day_target = base_target + sum(a.get("ml", 0) for a in (day.get("adjustments", []) if day else []))
        pct = intake / day_target * 100 if day_target else 0
        bar_len = min(int(pct / 5), 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        mark = "✅" if pct >= 80 else ("🟡" if pct >= 50 else "🔴") if intake > 0 else "⬜"
        print(f"   {d} {mark} |{bar}| {intake:4d}/{day_target:4d} ml")
    # Recommendations
    print(f"\n{'═' * 55}")
    print(f"   📝 Recommendations:")
    if consistency >= 80:
        print(f"      • Excellent! You're consistently hitting your hydration goal")
    elif consistency >= 50:
        print(f"      • Good progress — aim for more consistent daily intake")
    else:
        print(f"      • Focus on hitting your daily target")
        print(f"      • Set up a drinking schedule (run 'schedule')")
        print(f"      • Keep a water bottle visible at all times")
    if avg_intake < avg_target * 0.7:
        print(f"      • Your intake is significantly below target — increase per-drink amount")
    print(f"\n{'═' * 55}")


def cmd_color_check(db, args):
    print(f"🚽 Urine Color Self-Assessment Chart")
    print(f"{'═' * 60}")
    print(f"\n   Compare your urine color to this chart:\n")
    for level, color, status, action in URINE_CHART:
        print(f"   Level {level}: {color}")
        print(f"     {status} — {action}")
        print()
    print(f"{'═' * 60}")
    print(f"   Note: Some foods and medications change urine color")
    print(f"   (beets → red, B vitamins → neon yellow, asparagus → green)")
    print(f"   If color change persists without dietary cause, consult a doctor.")


def cmd_remind(db, args):
    day = get_day(db)
    target = calculate_target(db)
    intake = day.get("intake", 0)
    remaining = target - intake
    if remaining <= 0:
        print(f"🎉 You've already hit your target today! Great job!")
        return
    # Calculate time-based pace
    profile = db.get("profile", {})
    try:
        wake_h, wake_m = map(int, profile.get("wake_time", "07:00").split(":"))
    except (ValueError, AttributeError):
        wake_h, wake_m = 7, 0
    now = datetime.now()
    now_total = now.hour * 60 + now.minute
    wake_total = wake_h * 60 + wake_m
    hours_awake = (now_total - wake_total) / 60
    if hours_awake <= 0:
        print(f"💧 Next drink: Now! Start your day with a glass of water.")
        return
    expected_by_now = target * (hours_awake / 16)  # assume 16 waking hours
    pace_diff = intake - expected_by_now
    next_amount = min(remaining, 300)  # don't recommend more than 300ml at once
    if pace_diff < 0:
        print(f"⏰ You're behind pace by {abs(int(pace_diff))} ml")
        print(f"   Drank: {intake} ml | Expected by now: {int(expected_by_now)} ml")
        print(f"   💧 Drink {next_amount} ml now to catch up!")
    else:
        print(f"✅ You're on pace! {intake} ml so far ({pace_diff:+.0f} ml ahead)")
        print(f"   Next drink: ~{next_amount} ml in the next 30-60 min")
    entries = day.get("entries", [])
    if entries:
        last_time = entries[-1]["time"]
        print(f"   Last drink: {last_time} ({entries[-1]['amount']} ml)")


# --- Main ---

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    command = sys.argv[1]
    args = sys.argv[2:]
    db = load_db()
    commands = {
        "init": cmd_init,
        "log": cmd_log,
        "status": cmd_status,
        "target": cmd_target,
        "activity": cmd_activity,
        "weather": cmd_weather,
        "caffeine": cmd_caffeine,
        "alcohol": cmd_alcohol,
        "schedule": cmd_schedule,
        "streak": cmd_streak,
        "report": cmd_report,
        "color-check": cmd_color_check,
        "remind": cmd_remind,
    }
    if command not in commands:
        print(f"Unknown command: {command}")
        print(f"Available: {', '.join(commands.keys())}")
        return
    commands[command](db, args)


if __name__ == "__main__":
    main()
