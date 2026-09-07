---
name: storm-ready
description: "Use when a hurricane/typhoon, ice storm, tornado outbreak, atmospheric river, wildfire season, or blizzard is approaching your area, when building a household emergency kit, when deciding how much water and food to store, when sizing a generator or power station for outages, when an advisory or watch is issued and you don't know what to do in what order, or annually to audit family preparedness — profiles your region's real hazards (gulf-coast hurricanes demand 14-day supplies, tornado country demands shelter kits, wildfire WUI demands go-bags), sizes water/food/power for YOUR people and pets with real math, runs a gap audit against your inventory, and prints phase-by-phase countdown checklists from T-72h through the storm to recovery, with the life-safety rules (CO, flood water, downed lines) that kill people every year."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [emergency, preparedness, hurricane, storm, outage, generator, water-storage, family-safety]
---

# Storm Ready — Household Preparedness Audit & Planner

## Overview

Emergency preparedness advice fails people in two ways: it's generic ("have 72 hours of supplies" — meaningless in a 14-day gulf-coast outage), and it's unordered (a 200-item PDF where the life-safety items are indistinguishable from the nice-to-haves). When a named storm is 72 hours out, you don't need a brochure — you need to know what *your* household is missing, what to do *next*, and the math for how much water, food, and battery capacity *your* family actually needs.

This skill is that: region profiles that encode what each hazard actually demands (a hurricane county's 14-day standard vs. tornado country's minutes-long warning), household-specific sizing (4 people + 60-lb dog + CPAP machine = 63 gallons of water, 112,000 kcal, and a battery plan that respects compressor surge), a gap audit against what you've marked as having, and a phase-by-phase countdown checklist from T-72h to recovery — with the P0 rules (generator CO, flood-water depth, fridge discipline) that keep appearing in after-action reports for a reason.

## When to Use

- A watch/advisory is issued for your region and the storm is days out → `timeline`
- Building or reviewing a household emergency kit → `audit` (mark what you have, see the gaps)
- "How much water/food do we actually need to store?" → `water` / `food`
- Sizing a generator, power station, or battery backup → `power`
- Moving to a new region: understand what its hazards demand → `regions`
- Don't use for: active life-threatening emergencies (call local emergency services), tornado warnings already in progress (execute your existing plan, don't read docs), or real-time tracking (check NWS/national weather service).

## Region Profiles

| Profile | Water | Food | The real demand |
|---|---|---|---|
| hurricane-gulf | 14 d | 14 d | Grid down 1-3 wk, boil notices; county standard is 14 days |
| hurricane-atlantic | 7 d | 7 d | Days-long outages inland after landfall |
| tornado | 3 d | 3 d | Warning is MINUTES: safe room, helmets, shoes, whistle |
| ice-storm | 3 d | 5 d | Cold indoors is the killer; heat one room, CO alarm |
| atmospheric-river | 7 d | 5 d | Flooding contaminates water; boil notices follow |
| wildfire-wui | 3 d | 3 d | This is a GO kit: packed by May, 10-minute evacuation |
| blizzard-plains | 3 d | 7 d | Snowed IN for days: heat, cookable food, vehicle kit |
| generic | 3 d | 3 d | Ready.gov 72-hour baseline |

`regions` prints this with notes. Region drives: checklist items included, day-counts in quantities, and which countdown phases apply.

## Commands

```bash
# See region profiles and what each demands
python3 scripts/storm_ready.py regions

# Set up your household (people, pets with weights, region)
python3 scripts/storm_ready.py profile --region hurricane-gulf --people 4 \
    --pets "dog:60,cat:10"

# Gap audit: what you have (✓), partial (~), missing (✗) — P0 gaps listed last
python3 scripts/storm_ready.py audit
python3 scripts/storm_ready.py profile --mark-have radio first-aid flashlights
python3 scripts/storm_ready.py audit          # re-run: gaps shrink

# Sizing math for your household
python3 scripts/storm_ready.py water          # gallons + storage + purification
python3 scripts/storm_ready.py food           # kcal + pantry-basket plan
python3 scripts/storm_ready.py power --list   # known device loads
python3 scripts/storm_ready.py power --loads fridge,cpap,router-modem \
    --battery-wh 2000                          # Wh/day, runtime, surge, rules

# Countdown checklist when a storm is named
python3 scripts/storm_ready.py timeline --region hurricane-gulf

# Full demo on a gulf-coast family (4 people, 2 pets, CPAP)
python3 scripts/storm_ready.py example
```

Profile lives at `~/.storm-ready.json`. `--file` overrides on any command.

## The Math

- **Water:** 1 gal/person/day drinking+basic (Ready.gov) + pets at ~1 oz/lb/day + optional 50% hygiene cushion → total gallons with container-count breakdown (7-gal aquatainers / 2.5-gal jugs / bottle cases) and three purification fallbacks (boil, bleach dosing, filter limits).
- **Food:** people × days × 2,000 kcal with a pantry-rotation basket (canned meals first, calorie-dense no-cook foods, region-adjusted: cold regions get cookable options).
- **Power:** per-load W × h/day = Wh/day; fridge/freezer duty-cycled at 150 W × 8 h; **surge awareness** (compressor start ×3.5) for inverter/generator sizing; usable battery fraction 0.85 (inverter + depth-of-discharge); power-station ladder showing runtime for 500/1000/2000/3000/5000 Wh banks.

## Workflow

1. `regions` → pick your profile; `profile` → set people/pets/region.
2. `audit` → mark what you have (`profile --mark-have <ids>`); re-run until the P0 gap list is empty.
3. `water` / `food` → buy to the numbers, rotate with your pantry.
4. `power` → if you have medical devices or outages are common, size honestly (including surge); register medical needs with your utility.
5. When a storm is named: `timeline --region <yours>` → work top-to-bottom by phase; T-72h items exist because at T-12h the lines are long and the shelves empty.
6. After: photograph everything before cleanup, insurance first, DisasterAssistance.gov if declared.

## Common Pitfalls

1. **Running generators/grills indoors or in the garage.** CO kills silently every single storm, this is the #1 post-storm death cause that isn't water. Outdoors, ≥20 ft from any window/vent, CO alarm indoors. `power` repeats this because it must.
2. **Driving through flood water.** 6 in of moving water floats a car; 12 in takes an SUV. "Turn Around Don't Drown" is in the `during` phase for a reason.
3. **Generic 72-hour advice in a 14-day region.** A gulf-coast hurricane kit that would sail in Kansas is 5× undersized. The region profile exists precisely so the numbers match the hazard.
4. **Forgetting pets in the math.** A 60-lb dog drinks ~half a gallon a day and shelters won't take animals without shot records. Pet items are P0.
5. **Undersized inverters.** Nameplate watts ≠ surge. A fridge drawing 150 W running needs ~525 W for compressor start; peak-line sizing in `power` accounts for it, cheap listings don't.
6. **Storing water you never rotate.** Tap-water containers: refresh 6-12 months; keep bleach FRESH (it loses potency) and dated.
7. **Evacuating "to ride it out one more time."** If you're in an evacuation/surge zone and officials say go — GO. Every hurricane after-action report says the same thing: the people who died mostly could have left.
8. **Tape on windows.** Does nothing. Measured, cut, labeled plywood or tested film — installed at T-24h, not during the storm.

## Verification Checklist

- [ ] `python3 scripts/test_storm_ready.py` → ALL TESTS PASSED (35 assertions)
- [ ] `python3 scripts/storm_ready.py example` renders audit + water + power + timeline
- [ ] Profile set with correct region, people, and pets
- [ ] `audit` P0 gap list is empty before storm season starts
- [ ] Water/food stored to the computed numbers, dated for rotation
- [ ] Everyone in the household knows shutoffs, safe room, and meeting point
