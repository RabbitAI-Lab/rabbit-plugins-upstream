#!/usr/bin/env python3
"""
Symptom Timeline Tracker
========================
Tracks symptoms over time, detects trigger correlations, and generates
doctor-ready reports. Uses JSON for storage. Python stdlib only.

Usage:
    python3 symptom_tracker.py log --name headache --severity 7 --triggers "poor sleep,stress"
    python3 symptom_tracker.py log --name "joint pain" --severity 5 --triggers "humidity:high"
    python3 symptom_tracker.py timeline
    python3 symptom_tracker.py timeline --name headache --last 7
    python3 symptom_tracker.py correlate
    python3 symptom_tracker.py summary
    python3 symptom_tracker.py flare-up
    python3 symptom_tracker.py heatmap --name headache --days 14
    python3 symptom_tracker.py export --output report.txt

Author: Denis Voronin
License: MIT
"""

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta

DEFAULT_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "symptom_db.json")
DEFAULT_DB = os.path.normpath(DEFAULT_DB)

VALID_TRIGGERS = ["food", "stress", "weather", "medication", "sleep", "activity"]


# ─── Database I/O ───────────────────────────────────────────────────────────

def load_db(db_path):
    """Load the symptom database. Creates if missing."""
    if not os.path.exists(db_path):
        return {"entries": []}
    with open(db_path, "r") as f:
        return json.load(f)


def save_db(db, db_path):
    """Persist the database."""
    with open(db_path, "w") as f:
        json.dump(db, f, indent=2, sort_keys=True)


# ─── Entry Helpers ──────────────────────────────────────────────────────────

def parse_triggers(raw):
    """
    Parse trigger string into a list.
    Accepts: "poor sleep,stress,humidity:high" →
        [{"category": "sleep", "value": "poor sleep"},
         {"category": "stress", "value": "stress"},
         {"category": "weather", "value": "humidity:high"}]
    If no category prefix, tries to auto-categorize.
    """
    if not raw:
        return []
    parts = [t.strip().lower() for t in raw.split(",") if t.strip()]
    triggers = []
    for p in parts:
        category = auto_categorize_trigger(p)
        # If value has explicit prefix (e.g. "weather:high humidity"), strip it
        if p.startswith(category + ":"):
            value = p[len(category) + 1:]
        else:
            value = p
        triggers.append({"category": category, "value": value})
    return triggers


def auto_categorize_trigger(value):
    """Guess a trigger category from its text."""
    val = value.lower()
    # Check for explicit category prefix (e.g. "weather:high humidity")
    for trig in VALID_TRIGGERS:
        if val.startswith(trig + ":"):
            return trig
    # Keyword-based heuristics
    keyword_map = {
        "food": ["food", "meal", "ate", "dairy", "gluten", "spicy", "caffeine", "sugar",
                  "alcohol", "chocolate", "diet", "eating"],
        "stress": ["stress", "anxiety", "work", "deadline", "worried", "angry", "overwhelm"],
        "weather": ["weather", "rain", "humidity", "hot", "cold", "pressure", "barometric",
                     "storm", "wind", "temperature"],
        "medication": ["medication", "med", "pill", "ibuprofen", "aspirin", "antibiotic",
                        "dose", "skipped med"],
        "sleep": ["sleep", "insomnia", "tired", "fatigue", "rest", "poor sleep", "late night"],
        "activity": ["exercise", "run", "walk", "gym", "lifting", "hike", "sport", "yoga",
                      "activity", "sitting", "standing"],
    }
    for category, keywords in keyword_map.items():
        for kw in keywords:
            if kw in val:
                return category
    return "other"


# ─── Commands ───────────────────────────────────────────────────────────────

def cmd_log(args):
    """Record a symptom entry."""
    db = load_db(args.db)
    entry = {
        "id": len(db["entries"]) + 1,
        "name": args.name.lower().strip(),
        "severity": max(1, min(10, args.severity)),
        "timestamp": args.time if args.time else datetime.now().isoformat(timespec="minutes"),
        "notes": args.notes or "",
        "triggers": parse_triggers(args.triggers),
    }
    db["entries"].append(entry)
    save_db(db, args.db)
    print(f"✓ Logged: {entry['name']} (severity {entry['severity']}/10)")
    print(f"  Time: {entry['timestamp']}")
    if entry["triggers"]:
        tlist = ", ".join(f"{t['category']}:{t['value']}" for t in entry["triggers"])
        print(f"  Triggers: {tlist}")
    if entry["notes"]:
        print(f"  Notes: {entry['notes']}")
    return entry


def cmd_timeline(args):
    """Show chronological symptom log."""
    db = load_db(args.db)
    entries = db["entries"]
    # Filter by symptom name
    if args.name:
        entries = [e for e in entries if e["name"] == args.name.lower().strip()]
    # Filter by last N days
    if args.last:
        cutoff = datetime.now() - timedelta(days=args.last)
        entries = [e for e in entries if _parse_ts(e["timestamp"]) >= cutoff]
    if not entries:
        print("No entries found.")
        return
    entries.sort(key=lambda e: e["timestamp"])
    print(f"\n{'='*60}")
    print(f"  SYMPTOM TIMELINE ({len(entries)} entries)")
    print(f"{'='*60}\n")
    for e in entries:
        _print_entry(e)


def _print_entry(e):
    """Pretty-print a single entry."""
    bar = _severity_bar(e["severity"])
    print(f"  [{e['timestamp']}] {e['name'].title()}")
    print(f"    Severity: {e['severity']}/10 {bar}")
    if e["triggers"]:
        tlist = ", ".join(f"{t['category']}:{t['value']}" for t in e["triggers"])
        print(f"    Triggers: {tlist}")
    if e["notes"]:
        print(f"    Notes: {e['notes']}")
    print()


def _severity_bar(sev):
    """ASCII bar for severity."""
    filled = sev
    empty = 10 - sev
    return "[" + "█" * filled + "░" * empty + "]"


def cmd_correlate(args):
    """Find trigger-symptom correlations."""
    db = load_db(args.db)
    entries = db["entries"]
    if not entries:
        print("No entries to analyze.")
        return
    # Build: for each trigger, track severity averages
    trigger_severities = defaultdict(list)  # trigger_value -> [severities]
    symptom_trigger_count = defaultdict(lambda: defaultdict(int))  # symptom -> trigger -> count
    symptom_total = Counter(e["name"] for e in entries)

    for e in entries:
        for t in e["triggers"]:
            trigger_severities[t["value"]].append(e["severity"])
            symptom_trigger_count[e["name"]][t["value"]] += 1

    print(f"\n{'='*60}")
    print("  TRIGGER CORRELATIONS")
    print(f"{'='*60}\n")

    # For each symptom, show triggers and their correlation
    found_any = False
    for symptom in sorted(symptom_total.keys()):
        total = symptom_total[symptom]
        triggers = symptom_trigger_count[symptom]
        if not triggers:
            continue
        found_any = True
        print(f"  ■ {symptom.title()} ({total} entries)")
        # Get average severity without any trigger for comparison
        all_sevs = [e["severity"] for e in entries if e["name"] == symptom]
        avg_overall = sum(all_sevs) / len(all_sevs) if all_sevs else 0

        sorted_triggers = sorted(triggers.items(), key=lambda x: -x[1])
        for tval, count in sorted_triggers:
            sevs = trigger_severities[tval]
            avg_with = sum(sevs) / len(sevs) if sevs else 0
            pct = (count / total) * 100 if total else 0
            change = avg_with - avg_overall
            arrow = "↑" if change > 0.5 else ("↓" if change < -0.5 else "→")
            print(f"    {tval:30s} → {pct:5.1f}% of episodes  "
                  f"avg sev {avg_with:.1f} (overall {avg_overall:.1f}) {arrow}")
        print()

    if not found_any:
        print("  No trigger data recorded yet. Use --triggers when logging.\n")

    # Cross-correlation between symptoms
    _cross_correlate(entries)


def _cross_correlate(entries):
    """Detect if symptoms co-occur within the same day."""
    by_date = defaultdict(list)
    for e in entries:
        d = e["timestamp"][:10]
        by_date[d].append(e["name"])

    co_occurrence = defaultdict(int)
    symptom_days = Counter()
    for d, names in by_date.items():
        unique = set(names)
        for n in unique:
            symptom_days[n] += 1
        for n1 in unique:
            for n2 in unique:
                if n1 < n2:
                    co_occurrence[(n1, n2)] += 1

    pairs = [(pair, count) for pair, count in co_occurrence.items() if count >= 2]
    if pairs:
        print("  ■ Symptom Co-occurrence (same-day)")
        for (n1, n2), count in sorted(pairs, key=lambda x: -x[1]):
            pct = (count / min(symptom_days[n1], symptom_days[n2])) * 100
            print(f"    {n1} + {n2}: {count} same-day ({pct:.0f}% overlap)")
        print()


def cmd_summary(args):
    """Generate a doctor-ready summary report."""
    db = load_db(args.db)
    entries = db["entries"]
    if not entries:
        print("No entries to summarize.")
        return

    entries.sort(key=lambda e: e["timestamp"])
    start_date = entries[0]["timestamp"][:10]
    end_date = entries[-1]["timestamp"][:10]

    # Per-symptom stats
    symptoms = defaultdict(list)
    for e in entries:
        symptoms[e["name"]].append(e)

    print(f"\n{'='*60}")
    print("  DOCTOR-READY SUMMARY REPORT")
    print(f"{'='*60}")
    print(f"\n  Reporting Period: {start_date} to {end_date}")
    print(f"  Total Entries: {len(entries)}")
    print(f"  Symptoms Tracked: {len(symptoms)}\n")

    # Medications mentioned
    all_meds = set()
    for e in entries:
        for t in e["triggers"]:
            if t["category"] == "medication":
                all_meds.add(t["value"])
    if all_meds:
        print("  Medications Recorded:")
        for m in sorted(all_meds):
            print(f"    • {m}")
        print()

    # Per-symptom breakdown
    for name in sorted(symptoms.keys()):
        s_entries = symptoms[name]
        sevs = [e["severity"] for e in s_entries]
        avg = sum(sevs) / len(sevs)
        peak = max(sevs)
        # Trend: compare first half vs second half
        mid = len(sevs) // 2
        first_half = sum(sevs[:mid]) / mid if mid else sevs[0]
        second_half = sum(sevs[mid:]) / (len(sevs) - mid) if len(sevs) > mid else sevs[-1]
        if second_half > first_half + 0.5:
            trend = "↗ worsening"
        elif second_half < first_half - 0.5:
            trend = "↘ improving"
        else:
            trend = "→ stable"

        print(f"  ■ {name.title()}")
        print(f"    Episodes: {len(s_entries)}")
        print(f"    Average Severity: {avg:.1f}/10")
        print(f"    Peak Severity: {peak}/10")
        print(f"    Trend: {trend}")

        # Top triggers
        trig_count = Counter()
        for e in s_entries:
            for t in e["triggers"]:
                trig_count[t["value"]] += 1
        if trig_count:
            top = trig_count.most_common(3)
            print(f"    Common Triggers: {', '.join(f'{t} ({c}x)' for t, c in top)}")

        # Frequency
        dates = sorted(set(e["timestamp"][:10] for e in s_entries))
        if len(dates) >= 2:
            span = (_parse_ts(dates[-1]) - _parse_ts(dates[0])).days or 1
            freq = len(s_entries) / span
            print(f"    Frequency: ~{freq:.1f} episodes/day over {span} days")
        print()

    # Flare-up detection
    _detect_flareups_inline(entries)


def _detect_flareups_inline(entries):
    """Inline flare-up summary for the report."""
    flareups = _find_flareups(entries)
    if flareups:
        print("  ⚠ Notable Flare-ups:")
        for f in flareups:
            print(f"    {f}")
        print()


def cmd_flareup(args):
    """Detect worsening patterns."""
    db = load_db(args.db)
    entries = db["entries"]
    if not entries:
        print("No entries to analyze.")
        return
    entries.sort(key=lambda e: e["timestamp"])

    print(f"\n{'='*60}")
    print("  FLARE-UP DETECTION")
    print(f"{'='*60}\n")

    flareups = _find_flareups(entries)
    if not flareups:
        print("  No significant flare-up patterns detected.\n")
        return
    for f in flareups:
        print(f"  ⚠ {f}")
    print()


def _find_flareups(entries):
    """Identify periods of worsening severity."""
    flareups = []
    symptoms = defaultdict(list)
    for e in entries:
        symptoms[e["name"]].append(e)

    for name, s_entries in symptoms.items():
        s_entries.sort(key=lambda e: e["timestamp"])
        sevs = [e["severity"] for e in s_entries]

        # Detect consecutive high-severity entries (>=7)
        streak = 0
        for i, e in enumerate(s_entries):
            if e["severity"] >= 7:
                streak += 1
                if streak >= 2:
                    flareups.append(
                        f"{name.title()}: {streak} consecutive high-severity "
                        f"(≥7/10) episodes ending {e['timestamp'][:10]}"
                    )
            else:
                streak = 0

        # Detect sudden jumps (increase of 3+ in severity)
        for i in range(1, len(sevs)):
            if sevs[i] - sevs[i-1] >= 3:
                flareups.append(
                    f"{name.title()}: sudden severity jump "
                    f"({sevs[i-1]}→{sevs[i]}/10) on {s_entries[i]['timestamp'][:10]}"
                )

        # Detect new high-severity symptom
        if sevs and max(sevs) >= 8 and len(sevs) <= 3:
            flareups.append(
                f"{name.title()}: new symptom with high severity "
                f"(peak {max(sevs)}/10)"
            )

    return flareups


def cmd_heatmap(args):
    """Render ASCII severity heatmap."""
    db = load_db(args.db)
    entries = db["entries"]
    if not entries:
        print("No entries to display.")
        return

    days = args.days or 14
    name = args.name.lower().strip() if args.name else None

    if name:
        entries = [e for e in entries if e["name"] == name]
        _single_heatmap(entries, name, days)
    else:
        # Show all symptoms
        all_names = sorted(set(e["name"] for e in entries))
        for n in all_names:
            n_entries = [e for e in entries if e["name"] == n]
            _single_heatmap(n_entries, n, days)


def _single_heatmap(entries, name, days):
    """Render a heatmap for one symptom."""
    today = datetime.now().date()
    start = today - timedelta(days=days - 1)

    # Build date → severity mapping (max severity per day)
    day_severity = {}
    day_count = {}
    for e in entries:
        d = _parse_ts(e["timestamp"]).date()
        if d < start:
            continue
        if d not in day_severity or e["severity"] > day_severity[d]:
            day_severity[d] = e["severity"]
            day_count[d] = day_count.get(d, 0) + 1

    print(f"\n  {name.title()} — Severity Heatmap (last {days} days)\n")

    # Header: day numbers
    header = "  "
    for i in range(days):
        d = start + timedelta(days=i)
        header += f"{d.day:>3}"
    print(header)

    # Heatmap row
    row = "  "
    for i in range(days):
        d = start + timedelta(days=i)
        sev = day_severity.get(d)
        row += f"  {_heat_cell(sev)}"
    print(row)

    # Legend
    print(f"\n  Legend: {'  '.join(f'{v}:{_heat_cell(v)}' for v in range(0, 11))}")
    print()


def _heat_cell(sev):
    """Return a single character/emoji for severity level."""
    if sev is None or sev == 0:
        return "·"
    if sev <= 2:
        return "🟢"
    if sev <= 4:
        return "🟡"
    if sev <= 6:
        return "🟠"
    if sev <= 8:
        return "🔴"
    return "🟣"


def cmd_export(args):
    """Export a plain-text doctor report."""
    db = load_db(args.db)
    entries = db["entries"]
    if not entries:
        print("No entries to export.")
        return
    entries.sort(key=lambda e: e["timestamp"])

    lines = []
    lines.append("=" * 60)
    lines.append("  SYMPTOM REPORT FOR DOCTOR VISIT")
    lines.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 60)
    lines.append("")

    start = entries[0]["timestamp"][:10]
    end = entries[-1]["timestamp"][:10]
    lines.append(f"Tracking period: {start} to {end}")
    lines.append(f"Total symptom entries: {len(entries)}")
    lines.append("")

    symptoms = defaultdict(list)
    for e in entries:
        symptoms[e["name"]].append(e)

    lines.append("SYMPTOMS OVERVIEW")
    lines.append("-" * 40)
    for name in sorted(symptoms.keys()):
        s_entries = symptoms[name]
        sevs = [e["severity"] for e in s_entries]
        avg = sum(sevs) / len(sevs)
        lines.append(f"  {name.title()}:")
        lines.append(f"    Episodes: {len(s_entries)}, Avg: {avg:.1f}/10, Peak: {max(sevs)}/10")

        trig_count = Counter()
        for e in s_entries:
            for t in e["triggers"]:
                trig_count[t["value"]] += 1
        if trig_count:
            top = trig_count.most_common(5)
            lines.append(f"    Triggers: {', '.join(f'{t}({c}x)' for t, c in top)}")
        lines.append("")

    # Medications
    all_meds = set()
    for e in entries:
        for t in e["triggers"]:
            if t["category"] == "medication":
                all_meds.add(t["value"])
    if all_meds:
        lines.append("MEDICATIONS TAKEN")
        lines.append("-" * 40)
        for m in sorted(all_meds):
            lines.append(f"  • {m}")
        lines.append("")

    # Flare-ups
    flareups = _find_flareups(entries)
    if flareups:
        lines.append("NOTABLE EVENTS")
        lines.append("-" * 40)
        for f in flareups:
            lines.append(f"  ⚠ {f}")
        lines.append("")

    # Chronological log
    lines.append("DETAILED LOG (chronological)")
    lines.append("-" * 40)
    for e in entries:
        bar = _severity_bar(e["severity"])
        lines.append(f"  {e['timestamp']} | {e['name'].title()} | {e['severity']}/10 {bar}")
        if e["triggers"]:
            tlist = ", ".join(t["value"] for t in e["triggers"])
            lines.append(f"    Triggers: {tlist}")
        if e["notes"]:
            lines.append(f"    Notes: {e['notes']}")
    lines.append("")
    lines.append("=" * 60)
    lines.append("  END OF REPORT")
    lines.append("=" * 60)

    report = "\n".join(lines)
    if args.output:
        with open(args.output, "w") as f:
            f.write(report + "\n")
        print(f"Report exported to {args.output}")
    else:
        print(report)


# ─── Utilities ──────────────────────────────────────────────────────────────

def _parse_ts(ts):
    """Parse an ISO timestamp string flexibly."""
    # Handle date-only or datetime strings
    for fmt in ("%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
        try:
            return datetime.strptime(ts, fmt)
        except (ValueError, TypeError):
            continue
    # Fallback: try fromisoformat
    try:
        return datetime.fromisoformat(ts)
    except (ValueError, TypeError):
        pass
    # Last resort
    return datetime.now()


# ─── CLI ────────────────────────────────────────────────────────────────────

def build_parser():
    parser = argparse.ArgumentParser(
        description="Track symptoms over time and generate doctor-ready reports.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n"
               "  python3 symptom_tracker.py log --name headache --severity 7 --triggers 'poor sleep,stress'\n"
               "  python3 symptom_tracker.py correlate\n"
               "  python3 symptom_tracker.py export --output report.txt\n"
    )
    parser.add_argument("--db", default=DEFAULT_DB, help="Path to JSON database file")
    sub = parser.add_subparsers(dest="command", help="Available commands")

    # log
    p_log = sub.add_parser("log", help="Record a symptom entry")
    p_log.add_argument("--name", required=True, help="Symptom name (e.g. 'headache')")
    p_log.add_argument("--severity", type=int, required=True, help="Severity 1-10")
    p_log.add_argument("--time", help="Timestamp (ISO format, default: now)")
    p_log.add_argument("--notes", help="Additional notes")
    p_log.add_argument("--triggers", help="Comma-separated triggers (e.g. 'poor sleep,stress,humidity:high')")

    # timeline
    p_tl = sub.add_parser("timeline", help="Show chronological symptom log")
    p_tl.add_argument("--name", help="Filter by symptom name")
    p_tl.add_argument("--last", type=int, help="Show only last N days")

    # correlate
    sub.add_parser("correlate", help="Find trigger-symptom correlations")

    # summary
    sub.add_parser("summary", help="Generate a doctor-ready summary report")

    # flare-up
    sub.add_parser("flare-up", help="Detect worsening patterns")

    # heatmap
    p_hm = sub.add_parser("heatmap", help="Show severity heatmap (ASCII)")
    p_hm.add_argument("--name", help="Symptom name")
    p_hm.add_argument("--days", type=int, default=14, help="Number of days to show (default: 14)")

    # export
    p_ex = sub.add_parser("export", help="Export plain-text report for doctor visit")
    p_ex.add_argument("--output", "-o", help="Output file path (default: stdout)")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "log": cmd_log,
        "timeline": cmd_timeline,
        "correlate": cmd_correlate,
        "summary": cmd_summary,
        "flare-up": cmd_flareup,
        "heatmap": cmd_heatmap,
        "export": cmd_export,
    }

    cmd = commands.get(args.command)
    if cmd:
        cmd(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
