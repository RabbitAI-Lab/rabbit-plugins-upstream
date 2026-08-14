#!/usr/bin/env python3
"""
Posture Patrol — track posture quality, schedule breaks, estimate spinal load,
and build better posture habits.
Pure Python stdlib. JSON file database.

Usage:
    python3 posture_patrol.py init
    python3 posture_patrol.py check <good|fair|poor> [notes]
    python3 posture_patrol.py score [today|week]
    python3 posture_patrol.py report [week|month]
    python3 posture_patrol.py streak
    python3 posture_patrol.py breaks [--interval N]
    python3 posture_patrol.py stretch
    python3 posture_patrol.py spinal-load
    python3 posture_patrol.py ergonomics
    python3 posture_patrol.py pattern
    python3 posture_patrol.py goal [minutes]

Examples:
    python3 posture_patrol.py init
    python3 posture_patrol.py check good "feet flat, back straight"
    python3 posture_patrol.py check poor "slouching over laptop"
    python3 posture_patrol.py score
    python3 posture_patrol.py stretch
    python3 posture_patrol.py report week
"""

import json
import os
import sys
import math
from datetime import datetime, date, timedelta

DB_PATH = os.path.expanduser("~/.posture_patrol.json")

# Posture quality ratings
QUALITY_SCORES = {"good": 3, "fair": 2, "poor": 1}
QUALITY_LABELS = {3: "Good", 2: "Fair", 1: "Poor"}
QUALITY_ICONS = {"good": "✅", "fair": "🟡", "poor": "🔴"}

# Spinal load model: effective head weight at different forward angles
# Based on Hansraj (2014), Surgical Technology International
SPINAL_LOAD = [
    (0, 10),     # neutral: 10-12 lbs
    (15, 27),    # slight forward
    (30, 40),    # moderate forward
    (45, 49),    # significant forward
    (60, 60),    # severe forward
]

# Estimated forward tilt angle by posture quality
POSTURE_TILT = {"good": 5, "fair": 25, "poor": 45}

# Desk stretches targeting specific problems
STRETCHES = {
    "neck": [
        ("Chin Tucks", "Sit straight. Pull head straight back (don't tilt). Hold 5 sec. × 10", "Forward head posture"),
        ("Neck Rolls", "Slowly roll head in a circle. 5 each direction.", "General neck tension"),
        ("Upper Trap Stretch", "Tilt head to one side, hand gently pulls. Hold 20 sec. each side.", "Shoulder tension"),
    ],
    "shoulders": [
        ("Shoulder Blade Squeeze", "Pinch shoulder blades together. Hold 5 sec. × 10", "Rounded shoulders"),
        ("Doorway Stretch", "Forearms on doorframe. Step forward. Hold 30 sec.", "Tight chest muscles"),
        ("Shoulder Shrugs", "Raise shoulders to ears, hold 3 sec, drop. × 10", "Upper back tension"),
    ],
    "back": [
        ("Cat-Cow", "On hands and knees: arch then round back. × 10", "Spinal mobility"),
        ("Seated Spinal Twist", "Sit tall, twist torso. Hold 15 sec. each side.", "Lower back stiffness"),
        ("Child's Pose", "Kneel, fold forward, arms extended. Hold 30 sec.", "Lower back pain"),
    ],
    "hips": [
        ("Hip Flexor Stretch", "Lunge position, push hips forward. 30 sec each side.", "Tight from sitting"),
        ("Figure-4 Stretch", "Cross ankle over knee, lean forward. 30 sec each side.", "Piriformis/glutes"),
        ("Standing Quad Stretch", "Pull heel to glute. Hold 20 sec each side.", "Tight quadriceps"),
    ],
}


# --- Database ---

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            return json.load(f)
    return {"profile": {}, "checks": [], "daily_goal": 480}  # 8 hours in minutes

def save_db(db):
    with open(DB_PATH, "w") as f:
        json.dump(db, f, indent=2, default=str)

def today_str():
    return date.today().isoformat()


# --- Spinal Load Estimation ---

def tilt_to_load(angle_deg):
    """Interpolate spinal load from head tilt angle."""
    if angle_deg <= SPINAL_LOAD[0][0]:
        return SPINAL_LOAD[0][1]
    if angle_deg >= SPINAL_LOAD[-1][0]:
        return SPINAL_LOAD[-1][1]
    for i in range(len(SPINAL_LOAD) - 1):
        a1, l1 = SPINAL_LOAD[i]
        a2, l2 = SPINAL_LOAD[i + 1]
        if a1 <= angle_deg <= a2:
            # Linear interpolation
            t = (angle_deg - a1) / (a2 - a1)
            return l1 + t * (l2 - l1)
    return 12


# --- Commands ---

def cmd_init(db, args):
    print("🧍 Posture Patrol — Setup")
    print()
    height = input("Your height in cm (or 'skip'): ").strip()
    if height and height != "skip":
        try:
            db["profile"]["height_cm"] = int(height)
        except ValueError:
            pass
    desk_type = input("Desk type (sitting/standing/both): ").strip().lower()
    db["profile"]["desk_type"] = desk_type or "sitting"
    work_hours = input("Hours at desk per day (e.g. 8): ").strip()
    if work_hours:
        try:
            db["profile"]["work_hours"] = float(work_hours)
            db["daily_goal"] = int(float(work_hours) * 60 * 0.6)  # 60% good posture
        except ValueError:
            pass
    db["profile"]["created"] = today_str()
    save_db(db)
    print()
    print(f"✓ Profile created!")
    print(f"   Desk type: {db['profile'].get('desk_type', 'sitting')}")
    print(f"   Daily goal: {db.get('daily_goal', 480)} min of good posture")
    print(f"\n   Start logging: posture_patrol.py check good 'starting the day right'")


def cmd_check(db, args):
    if len(args) < 1:
        print("Usage: check <good|fair|poor> [notes]")
        return
    quality = args[0].lower()
    if quality not in QUALITY_SCORES:
        print(f"Error: quality must be 'good', 'fair', or 'poor'")
        return
    notes = " ".join(args[1:]) if len(args) > 1 else ""

    entry = {
        "time": datetime.now().strftime("%H:%M"),
        "date": today_str(),
        "quality": quality,
        "score": QUALITY_SCORES[quality],
        "notes": notes,
    }
    db["checks"].append(entry)
    save_db(db)

    icon = QUALITY_ICONS[quality]
    tilt = POSTURE_TILT[quality]
    load = tilt_to_load(tilt)
    print(f"{icon} Logged: {quality.upper()} posture")
    print(f"   Estimated head tilt: ~{tilt}°")
    print(f"   Spinal load: ~{load:.0f} lbs on neck")
    if quality == "poor":
        excess = load - 12
        print(f"   ⚠ {excess:.0f} lbs excess load vs neutral (10-12 lbs)")
        print(f"   💡 Tip: Raise your screen, do a chin tuck")


def cmd_score(db, args):
    period = args[0] if args else "today"
    if period == "today":
        checks = [c for c in db["checks"] if c["date"] == today_str()]
    else:
        # last 7 days
        cutoff = (date.today() - timedelta(days=7)).isoformat()
        checks = [c for c in db["checks"] if c["date"] >= cutoff]

    if not checks:
        print("No posture checks logged yet.")
        return

    avg_score = sum(c["score"] for c in checks) / len(checks)
    daily_score = avg_score / 3 * 100  # scale to 0-100

    good = sum(1 for c in checks if c["quality"] == "good")
    fair = sum(1 for c in checks if c["quality"] == "fair")
    poor = sum(1 for c in checks if c["quality"] == "poor")

    print(f"📊 Posture Score ({period})")
    print(f"{'─' * 45}")
    print(f"   Score: {daily_score:.0f}/100")
    grade = "A" if daily_score >= 85 else ("B" if daily_score >= 70 else ("C" if daily_score >= 50 else "D"))
    print(f"   Grade: {grade}")
    print(f"   {'─' * 40}")
    print(f"   ✅ Good: {good}  🟡 Fair: {fair}  🔴 Poor: {poor}")
    print(f"   Total checks: {len(checks)}")
    print()

    # Spinal load estimate
    total_load = 0
    neutral_load = 0
    for c in checks:
        tilt = POSTURE_TILT.get(c["quality"], 15)
        load = tilt_to_load(tilt)
        total_load += load
        neutral_load += 12
    excess = total_load - neutral_load
    print(f"   🦴 Cumulative spinal load: {total_load:.0f} lbs")
    print(f"      (vs {neutral_load:.0f} lbs if always neutral)")
    if excess > 0:
        print(f"      Excess load: {excess:.0f} lbs from poor posture")


def cmd_streak(db, args):
    checks = db.get("checks", [])
    if not checks:
        print("No checks logged yet.")
        return
    # Group by date
    by_date = {}
    for c in checks:
        by_date.setdefault(c["date"], []).append(c)
    # Calculate good-posture day streak (days where avg score >= 2.5)
    dates_sorted = sorted(by_date.keys(), reverse=True)
    streak = 0
    for d in dates_sorted:
        day_checks = by_date[d]
        avg = sum(c["score"] for c in day_checks) / len(day_checks)
        if avg >= 2.5:
            streak += 1
        else:
            break
    total_good_days = sum(1 for d in dates_sorted
                         if sum(c["score"] for c in by_date[d]) / len(by_date[d]) >= 2.5)
    print(f"🔥 Good Posture Streak: {streak} day{'s' if streak != 1 else ''}")
    print(f"   Total good-posture days: {total_good_days}")
    if streak >= 7:
        print(f"   🎉 Amazing! A full week of great posture!")
    elif streak >= 3:
        print(f"   Keep it up!")
    elif streak == 0:
        print(f"   Log more 'good' checks to start a streak!")


def cmd_breaks(db, args):
    interval = 30  # default
    for i, a in enumerate(args):
        if a == "--interval" and i + 1 < len(args):
            try:
                interval = int(args[i + 1])
            except ValueError:
                pass
    work_hours = db.get("profile", {}).get("work_hours", 8)
    total_min = int(work_hours * 60)
    num_breaks = total_min // interval

    print(f"⏰ Break Schedule (every {interval} min)")
    print(f"{'─' * 50}")
    print(f"   Work day: {work_hours:.0f} hours = {total_min} min")
    print(f"   Break interval: every {interval} min")
    print(f"   Total breaks: {num_breaks}")
    print()

    # Assume work starts at 9:00
    start_hour, start_min = 9, 0
    for i in range(num_breaks):
        break_total_min = start_hour * 60 + start_min + (i + 1) * interval
        bh, bm = divmod(break_total_min, 60)
        bh = bh % 24  # wrap past midnight
        activities = [
            "Stand up and walk for 1 min",
            "3 shoulder blade squeezes",
            "5 chin tucks",
            "Look 20ft away for 20 sec",
            "Doorway chest stretch",
            "Hip flexor stretch",
            "Full standing break (2 min walk)",
        ]
        activity = activities[i % len(activities)]
        print(f"   {bh:02d}:{bm:02d} — Break #{i+1}: {activity}")
    print(f"\n{'─' * 50}")
    print(f"   💡 Set a phone timer or use a posture reminder app")


def cmd_stretch(db, args):
    # Determine problem areas from recent checks
    checks = [c for c in db["checks"] if c["date"] >= (date.today() - timedelta(days=7)).isoformat()]
    poor_count = sum(1 for c in checks if c["quality"] == "poor")

    print(f"🤸 Desk Stretches")
    print(f"{'═' * 55}")

    if poor_count > 3 or not checks:
        # Recommend full set
        print(f"\n   Based on your recent posture, focus on:\n")
        for area, stretches in STRETCHES.items():
            print(f"   📍 {area.upper()}:")
            for name, desc, target in stretches[:2]:
                print(f"      • {name}: {desc}")
                print(f"        → Targets: {target}")
            print()
    else:
        # Targeted based on patterns
        notes_lower = " ".join(c.get("notes", "").lower() for c in checks)
        if any(w in notes_lower for w in ["neck", "head", "forward"]):
            print(f"\n   📍 NECK (forward head posture detected):\n")
            for name, desc, target in STRETCHES["neck"]:
                print(f"      • {name}: {desc}")
        if any(w in notes_lower for w in ["shoulder", "round", "chest"]):
            print(f"\n   📍 SHOULDERS (rounded shoulders detected):\n")
            for name, desc, target in STRETCHES["shoulders"]:
                print(f"      • {name}: {desc}")
        if any(w in notes_lower for w in ["back", "lower", "lumbar"]):
            print(f"\n   📍 BACK:\n")
            for name, desc, target in STRETCHES["back"]:
                print(f"      • {name}: {desc}")
        if any(w in notes_lower for w in ["hip", "leg", "sit"]):
            print(f"\n   📍 HIPS (prolonged sitting):\n")
            for name, desc, target in STRETCHES["hips"]:
                print(f"      • {name}: {desc}")

    print(f"\n{'═' * 55}")
    print(f"   💡 Hold each stretch for 20-30 seconds. Don't bounce.")
    print(f"   Do these 2-3 times during your work day.")


def cmd_spinal_load(db, args):
    checks = [c for c in db["checks"] if c["date"] >= (date.today() - timedelta(days=7)).isoformat()]
    if not checks:
        print("No checks logged. Log some checks first.")
        return
    print(f"🦴 Spinal Load Analysis (Last 7 Days)")
    print(f"{'═' * 55}")
    total_load = 0
    neutral_load = 0
    by_quality = {"good": 0, "fair": 0, "poor": 0}
    for c in checks:
        tilt = POSTURE_TILT.get(c["quality"], 15)
        load = tilt_to_load(tilt)
        total_load += load
        neutral_load += 12
        by_quality[c["quality"]] += load
    excess = total_load - neutral_load
    print(f"\n   Total checks: {len(checks)}")
    print(f"   Average load per check: {total_load/len(checks):.1f} lbs")
    print(f"   Neutral baseline: 12 lbs per check")
    print(f"\n   Load by posture quality:")
    for q in ["good", "fair", "poor"]:
        count = sum(1 for c in checks if c["quality"] == q)
        if count:
            avg = by_quality[q] / count
            print(f"      {QUALITY_ICONS[q]} {q:6s}: avg {avg:.1f} lbs ({count} checks)")
    print(f"\n   Total cumulative load: {total_load:.0f} lbs")
    print(f"   Excess from poor posture: {excess:.0f} lbs")
    if excess > 100:
        print(f"\n   ⚠ Significant excess load — prioritize posture improvement!")
    elif excess > 50:
        print(f"\n   ⚡ Moderate excess — room for improvement")
    else:
        print(f"\n   ✅ Low excess — good posture habits!")
    print(f"\n{'═' * 55}")


def cmd_ergonomics(db, args):
    desk_type = db.get("profile", {}).get("desk_type", "sitting")
    print(f"🪑 Ergonomic Checklist ({desk_type} desk)")
    print(f"{'═' * 55}")
    checklist = [
        ("Chair height", "Feet flat, knees at ~90°"),
        ("Lumbar support", "Lower back curve supported"),
        ("Monitor height", "Top of screen at eye level"),
        ("Monitor distance", "Arm's length (20-26 inches)"),
        ("Keyboard height", "Elbows at 90°, forearms parallel"),
        ("Wrists", "Neutral, not bent"),
        ("Shoulders", "Relaxed, not raised or rounded"),
        ("Head", "Ears over shoulders (neutral)"),
        ("Lighting", "No glare, brightness matches room"),
        ("Feet", "Flat on floor or footrest"),
    ]
    print()
    for i, (item, desc) in enumerate(checklist, 1):
        print(f"   [ ] {i}. {item}")
        print(f"       {desc}")
    print()
    if desk_type in ("standing", "both"):
        print(f"   Standing-specific:")
        print(f"   [ ] Desk at elbow height")
        print(f"   [ ] Anti-fatigue mat")
        print(f"   [ ] Weight on both feet, knees slightly bent")
        print(f"   [ ] Alternate sit/stand every 30 min")
    print(f"\n{'═' * 55}")
    print(f"   💡 Run this checklist every morning setup.")
    print(f"   Fix any items you can't check off.")


def cmd_pattern(db, args):
    checks = db.get("checks", [])
    if len(checks) < 5:
        print("Need at least 5 checks to detect patterns. Keep logging!")
        return
    print(f"🕐 Posture Pattern Analysis")
    print(f"{'═' * 55}")
    # Group by hour
    by_hour = {}
    for c in checks:
        try:
            hour = int(c["time"][:2])
        except (ValueError, IndexError):
            continue
        by_hour.setdefault(hour, []).append(c["score"])
    print(f"\n   Average score by hour of day:")
    worst_hour = None
    worst_score = 3.0
    best_hour = None
    best_score = 0.0
    for hour in sorted(by_hour.keys()):
        scores = by_hour[hour]
        avg = sum(scores) / len(scores)
        if avg < worst_score:
            worst_score = avg
            worst_hour = hour
        if avg > best_score:
            best_score = avg
            best_hour = hour
        bar_len = int(avg * 10)
        bar = "█" * bar_len + "░" * (30 - bar_len)
        print(f"   {hour:02d}:00 |{bar}| {avg:.1f} ({len(scores)} checks)")

    print(f"\n{'─' * 55}")
    if worst_hour is not None and worst_score < 2.0:
        print(f"   ⚠ High-risk hour: {worst_hour:02d}:00 (avg score {worst_score:.1f})")
        print(f"     Set a posture alarm for this time!")
    if best_hour is not None:
        print(f"   ✅ Best posture hour: {best_hour:02d}:00 (avg {best_score:.1f})")

    # Check post-lunch pattern
    lunch_checks = [c for c in checks if 13 <= int(c.get("time", "00")[:2] or 0) <= 15]
    if lunch_checks:
        lunch_avg = sum(c["score"] for c in lunch_checks) / len(lunch_checks)
        if lunch_avg < 2.0:
            print(f"   🍔 Post-lunch dip detected (avg {lunch_avg:.1f} during 13:00-15:00)")
            print(f"      Consider a walk after lunch to reset posture.")
    print(f"\n{'═' * 55}")


def cmd_report(db, args):
    period = args[0] if args else "week"
    days = 7 if period == "week" else 30
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    checks = [c for c in db["checks"] if c["date"] >= cutoff]
    if not checks:
        print(f"No posture checks in the last {days} days.")
        return

    avg = sum(c["score"] for c in checks) / len(checks)
    score = avg / 3 * 100
    good = sum(1 for c in checks if c["quality"] == "good")
    fair = sum(1 for c in checks if c["quality"] == "fair")
    poor = sum(1 for c in checks if c["quality"] == "poor")

    print(f"📋 {period.capitalize()}ly Posture Report ({len(checks)} checks)")
    print(f"{'═' * 55}")
    print(f"\n   Overall score: {score:.0f}/100")
    grade = "A" if score >= 85 else ("B" if score >= 70 else ("C" if score >= 50 else "D"))
    print(f"   Grade: {grade}")
    print(f"\n   Breakdown:")
    print(f"      ✅ Good: {good} ({good/len(checks)*100:.0f}%)")
    print(f"      🟡 Fair: {fair} ({fair/len(checks)*100:.0f}%)")
    print(f"      🔴 Poor: {poor} ({poor/len(checks)*100:.0f}%)")

    # Daily chart
    by_date = {}
    for c in checks:
        by_date.setdefault(c["date"], []).append(c["score"])
    print(f"\n   Daily Scores:")
    for d in sorted(by_date.keys()):
        day_scores = by_date[d]
        day_avg = sum(day_scores) / len(day_scores)
        day_pct = day_avg / 3 * 100
        bar_len = int(day_pct / 5)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"   {d} |{bar}| {day_pct:.0f}")

    # Recommendations
    print(f"\n{'═' * 55}")
    print(f"   📝 Recommendations:")
    if score >= 85:
        print(f"      • Excellent! Maintain your current habits")
        print(f"      • Focus on consistency — keep logging daily")
    elif score >= 70:
        print(f"      • Good progress! Target your poor-posture moments")
        print(f"      • Do targeted stretches for weak areas")
    elif score >= 50:
        print(f"      • Set up posture alarms for high-risk hours")
        print(f"      • Review your ergonomic setup (run 'ergonomics')")
        print(f"      • Do desk stretches 2-3x daily (run 'stretch')")
    else:
        print(f"      • Prioritize ergonomic setup — your posture needs help")
        print(f"      • Consider a standing desk converter")
        print(f"      • Take movement breaks every 20-30 minutes")
        print(f"      • Consult a physical therapist if pain persists")
    print(f"\n{'═' * 55}")


def cmd_goal(db, args):
    if args:
        try:
            minutes = int(args[0])
            db["daily_goal"] = minutes
            save_db(db)
            print(f"✓ Daily goal set to {minutes} minutes of good posture")
        except ValueError:
            print("Error: minutes must be a number")
    else:
        goal = db.get("daily_goal", 480)
        print(f"🎯 Daily good-posture goal: {goal} minutes ({goal/60:.1f} hours)")


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
        "check": cmd_check,
        "score": cmd_score,
        "report": cmd_report,
        "streak": cmd_streak,
        "breaks": cmd_breaks,
        "stretch": cmd_stretch,
        "spinal-load": cmd_spinal_load,
        "ergonomics": cmd_ergonomics,
        "pattern": cmd_pattern,
        "goal": cmd_goal,
    }
    if command not in commands:
        print(f"Unknown command: {command}")
        print(f"Available: {', '.join(commands.keys())}")
        return
    commands[command](db, args)


if __name__ == "__main__":
    main()
