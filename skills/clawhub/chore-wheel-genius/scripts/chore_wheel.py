#!/usr/bin/env python3
"""
Chore Wheel Genius — fair chore assignment for households.
Assigns tasks based on skills, schedule, age, and fairness scoring.
Pure Python stdlib. JSON file database.

Usage:
    python3 chore_wheel.py add-member <name> [age] [--skills s1,s2]
    python3 chore_wheel.py add-chore <name> [--effort 1-5] [--freq daily|weekly|monthly] [--skills s1,s2]
    python3 chore_wheel.py assign [weeks]
    python3 chore_wheel.py done <member> <chore>
    python3 chore_wheel.py skip <member> <chore> <reason>
    python3 chore_wheel.py fairness
    python3 chore_wheel.py report [weeks]
    python3 chore_wheel.py chart
    python3 chore_wheel.py swap <chore> <from> <to>
    python3 chore_wheel.py list-chores
    python3 chore_wheel.py list-members
    python3 chore_wheel.py history <member> [weeks]

Examples:
    python3 chore_wheel.py add-member Mom --skills cooking,laundry
    python3 chore_wheel.py add-member Alice 14
    python3 chore_wheel.py add-chore "Cook dinner" --effort 5 --freq daily --skills cooking
    python3 chore_wheel.py assign
    python3 chore_wheel.py done Alice "Take out trash"
    python3 chore_wheel.py fairness
"""

import json
import os
import sys
from datetime import datetime, date, timedelta

DB_PATH = os.path.expanduser("~/.chore_wheel.json")

# Age-based effort caps
def age_effort_cap(age):
    if age is None: return 5
    if age < 4: return 0
    if age < 8: return 2
    if age < 11: return 3
    if age < 14: return 4
    return 5

# Age-based effort multipliers (how much of the fair share they should do)
def age_effort_multiplier(age):
    if age is None: return 1.0
    if age < 6: return 0.0
    if age < 8: return 0.3
    if age < 11: return 0.5
    if age < 14: return 0.7
    if age < 18: return 0.85
    return 1.0

FREQ_DAYS = {"daily": 1, "weekly": 7, "monthly": 30}

EFFORT_LABELS = {
    1: "Trivial",
    2: "Light",
    3: "Moderate",
    4: "Heavy",
    5: "Very Heavy",
}

EFFORT_ICONS = {1: "🟢", 2: "🔵", 3: "🟡", 4: "🟠", 5: "🔴"}


# --- Database ---

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            return json.load(f)
    return {
        "members": {},
        "chores": {},
        "assignments": {},  # week_key -> [{member, chore, done, date}]
        "ledger": {},  # member -> cumulative effort
        "last_done": {},  # chore -> {member -> date} for rotation
    }

def save_db(db):
    with open(DB_PATH, "w") as f:
        json.dump(db, f, indent=2, default=str)

def week_key(offset=0):
    d = date.today() + timedelta(weeks=offset)
    iso = d.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


# --- Parsing ---

def parse_args_flags(args):
    """Parse positional args and --flag values."""
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

def cmd_add_member(db, args):
    positional, flags = parse_args_flags(args)
    if not positional:
        print("Usage: add-member <name> [age] [--skills s1,s2]")
        return
    name = positional[0]
    age = None
    if len(positional) > 1:
        try:
            age = int(positional[1])
        except ValueError:
            print(f"Error: age must be a number, got '{positional[1]}'")
            return
    skills_str = flags.get("skills", "")
    skills = [s.strip() for s in skills_str.split(",") if s.strip()] if skills_str else []
    if name in db["members"]:
        print(f"Member '{name}' already exists.")
        return
    db["members"][name] = {
        "age": age,
        "skills": skills,
        "available": True,
    }
    db["ledger"].setdefault(name, 0)
    save_db(db)
    age_str = f" (age {age})" if age else ""
    cap = age_effort_cap(age)
    mult = age_effort_multiplier(age)
    print(f"✓ Added member: {name}{age_str}")
    print(f"  Skills: {', '.join(skills) if skills else 'none'}")
    print(f"  Max chore effort: {cap} ({EFFORT_LABELS.get(cap, '?')})")
    print(f"  Effort share: {mult*100:.0f}% of adult baseline")


def cmd_add_chore(db, args):
    positional, flags = parse_args_flags(args)
    if not positional:
        print('Usage: add-chore "chore name" [--effort 1-5] [--freq daily|weekly|monthly] [--skills s1,s2]')
        return
    name = positional[0]
    effort = int(flags.get("effort", 3))
    freq = flags.get("freq", "weekly")
    if effort < 1 or effort > 5:
        print("Error: effort must be 1-5")
        return
    if freq not in FREQ_DAYS:
        print(f"Error: freq must be one of {', '.join(FREQ_DAYS.keys())}")
        return
    skills_str = flags.get("skills", "")
    skills = [s.strip() for s in skills_str.split(",") if s.strip()] if skills_str else []
    db["chores"][name] = {
        "effort": effort,
        "freq": freq,
        "skills": skills,
    }
    save_db(db)
    icon = EFFORT_ICONS[effort]
    print(f"✓ Added chore: {name}")
    print(f"  {icon} Effort: {effort}/5 ({EFFORT_LABELS[effort]})")
    print(f"  📅 Frequency: {freq}")
    print(f"  🎯 Skills: {', '.join(skills) if skills else 'none required'}")


def cmd_assign(db, args):
    if not db["members"]:
        print("No members. Use 'add-member' first.")
        return
    if not db["chores"]:
        print("No chores defined. Use 'add-chore' first.")
        return
    wk = week_key(0)
    if wk in db["assignments"] and db["assignments"][wk]:
        print(f"Assignments for {wk} already exist:")
        for a in db["assignments"][wk]:
            status = "✓" if a["done"] else "☐"
            print(f"   {status} {a['member']:12s} → {a['chore']}")
        print("\nUse 'chart' to view, or delete to reassign.")
        return

    # Calculate weekly effort per chore
    available_members = [m for m, d in db["members"].items() if d.get("available", True)]
    if not available_members:
        print("No available members to assign chores to.")
        return

    # Weekly effort per member
    member_weights = {m: age_effort_multiplier(db["members"][m].get("age")) for m in available_members}
    total_weight = sum(member_weights.values())

    # Sort chores by effort descending (assign hardest first)
    sorted_chores = sorted(db["chores"].items(), key=lambda x: x[1]["effort"], reverse=True)

    # Calculate current ledger deficits
    avg_ledger = sum(db["ledger"].get(m, 0) for m in available_members) / len(available_members)
    deficits = {m: avg_ledger - db["ledger"].get(m, 0) for m in available_members}

    assignments = []
    member_projected = {m: 0.0 for m in available_members}

    for chore_name, chore_data in sorted_chores:
        effort = chore_data["effort"]
        required_skills = chore_data.get("skills", [])
        freq = chore_data.get("freq", "weekly")
        # Daily chores happen FREQ_DAYS times per week
        weekly_instances = 7 // FREQ_DAYS.get(freq, 7)

        for instance in range(weekly_instances):
            # Filter eligible members
            eligible = []
            for m in available_members:
                member = db["members"][m]
                # Age check
                if age_effort_cap(member.get("age")) < effort:
                    continue
                # Skill check (soft: if skills required, prefer skilled but allow unskilled)
                has_skill = any(s in member.get("skills", []) for s in required_skills)
                eligible.append((m, has_skill))

            if not eligible:
                print(f"⚠ No eligible member for '{chore_name}' (effort {effort}) — skipping")
                continue

            # Sort by: skill match first, then deficit, then least projected effort
            skilled = [(m, hs) for m, hs in eligible if hs]
            if skilled and len(skilled) < len(eligible):
                # Prefer skilled members but mix in unskilled for learning
                if len(skilled) > 0 and instance == 0:
                    pool = skilled
                else:
                    pool = eligible
            else:
                pool = eligible

            # Recency penalty for unpleasant chores
            scored = []
            for m, hs in pool:
                score = deficits.get(m, 0) - member_projected[m]
                if hs:
                    score += 0.5  # skill bonus
                # Recency: if did this chore recently, penalize
                last = db.get("last_done", {}).get(chore_name, {}).get(m)
                if last:
                    try:
                        last_date = datetime.strptime(last, "%Y-%m-%d").date()
                        days_ago = (date.today() - last_date).days
                        if days_ago < 7:
                            score -= 2.0 * (1 - days_ago / 7)
                    except ValueError:
                        pass
                scored.append((m, score, hs))

            scored.sort(key=lambda x: x[1], reverse=True)
            assigned_member = scored[0][0]
            member_projected[assigned_member] += effort
            assignments.append({
                "member": assigned_member,
                "chore": chore_name,
                "effort": effort,
                "done": False,
                "date": None,
            })

    db["assignments"][wk] = assignments
    save_db(db)

    print(f"📋 Chore Assignments for {wk}")
    print(f"{'═' * 55}")
    for m in available_members:
        m_assigns = [a for a in assignments if a["member"] == m]
        total_effort = sum(a["effort"] for a in m_assigns)
        print(f"\n  {m}:")
        print(f"    Projected effort: {total_effort}")
        for a in m_assigns:
            icon = EFFORT_ICONS[a["effort"]]
            print(f"    {icon} {a['chore']} (effort {a['effort']})")
    print(f"\n{'═' * 55}")
    print(f"Total assignments: {len(assignments)}")


def cmd_done(db, args):
    if len(args) < 2:
        print("Usage: done <member> <chore>")
        return
    member = args[0]
    chore = " ".join(args[1:])
    if member not in db["members"]:
        print(f"Error: member '{member}' not found.")
        return
    wk = week_key(0)
    assignments = db["assignments"].get(wk, [])
    for a in assignments:
        if a["member"] == member and a["chore"].lower() == chore.lower():
            if a["done"]:
                print(f"Already marked done.")
                return
            a["done"] = True
            a["date"] = date.today().isoformat()
            effort = a.get("effort", db["chores"].get(chore, {}).get("effort", 3))
            db["ledger"][member] = db["ledger"].get(member, 0) + effort
            # Track last done for rotation
            db["last_done"].setdefault(chore, {})[member] = date.today().isoformat()
            save_db(db)
            print(f"✓ {member} completed: {chore} (+{effort} effort)")
            return
    # Also check past assignments / ad-hoc
    effort = db["chores"].get(chore, {}).get("effort", 3)
    db["ledger"][member] = db["ledger"].get(member, 0) + effort
    db["last_done"].setdefault(chore, {})[member] = date.today().isoformat()
    save_db(db)
    print(f"✓ {member} completed: {chore} (+{effort} effort) [ad-hoc]")


def cmd_skip(db, args):
    if len(args) < 2:
        print("Usage: skip <member> <chore> <reason>")
        return
    member = args[0]
    chore = " ".join(args[1:])
    if member not in db["members"]:
        print(f"Error: member '{member}' not found.")
        return
    wk = week_key(0)
    assignments = db["assignments"].get(wk, [])
    for a in assignments:
        if a["member"] == member and a["chore"].lower() == chore.lower():
            a["skipped"] = True
            a["skip_reason"] = " ".join(args[2:]) if len(args) > 2 else ""
            save_db(db)
            print(f"📝 {member} skipped: {chore}")
            return
    print(f"No assignment found for {member} → {chore} this week.")


def cmd_fairness(db, args):
    if not db["members"]:
        print("No members registered.")
        return
    members = list(db["members"].keys())
    ledgers = {m: db["ledger"].get(m, 0) for m in members}
    avg = sum(ledgers.values()) / len(members) if members else 0
    print(f"⚖️  Fairness Report")
    print(f"{'═' * 55}")
    print(f"{'Member':<15s} {'Effort':>8s} {'Share%':>8s} {'Balance':>10s}")
    print(f"{'─' * 55}")
    for m in sorted(members, key=lambda x: ledgers[x], reverse=True):
        effort = ledgers[m]
        share = (effort / sum(ledgers.values()) * 100) if sum(ledgers.values()) else 0
        balance = effort - avg
        status = "✅" if abs(balance) < 3 else ("📈" if balance < 0 else "📉")
        print(f"  {m:<13s} {effort:>8.0f} {share:>7.1f}% {balance:>+9.1f}  {status}")
    print(f"{'─' * 55}")
    print(f"  Average: {avg:.1f}")
    # Identify patterns
    if members:
        max_m = max(ledgers, key=ledgers.get)
        min_m = min(ledgers, key=ledgers.get)
        if ledgers[max_m] - ledgers[min_m] > 10:
            print(f"\n  💡 {max_m} has the highest effort ({ledgers[max_m]:.0f})")
            print(f"     {min_m} has the lowest ({ledgers[min_m]:.0f})")
            print(f"     Gap: {ledgers[max_m] - ledgers[min_m]:.0f} — consider rebalancing")


def cmd_report(db, args):
    weeks = int(args[0]) if args else 4
    print(f"📊 Chore Report (Last {weeks} Weeks)")
    print(f"{'═' * 60}")
    for w_offset in range(weeks - 1, -1, -1):
        wk = week_key(-w_offset)
        assignments = db["assignments"].get(wk, [])
        if not assignments:
            continue
        done = sum(1 for a in assignments if a.get("done"))
        total = len(assignments)
        rate = (done / total * 100) if total else 0
        print(f"\n  Week {wk}:")
        print(f"    Completion: {done}/{total} ({rate:.0f}%)")
        for a in assignments:
            status = "✓" if a.get("done") else ("❌" if a.get("skipped") else "☐")
            icon = EFFORT_ICONS.get(a.get("effort", 3), "")
            print(f"    {status} {a['member']:12s} {icon} {a['chore']}")
    print(f"\n{'═' * 60}")


def cmd_chart(db, args):
    wk = week_key(0)
    assignments = db["assignments"].get(wk, [])
    if not assignments:
        print("No assignments for this week. Run 'assign' first.")
        return
    members = sorted(set(a["member"] for a in assignments))
    chores_list = sorted(set(a["chore"] for a in assignments))
    print(f"\n📋 Weekly Chore Chart — {wk}")
    print(f"{'─' * 70}")
    # Header
    header = f"{'Chore':<30s}"
    for m in members:
        header += f" {m[:8]:>8s}"
    print(header)
    print(f"{'─' * 70}")
    for chore in chores_list:
        row = f"{chore[:28]:<30s}"
        for m in members:
            cell = "  "
            for a in assignments:
                if a["member"] == m and a["chore"] == chore:
                    cell = "  ✓" if a.get("done") else "  ☐"
            row += f" {cell:>8s}"
        print(row)
    print(f"{'─' * 70}")


def cmd_swap(db, args):
    if len(args) < 3:
        print("Usage: swap <chore> <from_member> <to_member>")
        return
    chore = args[0]
    from_m = args[1]
    to_m = args[2]
    wk = week_key(0)
    assignments = db["assignments"].get(wk, [])
    swapped = False
    for a in assignments:
        if a["member"] == from_m and a["chore"].lower() == chore.lower():
            a["member"] = to_m
            swapped = True
            break
    if swapped:
        save_db(db)
        print(f"✓ Swapped '{chore}': {from_m} → {to_m}")
    else:
        print(f"No assignment found: {from_m} → {chore}")


def cmd_list_chores(db, args):
    if not db["chores"]:
        print("No chores defined.")
        return
    print(f"📝 Defined Chores ({len(db['chores'])})")
    print(f"{'─' * 55}")
    for name, data in sorted(db["chores"].items(), key=lambda x: x[1]["effort"], reverse=True):
        icon = EFFORT_ICONS[data["effort"]]
        skills = ", ".join(data.get("skills", []))
        print(f"  {icon} {name}")
        print(f"     Effort: {data['effort']}/5 | Freq: {data['freq']} | Skills: {skills or 'none'}")


def cmd_list_members(db, args):
    if not db["members"]:
        print("No members registered.")
        return
    print(f"👥 Household Members ({len(db['members'])})")
    print(f"{'─' * 55}")
    for name, data in db["members"].items():
        age = data.get("age", "?")
        skills = ", ".join(data.get("skills", []))
        effort = db["ledger"].get(name, 0)
        avail = "✅" if data.get("available", True) else "❌ unavailable"
        print(f"  {name} (age {age}) — {avail}")
        print(f"     Skills: {skills or 'none'} | Lifetime effort: {effort}")


def cmd_history(db, args):
    if len(args) < 1:
        print("Usage: history <member> [weeks]")
        return
    member = args[0]
    weeks = int(args[1]) if len(args) > 1 else 4
    if member not in db["members"]:
        print(f"Error: member '{member}' not found.")
        return
    print(f"📜 Chore History: {member} (Last {weeks} Weeks)")
    print(f"{'─' * 55}")
    total_done = 0
    total_effort = 0
    for w_offset in range(weeks - 1, -1, -1):
        wk = week_key(-w_offset)
        assignments = db["assignments"].get(wk, [])
        member_assigns = [a for a in assignments if a["member"] == member]
        if not member_assigns:
            print(f"  {wk}: (no assignments)")
            continue
        done = [a for a in member_assigns if a.get("done")]
        skipped = [a for a in member_assigns if a.get("skipped")]
        effort = sum(a.get("effort", 3) for a in done)
        total_done += len(done)
        total_effort += effort
        status = f"✓{len(done)} ❌{len(skipped)} ☐{len(member_assigns) - len(done) - len(skipped)}"
        print(f"  {wk}: {status} | Effort: {effort}")
        for a in member_assigns:
            mark = "✓" if a.get("done") else ("❌" if a.get("skipped") else "☐")
            print(f"     {mark} {a['chore']}")
    print(f"{'─' * 55}")
    print(f"  Total completed: {total_done} | Total effort: {total_effort}")


# --- Main ---

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    command = sys.argv[1]
    args = sys.argv[2:]
    db = load_db()
    commands = {
        "add-member": cmd_add_member,
        "add-chore": cmd_add_chore,
        "assign": cmd_assign,
        "done": cmd_done,
        "skip": cmd_skip,
        "fairness": cmd_fairness,
        "report": cmd_report,
        "chart": cmd_chart,
        "swap": cmd_swap,
        "list-chores": cmd_list_chores,
        "list-members": cmd_list_members,
        "history": cmd_history,
    }
    if command not in commands:
        print(f"Unknown command: {command}")
        print(f"Available: {', '.join(commands.keys())}")
        return
    commands[command](db, args)


if __name__ == "__main__":
    main()
