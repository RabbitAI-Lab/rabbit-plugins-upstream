---
name: sleep-debt-calculator
version: 1.0.0
author: Denis Voronin
license: MIT
description: >
  Track sleep vs optimal, calculate accumulated sleep debt, and suggest
  evidence-based recovery schedules. Chronotype detection, quality-weighted
  sleep tracking, ASCII charts, and caffeine/alcohol impact monitoring.
tags:
  - sleep
  - health
  - tracker
  - wellness
---

# Sleep Debt Calculator

A standalone command-line tool for tracking sleep, calculating accumulated sleep
debt against age-based recommendations, and generating personalized recovery
schedules. Pure Python (stdlib only) with a JSON file database.

## Quick Start

```bash
# Set up your profile (age)
python3 scripts/sleep_debt.py init

# Log last night's sleep: bedtime wake quality notes
python3 scripts/sleep_debt.py log 23:30 07:15 4 "slept well, coffee at 3pm"

# See your debt
python3 scripts/sleep_debt.py debt

# How long to recover at 8.5h/night?
python3 scripts/sleep_debt.py recovery 8.5
```

## Commands

| Command | Description |
|---------|-------------|
| `init` | Create your profile (enter age for optimal calculation) |
| `log <bedtime> <wake> [quality 1-5] [notes]` | Record a sleep session |
| `debt` | Show current accumulated sleep debt |
| `recovery <hours_per_night>` | Calculate days to recover at given nightly hours |
| `optimal` | Show your personal optimal sleep based on age |
| `streak` | Show your logging consistency streak |
| `report [week\|month]` | Weekly or monthly summary with mini-chart |
| `schedule` | Suggest optimal bedtime tonight to minimize debt |
| `chronotype` | Detect early bird vs night owl from patterns |
| `chart [days]` | ASCII chart of sleep duration with optimal line |

## How It Works

### Sleep Debt Calculation
Sleep debt is the cumulative gap between your **effective sleep** and your
**age-based optimal** sleep. Effective sleep is duration weighted by quality:
6 hours of excellent sleep counts more than 8 hours of poor sleep.

### Quality-Weighted Sleep
Each sleep entry is weighted by quality (1-5):
- 5 (excellent): 100% restorative
- 4 (good): 92%
- 3 (average): 80%
- 2 (poor): 65%
- 1 (terrible): 45%

### Chronotype Detection
Your average bedtime over the past 14 nights determines your chronotype:
- Before 22:00 → Early Bird
- 22:00–23:30 → Balanced
- 23:30–00:30 → Night Owl
- After 00:30 → Extreme Night Owl

### Substance Impact Tracking
Notes mentioning caffeine or alcohol are flagged and correlated with quality
in reports.

## Database

Sleep data is stored in `~/.sleep_debt.json`. To start fresh, delete this file.

## References

- [Sleep Science Basics](references/sleep-science-basics.md)
- [Recovery Strategies](references/recovery-strategies.md)

## License

MIT © Denis Voronin
