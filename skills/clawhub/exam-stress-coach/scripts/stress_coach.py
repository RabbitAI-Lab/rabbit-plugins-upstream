#!/usr/bin/env python3
"""
Exam Stress Coach — adaptive stress management for students.

Subcommands:
  assess   — classify stress level (1-10) into zones with recommendations
  breathe  — guided breathing exercise (box, 478, coherent)
  plan     — generate a spaced, interleaved study plan
  log      — log daily stress score to JSON
  trend    — plot stress trends over time
  coach    — get a motivational message matched to stress zone

Usage:
  python stress_coach.py assess --level 7
  python stress_coach.py breathe --technique box --duration 5
  python stress_coach.py plan --subjects "Math,History" --days 14 --hours-per-day 3
  python stress_coach.py log --level 6 --note "Good study session"
  python stress_coach.py trend --days 30
  python stress_coach.py coach --level 5
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta

STRESS_LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "stress_log.json")

# ---------------------------------------------------------------------------
# Breathing techniques
# ---------------------------------------------------------------------------

BREATHING_TECHNIQUES = {
    "box": {
        "name": "Box Breathing (4-4-4-4)",
        "description": "Equal inhale, hold, exhale, hold. Used by Navy SEALs for calm under pressure.",
        "phases": [
            ("Inhale slowly through the nose", 4),
            ("Hold your breath gently (lungs full)", 4),
            ("Exhale smoothly through the mouth", 4),
            ("Hold your breath gently (lungs empty)", 4),
        ],
    },
    "478": {
        "name": "4-7-8 Relaxation Breath",
        "description": "Extended exhale activates parasympathetic response. Great for sleep and panic relief.",
        "phases": [
            ("Inhale through the nose", 4),
            ("Hold the breath", 7),
            ("Exhale through the mouth (whoosh)", 8),
        ],
    },
    "coherent": {
        "name": "Coherent Breathing (~5.5 breaths/min)",
        "description": "Resonant frequency breathing. Maximizes HRV. Best for long-term stress resilience.",
        "phases": [
            ("Inhale slowly", 6),
            ("Exhale slowly", 5),
        ],
    },
}


def run_breathing_session(technique, duration_min):
    """Run an interactive breathing session for the given duration."""
    tech = BREATHING_TECHNIQUES.get(technique)
    if not tech:
        print(f"Unknown technique: {technique}. Choose from: {', '.join(BREATHING_TECHNIQUES)}")
        sys.exit(1)

    total_sec = duration_min * 60
    cycle_sec = sum(p[1] for p in tech["phases"])

    print("=" * 60)
    print(f"  {tech['name']}")
    print(f"  {tech['description']}")
    print(f"  Duration: {duration_min} minutes | Cycle: {cycle_sec}s | ~{total_sec // cycle_sec} cycles")
    print("=" * 60)
    print()
    print("Starting in 3 seconds... Close your eyes if it feels safe.")
    time.sleep(3)

    elapsed = 0
    cycle_count = 0
    try:
        while elapsed < total_sec:
            cycle_count += 1
            print(f"\n--- Cycle {cycle_count} ---")
            for phase_name, phase_sec in tech["phases"]:
                if elapsed >= total_sec:
                    break
                print(f"\n▶ {phase_name} ({phase_sec}s)")
                for remaining in range(phase_sec, 0, -1):
                    if elapsed >= total_sec:
                        break
                    sys.stdout.write(f"\r  {remaining}  ")
                    sys.stdout.flush()
                    time.sleep(1)
                    elapsed += 1
                print()
    except KeyboardInterrupt:
        print("\n\nSession ended early. Well done for taking a break to breathe.")

    print("\n" + "=" * 60)
    print(f"  Session complete. {cycle_count} cycles in {elapsed // 60}m{elapsed % 60}s.")
    print("  Notice how your body feels now. Carry this calm into your next task.")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Stress assessment
# ---------------------------------------------------------------------------

def classify_stress(level):
    """Return zone, color, description, and action list for a stress level."""
    if level <= 3:
        return {
            "zone": "GREEN",
            "color": "🟢",
            "label": "Calm / Focused",
            "description": "Optimal state for deep, focused work. You can tackle your hardest material.",
            "actions": [
                "Study the most challenging topics now — your working memory is at peak capacity.",
                "Try practice problems under timed conditions to build exam confidence.",
                "No breathing exercise needed, but a 3-min coherent breath session can extend your focus.",
                "Log your stress: python stress_coach.py log --level " + str(level),
            ],
        }
    elif level <= 6:
        return {
            "zone": "AMBER",
            "color": "🟡",
            "label": "Manageable Stress",
            "description": "Mild-to-moderate stress. Useful for motivation but needs management.",
            "actions": [
                "Start with a 3-minute box breathing session before studying.",
                "Use 50/10 Pomodoro blocks — 50 min study, 10 min break.",
                "Review what you already know first to build confidence, then tackle new material.",
                "Schedule a walk or light exercise between study blocks.",
                "Log your stress: python stress_coach.py log --level " + str(level),
            ],
        }
    else:
        return {
            "zone": "RED",
            "color": "🔴",
            "label": "High Anxiety",
            "description": "Stress is impairing cognition. You must regulate before productive study.",
            "actions": [
                "STOP — do not try to study right now. Your working memory is compromised.",
                "Run a 5-minute breathing exercise: python stress_coach.py breathe --technique 478 --duration 5",
                "After breathing, do only light review of familiar material for 20-30 minutes.",
                "Talk to someone — a friend, family member, or counselor. You don't have to carry this alone.",
                "If this level persists for 3+ days, please seek professional support.",
                "Log your stress: python stress_coach.py log --level " + str(level),
            ],
        }


def assess_stress(level):
    info = classify_stress(level)
    print("=" * 60)
    print(f"  {info['color']} STRESS ZONE: {info['zone']} — {info['label']}")
    print(f"  Reported level: {level}/10")
    print("=" * 60)
    print(f"\n{info['description']}\n")
    print("RECOMMENDED ACTIONS:")
    for i, action in enumerate(info["actions"], 1):
        print(f"  {i}. {action}")
    print()


# ---------------------------------------------------------------------------
# Study planning
# ---------------------------------------------------------------------------

def generate_study_plan(subjects_str, days, hours_per_day):
    """Generate a spaced, interleaved study plan."""
    subjects = [s.strip() for s in subjects_str.split(",") if s.strip()]
    if not subjects:
        print("Error: provide at least one subject.")
        sys.exit(1)

    buffer_days = min(2, days // 5)  # reserve last 2 days (or fewer for short plans)
    study_days = days - buffer_days

    # Build a topic pool for each subject (generic topics — real use would be customized)
    topic_pool = {
        "Fundamentals": ["Core concepts", "Key definitions", "Basic principles"],
        "Intermediate": ["Problem solving", "Application", "Analysis"],
        "Advanced": ["Complex problems", "Edge cases", "Synthesis"],
        "Review": ["Practice test", "Weak area review", "Speed drill"],
    }

    # Distribute topics across study days with interleaving
    block_min = 50
    break_min = 10
    blocks_per_day = hours_per_day * 60 // (block_min + break_min)
    blocks_per_day = max(1, blocks_per_day)

    start_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    schedule = []

    difficulty_cycle = ["Fundamentals", "Intermediate", "Advanced", "Intermediate", "Review"]
    topic_counter = {s: 0 for s in subjects}

    for day_idx in range(study_days):
        date = start_date + timedelta(days=day_idx)
        day_blocks = []
        current_time = date

        for block_idx in range(blocks_per_day):
            # Interleave subjects
            subject = subjects[(day_idx + block_idx) % len(subjects)]
            difficulty = difficulty_cycle[(day_idx + block_idx) % len(difficulty_cycle)]
            topics = topic_pool[difficulty]
            topic = topics[topic_counter[subject] % len(topics)]
            topic_counter[subject] += 1

            block_type = "review" if day_idx >= study_days - 2 or difficulty == "Review" else "new"

            day_blocks.append({
                "time": current_time.strftime("%H:%M"),
                "duration_min": block_min,
                "subject": subject,
                "topic": f"{difficulty}: {topic}",
                "type": block_type,
            })
            current_time += timedelta(minutes=block_min + break_min)

        schedule.append({
            "date": date.strftime("%Y-%m-%d"),
            "day": day_idx + 1,
            "phase": "study" if day_idx < study_days - 2 else "review",
            "blocks": day_blocks,
        })

    # Buffer days
    for b in range(buffer_days):
        date = start_date + timedelta(days=study_days + b)
        schedule.append({
            "date": date.strftime("%Y-%m-%d"),
            "day": study_days + b + 1,
            "phase": "buffer",
            "blocks": [{
                "time": "09:00",
                "duration_min": 120,
                "subject": "All",
                "topic": f"Full review + practice exam",
                "type": "review",
            }],
        })

    exam_date = start_date + timedelta(days=days)
    plan = {
        "generated": datetime.now().isoformat(),
        "subjects": subjects,
        "exam_date": exam_date.strftime("%Y-%m-%d"),
        "total_days": days,
        "study_days": study_days,
        "buffer_days": buffer_days,
        "hours_per_day": hours_per_day,
        "blocks_per_day": blocks_per_day,
        "principles": [
            "Distributed practice — topics spread across days, not crammed",
            "Interleaving — subjects rotate within each day",
            "Pomodoro rhythm — 50 min blocks, 10 min breaks",
            "Buffer days — last 2 days are review-only, no new material",
        ],
        "schedule": schedule,
    }
    return plan


def print_plan_summary(plan):
    print("=" * 70)
    print(f"  STUDY PLAN — {len(plan['subjects'])} subjects | {plan['total_days']} days")
    print(f"  Exam: {plan['exam_date']} | {plan['hours_per_day']}h/day | {plan['blocks_per_day']} blocks/day")
    print("=" * 70)
    for principles in plan["principles"]:
        print(f"  ✓ {principles}")
    print()
    for entry in plan["schedule"]:
        phase_tag = "📖 STUDY" if entry["phase"] == "study" else "🔄 REVIEW" if entry["phase"] == "review" else "🛡️ BUFFER"
        print(f"  Day {entry['day']:>2} | {entry['date']} | {phase_tag}")
        for b in entry["blocks"]:
            tag = "🆕" if b["type"] == "new" else "🔁"
            print(f"         {b['time']}  {tag} {b['subject']:<12} — {b['topic']}")
        print()


# ---------------------------------------------------------------------------
# Stress logging & trends
# ---------------------------------------------------------------------------

def log_stress(level, note):
    log_path = os.path.abspath(STRESS_LOG_FILE)
    log = []
    if os.path.exists(log_path):
        try:
            with open(log_path) as f:
                log = json.load(f)
        except (json.JSONDecodeError, IOError):
            log = []
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "timestamp": datetime.now().isoformat(),
        "level": level,
        "zone": classify_stress(level)["zone"],
        "note": note or "",
    }
    log.append(entry)
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2)
    print(f"✓ Logged: {entry['date']} | Level {level}/10 ({entry['zone']})")
    if note:
        print(f"  Note: {note}")


def show_trend(days):
    log_path = os.path.abspath(STRESS_LOG_FILE)
    if not os.path.exists(log_path):
        print("No stress log found. Start logging with: python stress_coach.py log --level 5")
        return

    with open(log_path) as f:
        log = json.load(f)

    cutoff = datetime.now() - timedelta(days=days)
    entries = [e for e in log if datetime.strptime(e["date"], "%Y-%m-%d") >= cutoff]

    if not entries:
        print(f"No entries in the last {days} days.")
        return

    levels = [e["level"] for e in entries]
    avg = sum(levels) / len(levels)
    print("=" * 50)
    print(f"  STRESS TREND — Last {len(entries)} entries ({days}d window)")
    print("=" * 50)
    print(f"  Average: {avg:.1f}/10")
    print(f"  Min: {min(levels)}/10  |  Max: {max(levels)}/10")
    print(f"  Trend: {'↓ improving' if levels[-1] < levels[0] else '↑ worsening' if levels[-1] > levels[0] else '→ stable'}")
    print()
    print("  Date         Level  Zone    Bar")
    print("  " + "-" * 46)
    for e in entries:
        bar = "█" * e["level"] + "░" * (10 - e["level"])
        print(f"  {e['date']}   {e['level']:>2}/10  {e['zone']:<6}  {bar}")
        if e.get("note"):
            print(f"                               ↳ {e['note']}")

    # Try matplotlib chart
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        dates = [e["date"] for e in entries]
        fig, ax = plt.subplots(figsize=(10, 4))
        colors = ["#2ecc71" if l <= 3 else "#f39c12" if l <= 6 else "#e74c3c" for l in levels]
        ax.bar(range(len(levels)), levels, color=colors)
        ax.set_xticks(range(len(levels)))
        ax.set_xticklabels([d[5:] for d in dates], rotation=45, fontsize=8)
        ax.axhline(y=avg, color="blue", linestyle="--", alpha=0.5, label=f"Avg {avg:.1f}")
        ax.set_ylabel("Stress Level (1-10)")
        ax.set_title(f"Stress Trend — Last {days} Days")
        ax.legend()
        chart_path = os.path.join(os.path.dirname(log_path), "stress_trend.png")
        plt.tight_layout()
        plt.savefig(chart_path, dpi=100)
        print(f"\n  📊 Chart saved: {chart_path}")
    except ImportError:
        print("\n  (Install matplotlib for visual chart: pip install matplotlib)")


# ---------------------------------------------------------------------------
# Motivational coaching
# ---------------------------------------------------------------------------

COACH_MESSAGES = {
    "GREEN": [
        "You're in a great headspace. Channel this into your hardest topic — future you will thank present you.",
        "Calm and focused is your superpower. Do one hard thing today that scares you a little.",
        "This is what prepared feels like. Trust your preparation and keep building.",
    ],
    "AMBER": [
        "A little stress is just your body caring about the outcome. Use it — don't fight it. Breathe, then begin.",
        "You don't have to feel perfect to do good work. Start with 10 minutes. Momentum follows action.",
        "Every expert was once a beginner who kept going. You're in the middle of becoming. Keep walking.",
    ],
    "RED": [
        "Feeling overwhelmed doesn't mean you're failing. It means you care. Take 3 deep breaths — we'll take the next step together.",
        "You have survived 100% of your worst days. This exam is one moment, not your whole story. Breathe first.",
        "It's okay to not be okay right now. Step away, breathe, call someone. The books will wait. You come first.",
    ],
}


def coach(level):
    zone = classify_stress(level)
    import random
    messages = COACH_MESSAGES[zone["zone"]]
    msg = random.choice(messages)
    print("=" * 60)
    print(f"  {zone['color']} COACH — {zone['zone']} ZONE")
    print("=" * 60)
    print(f"\n  💬 \"{msg}\"\n")
    if zone["zone"] == "RED":
        print("  ⚠️  Your stress is high. Please run:")
        print("     python stress_coach.py breathe --technique 478 --duration 5")
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Exam Stress Coach — adaptive stress management for students.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Take care of yourself. Exams are important. You are more important.",
    )
    sub = parser.add_subparsers(dest="command")

    p_assess = sub.add_parser("assess", help="Assess stress level and get zone-based recommendations")
    p_assess.add_argument("--level", type=int, required=True, help="Current stress level 1-10")

    p_breathe = sub.add_parser("breathe", help="Guided breathing exercise")
    p_breathe.add_argument("--technique", choices=list(BREATHING_TECHNIQUES.keys()), required=True)
    p_breathe.add_argument("--duration", type=int, default=5, help="Duration in minutes (default 5)")

    p_plan = sub.add_parser("plan", help="Generate a spaced, interleaved study plan")
    p_plan.add_argument("--subjects", required=True, help='Comma-separated subjects, e.g. "Math,History"')
    p_plan.add_argument("--days", type=int, required=True, help="Days until exam")
    p_plan.add_argument("--hours-per-day", type=int, default=3, help="Study hours per day (default 3)")
    p_plan.add_argument("--output", help="Save plan JSON to this path")

    p_log = sub.add_parser("log", help="Log today's stress level")
    p_log.add_argument("--level", type=int, required=True, help="Stress level 1-10")
    p_log.add_argument("--note", default="", help="Optional note")

    p_trend = sub.add_parser("trend", help="Show stress trend over recent days")
    p_trend.add_argument("--days", type=int, default=30, help="Number of days to show (default 30)")

    p_coach = sub.add_parser("coach", help="Get a motivational message for your stress zone")
    p_coach.add_argument("--level", type=int, required=True, help="Current stress level 1-10")

    args = parser.parse_args()

    if args.command == "assess":
        if not 1 <= args.level <= 10:
            print("Level must be 1-10"); sys.exit(1)
        assess_stress(args.level)
    elif args.command == "breathe":
        run_breathing_session(args.technique, args.duration)
    elif args.command == "plan":
        if args.days < 1:
            print("Days must be >= 1"); sys.exit(1)
        plan = generate_study_plan(args.subjects, args.days, args.hours_per_day)
        print_plan_summary(plan)
        if args.output:
            with open(args.output, "w") as f:
                json.dump(plan, f, indent=2)
            print(f"\n✓ Plan saved to {args.output}")
        else:
            out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "study_plan.json")
            with open(out, "w") as f:
                json.dump(plan, f, indent=2)
            print(f"\n✓ Plan saved to {out}")
    elif args.command == "log":
        if not 1 <= args.level <= 10:
            print("Level must be 1-10"); sys.exit(1)
        log_stress(args.level, args.note)
    elif args.command == "trend":
        show_trend(args.days)
    elif args.command == "coach":
        if not 1 <= args.level <= 10:
            print("Level must be 1-10"); sys.exit(1)
        coach(args.level)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
