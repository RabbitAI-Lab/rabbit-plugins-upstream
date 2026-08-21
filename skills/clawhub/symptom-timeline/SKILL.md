---
name: symptom-timeline
version: 1.0.0
author: Denis Voronin
license: MIT
description: >
  Track symptoms over time and generate doctor-ready timelines. Correlates
  symptoms with food, weather, medication, activity, sleep, and stress.
  Detects patterns, flare-ups, and produces concise clinical reports.
---

# Symptom Timeline

Track symptoms over time. Find what triggers them. Generate doctor-ready reports.

## Quick Start

```bash
# Log a symptom with triggers
python3 scripts/symptom_tracker.py log \
  --name headache \
  --severity 7 \
  --triggers "poor sleep,stress,caffeine"

# View all entries chronologically
python3 scripts/symptom_tracker.py timeline

# Find what triggers your symptoms
python3 scripts/symptom_tracker.py correlate

# Get a doctor-ready summary
python3 scripts/symptom_tracker.py summary

# Export a plain-text report for your appointment
python3 scripts/symptom_tracker.py export --output report.txt
```

## Commands

| Command | Description |
|---------|-------------|
| `log` | Record a symptom (name, severity 1-10, time, notes, triggers) |
| `timeline` | Show chronological log, optionally filtered by name or date range |
| `correlate` | Detect trigger-symptom patterns and co-occurring symptoms |
| `summary` | Generate a doctor-ready report with trends and triggers |
| `flare-up` | Detect worsening patterns (consecutive high severity, sudden jumps) |
| `heatmap` | ASCII severity heatmap over days/weeks |
| `export` | Export a plain-text report for a doctor visit |

## Trigger Categories

The script auto-categorizes triggers into:

- **food** — meals, dairy, gluten, caffeine, alcohol, etc.
- **stress** — anxiety, work pressure, deadlines
- **weather** — humidity, barometric pressure, temperature
- **medication** — drugs, doses, missed medications
- **sleep** — insomnia, poor sleep, fatigue
- **activity** — exercise, prolonged sitting/standing

You can also use explicit prefixes: `food:dairy`, `weather:high humidity`.

## Data Storage

All data is stored in `symptom_db.json` (in the skill directory by default).
Use `--db /path/to/file.json` to specify a custom location.

## References

- [Symptom Tracking Guide](references/symptom-tracking-guide.md) — what to track for common conditions
- [Doctor Visit Prep](references/doctor-visit-prep.md) — how to present symptoms effectively
