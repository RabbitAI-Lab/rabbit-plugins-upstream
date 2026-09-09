#!/usr/bin/env python3
"""
wifi_heatmap.py — plan and diagnose home Wi-Fi from plain observations.

You feed it what you already know (rooms, where the router sits, where the
signal is weak, what the walls are made of) and it computes per-room signal
estimates (FSPL + wall attenuation), draws an ASCII floorplan heatmap, and
tells you exactly what to do: where to move the router, which rooms need a
mesh node, and which channels to pick given your neighbors.

Pure stdlib. This is a planning model, not a site survey — it tells you where
to measure and what to expect.

Commands:
  materials            list known wall/floor attenuation values
  plan                 full analysis: per-room RSSI + heatmap + advice
  survey               record actual measurements per room (ground truth)
  compare              model vs measured (finds systematic bias)
  channels             2.4/5/6 GHz channel guidance given neighbor APs
  example              self-contained demo on a sample home

Data file (JSON, override with --home): ~/.wifi-home.json
"""
import argparse
import datetime as dt
import json
import math
import os
import sys

DEFAULT_HOME = os.path.expanduser("~/.wifi-home.json")

# ---------------------------------------------------------------- materials
# Median extra attenuation in dB per obstruction (one pass).
# Planning-grade values from industry propagation guides (Cisco/Ubiquiti
# wall-material tables). Override per home via the "materials" map.
MATERIALS = {
    "open":            0.0,   # doorway / open plan
    "drywall":         3.0,   # interior wall, wood or metal studs
    "plaster":         4.0,   # plaster + wood lath (older homes)
    "glass":           4.0,   # single pane window
    "tile":            5.0,   # tiled bathroom/kitchen wall
    "brick":           6.0,
    "metal-stud-wall": 6.0,   # drywall on metal studs full of wiring
    "concrete-block":  8.0,
    "glass-low-e":     8.0,   # low-E / coated / triple glazed
    "mirror":          8.0,   # glass + metal backing
    "concrete":        10.0,  # solid poured wall or slab
    "aquarium":        10.0,
    "water-wall":      12.0,  # wall full of plumbing
    "floor-timber":    8.0,   # ceiling/floor between storeys (wood)
    "floor-concrete":  12.0,  # slab between storeys
    "metal-door":      12.0,
    "hvac-duct":       14.0,  # ductwork / metal cabinet on the path
    "fridge":          18.0,  # large appliance on the path
    "bookshelf-full":  4.0,
    "closet-full":     4.0,
}


def channel_plan(band, neighbors):
    """Return (recommended, [alternatives], reason) given neighbor channels."""
    n = neighbors or []
    if band == "2.4":
        counts = {c: 0 for c in (1, 6, 11)}
        for x in n:
            for c in counts:
                if abs(x - c) <= 2:
                    counts[c] += 1
        best = min(counts, key=lambda c: (counts[c], c))
        alts = [c for c in (1, 6, 11) if c != best]
        reason = "least-crowded of the only non-overlapping set (1/6/11); "
        reason += f"{counts[best]} neighbor(s) within ±2"
        return best, alts, reason
    if band == "5":
        blocks = {36: (36, 48), 52: (52, 64), 100: (100, 112),
                  116: (116, 128), 132: (132, 144), 149: (149, 161)}
        counts = {b: 0 for b in blocks}
        for x in n:
            for b, (lo, hi) in blocks.items():
                if lo <= x <= hi:
                    counts[b] += 1
        order = sorted(blocks, key=lambda b: (counts[b], 0 if b in (36, 149) else 1, b))
        best = order[0]
        lo, hi = blocks[best]
        reason = f"{counts[best]} neighbor(s) in block {lo}-{hi}"
        if best in (52, 100, 116, 132):
            reason += "; DFS block — radar detection can force a brief channel switch"
        return best, order[1:4], reason
    if band == "6":
        return 37, [53, 69, 101], "6E prefers PSC channels (37/53/69/...); few neighbors exist today"
    return None, [], "unknown band"


# ---- physics -------------------------------------------------------------
# Log-distance model anchored at 1 m:
#   loss = FSPL(1 m) + 10*n*log10(d) + walls + fade
# n ("path-loss exponent") is 2.0 in free space; indoor clutter raises it.
# 2.4 GHz penetrates clutter better, so it gets a lower exponent.
EXPONENT = {"2.4": 2.2, "5": 2.6, "6": 2.8}
FADE_MARGIN_DB = 3.0


def freq_of(band):
    return {"2.4": 2.4, "5": 5.0, "6": 6.0}[band]


def fspl_1m(freq_ghz):
    """Free-space loss at 1 m reference distance."""
    return 20 * math.log10(freq_ghz * 1000) - 27.55


def path_loss(dist_m, band, walls, materials_override=None):
    mats = dict(MATERIALS)
    if materials_override:
        mats.update(materials_override)
    d = max(dist_m, 1.0)
    loss = fspl_1m(freq_of(band)) + 10.0 * EXPONENT[band] * math.log10(d)
    for w in walls or []:
        kind = w if isinstance(w, str) else w.get("material", "drywall")
        loss += mats.get(kind, 4.0)
    return loss + FADE_MARGIN_DB


def rssi(tx_dbm, dist_m, band, walls, materials_override=None):
    return tx_dbm - path_loss(dist_m, band, walls, materials_override)


def link_quality(rssi_val):
    """RSSI → expected experience."""
    if rssi_val >= -55:
        return "excellent", 4
    if rssi_val >= -67:
        return "good", 3
    if rssi_val >= -72:
        return "workable", 2
    if rssi_val >= -80:
        return "weak", 1
    return "dead", 0


def bandwidth_estimate(rssi_val, band, width_mhz):
    base = {20: 130, 40: 250, 80: 480, 160: 900}.get(width_mhz, 480)
    if band == "2.4":
        base *= 0.45
    if rssi_val >= -55:
        f = 1.0
    elif rssi_val >= -67:
        f = 0.75
    elif rssi_val >= -72:
        f = 0.5
    elif rssi_val >= -80:
        f = 0.25
    else:
        f = 0.05
    return base * f


# ---- geometry ------------------------------------------------------------
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _orient(a, b, c):
    v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if abs(v) < 1e-9:
        return 0
    return 1 if v > 0 else -1


def segments_intersect(p1, p2, q1, q2):
    o1 = _orient(p1, p2, q1)
    o2 = _orient(p1, p2, q2)
    o3 = _orient(q1, q2, p1)
    o4 = _orient(q1, q2, p2)
    return o1 * o2 < 0 and o3 * o4 < 0


def walls_on_path(router_xy, room_xy, walls_list):
    """Walls whose segment crosses the router→room straight path."""
    out = []
    for w in walls_list or []:
        (ax, ay), (bx, by) = w["segment"]
        if segments_intersect(router_xy, room_xy, (ax, ay), (bx, by)):
            out.append(w)
    return out


# ---- home model ----------------------------------------------------------
def load_home(path):
    with open(path) as f:
        return json.load(f)


def router_xy(home):
    return tuple(home.get("router", {}).get("xy", [0, 0]))


def tx_power(home):
    return home.get("router", {}).get("tx_dbm", 20)


def analyze(home):
    """Per-room RSSI rows, worst first."""
    rxy = router_xy(home)
    tx = tx_power(home)
    mats = home.get("materials")
    width = home.get("width_mhz", 80)
    band = home.get("band", "5")
    rows = []
    for room in home.get("rooms", []):
        xy = room["xy"]
        d = dist(rxy, xy)
        walls = walls_on_path(rxy, xy, home.get("walls"))
        db = rssi(tx, d, band, walls, mats)
        grade, score = link_quality(db)
        rows.append({
            "room": room["name"],
            "dist": round(d, 1),
            "walls": [w["material"] for w in walls],
            "rssi": round(db, 1),
            "grade": grade,
            "score": score,
            "phy_mbps": round(bandwidth_estimate(db, band, width)),
            "important": bool(room.get("important")),
        })
    rows.sort(key=lambda r: r["rssi"])
    return rows


def print_room_table(rows):
    print("\nPer-room signal (worst first):")
    print(f"{'room':<22}{'dist':>7}{'walls on path':>20}{'RSSI':>9}{'grade':>11}{'~PHY':>8}")
    for r in rows:
        w = "+".join(r["walls"])[:18] or "-"
        star = "*" if r["important"] else ""
        print(f"{r['room'] + star:<22}{str(r['dist']) + 'm':>7}{w:>20}"
              f"{str(r['rssi']) + 'dBm':>9}{r['grade']:>11}{str(r['phy_mbps']) + 'M':>8}")
    print("(* = room you flagged important)\n")


# ---- heatmap -------------------------------------------------------------
SHADE = {"excellent": "█", "good": "▓", "workable": "▒", "weak": "░", "dead": " "}


def home_extent(home):
    pts = [r["xy"] for r in home.get("rooms", [])] + [router_xy(home)]
    for w in home.get("walls", []):
        pts.extend(w["segment"])
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    pad = 1.0
    return min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad


def render_heatmap(home, grid_w=46):
    x0, x1, y0, y1 = home_extent(home)
    span_x = max(x1 - x0, 0.5)
    span_y = max(y1 - y0, 0.5)
    h = max(int(grid_w * span_y / span_x / 2.0), 8)
    band = home.get("band", "5")
    tx = tx_power(home)
    mats = home.get("materials")
    walls = home.get("walls")
    rxy = router_xy(home)
    rooms = home.get("rooms", [])
    grid = []
    for j in range(h):
        line = []
        for i in range(grid_w):
            wx = x0 + (i + 0.5) * span_x / grid_w
            wy = y1 - (j + 0.5) * span_y / h
            db = rssi(tx, dist((wx, wy), rxy), band,
                      walls_on_path(rxy, (wx, wy), walls), mats)
            grade, _ = link_quality(db)
            ch = SHADE[grade]
            best, bestd = None, 1e9
            for room in rooms:
                dd = dist((wx, wy), room["xy"])
                if dd < bestd:
                    bestd, best = dd, room
            if bestd <= 1.2 and best is not None:
                ch = best["name"][0].upper() if best.get("important") else best["name"][0]
            if dist((wx, wy), rxy) <= 1.2:
                ch = "@"
            line.append(ch)
        grid.append("".join(line))

    def to_cell(x, y):
        i = int((x - x0) / span_x * grid_w)
        j = int((y1 - y) / span_y * h)
        return i, j

    for w in walls:
        (ax, ay), (bx, by) = w["segment"]
        steps = max(int(dist((ax, ay), (bx, by)) / 0.25), 1)
        for s in range(steps + 1):
            t = s / steps
            i, j = to_cell(ax + (bx - ax) * t, ay + (by - ay) * t)
            if 0 <= i < grid_w and 0 <= j < h:
                grid[j] = grid[j][:i] + "#" + grid[j][i + 1:]

    print("Heatmap (@=router, #=wall, letters=rooms; █ ▓ ▒ ░ blank = signal):")
    print("+" + "-" * grid_w + "+")
    for line in grid:
        print("|" + line + "|")
    print("+" + "-" * grid_w + "+")
    print()


# ---- advice --------------------------------------------------------------
def placement_score(home, cx, cy):
    """Objective: mean RSSI + 2 × worst-room RSSI (protect the weakest room)."""
    tx = tx_power(home)
    mats = home.get("materials")
    walls = home.get("walls")
    band = home.get("band", "5")
    total, worst, cnt = 0.0, 1e9, 0
    for room in home.get("rooms", []):
        xy = room["xy"]
        db = rssi(tx, dist((cx, cy), xy), band,
                  walls_on_path((cx, cy), xy, walls), mats)
        total += db
        cnt += 1
        worst = min(worst, db)
    if cnt == 0:
        return -1e9
    return total / cnt + 2.0 * worst


def best_placement(home, n=25):
    """Grid-search the floor for the spot maximizing mean + 2×worst RSSI."""
    x0, x1, y0, y1 = home_extent(home)
    best_xy, best_obj = None, -1e9
    for gi in range(n + 1):
        for gj in range(n + 1):
            cx = x0 + (x1 - x0) * gi / n
            cy = y0 + (y1 - y0) * gj / n
            obj = placement_score(home, cx, cy)
            if obj >= best_obj:
                best_obj, best_xy = obj, (cx, cy)
    return best_xy, best_obj


def worst_room_rssi(home, cx, cy):
    band = home.get("band", "5")
    worst = 1e9
    for room in home.get("rooms", []):
        db = rssi(tx_power(home), dist((cx, cy), room["xy"]), band,
                  walls_on_path((cx, cy), room["xy"], home.get("walls")),
                  home.get("materials"))
        worst = min(worst, db)
    return worst


def advice(home, rows):
    tips = []
    rxy = router_xy(home)
    best_xy, _ = best_placement(home)
    cur_worst = worst_room_rssi(home, rxy[0], rxy[1])
    new_worst = worst_room_rssi(home, best_xy[0], best_xy[1])
    gain = new_worst - cur_worst
    if gain > 1.5:
        tips.append(
            f"MOVE ROUTER: from ({rxy[0]:.1f}, {rxy[1]:.1f}) to "
            f"({best_xy[0]:.1f}, {best_xy[1]:.1f}) — the weakest room goes from "
            f"{cur_worst:.0f} to {new_worst:.0f} dBm (+{gain:.0f} dB; best of 676 candidate spots)."
        )
    else:
        tips.append(
            f"Router placement is fine: the current spot is within {gain:.0f} dB of the "
            f"best found spot ({best_xy[0]:.1f}, {best_xy[1]:.1f}) — fix obstructions "
            f"or add hardware instead of moving it."
        )

    important = [r for r in rows if r["important"]] or rows
    weak = [r for r in important if r["score"] <= 2]
    if weak:
        names = "; ".join(
            f"{r['room']} ({r['rssi']:.0f} dBm via {'+'.join(r['walls']) or 'open'})"
            for r in weak)
        tips.append(
            "WEAK ROOMS — mesh/extender candidates: " + names + "\n"
            "  Rule: place the node where it still sees the router WELL (≤1 wall, "
            "RSSI ≥ -60 at the node), NOT inside the dead room — otherwise you "
            "just extend the dead zone."
        )

    tips.append(
        "BAND SPLIT: keep a separate 5 GHz SSID so weak rooms fall back cleanly to "
        "2.4 GHz. 2.4 GHz buys ~10 dB of link budget at the same spot — often the "
        "difference between dead and usable two walls away."
    )

    killers = {w["material"] for w in home.get("walls", [])
               if w["material"] in ("concrete", "concrete-block", "brick",
                                    "metal-stud-wall", "fridge", "hvac-duct",
                                    "water-wall", "mirror", "glass-low-e")}
    if killers:
        tips.append(
            "HARD BLOCKERS on file: " + ", ".join(sorted(killers)) + ". These cost "
            "6-18 dB per pass — no router move fixes that. The answer is a wired "
            "backhaul AP or mesh node on the FAR side of the blocker."
        )
    return tips


def print_advice(tips):
    print("What to do:")
    for i, t in enumerate(tips, 1):
        first, _, rest = t.partition("\n")
        print(f"{i}. {first}")
        for line in rest.splitlines():
            print("   " + line.strip())
    print()


# ---- sample home ---------------------------------------------------------
def sample_home():
    return {
        "name": "sample 2-bed apartment",
        "band": "5",
        "width_mhz": 80,
        "router": {"xy": [2.0, 2.0], "tx_dbm": 20},
        "materials": {},
        "rooms": [
            {"name": "living",    "xy": [4.0, 3.5], "important": True},
            {"name": "kitchen",   "xy": [8.5, 2.5]},
            {"name": "bedroom1",  "xy": [3.5, 8.5], "important": True},
            {"name": "bedroom2",  "xy": [9.5, 8.5]},
            {"name": "bathroom",  "xy": [6.5, 6.0]},
            {"name": "balcony",   "xy": [11.5, 2.0]},
        ],
        "walls": [
            {"material": "drywall", "segment": [[5.5, 0.5], [5.5, 5.0]]},
            {"material": "drywall", "segment": [[5.5, 5.0], [3.0, 5.0]]},
            {"material": "tile",    "segment": [[5.0, 6.8], [8.0, 6.8]]},
            {"material": "drywall", "segment": [[0.5, 5.8], [3.0, 5.8]]},
            {"material": "brick",   "segment": [[8.2, 6.8], [8.2, 10.5]]},
            {"material": "glass-low-e", "segment": [[10.8, 0.5], [10.8, 4.0]]},
        ],
        "measurements": {
            "bedroom1": [
                {"date": "2026-08-30", "band": "5", "rssi": -74, "where": "desk"},
                {"date": "2026-08-30", "band": "2.4", "rssi": -63, "where": "desk"},
            ],
            "balcony": [
                {"date": "2026-08-30", "band": "5", "rssi": -79, "where": "table"},
            ],
        },
    }


# ---- commands ------------------------------------------------------------
def cmd_materials(args):
    print("Wall/floor attenuation values used by the model (dB per pass):")
    for k, v in sorted(MATERIALS.items(), key=lambda kv: -kv[1]):
        print(f"  {k:<16}{v:>5.1f}")
    print("\nOverride any value in your home file's \"materials\" map.")


def cmd_plan(args):
    home = load_home(args.home)
    print(f"Home: {home.get('name', args.home)} | band {home.get('band', '5')} GHz "
          f"| router at {list(router_xy(home))} @ {tx_power(home)} dBm")
    rows = analyze(home)
    print_room_table(rows)
    render_heatmap(home, grid_w=args.width)
    for t in advice(home, rows):
        first, _, rest = t.partition("\n")
        print("• " + first)
        for line in rest.splitlines():
            print("  " + line.strip())
    print()


def cmd_survey(args):
    home = load_home(args.home)
    rooms = {r["name"] for r in home.get("rooms", [])}
    if args.room not in rooms:
        print(f"Room '{args.room}' not in home file. Known rooms: {', '.join(sorted(rooms))}")
        sys.exit(1)
    if args.rssi is None:
        ms = home.get("measurements", {}).get(args.room, [])
        if ms:
            print(f"Stored measurements for {args.room}:")
            for m in ms:
                print(f"  {m['date']}  {m['band']} GHz  {m['rssi']} dBm  ({m.get('where', '?')})")
        else:
            print(f"No measurements for {args.room} yet. Record one with:")
            print(f"  python3 {sys.argv[0]} survey --home {args.home} "
                  f"--room {args.room} --rssi -71 --band 5 --where desk")
        return
    if args.band not in ("2.4", "5", "6"):
        print("--band must be 2.4, 5 or 6")
        sys.exit(1)
    home.setdefault("measurements", {}).setdefault(args.room, []).append({
        "date": dt.date.today().isoformat(),
        "band": args.band,
        "rssi": args.rssi,
        "where": args.where or "",
    })
    with open(args.home, "w") as f:
        json.dump(home, f, indent=2)
    m = home["measurements"][args.room][-1]
    grade, _ = link_quality(m["rssi"])
    print(f"Recorded: {args.room}  {m['band']} GHz  {m['rssi']} dBm ({m['where']}) — grade: {grade}")


def cmd_compare(args):
    home = load_home(args.home)
    meas = home.get("measurements", {})
    if not meas:
        print("No measurements recorded. Add some with the survey command first.")
        return
    tx = tx_power(home)
    mats = home.get("materials")
    rxy = router_xy(home)
    home_band = str(home.get("band", "5"))
    roomdefs = {r["name"]: r for r in home.get("rooms", [])}
    print(f"\nModel vs measured ({home_band} GHz):")
    print(f"{'room':<22}{'measured':>10}{'model':>9}{'delta':>9}")
    deltas = []
    for room, ms in meas.items():
        if room not in roomdefs:
            continue
        same = [m for m in ms if str(m.get("band")) == home_band] or ms
        avg = sum(m["rssi"] for m in same) / len(same)
        xy = roomdefs[room]["xy"]
        pred = rssi(tx, dist(rxy, xy), home_band,
                    walls_on_path(rxy, xy, home.get("walls")), mats)
        delta = avg - pred
        deltas.append(delta)
        flag = ""
        if delta < -3:
            flag = "  <- model optimistic (missed a wall?)"
        elif delta > 3:
            flag = "  <- model pessimistic (materials too lossy?)"
        print(f"{room:<22}{avg:>9.1f}dBm{pred:>8.1f}dB{delta:>+8.1f}dB{flag}")
    if not deltas:
        print("No overlapping rooms between measurements and home file.")
        return
    mean_d = sum(deltas) / len(deltas)
    print(f"\nMean delta {mean_d:+.1f} dB (measured − model).")
    if mean_d > 4:
        print("Model is pessimistic — walls are less lossy than assumed; soften materials.")
    elif mean_d < -4:
        print("Model is optimistic — something blocks more than modeled; add walls or raise material dB.")
    else:
        print("Agreement within ±4 dB — calibrated enough to trust for placement decisions.")


def cmd_channels(args):
    band = args.band
    neighbors = [int(x) for x in (args.neighbors or "").split(",") if x.strip()]
    best, alts, reason = channel_plan(band, neighbors)
    print(f"Band {band} GHz, neighbors on: {neighbors or 'none reported'}")
    print(f"  Recommended channel: {best}")
    print(f"  Alternatives: {', '.join(str(a) for a in alts)}")
    print(f"  Why: {reason}")
    if band == "2.4":
        print("  Width: use 20 MHz — 40 MHz doubles interference and breaks 1/6/11 orthogonality.")
    if band == "5" and best in (52, 100, 116, 132):
        print("  Note: DFS channels need radar-clear air; expect occasional quiet switches.")
    print()


def cmd_example(args):
    home = sample_home()
    print("=== EXAMPLE: 2-bed apartment, router in the corner by the entrance ===\n")
    print(f"Router at {list(router_xy(home))}, {home['band']} GHz, {home['width_mhz']} MHz\n")
    rows = analyze(home)
    print_room_table(rows)
    render_heatmap(home, grid_w=46)
    for t in advice(home, rows):
        first, _, rest = t.partition("\n")
        print("• " + first)
        for line in rest.splitlines():
            print("  " + line.strip())
    print()
    print("--- Now the SAME home with the router at the model's recommended spot ---\n")
    moved = json.loads(json.dumps(home))
    rec_xy, _ = best_placement(moved)
    moved["router"]["xy"] = [round(rec_xy[0], 1), round(rec_xy[1], 1)]
    rows2 = analyze(moved)
    print_room_table(rows2)
    ch, alts, why = channel_plan("2.4", [1, 6, 6, 11])
    print(f"Channel check (neighbors on 1,6,6,11): pick {ch}; alternatives {alts} — {why}")
    print()


def main():
    ap = argparse.ArgumentParser(
        prog="wifi_heatmap.py",
        description="Plan and diagnose home Wi-Fi from plain observations. Pure stdlib.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("materials", help="list wall attenuation values")

    p = sub.add_parser("plan", help="full analysis of your home file")
    p.add_argument("--home", default=DEFAULT_HOME, help=f"home JSON (default {DEFAULT_HOME})")
    p.add_argument("--width", type=int, default=46, help="heatmap width in chars")

    p = sub.add_parser("survey", help="record or show measurements for a room")
    p.add_argument("--home", default=DEFAULT_HOME)
    p.add_argument("--room", required=True)
    p.add_argument("--rssi", type=int, help="measured dBm (omit to just list)")
    p.add_argument("--band", default="5", help="2.4 / 5 / 6")
    p.add_argument("--where", default="", help="where in the room, e.g. 'desk'")

    p = sub.add_parser("compare", help="model vs your measurements")
    p.add_argument("--home", default=DEFAULT_HOME)

    p = sub.add_parser("channels", help="channel recommendation")
    p.add_argument("--band", default="2.4", choices=["2.4", "5", "6"])
    p.add_argument("--neighbors", default="", help="comma list of neighbor channels, e.g. 1,6,6,11")

    sub.add_parser("example", help="self-contained demo")

    args = ap.parse_args()
    {"materials": cmd_materials, "plan": cmd_plan, "survey": cmd_survey,
     "compare": cmd_compare, "channels": cmd_channels,
     "example": cmd_example}[args.cmd](args)


if __name__ == "__main__":
    main()
