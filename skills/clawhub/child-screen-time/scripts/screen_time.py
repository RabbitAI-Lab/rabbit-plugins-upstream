#!/usr/bin/env python3
"""
Child Screen Time Negotiator — manage children's screen time through fair
AI-mediated contracts with an earned-time economy.

Pure Python stdlib. JSON file database.

Usage:
    python3 screen_time.py add-child <name> <age>
    python3 screen_time.py set-limit <name> <minutes>
    python3 screen_time.py set-edu-limit <name> <minutes>
    python3 screen_time.py log <name> <minutes> <activity> <fun|edu>
    python3 screen_time.py award <name> <minutes> <reason>
    python3 screen_time.py deduct <name> <minutes> <reason>
    python3 screen_time.py status <name>
    python3 screen_time.py report-card <name> [days]
    python3 screen_time.py contract <name>
    python3 screen_time.py negotiate <name> <minutes> <reason>
    python3 screen_time.py balance
    python3 screen_time.py history <name> [days]
    python3 screen_time.py weekly-summary

Examples:
    python3 screen_time.py add-child Alice 10
    python3 screen_time.py set-limit Alice 120
    python3 screen_time.py log Alice 45 "Minecraft" fun
    python3 screen_time.py award Alice 15 "finished homework"
    python3 screen_time.py status Alice
    python3 screen_time.py negotiate Alice 30 "friend is online"
    python3 screen_time.py report-card Alice 7
"""

import json
import os
import sys
from datetime import datetime, date, timedelta

DB_PATH = os.path.expanduser("~/.screen_time.json")

# AAP-based age defaults (entertainment minutes per day)
def age_default_limit(age):
    if age < 2: return 0
    if age < 6: return 60
    if age < 10: return 90
    if age < 14: return 120
    return 150

# Bonus earning rules
EARN_RULES = {
    "homework": {"bonus": 15, "desc": "Homework completion (per subject)"},
    "chore": {"bonus": 10, "desc": "Chore done without being asked"},
    "reading": {"bonus": 5, "desc": "15 min physical book reading"},
    "behavior": {"bonus": 10, "desc": "Good behavior / kindness"},
    "outdoor": {"bonus": 5, "desc": "30 min outdoor play"},
    "sibling_help": {"bonus": 10, "desc": "Helping a sibling"},
    "instrument": {"bonus": 5, "desc": "15 min instrument practice"},
}

CATEGORY_ICONS = {"fun": "🎮", "edu": "📚", "bonus": "⭐", "deduct": "➖"}


# --- Database ---

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            return json.load(f)
    return {"children": {}}

def save_db(db):
    with open(DB_PATH, "w") as f:
        json.dump(db, f, indent=2, default=str)

def today_str():
    return date.today().isoformat()

def get_child(db, name):
    name_lower = name.lower()
    for cname, data in db["children"].items():
        if cname.lower() == name_lower:
            return cname, data
    return None, None


# --- Commands ---

def cmd_add_child(db, args):
    if len(args) < 2:
        print("Usage: add-child <name> <age>")
        return
    name = args[0]
    try:
        age = int(args[1])
    except ValueError:
        print("Error: age must be a number.")
        return
    if name in db["children"]:
        print(f"Child '{name}' already exists.")
        return
    default_limit = age_default_limit(age)
    db["children"][name] = {
        "age": age,
        "base_limit": default_limit,
        "edu_limit": -1,  # -1 = unlimited
        "created": today_str(),
        "daily": {},  # date -> {fun_minutes, edu_minutes, bonus, deductions, activities: [...]}
        "compliance_log": [],  # [{date, event, score_delta}]
    }
    save_db(db)
    print(f"✓ Added child: {name} (age {age})")
    print(f"  Default entertainment limit: {default_limit} min/day")
    edu_str = "unlimited" if db["children"][name]["edu_limit"] < 0 else f"{db['children'][name]['edu_limit']} min/day"
    print(f"  Educational limit: {edu_str}")


def cmd_set_limit(db, args):
    if len(args) < 2:
        print("Usage: set-limit <name> <minutes>")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    try:
        minutes = int(args[1])
    except ValueError:
        print("Error: minutes must be a number.")
        return
    child["base_limit"] = minutes
    save_db(db)
    print(f"✓ {cname}'s entertainment limit set to {minutes} min/day")


def cmd_set_edu_limit(db, args):
    if len(args) < 2:
        print("Usage: set-edu-limit <name> <minutes>")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    try:
        minutes = int(args[1])
    except ValueError:
        print("Error: minutes must be a number.")
        return
    child["edu_limit"] = minutes
    save_db(db)
    edu_str = "unlimited" if minutes < 0 else f"{minutes} min/day"
    print(f"✓ {cname}'s educational limit set to {edu_str}")


def _get_or_create_day(child, d=None):
    d = d or today_str()
    if d not in child["daily"]:
        child["daily"][d] = {
            "fun_used": 0,
            "edu_used": 0,
            "bonus_earned": 0,
            "bonus_deducted": 0,
            "activities": [],
            "compliance_events": 0,
        }
    return child["daily"][d]


def cmd_log(db, args):
    if len(args) < 4:
        print("Usage: log <name> <minutes> <activity> <fun|edu>")
        print('Example: log Alice 45 "Minecraft" fun')
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    try:
        minutes = int(args[1])
    except ValueError:
        print("Error: minutes must be a number.")
        return
    activity = args[2]
    category = args[3].lower()
    if category not in ("fun", "edu"):
        print("Error: category must be 'fun' or 'edu'")
        return
    day = _get_or_create_day(child)
    entry = {
        "time": datetime.now().strftime("%H:%M"),
        "minutes": minutes,
        "activity": activity,
        "category": category,
    }
    day["activities"].append(entry)
    if category == "fun":
        day["fun_used"] += minutes
    else:
        day["edu_used"] += minutes
    save_db(db)
    icon = CATEGORY_ICONS.get(category, "")
    print(f"✓ Logged {minutes} min of {activity} ({category}) for {cname}")
    _show_remaining(cname, child, day)


def cmd_award(db, args):
    if len(args) < 2:
        print("Usage: award <name> <minutes> <reason>")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    try:
        minutes = int(args[1])
    except ValueError:
        print("Error: minutes must be a number.")
        return
    reason = " ".join(args[2:]) if len(args) > 2 else "bonus"
    day = _get_or_create_day(child)
    day["bonus_earned"] += minutes
    day["activities"].append({
        "time": datetime.now().strftime("%H:%M"),
        "minutes": minutes,
        "activity": f"⭐ Earned: {reason}",
        "category": "bonus",
    })
    save_db(db)
    print(f"⭐ Awarded {cname} +{minutes} min: {reason}")
    _show_remaining(cname, child, day)


def cmd_deduct(db, args):
    if len(args) < 2:
        print("Usage: deduct <name> <minutes> <reason>")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    try:
        minutes = int(args[1])
    except ValueError:
        print("Error: minutes must be a number.")
        return
    reason = " ".join(args[2:]) if len(args) > 2 else "deduction"
    day = _get_or_create_day(child)
    day["bonus_deducted"] += minutes
    day["compliance_events"] += 1
    day["activities"].append({
        "time": datetime.now().strftime("%H:%M"),
        "minutes": -minutes,
        "activity": f"➖ Deducted: {reason}",
        "category": "deduct",
    })
    save_db(db)
    print(f"➖ Deducted {minutes} min from {cname}: {reason}")
    _show_remaining(cname, child, day)


def _show_remaining(cname, child, day):
    """Print remaining time for the day."""
    limit = child.get("base_limit", 120)
    total_budget = limit + day.get("bonus_earned", 0) - day.get("bonus_deducted", 0)
    fun_used = day.get("fun_used", 0)
    remaining = total_budget - fun_used
    print(f"   Budget: {total_budget} min | Used: {fun_used} min | Remaining: {remaining} min")


def _compliance_score(child, days=7):
    """Calculate compliance score (0-100) over recent days."""
    recent_dates = [(date.today() - timedelta(days=i)).isoformat() for i in range(days)]
    total_events = 0
    negative_events = 0
    for d in recent_dates:
        day = child.get("daily", {}).get(d)
        if day:
            total_events += 1
            neg = day.get("compliance_events", 0)
            negative_events += neg
            # Bonus earning counts as positive
            if day.get("bonus_earned", 0) > 0:
                total_events += 1
    if total_events == 0:
        return 75  # neutral start
    score = max(0, 100 - (negative_events * 15) + (min(total_events - negative_events, total_events) * 3))
    return min(100, max(0, score))


def cmd_status(db, args):
    if len(args) < 1:
        print("Usage: status <name>")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    day = _get_or_create_day(child)
    limit = child.get("base_limit", 120)
    total_budget = limit + day.get("bonus_earned", 0) - day.get("bonus_deducted", 0)
    fun_used = day.get("fun_used", 0)
    edu_used = day.get("edu_used", 0)
    remaining = total_budget - fun_used
    compliance = _compliance_score(child)
    print(f"📱 Screen Time Status: {cname}")
    print(f"{'─' * 45}")
    print(f"   Age: {child['age']} | Compliance: {compliance}%")
    print(f"   Entertainment: {fun_used}/{total_budget} min used")
    status_emoji = "✅" if remaining >= 0 else "⚠️"
    print(f"   {status_emoji} Remaining: {remaining} min")
    edu_limit = child.get("edu_limit", -1)
    edu_str = f"{edu_used}/{edu_limit} min" if edu_limit >= 0 else f"{edu_used} min (unlimited)"
    print(f"   Educational: {edu_str}")
    print(f"   ⭐ Bonus earned: +{day.get('bonus_earned', 0)} min")
    print(f"   ➖ Deducted: -{day.get('bonus_deducted', 0)} min")
    print()
    # Today's activities
    if day.get("activities"):
        print(f"   Today's log:")
        for act in day["activities"]:
            icon = CATEGORY_ICONS.get(act["category"], "")
            print(f"   {act['time']} {icon} {act['activity']} ({act['minutes']} min)")


def cmd_report_card(db, args):
    if len(args) < 1:
        print("Usage: report-card <name> [days]")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    days = int(args[1]) if len(args) > 1 else 7
    print(f"📊 Report Card: {cname} (Last {days} days)")
    print(f"{'═' * 50}")
    total_fun = 0
    total_edu = 0
    total_bonus = 0
    total_deduct = 0
    active_days = 0
    for i in range(days):
        d = (date.today() - timedelta(days=i)).isoformat()
        day = child.get("daily", {}).get(d)
        if day and (day.get("fun_used", 0) > 0 or day.get("edu_used", 0) > 0):
            active_days += 1
            total_fun += day.get("fun_used", 0)
            total_edu += day.get("edu_used", 0)
            total_bonus += day.get("bonus_earned", 0)
            total_deduct += day.get("bonus_deducted", 0)
    limit = child.get("base_limit", 120)
    compliance = _compliance_score(child, days)
    avg_fun = total_fun / active_days if active_days else 0
    avg_edu = total_edu / active_days if active_days else 0
    edu_ratio = (total_edu / (total_fun + total_edu) * 100) if (total_fun + total_edu) > 0 else 0
    print(f"\n   📈 Summary Statistics:")
    print(f"      Active days: {active_days}/{days}")
    print(f"      Avg entertainment: {avg_fun:.0f} min/day (limit: {limit} min)")
    print(f"      Avg educational:   {avg_edu:.0f} min/day")
    print(f"      Education ratio:   {edu_ratio:.0f}% of total screen time")
    print(f"      Bonus earned:      +{total_bonus} min total")
    print(f"      Deducted:          -{total_deduct} min total")
    print(f"      Compliance score:  {compliance}%")
    # Letter grade
    if compliance >= 85 and edu_ratio >= 30:
        grade = "A"
    elif compliance >= 70 and edu_ratio >= 20:
        grade = "B"
    elif compliance >= 55:
        grade = "C"
    elif compliance >= 40:
        grade = "D"
    else:
        grade = "F"
    print(f"\n   🏆 Overall Grade: {grade}")
    # Praise
    print(f"\n   💚 Areas of praise:")
    if edu_ratio >= 30:
        print(f"      • Great balance of educational screen time ({edu_ratio:.0f}%)")
    if total_bonus > total_deduct:
        print(f"      • Earning more time than losing it — good choices!")
    if active_days >= days * 0.7:
        print(f"      • Consistent logging — staying aware of usage")
    if compliance >= 70:
        print(f"      • Following screen time rules well ({compliance}% compliance)")
    # Improvement
    print(f"\n   📝 Areas for improvement:")
    if avg_fun > limit * 1.2:
        print(f"      • Entertainment time exceeds limit — consider more offline activities")
    if edu_ratio < 15:
        print(f"      • Try adding more educational screen time")
    if total_deduct > total_bonus:
        print(f"      • More deductions than bonuses — focus on following rules")
    if active_days < days * 0.5:
        print(f"      • Track usage more consistently")
    if compliance < 60:
        print(f"      • Work on smoother transitions when time is up")
    print(f"\n{'═' * 50}")


def cmd_contract(db, args):
    if len(args) < 1:
        print("Usage: contract <name>")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    limit = child.get("base_limit", 120)
    edu_limit = child.get("edu_limit", -1)
    edu_str = f"{edu_limit} min/day" if edu_limit >= 0 else "unlimited"
    print(f"📜 Screen Time Contract: {cname}")
    print(f"{'═' * 50}")
    print(f"\n   I, {cname} (age {child['age']}), agree to:")
    print(f"\n   1. Use no more than {limit} minutes of entertainment screen")
    print(f"      time per day (games, YouTube, social media).")
    print(f"\n   2. Use educational screen time responsibly (limit: {edu_str}).")
    print(f"\n   3. Stop my screen activity when my time is up, without")
    print(f"      arguing or asking for 'just 5 more minutes.'")
    print(f"\n   4. Earn bonus time through:")
    for key, rule in EARN_RULES.items():
        print(f"      • {rule['desc']}: +{rule['bonus']} min")
    print(f"\n   5. Understand that breaking rules means losing time:")
    print(f"      • Not stopping when asked: -10 min")
    print(f"      • Lying about usage: -15 min")
    print(f"      • Screen in screen-free zones: -10 min")
    print(f"\n   6. Can negotiate for extra time — the system will decide")
    print(f"      fairly based on my behavior.")
    print(f"\n   Signed: {cname}")
    print(f"   Date:  {today_str()}")
    print(f"\n{'═' * 50}")


def cmd_negotiate(db, args):
    if len(args) < 2:
        print("Usage: negotiate <name> <minutes> <reason>")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    try:
        minutes = int(args[1])
    except ValueError:
        print("Error: minutes must be a number.")
        return
    reason = " ".join(args[2:]) if len(args) > 2 else "no reason given"
    day = _get_or_create_day(child)
    limit = child.get("base_limit", 120)
    fun_used = day.get("fun_used", 0)
    total_budget = limit + day.get("bonus_earned", 0) - day.get("bonus_deducted", 0)
    over = fun_used - total_budget
    compliance = _compliance_score(child)
    edu_today = day.get("edu_used", 0)
    print(f"🤝 Negotiation Request: {cname}")
    print(f"{'─' * 50}")
    print(f"   Requesting: +{minutes} min")
    print(f"   Reason: {reason}")
    print(f"   Compliance score: {compliance}%")
    print(f"   Educational time today: {edu_today} min")
    print(f"   Entertainment used: {fun_used}/{total_budget} min")
    # Evaluate
    conditions = []
    approved = False
    conditional = False
    # Auto-approve conditions
    if compliance >= 70 and minutes <= 15 and over < 30 and edu_today >= 30:
        approved = True
    elif compliance >= 60 and minutes <= 15 and over <= 0:
        approved = True
    elif over >= 60:
        approved = False
        conditions.append("Already over by 60+ minutes today")
    elif compliance < 40:
        approved = False
        conditions.append(f"Compliance score too low ({compliance}% < 40%)")
    elif minutes > 60:
        approved = False
        conditions.append("Request too large (>60 min)")
    else:
        conditional = True
        if edu_today < 30:
            conditions.append("Log 30 min of educational time first")
        if over > 20:
            conditions.append("Wait until tomorrow")
        if compliance < 60:
            conditions.append("Improve compliance score")
    print(f"\n{'─' * 50}")
    if approved:
        day["bonus_earned"] += minutes
        day["activities"].append({
            "time": datetime.now().strftime("%H:%M"),
            "minutes": minutes,
            "activity": f"🤝 Negotiated: {reason}",
            "category": "bonus",
        })
        save_db(db)
        print(f"✅ APPROVED! +{minutes} min granted.")
        print(f"   New budget: {total_budget + minutes} min")
    elif conditional:
        print(f"⚠️ CONDITIONAL — Earn it first:")
        for c in conditions:
            print(f"   • {c}")
        print(f"\n   Complete the conditions and try again!")
    else:
        print(f"❌ DENIED — Reason:")
        for c in conditions:
            print(f"   • {c}")
        print(f"\n   Better luck tomorrow! Try earning bonus time instead.")


def cmd_balance(db, args):
    """Show all children's remaining time today."""
    if not db["children"]:
        print("No children registered. Use 'add-child' first.")
        return
    print(f"📱 Today's Screen Time Balance ({today_str()})")
    print(f"{'─' * 60}")
    for name, child in db["children"].items():
        day = _get_or_create_day(child)
        limit = child.get("base_limit", 120)
        total_budget = limit + day.get("bonus_earned", 0) - day.get("bonus_deducted", 0)
        fun_used = day.get("fun_used", 0)
        remaining = total_budget - fun_used
        edu_used = day.get("edu_used", 0)
        status = "✅" if remaining >= 0 else "⚠️"
        print(f"   {status} {name:12s} | Fun: {fun_used}/{total_budget} min | Remaining: {remaining:4d} min | Edu: {edu_used} min")
    print(f"{'─' * 60}")


def cmd_history(db, args):
    if len(args) < 1:
        print("Usage: history <name> [days]")
        return
    cname, child = get_child(db, args[0])
    if not child:
        print(f"Error: child '{args[0]}' not found.")
        return
    days = int(args[1]) if len(args) > 1 else 7
    print(f"📅 Usage History: {cname} (Last {days} days)")
    print(f"{'─' * 55}")
    for i in range(days - 1, -1, -1):
        d = (date.today() - timedelta(days=i)).isoformat()
        day_data = child.get("daily", {}).get(d)
        if not day_data:
            print(f"   {d} | (no data)")
            continue
        fun = day_data.get("fun_used", 0)
        edu = day_data.get("edu_used", 0)
        bonus = day_data.get("bonus_earned", 0)
        deduct = day_data.get("bonus_deducted", 0)
        bar_len = min(fun // 10, 20)
        bar = "█" * bar_len
        print(f"   {d} | Fun: {fun:3d}m |{bar:<20s}| Edu: {edu:3d}m | ⭐{bonus} ➖{deduct}")


def cmd_weekly_summary(db, args):
    """Compare all children's usage this week."""
    if not db["children"]:
        print("No children registered.")
        return
    print(f"📊 Weekly Summary — All Children")
    print(f"{'═' * 65}")
    for name, child in db["children"].items():
        total_fun = 0
        total_edu = 0
        total_bonus = 0
        for i in range(7):
            d = (date.today() - timedelta(days=i)).isoformat()
            day = child.get("daily", {}).get(d)
            if day:
                total_fun += day.get("fun_used", 0)
                total_edu += day.get("edu_used", 0)
                total_bonus += day.get("bonus_earned", 0)
        compliance = _compliance_score(child, 7)
        limit = child.get("base_limit", 120)
        avg_fun = total_fun / 7
        print(f"\n   {name} (age {child['age']}):")
        print(f"      Total entertainment: {total_fun} min (avg {avg_fun:.0f}/day, limit {limit})")
        print(f"      Total educational:   {total_edu} min")
        print(f"      Bonus earned:        {total_bonus} min")
        print(f"      Compliance:          {compliance}%")
    print(f"\n{'═' * 65}")


# --- Main ---

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    command = sys.argv[1]
    args = sys.argv[2:]
    db = load_db()
    commands = {
        "add-child": cmd_add_child,
        "set-limit": cmd_set_limit,
        "set-edu-limit": cmd_set_edu_limit,
        "log": cmd_log,
        "award": cmd_award,
        "deduct": cmd_deduct,
        "status": cmd_status,
        "report-card": cmd_report_card,
        "contract": cmd_contract,
        "negotiate": cmd_negotiate,
        "balance": cmd_balance,
        "history": cmd_history,
        "weekly-summary": cmd_weekly_summary,
    }
    if command not in commands:
        print(f"Unknown command: {command}")
        print(f"Available: {', '.join(commands.keys())}")
        return
    commands[command](db, args)


if __name__ == "__main__":
    main()
