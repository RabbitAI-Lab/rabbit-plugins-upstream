---
name: seed-calendar-planner
description: "Use when planning a vegetable garden, deciding when to start seeds indoors versus direct-sowing, scheduling succession plantings, sizing seed trays and transplant dates, or figuring out what can still be sown now for a fall harvest — builds a personalized seed-starting calendar from your last/first frost dates with per-crop windows, tray math, row-footage estimates, succession schedules, and optional moon-phase annotations."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [garden, seeds, vegetable-garden, frost-dates, succession-planting, seed-starting, calendar]
---

# Seed Calendar Planner

## Overview

Every seed packet says the same useless thing: *"sow after all danger of frost has passed."* That's not a plan — it's a shrug. Real gardens have ten crops that each want different treatment: tomatoes sown indoors 7 weeks before your last frost, peas outside 6 weeks *before* it, lettuce re-sown every 2 weeks until fall, carrots sown by late July if you want a fall crop, garlic going in a month before first frost. Getting these wrong is the #1 beginner failure mode: leggy seedlings started too early, tender peppers transplanted into cold soil, and a barren August garden because everything was planted in one May weekend.

This skill turns two dates — your last spring frost and first fall frost — into a complete, dated action calendar for your specific crop list, plus the logistics numbers people always forget: how many tray cells you need for 4 people's worth of tomatoes (with a 20% germination buffer), how many row-feet your garden bed must hold, and when each succession sowing should happen so you're not drowning in lettuce in June and buying it in September.

## When to Use

- "When should I start my tomato/pepper/broccoli seeds?" (indoors, with exact dates)
- "What can I plant right now?" / "Is it too late to plant X?"
- "I want a fall garden — what do I sow and by when?"
- Planning succession sowings so salad greens don't all mature at once
- Sizing seed-starting: how many trays, cells, and shelf-weeks a garden needs
- "Is it too late in the season to start anything?"
- Don't use for: indoor/herbs-only windowsill gardens, greenhouse production scheduling with heated beds, or permaculture design. This is frost-date-driven annual vegetable planning.

## Inputs You Need

1. **Last spring frost date** (the date with ~50% probability of no frost after it). Find yours from NOAA plant hardiness/frost data (weather.gov), your state extension service, or the `frost --zone` helper (rough estimates — verify locally).
2. **First fall frost date** (same idea, reversed).
3. **Your crop list** and household size (people to feed).

Everything else has library defaults (spacing, plants-per-person, maturity days, succession intervals) in `references/seed-crop-library.md`.

## Commands

```bash
# Browse the 35-crop library: maturity, sowing style, spacing, succession interval
python3 scripts/seed_calendar.py crops
python3 scripts/seed_calendar.py crops tomato        # one crop, full detail

# Rough frost-date estimates by zone (VERIFY with local data before relying on)
python3 scripts/seed_calendar.py frost --zone 6b

# One crop, full dated timeline
python3 scripts/seed_calendar.py plan --crop tomato --last-frost 2026-05-15 \
    --first-frost 2026-10-05 --people 4

# Whole-garden calendar from a crop list (+ people count), with tray + row-feet tables
python3 scripts/seed_calendar.py garden --crops "tomato,pepper,lettuce,carrot,pea,bean,kale,zucchini" \
    --last-frost 2026-05-15 --first-frost 2026-10-05 --people 4

# Succession schedule for one crop between two dates
python3 scripts/seed_calendar.py succession --crop lettuce --from 2026-04-15 --until 2026-09-01 \
    --first-frost 2026-10-05

# Moon-phase annotations on all sow events (folklore, clearly labeled)
python3 scripts/seed_calendar.py garden --crops "carrot,lettuce" --last-frost 2026-05-15 --moon

# Machine-readable output
python3 scripts/seed_calendar.py plan --crop broccoli --last-frost 2026-05-15 --json
```

## How It Works

Every crop in the library carries the numbers that drive the calendar:

| Field | Drives | Example (tomato) |
|---|---|---|
| `start` | indoor / direct / either | indoor |
| `wks_indoor` | weeks before last frost to sow indoors | 7 |
| `transplant_delay` | days after last frost to transplant (soil warmth) | +14 |
| `dt` | days to harvest from transplant/sow | 65 |
| `frost_class` | hardy / half-hardy / tender → sow windows + fall buffer | tender |
| `succ` | succession interval in days (None = single planting) | None |
| `per_person` | plants per person for steady supply | 3 |
| `spacing_in` | in-row spacing → row-feet needed | 24 |

Derived events:

```
indoor sow    = last_frost − wks_indoor×7
harden off    = transplant − 7        pot-up = transplant − 14 (solanaceae)
transplant    = last_frost + transplant_delay   (negative delay for hardy brassicas)
direct sow    = window [last_frost + win_start, last_frost + win_end]
fall sow-by   = first_frost + frost_buffer − dt − 7      (ripening buffer)
succession    = every `succ` days while (sow + dt) ≤ first_frost + frost_buffer
harvest ~     = transplant/sow date + dt
```

Tray math for indoor crops: `cells = ceil(plants × 1.2)` germination buffer, `trays = ceil(cells / 72)` (standard 72-cell flat; 50/32-cell math shown too). Row-feet: `plants × spacing_in ÷ 12`.

## Reading the Output

Events are sorted by date and tagged:

```
2026-03-27  SOW-INDOORS   tomato     15 cells → 1 tray (72-cell); bottom heat 25°C
2026-05-08  POT-UP        tomato     into 4" pots if crowded
2026-05-22  HARDEN-OFF    tomato     7 days, 1h outdoors → full day
2026-05-29  TRANSPLANT    tomato     soil ≥ 15°C; bury stem to first leaves
2026-07-03  HARVEST ~     tomato     ±2 weeks, first ripe fruit
```

Dates already past when you run the tool are flagged `(PAST)` with recovery advice ("buy transplants instead"). Fall sow-by dates that are already past are flagged as missed for the year.

## Common Pitfalls

1. **Trusting zone-based frost dates blindly.** Zone is average *winter* cold, not last-frost timing; elevation and microclimate shift dates by weeks. Use `frost --zone` only as a starting guess, then verify with local extension data.
2. **Starting seeds too early "to get a jump."** Tomatoes sown 12 weeks early become leggy, root-bound, and transplant worse than 7-week plants. The calendar dates *are* the jump.
3. **Ignoring soil temperature for tender crops.** Peppers transplanted into soil below 18°C stall for weeks. The `transplant_delay` values encode the wait; don't shortcut it.
4. **One-and-done spring planting.** Without succession sowings, lettuce/bush beans/radish all mature in a 2-week glut, then stop. Follow the succession dates.
5. **Forgetting the fall garden exists.** July is not "over" — it's the deadline for fall carrots/beets/broccoli. Watch the SOW-BY-FALL events.
6. **Treating moon-phase annotations as agronomy.** They're traditional folklore included because gardeners ask; no yield evidence. Use `--moon` for fun, not for decisions.

## Verification Checklist

- [ ] Frost dates verified against local extension/NOAA data (not just zone guess)
- [ ] Every indoor crop appears in the tray table with cells/trays count
- [ ] Succession crops show multiple SOW dates spanning the season
- [ ] SOW-BY-FALL dates checked against your actual first-frost probability date
- [ ] Run with `--json` when feeding the calendar into another tool
