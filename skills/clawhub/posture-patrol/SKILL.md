---
name: posture-patrol
version: 1.0.0
author: Denis Voronin
license: MIT
description: >
  Track your posture throughout the workday with manual logging, smart
  break reminders, ergonomic scoring, posture streaks, and trend analysis.
  Calculates spinal load, suggests desk stretches, tracks slouch patterns,
  and generates weekly posture reports with actionable recommendations.
tags:
  - posture
  - health
  - ergonomics
  - workplace
  - wellness
---

# Posture Patrol

A standalone command-line tool for tracking posture quality, scheduling
movement breaks, calculating spinal load, and building better sitting habits.
Pure Python (stdlib only) with a JSON file database.

## Quick Start

```bash
# Set up your profile
python3 scripts/posture_patrol.py init

# Log a posture check
python3 scripts/posture_patrol.py check good "feet flat, back straight"
python3 scripts/posture_patrol.py check poor "slouching forward"

# Schedule break reminders
python3 scripts/posture_patrol.py breaks --interval 30

# See today's score
python3 scripts/posture_patrol.py score

# Weekly report
python3 scripts/posture_patrol.py report week
```

## Commands

| Command | Description |
|---------|-------------|
| `init` | Create your profile (height, desk type) |
| `check <good\|fair\|poor> [notes]` | Log a posture observation |
| `score [today\|week]` | Show your posture score |
| `report [week\|month]` | Detailed report with charts and recommendations |
| `streak` | Show your good-posture streak |
| `breaks [--interval N]` | Generate a break reminder schedule |
| `stretch` | Show desk stretches for your problem areas |
| `spinal-load` | Calculate estimated spinal loading from posture data |
| `ergonomics` | Show ergonomic checklist and personalized recommendations |
| `pattern` | Identify when you're most likely to slouch |
| `goal [minutes]` | Set daily good-posture goal |

## How It Works

### Posture Scoring
Each check is rated 1-3:
- **Good (3)**: Ears over shoulders, shoulders back, feet flat, lumbar supported
- **Fair (2)**: Slight forward lean, one foot up, shoulders rounded slightly
- **Poor (1)**: Slouched, hunched forward, head far forward, legs crossed

Daily score = average of all checks × 33.3 (scaled to 0-100).

### Spinal Load Calculation
Poor posture increases the effective load on your cervical spine:
- Neutral head (0°): ~10-12 lbs on neck
- 15° forward: ~27 lbs
- 30° forward: ~40 lbs
- 45° forward: ~49 lbs
- 60° forward: ~60 lbs

The tool estimates cumulative excess spinal load from your posture data.

### Pattern Detection
Analyzes your check times to identify:
- **High-risk hours** — when you're most likely to slouch
- **Post-lunch dip** — posture degradation after eating
- **End-of-day fatigue** — slouching increases with work hours
- **Meeting vs. solo work** — if you log context

### Desk Stretches
Recommends stretches based on your problem patterns:
- Neck rolls for forward head posture
- Shoulder blade squeezes for rounded shoulders
- Hip flexor stretches for prolonged sitting
- Chin tucks for text neck

## Data Storage

Data is stored in `~/.posture_patrol.json`. Delete to reset.

## References

- [Spinal Biomechanics](references/spinal-biomechanics.md)
- [Desk Ergonomics Guide](references/ergonomics-guide.md)

## License

MIT © Denis Voronin
