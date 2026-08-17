---
name: hydration-hero
version: 1.0.0
author: Denis Voronin
license: MIT
description: >
  Smart water intake tracking based on body weight, weather, and activity
  level. Calculates personalized hydration targets, adjusts for caffeine
  and alcohol consumption, tracks streaks with gamification, generates
  hourly drinking schedule, and provides hydration education with urine
  color chart reference.
tags:
  - hydration
  - water
  - health
  - wellness
  - tracker
---

# Hydration Hero

A standalone command-line tool for smart water intake tracking. Calculates
your personalized hydration needs based on body weight, adjusts for weather
and activity, tracks your intake with gamified streaks, and generates an
optimal drinking schedule.

## Quick Start

```bash
# Set up your profile
python3 scripts/hydration_hero.py init

# Log water intake throughout the day
python3 scripts/hydration_hero.py log 250
python3 scripts/hydration_hero.py log 500

# Check progress
python3 scripts/hydration_hero.py status

# Log factors that change your needs
python3 scripts/hydration_hero.py activity --exercise 30 --intensity moderate
python3 scripts/hydration_hero.py weather --temp 32 --humidity 70
python3 scripts/hydration_hero.py caffeine --cups 2
python3 scripts/hydration_hero.py alcohol --drinks 3

# See your drinking schedule
python3 scripts/hydration_hero.py schedule

# Weekly report
python3 scripts/hydration_hero.py report week
```

## Commands

| Command | Description |
|---------|-------------|
| `init` | Create profile (weight, activity level, climate) |
| `log <ml>` | Log water intake (milliliters) |
| `log <ml> --oz` | Log in ounces instead |
| `status` | Show today's progress vs target |
| `target` | Show your calculated daily hydration target |
| `activity --exercise <min> --intensity <level>` | Log exercise (adds water need) |
| `weather --temp <C> --humidity <percent>` | Log weather (adjusts target) |
| `caffeine --cups <N>` | Log caffeine intake (diuretic effect) |
| `alcohol --drinks <N>` | Log alcohol (strong diuretic) |
| `schedule` | Generate hourly drinking schedule |
| `streak` | Show hydration streak |
| `report [week\|month]` | Period summary with charts |
| `color-check` | Urine color reference chart |
| `remind` | Show next drinking reminder time |

## How It Works

### Personalized Hydration Formula
Base target is calculated from body weight:

```
Base = Weight(kg) × 35 ml/day     (standard recommendation)
```

### Dynamic Adjustments
- **Exercise**: +350-700ml per 30 min depending on intensity
- **Hot weather** (>25°C): +500ml per 5°C above baseline
- **High humidity** (>70%): +300ml (reduced evaporative cooling)
- **Caffeine**: +150ml compensatory water per cup
- **Alcohol**: +400ml compensatory water per drink
- **Altitude** (>2500m): +500ml (dry air, increased respiration)
- **Pregnancy/nursing**: +300-700ml
- **Illness/fever**: +200ml per 1°C above normal

### Gamification
- **Daily goal completion streak** 🔥
- **Weekly achievement levels**: Bronze (5/7 days), Silver (6/7), Gold (7/7)
- **Hydration score**: based on consistency, not just volume
- **Milestone badges**: 7-day, 30-day, 100-day streaks

### Urine Color Reference
Includes the standard 8-level urine color chart for self-assessment:
- Levels 1-3: Well hydrated ✅
- Level 4: Slightly dehydrated 🟡
- Levels 5-6: Dehydrated 🔴
- Levels 7-8: Severely dehydrated — drink immediately ⚠️

## Data Storage

Data is stored in `~/.hydration_hero.json`. Delete to reset.

## References

- [Hydration Science](references/hydration-science.md)
- [Hydration Schedule Guide](references/schedule-guide.md)

## License

MIT © Denis Voronin
