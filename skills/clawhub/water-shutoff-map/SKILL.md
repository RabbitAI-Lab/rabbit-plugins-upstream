---
name: water-shutoff-map
description: "Use before a plumbing emergency, when moving into a new home, before DIY repairs, when a pipe bursts or a toilet overflows, or when creating a household emergency reference sheet — walks you through locating every water shutoff in your home (main, fixture stops, water heater, irrigation), records what you find into a durable JSON registry with photos, generates a printable emergency card for the fridge, and gives the 3-step first response for floods, burst pipes, and overflowing fixtures."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [home, plumbing, emergency-preparedness, water-shutoff, maintenance, safety]
---

# Water Shutoff Map

## Overview

A pipe bursts. Water is spreading across the floor. The main shutoff is *somewhere* — basement? Crawl space? By the street? The average person has never turned it and doesn't know where it is, and a homeowner wastes precious minutes searching while the damage grows. Burst-flex-line claims average $10,000+, and response time is the single biggest controllable factor: every minute of flow is roughly 2–5 gallons onto your floors.

This skill solves the "know before you need it" problem in two parts:

1. **A guided location procedure** (`references/locating-shutoffs.md`) — where shutoffs hide by home type (basement, slab, crawlspace, condo), how to identify each valve type, how to test it safely, and what to do if it's stuck (the #1 discovery people make the hard way).
2. **A registry + emergency card generator** (`scripts/shutoff_registry.py`) — record every valve you find with location, type, tool needed, direction, test date. Validate the registry for completeness, print a fridge card with the 3-step first response, and export JSON so your household (and your agent) always knows where everything is.

## When to Use

- **Moving into any home** — the very first weekend, before unpacking the kitchen
- **Before DIY plumbing work** — replacing a faucet, toilet flapper, dishwasher, water heater
- **Leaving town / freezing weather** — confirm the main works and know how to drain down
- **Creating a household emergency reference** for family members, babysitters, renters
- **After the fact**: a plumber showed you a valve — log it so it's never lost knowledge again
- **Right now, during a leak**: jump to *Emergency First Response* below
- Don't use for: gas shutoffs (different tool/procedure), electrical issues, or municipal supply problems outside your property line.

## Emergency First Response (memorize this much)

1. **Kill the fixture if you can** — angle stop under the toilet/sink (clockwise). Fixture stop handles the 80% case with zero tools.
2. **If you can't isolate it, kill the house** — main shutoff clockwise. It's stiff: use a wrench if needed; never force half-way — full closed or leave it.
3. **Then damage control** — power off the affected area if water is near outlets (breaker first), towels/shop-vac, move valuables, then call a plumber and your insurer (mitigation duty starts immediately).

Run `python3 scripts/shutoff_registry.py drill` for a 60-second quarterly rehearsal script.

## Commands

```bash
# Start / edit the registry (interactive, or via flags in one shot)
python3 scripts/shutoff_registry.py add --id main --label "Main shutoff" \
    --location "Basement, east wall behind furnace" --type gate \
    --tool "12in crescent wrench" --direction clockwise --tested 2026-08-30 \
    --notes "Stiff first 2 turns; exercise annually"
python3 scripts/shutoff_registry.py add --id water-heater --label "Water heater" \
    --location "Garage, cold inlet above unit" --type ball --direction perpendicular \
    --tested 2026-08-30

# Guided entry — prompts for the fields that matter
python3 scripts/shutoff_registry.py add --interactive

# See what you've recorded and what's missing
python3 scripts/shutoff_registry.py list
python3 scripts/shutoff_registry.py validate

# Printable fridge card with the 3-step response + your valve table
python3 scripts/shutoff_registry.py card > shutoff-card.txt

# Quarterly rehearsal script (the thing that makes this real)
python3 scripts/shutoff_registry.py drill

# Where things hide, by home type — the hunting guide
python3 scripts/shutoff_registry.py hunt --home basement
python3 scripts/shutoff_registry.py hunt --home slab

# Export for other tools / your agent
python3 scripts/shutoff_registry.py export --json
```

Registry lives at `~/.shutoff-registry.json` by default (`--file` to override; keep a printed copy — emergencies take power and Wi-Fi with them).

## Registry Fields

| Field | Why it matters |
|---|---|
| `id` | short handle (`main`, `toilet-1`, `water-heater`) |
| `location` | specific enough that a panicked person finds it: "under kitchen sink, left wall, behind cleaning bottles" |
| `type` | gate / ball / angle-stop / straight-stop / meter-key / other — determines how it closes |
| `direction` | clockwise / perpendicular (ball valves: handle across pipe = OFF) |
| `tool` | none / flat screwdriver / crescent wrench / meter key — stored WHERE? |
| `tested` | date you last exercised it — untested valves are seized valves |
| `photo` | path/filename of the photo you took (photo > description) |
| `notes` | quirks: "stiff", "access panel behind toilet", "shared with unit 4B" |

## Valve Types at a Glance

| Type | Looks like | Closes by | Common failure |
|---|---|---|---|
| Ball | lever handle, 90° arc | quarter-turn: handle ⟂ pipe = OFF | rarely sticks; leaks at stem |
| Gate | round wheel like an outdoor faucet | many clockwise turns | seizes OPEN after years — the classic |
| Angle/straight stop | small oval/knurled handle under sinks & toilets | clockwise few turns | seizes, strips; replace with quarter-turn |
| Meter key valve | in concrete box at property/street edge | 5-sided key or meter wrench | needs the key — own one ($12) |
| Washing machine valves | behind washer, red/blue or single lever | clockwise / lever | aging flex lines burst — replace w/ braided + lever box |

## Common Pitfalls

1. **Never testing the main until the emergency.** Gate valves that sit open for a decade often won't close. Test at move-in, then exercise yearly (`drill`). If it won't turn, a plumber can replace it for ~$150–400 — vastly cheaper than discovering it seized during a flood.
2. **Confusing the house main with the irrigation/yard main.** Closing the wrong one leaves the leak flowing. The registry records which is which.
3. **Forcing a stuck valve with a giant cheater bar.** You can snap the stem and *create* the flood. Gentle penetrating oil, back-and-forth rocking, then call a plumber.
4. **Closing only the water heater's cold inlet for a whole-house leak** (or vice versa). Fixture → appliance → main: isolate at the smallest valve that contains the leak.
5. **Not owning the tools your valves need.** A meter key and a 12" adjustable wrench, stored where the card says, are part of the system.
6. **Relying on memory or a phone note.** Emergencies happen to whoever is home — babysitter, guest, teen. The printed card in a known spot is the deliverable.
7. **Shutting off power AFTER wading into water.** Breaker first, then wet-vac. GFCI outlets don't make water safe.

## Verification Checklist

- [ ] `main` entry exists, with tool + direction, and `tested` within 12 months
- [ ] Every toilet and sink has an entry (angle stops) — or a note that it lacks one
- [ ] Water heater cold inlet entry exists (also your drain-down point)
- [ ] Photo filenames recorded (or photos taped inside a cabinet near the valve)
- [ ] Card printed and posted where household members already look (fridge)
- [ ] Meter key + wrench purchased and stored in the location the card names
- [ ] `drill` run once per quarter — 60 seconds, calendar it
