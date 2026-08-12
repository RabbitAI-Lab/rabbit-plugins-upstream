# Usage Guide

Detailed reference for `medication_commander.py` commands and output formats.

## Commands

### `schedule medications.json`

Generates a daily schedule from the medication list.

**Output:**

```json
{
  "schedule": [
    {
      "time": "08:00",
      "medications": [
        {"name": "Metformin", "dose": "500 mg"}
      ],
      "note": "Take with food"
    }
  ],
  "warnings": [
    "Warfarin and Aspirin: significantly increased bleeding risk (major)"
  ]
}
```

### `interactions medications.json`

Checks all pairs of medications against the interaction database.

**Output:**

```json
{
  "checked_pairs": 3,
  "interactions_found": 1,
  "interactions": [
    {
      "drug_a": "Warfarin",
      "drug_b": "Aspirin",
      "severity": "major",
      "description": "Significantly increased bleeding risk",
      "recommendation": "Avoid co-administration; consult prescribing physician immediately."
    }
  ]
}
```

### `checklist medications.json`

Outputs a plain-text printable daily checklist.

**Output:**

```text
═══════════════════════════════════════════
          DAILY MEDICATION CHECKLIST
═══════════════════════════════════════════

Date: ____________

Morning (08:00)
  [ ] Metformin — 500 mg — Take with food
  [ ] Warfarin — 5 mg

Evening (20:00)
  [ ] Metformin — 500 mg

───────────────────────────────────────────
⚠️  INTERACTION WARNING:
    Warfarin + Aspirin → major bleeding risk
───────────────────────────────────────────
```

### `adhere --med NAME --time HH:MM [--taken | --missed]`

Records a dose as taken or missed. Adherence data is stored in
`~/.medication_commander_adherence.json`.

**Output:**

```json
{
  "medication": "Metformin",
  "time": "08:00",
  "status": "taken",
  "adherence_rate": 92.5
}
```

### `refills medications.json`

Checks each medication's remaining supply and flags those needing refill
within 7 days.

**Output:**

```json
{
  "refills_needed": [
    {
      "name": "Warfarin",
      "days_remaining": 4,
      "pills_remaining": 4,
      "pills_per_day": 1
    }
  ],
  "all_clear": []
}
```

## Adherence Data Format

Adherence records are stored in `~/.medication_commander_adherence.json`:

```json
{
  "Metformin": {
    "08:00": {"taken": 18, "missed": 2},
    "20:00": {"taken": 19, "missed": 1}
  },
  "Warfarin": {
    "09:00": {"taken": 20, "missed": 0}
  }
}
```

The adherence rate is calculated as:

```
adherence_rate = (total_taken / (total_taken + total_missed)) × 100
```

## Tips

- Run `interactions` whenever a medication is added or changed.
- Run `schedule` and print the `checklist` each morning.
- Run `refills` weekly to stay ahead of pharmacy visits.
- Use `adhere` after each dose to maintain accurate tracking.
