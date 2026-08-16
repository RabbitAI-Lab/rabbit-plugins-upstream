---
name: packing-pro
description: Generates smart, categorized packing lists based on destination weather, trip duration, activities, and transport type. Produces weighted checklists with a critical-items section and weather-adaptive recommendations.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - travel
  - packing
  - checklist
  - productivity
  - planning
---

# Packing Pro

An agent skill that generates smart, categorized packing lists so you never forget essentials again.

## What It Does

- **Weather-adaptive** — selects clothing based on destination temperature/season (cold → thermals, beach → sunscreen, monsoon → rain gear).
- **Duration-aware** — scales clothing quantities to the number of days, with laundry buffer for longer trips.
- **Activity-driven** — adds specialized gear for hiking, swimming, business, skiing, photography, and more.
- **Transport-aware** — applies liquid limits for flights, adds car-trip accessories, etc.
- **Weighted** — estimates item weights so you can manage baggage limits.
- **Critical items** — highlights must-not-forget essentials (passport, medications, chargers) in a separate section.

## Quick Start

```bash
# Basic trip (interactive prompts)
python3 scripts/packing_pro.py

# Full specification via CLI flags
python3 scripts/packing_pro.py \
  --destination "Tokyo, Japan" \
  --duration 7 \
  --season winter \
  --activities hiking photography \
  --transport flight \
  --output checklist.json
```

## Input Parameters

| Parameter | Example | Description |
|---|---|---|
| `--destination` | `"Bali, Indonesia"` | Trip destination |
| `--duration` | `7` | Number of days |
| `--season` | `summer \| winter \| spring \| autumn` | Season of travel |
| `--temp-c` | `25` | Optional: override average temperature |
| `--activities` | `hiking swimming business` | Space-separated activity list |
| `--transport` | `flight \| train \| car \| bus` | Primary transport |
| `--output` | `checklist.json` | Save to file (default: print to stdout) |

## Output

The script produces a structured JSON packing list:

```json
{
  "destination": "Bali, Indonesia",
  "duration_days": 7,
  "season": "summer",
  "transport": "flight",
  "estimated_total_weight_g": 6800,
  "critical_items": [
    {"item": "Passport", "category": "documents", "weight_g": 30, "note": "Check expiry >6 months"}
  ],
  "categories": {
    "clothing": [
      {"item": "T-shirts", "quantity": 8, "weight_g": 150}
    ],
    "toiletries": [...],
    "electronics": [...],
    "activity_gear": [...]
  }
}
```

## Reference Documentation

- [`references/item-database.md`](references/item-database.md) — full catalog of packable items with weights
- [`references/weather-logic.md`](references/weather-logic.md) — weather and activity selection rules

## License

MIT © Denis Voronin
