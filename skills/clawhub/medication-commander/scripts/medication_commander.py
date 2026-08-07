#!/usr/bin/env python3
"""
medication_commander.py — Medication schedule, interaction, adherence, and refill manager.

Usage:
    python3 medication_commander.py schedule     medications.json
    python3 medication_commander.py interactions medications.json
    python3 medication_commander.py checklist    medications.json
    python3 medication_commander.py refills      medications.json
    python3 medication_commander.py adhere --med "Metformin" --time "08:00" --taken
    python3 medication_commander.py adhere --med "Metformin" --time "08:00" --missed

Standard library only. Python 3.8+.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from itertools import combinations

# ---------------------------------------------------------------------------
# Interaction Database — 35 common drug-drug interaction pairs
# ---------------------------------------------------------------------------
INTERACTIONS = [
    # --- Major ---
    {"drug_a": "warfarin", "drug_b": "aspirin", "severity": "major",
     "description": "Significantly increased bleeding risk",
     "recommendation": "Avoid co-administration; consult prescribing physician immediately."},
    {"drug_a": "warfarin", "drug_b": "ibuprofen", "severity": "major",
     "description": "Increased anticoagulant effect and GI bleeding",
     "recommendation": "Use acetaminophen instead; consult physician."},
    {"drug_a": "warfarin", "drug_b": "amiodarone", "severity": "major",
     "description": "Markedly increases warfarin plasma levels",
     "recommendation": "Reduce warfarin dose 25-50% under medical supervision."},
    {"drug_a": "warfarin", "drug_b": "fluconazole", "severity": "major",
     "description": "Inhibits warfarin metabolism, raising bleeding risk",
     "recommendation": "Monitor INR closely; consider alternative antifungal."},
    {"drug_a": "warfarin", "drug_b": "sulfamethoxazole", "severity": "major",
     "description": "Enhanced anticoagulant effect",
     "recommendation": "Avoid combination; use alternative antibiotic."},
    {"drug_a": "warfarin", "drug_b": "ciprofloxacin", "severity": "major",
     "description": "Increased warfarin effect and bleeding",
     "recommendation": "Monitor INR; consider alternative antibiotic."},
    {"drug_a": "warfarin", "drug_b": "metronidazole", "severity": "major",
     "description": "Potent inhibition of warfarin metabolism",
     "recommendation": "Avoid combination or reduce warfarin dose significantly."},
    {"drug_a": "lisinopril", "drug_b": "spironolactone", "severity": "major",
     "description": "Severe hyperkalemia risk",
     "recommendation": "Monitor potassium frequently; consider alternative."},
    {"drug_a": "enalapril", "drug_b": "potassium chloride", "severity": "major",
     "description": "Hyperkalemia",
     "recommendation": "Monitor potassium closely; adjust dose."},
    {"drug_a": "lisinopril", "drug_b": "potassium chloride", "severity": "major",
     "description": "Hyperkalemia",
     "recommendation": "Monitor potassium closely; adjust dose."},
    {"drug_a": "clonidine", "drug_b": "propranolol", "severity": "major",
     "description": "Rebound hypertension if clonidine withdrawn",
     "recommendation": "Withdraw beta-blocker before tapering clonidine."},
    {"drug_a": "fluoxetine", "drug_b": "phenelzine", "severity": "major",
     "description": "Serotonin syndrome risk",
     "recommendation": "Allow 14-day washout between MAOI and SSRI."},
    {"drug_a": "tramadol", "drug_b": "fluoxetine", "severity": "major",
     "description": "Serotonin syndrome risk",
     "recommendation": "Avoid combination; consider alternative pain management."},
    {"drug_a": "tramadol", "drug_b": "phenelzine", "severity": "major",
     "description": "Serotonin syndrome and seizure risk",
     "recommendation": "Avoid combination."},
    {"drug_a": "hydrocodone", "drug_b": "alprazolam", "severity": "major",
     "description": "Severe respiratory depression",
     "recommendation": "Avoid co-prescription; if unavoidable, reduce doses."},
    {"drug_a": "oxycodone", "drug_b": "lorazepam", "severity": "major",
     "description": "Respiratory depression risk",
     "recommendation": "Avoid combination; monitor respiration if combined."},
    {"drug_a": "methotrexate", "drug_b": "trimethoprim", "severity": "major",
     "description": "Increased methotrexate toxicity (bone marrow suppression)",
     "recommendation": "Avoid combination; use alternative antibiotic."},
    {"drug_a": "simvastatin", "drug_b": "amiodarone", "severity": "major",
     "description": "High rhabdomyolysis risk",
     "recommendation": "Do not exceed simvastatin 20 mg/day with amiodarone."},
    {"drug_a": "simvastatin", "drug_b": "clarithromycin", "severity": "major",
     "description": "Rhabdomyolysis risk",
     "recommendation": "Hold statin during clarithromycin therapy."},
    {"drug_a": "digoxin", "drug_b": "amiodarone", "severity": "major",
     "description": "Increased digoxin toxicity",
     "recommendation": "Reduce digoxin dose 50%; monitor levels."},
    {"drug_a": "digoxin", "drug_b": "verapamil", "severity": "major",
     "description": "Elevated digoxin levels",
     "recommendation": "Monitor digoxin levels; adjust dose."},
    {"drug_a": "theophylline", "drug_b": "ciprofloxacin", "severity": "major",
     "description": "Theophylline toxicity",
     "recommendation": "Reduce theophylline dose; monitor levels."},
    {"drug_a": "lithium", "drug_b": "ibuprofen", "severity": "major",
     "description": "Increased lithium levels (toxicity)",
     "recommendation": "Monitor lithium levels; consider acetaminophen."},
    {"drug_a": "lithium", "drug_b": "hydrochlorothiazide", "severity": "major",
     "description": "Reduced lithium excretion, toxicity",
     "recommendation": "Monitor lithium levels closely; adjust dose."},
    # --- Moderate ---
    {"drug_a": "simvastatin", "drug_b": "diltiazem", "severity": "moderate",
     "description": "Increased statin levels, myopathy risk",
     "recommendation": "Do not exceed simvastatin 10 mg/day with diltiazem."},
    {"drug_a": "metformin", "drug_b": "cimetidine", "severity": "moderate",
     "description": "Decreased metformin clearance",
     "recommendation": "Monitor for lactic acidosis; consider alternative."},
    {"drug_a": "ramipril", "drug_b": "spironolactone", "severity": "moderate",
     "description": "Hyperkalemia risk",
     "recommendation": "Monitor potassium levels."},
    {"drug_a": "gabapentin", "drug_b": "hydrocodone", "severity": "moderate",
     "description": "Increased CNS depression",
     "recommendation": "Monitor for sedation; adjust doses as needed."},
    {"drug_a": "amlodipine", "drug_b": "simvastatin", "severity": "moderate",
     "description": "Increased statin levels",
     "recommendation": "Do not exceed simvastatin 20 mg/day."},
    {"drug_a": "sertraline", "drug_b": "ibuprofen", "severity": "moderate",
     "description": "Increased GI bleeding risk",
     "recommendation": "Consider PPI co-therapy; monitor for bleeding."},
    {"drug_a": "clopidogrel", "drug_b": "omeprazole", "severity": "moderate",
     "description": "Reduced clopidogrel activation",
     "recommendation": "Use pantoprazole instead of omeprazole."},
    {"drug_a": "levothyroxine", "drug_b": "calcium carbonate", "severity": "moderate",
     "description": "Decreased levothyroxine absorption",
     "recommendation": "Separate doses by at least 4 hours."},
    {"drug_a": "levothyroxine", "drug_b": "iron sulfate", "severity": "moderate",
     "description": "Decreased levothyroxine absorption",
     "recommendation": "Separate doses by at least 4 hours."},
    {"drug_a": "tamsulosin", "drug_b": "tadalafil", "severity": "moderate",
     "description": "Orthostatic hypotension",
     "recommendation": "Monitor blood pressure; separate dosing times."},
    # --- Minor ---
    {"drug_a": "acetaminophen", "drug_b": "warfarin", "severity": "minor",
     "description": "Minor INR increase with chronic high-dose use",
     "recommendation": "Keep acetaminophen under 2 g/day; monitor INR."},
]

ADHERENCE_FILE = os.path.expanduser("~/.medication_commander_adherence.json")

# Common food / timing notes
FOOD_NOTES = {
    "metformin": "Take with food",
    "ibuprofen": "Take with food",
    "aspirin": "Take with food",
    "iron sulfate": "Take on empty stomach with vitamin C",
    "levothyroxine": "Take on empty stomach, 30 min before breakfast",
    "alendronate": "Take on empty stomach, stay upright 30 min",
    "prednisone": "Take with food",
    "doxycycline": "Take with water, avoid dairy",
}


def load_medications(path):
    """Load medication list from JSON file."""
    with open(path, "r") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Medication file must contain a JSON array.")
    return data


def normalize(name):
    """Normalize a drug name for matching (lowercase, stripped)."""
    return name.strip().lower()


def check_interactions(medications):
    """Check all pairs of medications against the interaction database."""
    names = [normalize(m["name"]) for m in medications]
    found = []
    for pair in combinations(range(len(names)), 2):
        a, b = names[pair[0]], names[pair[1]]
        for entry in INTERACTIONS:
            da, db = entry["drug_a"], entry["drug_b"]
            if (a == da and b == db) or (a == db and b == da):
                found.append({
                    "drug_a": medications[pair[0]]["name"],
                    "drug_b": medications[pair[1]]["name"],
                    "severity": entry["severity"],
                    "description": entry["description"],
                    "recommendation": entry["recommendation"],
                })
    return found


def generate_schedule(medications):
    """Generate a daily schedule sorted by time."""
    slots = {}
    warnings = []
    interactions = check_interactions(medications)
    for ix in interactions:
        warnings.append(
            f"{ix['drug_a']} and {ix['drug_b']}: {ix['description']} ({ix['severity']})"
        )
    for med in medications:
        norm = normalize(med["name"])
        note = FOOD_NOTES.get(norm, "")
        for t in med.get("times", []):
            slots.setdefault(t, []).append(
                {"name": med["name"], "dose": med["dose"], "note": note}
            )
    schedule = []
    for t in sorted(slots.keys()):
        schedule.append({"time": t, "medications": slots[t]})
    return {"schedule": schedule, "warnings": warnings}


def time_label(t):
    """Convert HH:MM to a readable period label."""
    try:
        hour = int(t.split(":")[0])
    except (ValueError, IndexError):
        return "Other"
    if hour < 12:
        return "Morning"
    elif hour < 17:
        return "Afternoon"
    elif hour < 21:
        return "Evening"
    return "Night"


def generate_checklist(medications):
    """Generate a plain-text printable daily checklist."""
    sched = generate_schedule(medications)
    lines = []
    sep = "=" * 50
    lines.append(sep)
    lines.append("          DAILY MEDICATION CHECKLIST")
    lines.append(sep)
    lines.append("")
    lines.append("Date: ____________")
    lines.append("")
    current_period = None
    for slot in sched["schedule"]:
        period = time_label(slot["time"])
        if period != current_period:
            current_period = period
            lines.append(f"{period} ({slot['time']})")
        for med in slot["medications"]:
            note_text = f" — {med['note']}" if med["note"] else ""
            lines.append(f"  [ ] {med['name']} — {med['dose']}{note_text}")
        lines.append("")
    # Interaction warnings
    if sched["warnings"]:
        sub = "─" * 50
        lines.append(sub)
        lines.append("⚠️  INTERACTION WARNINGS:")
        for w in sched["warnings"]:
            lines.append(f"    • {w}")
        lines.append(sub)
    else:
        lines.append("✓ No known interactions detected.")
    lines.append("")
    lines.append(sep)
    return "\n".join(lines)


def load_adherence():
    """Load adherence data from file."""
    if os.path.exists(ADHERENCE_FILE):
        try:
            with open(ADHERENCE_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_adherence(data):
    """Save adherence data to file."""
    with open(ADHERENCE_FILE, "w") as f:
        json.dump(data, f, indent=2)


def record_adherence(med_name, time_str, taken):
    """Record a dose as taken or missed and return updated adherence rate."""
    data = load_adherence()
    key = med_name.strip()
    if key not in data:
        data[key] = {}
    if time_str not in data[key]:
        data[key][time_str] = {"taken": 0, "missed": 0}
    if taken:
        data[key][time_str]["taken"] += 1
    else:
        data[key][time_str]["missed"] += 1
    save_adherence(data)
    total_taken = sum(s["taken"] for s in data[key].values())
    total_missed = sum(s["missed"] for s in data[key].values())
    total = total_taken + total_missed
    rate = round((total_taken / total) * 100, 1) if total > 0 else 0.0
    return {
        "medication": key,
        "time": time_str,
        "status": "taken" if taken else "missed",
        "adherence_rate": rate,
    }


def check_refills(medications, threshold_days=7):
    """Check which medications need refills within threshold_days."""
    refills_needed = []
    all_clear = []
    for med in medications:
        pills_remaining = med.get("pills_remaining", 0)
        pills_per_dose = med.get("pills_per_dose", 1)
        times = med.get("times", [])
        doses_per_day = len(times) if times else 1
        pills_per_day = doses_per_day * pills_per_dose
        if pills_per_day == 0:
            days_remaining = 999
        else:
            days_remaining = pills_remaining // pills_per_day
        entry = {
            "name": med["name"],
            "days_remaining": days_remaining,
            "pills_remaining": pills_remaining,
            "pills_per_day": pills_per_day,
        }
        if days_remaining <= threshold_days:
            refills_needed.append(entry)
        else:
            all_clear.append(entry)
    return {"refills_needed": refills_needed, "all_clear": all_clear}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Medication schedule, interaction, and adherence manager."
    )
    sub = parser.add_subparsers(dest="command")

    p_sched = sub.add_parser("schedule", help="Generate daily schedule")
    p_sched.add_argument("file", help="Path to medications JSON file")

    p_inter = sub.add_parser("interactions", help="Check drug interactions")
    p_inter.add_argument("file", help="Path to medications JSON file")

    p_check = sub.add_parser("checklist", help="Generate printable checklist")
    p_check.add_argument("file", help="Path to medications JSON file")

    p_refill = sub.add_parser("refills", help="Check refill status")
    p_refill.add_argument("file", help="Path to medications JSON file")
    p_refill.add_argument("--threshold", type=int, default=7,
                          help="Days threshold for refill alert (default: 7)")

    p_adhere = sub.add_parser("adhere", help="Record dose adherence")
    p_adhere.add_argument("--med", required=True, help="Medication name")
    p_adhere.add_argument("--time", required=True, help="Scheduled time HH:MM")
    group = p_adhere.add_mutually_exclusive_group(required=True)
    group.add_argument("--taken", action="store_true", help="Mark dose as taken")
    group.add_argument("--missed", action="store_true", help="Mark dose as missed")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "schedule":
        meds = load_medications(args.file)
        result = generate_schedule(meds)
        print(json.dumps(result, indent=2))

    elif args.command == "interactions":
        meds = load_medications(args.file)
        found = check_interactions(meds)
        result = {
            "checked_pairs": len(list(combinations(range(len(meds)), 2))),
            "interactions_found": len(found),
            "interactions": found,
        }
        print(json.dumps(result, indent=2))

    elif args.command == "checklist":
        meds = load_medications(args.file)
        print(generate_checklist(meds))

    elif args.command == "refills":
        meds = load_medications(args.file)
        result = check_refills(meds, args.threshold)
        print(json.dumps(result, indent=2))

    elif args.command == "adhere":
        result = record_adherence(args.med, args.time, args.taken)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
