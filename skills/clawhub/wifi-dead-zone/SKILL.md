---
name: wifi-dead-zone
description: "Use when Wi-Fi is slow or drops in specific rooms, when placing a router or mesh node in a new home, when deciding if you need a mesh system or just a better router spot, when your 5 GHz doesn't reach the bedroom, or when picking clean channels among neighbors — builds a floor plan of your home as a simple model (rooms, walls, materials), estimates per-room signal with real RF physics (log-distance path loss + per-material wall attenuation), renders an ASCII heatmap, grid-searches 676 candidate spots for the optimal router placement, tells you exactly where to put mesh nodes (and where NOT to), calibrates against your actual phone measurements, and recommends non-overlapping channels given your neighbors' networks."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [wifi, home-network, router-placement, heatmap, mesh, signal, diagnostics]
---

# Wi-Fi Dead Zone Solver

## Overview

Every home has That One Room where video calls freeze. The usual fixes people try — rebooting the router, buying a $300 mesh kit, swearing — mostly fail because the problem is physics: distance, and what the walls are made of. A fridge, a bathroom wall full of plumbing, or one load-bearing brick wall eats more signal than 10 meters of open air.

This skill turns what you already know about your home (room layout, where the router sits, roughly what the walls are) into a working RF model. It computes per-room signal estimates, draws a heatmap of your floor plan, and — the part nobody else does for free — **grid-searches 676 candidate positions** for the spot that lifts your *weakest* room the most. It also knows the mesh-node placement rule everyone gets wrong, and calibrates its model against real measurements from your phone.

## When to Use

- "Wi-Fi is terrible in the bedroom / office / bathroom" — find out *why* and what fixes it
- Moving into a new place: pick the router spot **before** the furniture arrives
- Deciding between "move the router", "add a mesh node", or "blame the ISP"
- Choosing channels when neighbors' networks crowd yours
- Don't use for: enterprise deployment, outdoor bridging, or proving anything to your ISP — it's a planning model with honest error bars, not a spectrum analyzer.

## The Model

Two physical effects, both standard indoor-RF practice:

```
loss(d) = FSPL(1 m) + 10·n·log10(d) + Σ wall_attenuation + fade margin
RSSI     = router tx power − loss
```

| Band | Path-loss exponent n | 1 m anchor | Why |
|---|---|---|---|
| 2.4 GHz | 2.2 | 40.0 dB | penetrates clutter better |
| 5 GHz   | 2.6 | 46.6 dB | faster, dies at walls |
| 6 GHz   | 2.8 | 48.1 dB | fastest, most fragile |

Wall materials cost extra dB per pass: drywall 3, brick 6, concrete 10, low-E glass 8, a fridge 18. The `materials` command lists all 21; your home file can override any of them. Walls are geometric segments — the model counts only the walls your router→room line actually crosses (segment intersection test), so a diagonal path through open plan isn't penalized.

RSSI grades map to real experience: −55 excellent / −67 good / −72 workable / −80 weak / below = dead at 5 GHz (2.4 GHz shifts these favorably).

## Commands

```bash
# List the 21 wall-material attenuation values
python3 scripts/wifi_heatmap.py materials

# Full analysis of your home: table + heatmap + ranked advice
python3 scripts/wifi_heatmap.py plan --home myhome.json

# Record a real measurement (phone app / laptop) to calibrate
python3 scripts/wifi_heatmap.py survey --home myhome.json --room bedroom1 \
    --rssi -71 --band 5 --where desk

# Model vs reality: finds systematic optimism/pessimism
python3 scripts/wifi_heatmap.py compare --home myhome.json

# Channel guidance given neighbors' channels
python3 scripts/wifi_heatmap.py channels --band 2.4 --neighbors 1,6,6,11
python3 scripts/wifi_heatmap.py channels --band 5 --neighbors 36,40,44,149

# Self-contained demo on a sample apartment
python3 scripts/wifi_heatmap.py example
```

Home file format (see `references/home-file-guide.md` for all fields and a worked example):

```json
{
  "band": "5", "width_mhz": 80,
  "router": {"xy": [2, 2], "tx_dbm": 20},
  "rooms": [
    {"name": "living",   "xy": [4, 3.5], "important": true},
    {"name": "bedroom1", "xy": [3.5, 8.5], "important": true}
  ],
  "walls": [
    {"material": "drywall", "segment": [[5.5, 0.5], [5.5, 5.0]]},
    {"material": "brick",   "segment": [[8.2, 6.8], [8.2, 10.5]]}
  ]
}
```

Coordinates are meters, origin anywhere you like. Sketch your floor plan on paper first — approximate is fine, the model has ±4 dB honesty anyway.

## Workflow

1. Sketch your floor plan: rooms as (x, y) points in meters, walls as line segments, note materials (concrete block? brick chimney? mirrored closet?).
2. Create the home JSON (start from `references/home-file-guide.md`).
3. Run `plan` — get the per-room table, the heatmap, and the advice list.
4. If advice says MOVE ROUTER: try it (longer cable, move the shelf) and re-run; the table should shift a grade.
5. Take 2-3 real measurements with your phone at the worst spots (`survey`), then `compare` — if the model is systematically off, fix the wall materials it names.
6. Only now consider hardware: the WEAK ROOMS advice names the rooms worth a mesh node and states the placement rule (see pitfalls).
7. Run `channels` with your neighbors' list from any Wi-Fi analyzer app; set the router accordingly.

## Common Pitfalls

1. **Putting the mesh node inside the dead room.** It then has a dead link back to the router and you've built an expensive repeater of misery. The node goes where it still sees the router well (≤1 wall, RSSI ≥ −60); Ethernet backhaul beats wireless always.
2. **Trusting the model over measurements.** The model is planning-grade (±4-8 dB). When `compare` shows a systematic bias, believe the measurements and adjust wall materials — not the other way round.
3. **Ignoring 2.4 GHz as "slow".** At the far end of the home it's often the only usable link. Keep separate SSIDs so devices fall back deliberately instead of clinging to one-bar 5 GHz.
4. **Forgetting floors count as walls.** Multi-storey homes: add a `floor-timber` (8 dB) or `floor-concrete` (12 dB) wall segment along the storey boundary in the model.
5. **Channel-width greed.** 40 MHz on 2.4 GHz breaks the 1/6/11 orthogonality that makes those channels shareable — stay at 20 MHz.
6. **Router in a cabinet / on the floor.** The model assumes clear air; a closed media cabinet adds real dB the model can't see. Fix placement before buying anything.
7. **Believing advertised mesh coverage numbers.** Those assume open air. Your model output (walls on path) is a better predictor than any box claim.

## Verification Checklist

- [ ] `python3 scripts/test_wifi_heatmap.py` → ALL TESTS PASSED (28 assertions)
- [ ] `python3 scripts/wifi_heatmap.py example` renders table + heatmap + before/after
- [ ] Home file lists every room you care about, with `important: true` on the ones that matter
- [ ] At least 2 real measurements recorded and `compare` within ±4 dB before hardware purchases
- [ ] Advice list actioned top-to-bottom before spending money
