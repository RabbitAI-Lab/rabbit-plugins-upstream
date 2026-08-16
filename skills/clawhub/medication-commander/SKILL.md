---
name: medication-commander
description: Manages medication schedules, detects drug interactions, tracks adherence, and generates refill reminders. Produces safe daily schedules and printable checklists from a medication list.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - health
  - medication
  - scheduling
  - safety
  - adherence
---

# Medication Commander

A medication management agent skill that helps patients (especially elderly and chronic-disease patients) safely manage complex medication regimens.

## What It Does

- **Schedule generation** — takes a list of medications (name, dose, frequency, times) and produces a safe, conflict-free daily schedule.
- **Drug interaction checking** — cross-references a built-in database of 30+ common drug-drug interactions and warns about severity (major / moderate / minor).
- **Adherence tracking** — records doses taken / missed and calculates adherence percentage.
- **Refill reminders** — calculates remaining days of supply based on pills remaining and daily usage, flagging refills needed within 7 days.
- **Printable checklist** — outputs a plain-text daily checklist that can be printed or read aloud.

## Quick Start

```bash
# Generate a schedule from a medication list (JSON)
python3 scripts/medication_commander.py schedule medications.json

# Check interactions between medications
python3 scripts/medication_commander.py interactions medications.json

# Generate a printable daily checklist
python3 scripts/medication_commander.py checklist medications.json

# Track adherence (mark a dose as taken)
python3 scripts/medication_commander.py adhere --med "Metformin" --time "08:00" --taken

# Check refill status
python3 scripts/medication_commander.py refills medications.json
```

## Input Format

`medications.json`:

```json
[
  {
    "name": "Metformin",
    "dose": "500 mg",
    "frequency": "twice daily",
    "times": ["08:00", "20:00"],
    "pills_remaining": 42,
    "pills_per_dose": 1
  },
  {
    "name": "Warfarin",
    "dose": "5 mg",
    "frequency": "once daily",
    "times": ["09:00"],
    "pills_remaining": 10,
    "pills_per_dose": 1
  }
]
```

## Output

Each command produces structured JSON to stdout:

- **schedule** — timeline of doses grouped by time slot, with spacing notes.
- **interactions** — list of detected interaction pairs with severity, description, and recommendation.
- **checklist** — plain-text, printable daily checklist.
- **adhere** — updated adherence record (stored in `~/.medication_commander_adherence.json`).
- **refills** — medications needing refill within 7 days, with days-of-supply remaining.

## Reference Documentation

See [`references/interactions.md`](references/interactions.md) for the full interaction database reference, and [`references/usage.md`](references/usage.md) for detailed usage and output examples.

## Safety Disclaimer

This tool is for informational and organizational purposes only. It is **not** a substitute for professional medical advice. Always consult a doctor or pharmacist about drug interactions, dosing changes, or adverse effects.
