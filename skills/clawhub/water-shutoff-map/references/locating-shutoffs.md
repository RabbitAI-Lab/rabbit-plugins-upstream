# Locating Water Shutoffs — The Hunting Guide

How to find every shutoff in any home, identify what you're looking at, and test it safely. Use with `python3 scripts/shutoff_registry.py hunt --home <type>`.

## 1. The shutoff hierarchy (isolate at the smallest valve that works)

```
fixture stop (toilet/sink)  →  appliance valve (washer, dishwasher, fridge)
  →  water heater cold inlet  →  house main  →  municipal meter (curb/property line)
```

A toilet angle stop kills 100% of toilet leaks with two fingers. The house main kills everything but costs you hot water tanks' worth of pressure and needs tools. The meter key is the last resort when your main is seized — and the one the fire department uses.

## 2. Where the house main hides, by home type

**Basement homes (US Midwest/Northeast):** usually IN the basement — face the wall where the water service enters (look for the pipe coming up through the floor near the front wall, often near the water meter). Gate wheel or ball lever within 3–5 ft of entry, sometimes with a pressure regulator (bell-shaped) beside it.

**Slab-on-grade (US South/Southwest):** no basement. Look for: (a) a pipe emerging from the slab near the water heater or in the garage, often in a small metal or plastic box; (b) an exterior wall penetration on the street-facing side with an access panel; (c) the garage ceiling if plumbing runs through the attic (also check attic for the manifold). Many slab homes' ONLY interior main is at the water heater — which is why the meter key matters.

**Crawlspace homes (Pacific NW/South):** pipe enters through the crawlspace wall or rim joist; shutoff often right inside the crawlspace entrance, but sometimes only at the meter. Bring a headlamp; log the access hatch location in the registry.

**Condos/apartments:** unit shutoff is commonly behind an access panel — next to the water heater closet, under the kitchen or bathroom sink, or inside a utility closet near the entry. Building staff keep the riser valves; your unit valve is the one you control. Log the building's after-hours maintenance number on the card.

**Older homes / municipal variation:** the main may be a curb stop under a round metal cover in the yard or planting strip ("buffalo box" in the Midwest). Do NOT close curb stops yourself unless you own the key and know the local rules — some municipalities want their valve operated by them; log the utility phone number instead.

## 3. Fixture and appliance stops

- **Toilet:** angle stop on the wall beneath the left side of the tank (facing it). Metal or plastic oval handle, clockwise to close. If it has no stop (rare, old installs), the house main is your only option — log that.
- **Sinks:** straight stops (or angle stops) in the cabinet, one hot (left pipe) one cold (right), against the wall. Often buried under cleaning products — that's fine, log "behind the bottles."
- **Washing machine:** valves behind the machine (pull it out ~18"; don't yank the drain hose). Red/blue wheels or a single lever box. While you're back there: rubber/plastic flex lines are the #1 burst source in homes — replace with braided stainless if aged, and consider a lever shutoff box.
- **Dishwasher:** often only a small valve under the kitchen sink tied to the hot line (a tee with a tiny handle), sometimes none (hard-piped) — then it's the sink's hot stop or the main.
- **Fridge ice maker:** saddle valve pinched onto a line (bad) or a proper quarter-turn behind/under the fridge. Log it; these leak slowly and invisibly.
- **Water heater:** COLD inlet stop on top of the unit (or a wall valve feeding it). Also your friend for draining: close it, open a hot tap upstairs (air break), attach a hose to the drain spigot. Gas units: know where the gas valve is too (out of scope here, but photograph it while you're there). Note: closing only the cold inlet can relieve pressure via the tank — for tank leaks, kill cold inlet + open a hot faucet.
- **Irrigation/sprinklers:** usually a separate valve near the backflow preventor (that brass tower of pipes) or in a valve box in the ground. Closing the HOUSE main often does NOT stop irrigation lines (or vice versa) — this is the classic wrong-valve mistake. Log both separately.
- **Hose bibs:** mostly self-contained (the faucet is its own valve), but a separate shut-off inside the house feeding each exterior bib is gold in freezing climates — log it, and close + drain it each fall.

## 4. Valve identification: what you're looking at

| Feature | Gate valve | Ball valve | Angle/straight stop | Meter/curb stop |
|---|---|---|---|---|
| Handle | round wheel | straight lever | small oval/knurled wheel or lever | recessed square/5-sided nut |
| Travel | 3–10+ full turns | 1/4 turn | 1–3 turns | many turns via key |
| OFF state | wheel fully clockwise (gently seated) | lever ⟂ across pipe | wheel seated / lever ⟂ | — |
| Seizes? | YES — commonly, when open for years | rarely | yes, and handles strip | yes; needs meter key |

**Mark it while you're there:** tag each valve with a zip-tie tag or paint pen ("MAIN — CW TO CLOSE"). Photo. Log it.

## 5. Testing a valve safely (the 2-minute procedure per valve)

1. Pick a moment when brief water loss is fine (not during someone's shower).
2. Close the valve FULLY (clockwise / quarter-turn) — gently at the end; do not reef on it.
3. Open a downstream faucet to confirm zero flow. Cold tap for cold-side valves; any tap for the main.
4. **Watch for leaks at the valve itself** while pressurized-side is closed — a weeping packing nut is a finding: note it, snug the packing nut 1/8 turn if you know how, else plumber.
5. Reopen FULLY (gate valves: back-seat it counterclockwise to the stop; half-open gate valves erode and hammer).
6. Run the downstream faucet again; check the valve for drips.
7. Log `tested=<today>` and any quirk ("stiff first two turns", "needs penetrating oil next time").

If the valve won't close fully (water keeps dribbling): it's failed. Leave it open, log "SEIZED — replace", and rely on the next valve up the hierarchy until a plumber swaps it (angle stops are 20-minute jobs; mains are bigger but routine).

## 6. Freezing-weather extras

- Know the main + drain plan: close main, open the lowest faucet in the house + a high one (air break), drain water heater via hose if leaving for winter.
- Interior shutoffs for hose bibs: close, open the bib outside, drain.
- Leaving for >48h in a hard-freeze forecast: shut the main and drain, or keep heat ≥ 55°F and open cabinet doors under sinks on exterior walls.
- Foam insulating caps on exterior bibs are $3; a split pipe is not.

## 7. The printed card

Generate with `shutoff_registry.py card`. Post it where household members already look (fridge, inside a pantry door). The card contains: the 3-step first response, the valve table (id / location / type / direction / tool), tool storage location, plumber + insurance + utility phone lines, and the quarterly drill date. Lamination optional; legibility mandatory. Photos beat text: tape a photo of the main next to the card.

## 8. Insurance-claim notes (US-centric)

Insurers require prompt mitigation — your duty starts immediately, before adjusters arrive. Document everything (photos BEFORE cleanup), keep damaged materials until the adjuster agrees, save receipts for fans/dryers/plumber. Slow hidden leaks (ice-maker lines, slab leaks) are often "gradual damage" — coverage varies; the registry's `tested` dates and notes double as maintenance evidence. Burst-flex-line and supply-line failures are the most common sudden-discharge claims; that's why the washing-machine and fridge entries in your registry aren't optional.
