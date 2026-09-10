# Home File Guide — Modeling Your Home in 10 Minutes

The model is only as good as your sketch. This guide walks you through
building `~/.wifi-home.json` (or any `--home` file) from a paper sketch, with
a worked example and troubleshooting for common mistakes.

## 1. Coordinate system

- Units are **meters**. Origin (0,0) is anywhere you like — a corner of the
  building is conventional.
- +x = east/right, +y = north/up on your sketch. Only relative positions
  matter.
- Accuracy of ±0.5 m is plenty; the model's honesty is ±4-8 dB anyway.

## 2. Rooms

Each room is a point where you'd actually sit with a laptop:

```json
{"name": "office", "xy": [3.5, 8.5], "important": true}
```

- `"important": true` marks rooms whose experience you care about (bedroom,
  office, living room). Advice targets these first; unimportant rooms
  (hallway, storage) won't drive router placement.
- Room names must be unique — the first letter of each is used as the heatmap
  label (important rooms get uppercase).

## 3. Walls

Each wall is a material + a line segment (two endpoints):

```json
{"material": "brick", "segment": [[8.2, 6.8], [8.2, 10.5]]}
```

- Draw walls on your sketch at roughly their real position; endpoints can
  extend past the building outline — harmless.
- The model counts a wall only when the straight router→room line **crosses
  its segment**. A wall you walk parallel to costs nothing.
- Interior partitions: `drywall` (3 dB). Load-bearing / older external:
  `brick` (6), `concrete-block` (8), `concrete` (10).
- Sneaky killers people forget:
  - `mirror` (8 dB) — mirrored wardrobe, bathroom mirror wall
  - `fridge` (18 dB) — the kitchen wall the fridge backs onto
  - `water-wall` (12 dB) — plumbing wall shared with a bathroom
  - `hvac-duct` (14 dB) — duct chased floor-to-ceiling
  - `bookshelf-full` (4 dB) — the wall of books behind your desk
  - `glass-low-e` (8 dB) — modern energy-efficient windows (balconies!)
- **Multi-storey:** model the floor between storeys as one long wall segment
  of `floor-timber` (8 dB) or `floor-concrete` (12 dB) laid across the plan,
  and put the other storey's rooms at their (x,y) positions on the same
  canvas. Distance becomes the 3-D diagonal — close enough at this grade.

## 4. Router, band, overrides

```json
{
  "band": "5", "width_mhz": 80,
  "router": {"xy": [2.0, 2.0], "tx_dbm": 20},
  "materials": {"drywall": 4.0}
}
```

- `tx_dbm`: consumer routers ship ~20-23 dBm; leave default unless known.
- `band`: model the band your problem lives on. Rule of thumb: complaints
  about *speed near the router* → 5; complaints about *reach* → 2.4.
- `materials`: local override of any attenuation value — use after
  `compare` shows systematic bias (e.g. your "drywall" is actually plaster
  on metal studs).

## 5. Worked example: the corner-router apartment

A 12×10 m two-bed flat. Router arrives by the door at (2,2) because that's
where the ISP socket is. Sketch:

```
y=10 +--------+-------+---+----+
      | bedroom1    bedroom2   |
      |      (3.5,8.5) (9.5,8.5)
y=6.8 +----[tile]----+--[brick]+
      | bathroom(6.5,6)        |
y=5.8 +---+                    |
      |   +----[drywall]       |
      | living      kitchen    |
      | (4,3.5)     (8.5,2.5)  |  balcony (11.5,2)
      |        [glass-low-e]   |
y=0   +------@-----------------+
     x=0    router(2,2)     x=12
```

Resulting weaknesses (from `plan`): bedroom2 at −69 dBm through
drywall+tile+brick — workable but the first to drop on a bad day; balcony at
−66 through low-E glass. The model's answer: move the router to (8.3, 2.9) —
the kitchen end of the living space — lifting the weakest room 17 dB, more
than any mesh node would. If the sofa wall prevents that, second-best is a
mesh node in the hallway at (6.5, 5.5): one drywall from the router, clean
line to both bedrooms.

## 6. Calibrating with measurements

1. Stand in a room, phone Wi-Fi analyzer app open, note dBm on the **same
   band** as the model (`--band 5`).
2. `survey --room bedroom1 --rssi -71 --band 5 --where desk`
3. `compare` — three outcomes:
   - within ±4 dB: model is calibrated, trust the advice
   - model optimistic (predicts better than reality): add missing walls or
     raise material dB
   - model pessimistic: your walls are kinder than assumed — lower values
   Repeat once; indoor models converge fast because errors are systematic.

## 7. Troubleshooting

- *"Room shows open path but signal is bad"* → look up: is the router under
  the desk? Add a fake `bookshelf-full` wall near the router to model
  furniture clutter, or accept the model can't see furniture.
- *"Everything is excellent but Netflix still buffers"* → signal isn't the
  problem; suspect interference (`channels`), the ISP line, or the TV's
  ancient Wi-Fi chip.
- *"Two rooms, same distance, wildly different reality"* → walls differ.
  This is exactly what the model exists to reveal: count the crossings.
