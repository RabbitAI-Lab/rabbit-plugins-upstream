#!/usr/bin/env python3
"""
seed_calendar.py — personalized seed-starting & sowing calendar from frost dates.

All dates derive from two anchors: last spring frost and first fall frost.
Pure stdlib. Run with -h for usage.
"""
import argparse
import datetime as dt
import json
import math
import sys

# ---------------------------------------------------------------------------
# Crop library
# start: indoor | direct | either
# wks_indoor: weeks before last frost to sow indoors (int, indoor/either crops)
# tdelay: days after (+) / before (-) last frost to transplant
# dt: days to harvest from transplant (indoor crops) or from sow (direct)
# frost_class: hardy | half | tender
# win_start/win_end: direct-sow window, days after last frost
# frost_buffer: days past first fall frost crop still produces
# succ: succession sowing interval days (None = single planting)
# per_person: plants for steady supply of one adult
# spacing_in: in-row spacing, inches
# notes: culture hints
# ---------------------------------------------------------------------------
CROPS = {
    # solanaceae
    "tomato":   dict(name="Tomato", start="indoor", wks=7, tdelay=14, dt=65,
                     cls="tender", win=(14, 42), fb=0, succ=None, pp=3, sp=24,
                     notes="Bottom heat 25C; pot up at 2 wks pre-transplant; bury stem deep."),
    "pepper":   dict(name="Pepper", start="indoor", wks=9, tdelay=21, dt=75,
                     cls="tender", win=(21, 49), fb=0, succ=None, pp=3, sp=18,
                     notes="Germ 10-14d at 27C; needs warm soil 18C+; purple leaves = cold soil."),
    "eggplant": dict(name="Eggplant", start="indoor", wks=9, tdelay=21, dt=80,
                     cls="tender", win=(21, 49), fb=0, succ=None, pp=2, sp=18,
                     notes="Like pepper but slower; warmth and row cover speed it up."),
    # cucurbits
    "cucumber": dict(name="Cucumber", start="indoor", wks=3, tdelay=7, dt=58,
                     cls="tender", win=(14, 70), fb=-7, succ=None, pp=3, sp=12,
                     notes="Resents root disturbance: peat pots/soil blocks; trellis to save space."),
    "zucchini": dict(name="Zucchini", start="indoor", wks=3, tdelay=7, dt=52,
                     cls="tender", win=(14, 70), fb=-7, succ=None, pp=2, sp=36,
                     notes="One healthy plant feeds a family; 2 max per person."),
    "summer-squash": dict(name="Summer Squash", start="indoor", wks=3, tdelay=7, dt=52,
                     cls="tender", win=(14, 70), fb=-7, succ=None, pp=2, sp=36,
                     notes="Same culture as zucchini."),
    "winter-squash": dict(name="Winter Squash", start="indoor", wks=3, tdelay=7, dt=100,
                     cls="tender", win=(14, 42), fb=0, succ=None, pp=1, sp=48,
                     notes="Long season: don't sow past window end; Cure 10d warm before storage."),
    "pumpkin":  dict(name="Pumpkin", start="indoor", wks=3, tdelay=7, dt=100,
                     cls="tender", win=(14, 42), fb=0, succ=None, pp=1, sp=48,
                     notes="For Hallowe'en, back-date 100-110 days + curing."),
    "melon":    dict(name="Melon", start="indoor", wks=4, tdelay=21, dt=85,
                     cls="tender", win=(21, 42), fb=0, succ=None, pp=2, sp=24,
                     notes="Needs heat + dry leaves; plastic mulch helps in short seasons."),
    "watermelon": dict(name="Watermelon", start="indoor", wks=4, tdelay=21, dt=85,
                     cls="tender", win=(21, 42), fb=0, succ=None, pp=1, sp=24,
                     notes="Heat and room; short seasons need early varieties."),
    # brassicas
    "broccoli": dict(name="Broccoli", start="indoor", wks=6, tdelay=-14, dt=65,
                     cls="hardy", win=(-42, -7), fb=21, succ=None, pp=3, sp=18,
                     notes="Spring crop jumps frost; fall crop is easier (sow mid-summer)."),
    "cabbage":  dict(name="Cabbage", start="indoor", wks=6, tdelay=-14, dt=70,
                     cls="hardy", win=(-42, -7), fb=21, succ=None, pp=3, sp=20,
                     notes="Two crops: spring + fall storage heads."),
    "cauliflower": dict(name="Cauliflower", start="indoor", wks=6, tdelay=-7, dt=65,
                     cls="half", win=(-21, -7), fb=10, succ=None, pp=3, sp=18,
                     notes="Fussy: needs steady moisture; self-blanch or tie leaves over head."),
    "kale":     dict(name="Kale", start="indoor", wks=6, tdelay=-14, dt=55,
                     cls="hardy", win=(-42, 21), fb=28, succ=21, pp=2, sp=12,
                     notes="Sweetest after frost; harvest outer leaves all season."),
    "bok-choy": dict(name="Bok Choy", start="indoor", wks=4, tdelay=-7, dt=45,
                     cls="half", win=(-21, 14), fb=14, succ=14, pp=4, sp=8,
                     notes="Spring + fall only; bolts in summer heat."),
    "radish":   dict(name="Radish", start="direct", wks=None, tdelay=None, dt=28,
                     cls="hardy", win=(-42, 70), fb=21, succ=7, pp=20, sp=2,
                     notes="Fastest crop; sow weekly for constant supply; thin ruthlessly."),
    "turnip":   dict(name="Turnip", start="direct", wks=None, tdelay=None, dt=45,
                     cls="hardy", win=(-42, 70), fb=21, succ=14, pp=10, sp=4,
                     notes="Greens + roots; fall crop is sweeter."),
    # roots
    "carrot":   dict(name="Carrot", start="direct", wks=None, tdelay=None, dt=75,
                     cls="half", win=(-21, 84), fb=21, succ=21, pp=30, sp=2,
                     notes="Sandy stone-free bed; keep seedbed moist 10d; fall crop keeps in ground."),
    "beet":     dict(name="Beet", start="direct", wks=None, tdelay=None, dt=55,
                     cls="half", win=(-21, 84), fb=21, succ=21, pp=20, sp=4,
                     notes="Sow cluster 'seeds' 1in apart, thin to 4in; eat thinnings as greens."),
    "potato":   dict(name="Potato", start="direct", wks=None, tdelay=None, dt=95,
                     cls="half", win=(-14, 42), fb=14, succ=None, pp=10, sp=12,
                     notes="Seed potatoes (not grocery); hill when 8in tall; 10 lb seed ≈ 10 ft row."),
    "onion":    dict(name="Onion", start="indoor", wks=8, tdelay=-14, dt=100,
                     cls="hardy", win=(-42, 21), fb=0, succ=None, pp=20, sp=4,
                     notes="Day-length sensitive: pick long/short-day for your latitude."),
    "leek":     dict(name="Leek", start="indoor", wks=10, tdelay=-14, dt=110,
                     cls="hardy", win=(-42, 0), fb=28, succ=None, pp=8, sp=6,
                     notes="Start earliest of all; trench + hill for long white shank."),
    "garlic":   dict(name="Garlic", start="direct", wks=None, tdelay=None, dt=240,
                     cls="hardy", win=(0, 0), fb=None, succ=None, pp=6, sp=6,
                     notes="FALL-PLANT 4-6 wks before first frost; harvest next July."),
    # legumes
    "pea":      dict(name="Pea", start="direct", wks=None, tdelay=None, dt=65,
                     cls="hardy", win=(-42, 28), fb=10, succ=None, pp=15, sp=2,
                     notes="Soak seed 6h; inoculant helps; mid-July resow for fall."),
    "bush-bean": dict(name="Bush Bean", start="direct", wks=None, tdelay=None, dt=55,
                     cls="tender", win=(7, 84), fb=0, succ=21, pp=10, sp=4,
                     notes="Don't soak; succession every 3 wks; pinch tips if aphids."),
    "pole-bean": dict(name="Pole Bean", start="direct", wks=None, tdelay=None, dt=65,
                     cls="tender", win=(7, 70), fb=0, succ=None, pp=5, sp=4,
                     notes="Trellis once, pick all summer; easier than bush succession."),
    # greens
    "lettuce":  dict(name="Lettuce (head)", start="indoor", wks=4, tdelay=-7, dt=55,
                     cls="half", win=(-21, 70), fb=14, succ=14, pp=10, sp=10,
                     notes="Succession is everything; shade cloth mid-summer."),
    "spinach":  dict(name="Spinach", start="direct", wks=None, tdelay=None, dt=45,
                     cls="hardy", win=(-42, 28), fb=28, succ=14, pp=10, sp=4,
                     notes="Spring then STOP (bolts); resume sowings late Aug for fall."),
    "arugula":  dict(name="Arugula", start="direct", wks=None, tdelay=None, dt=35,
                     cls="hardy", win=(-35, 70), fb=21, succ=14, pp=5, sp=4,
                     notes="Peppery; bolts fast in heat — succession tightly."),
    "swiss-chard": dict(name="Swiss Chard", start="direct", wks=None, tdelay=None, dt=55,
                     cls="half", win=(-14, 56), fb=21, succ=None, pp=3, sp=10,
                     notes="Cut-and-come-again all season; survives light frost."),
    # corn + okra
    "sweet-corn": dict(name="Sweet Corn", start="direct", wks=None, tdelay=None, dt=75,
                     cls="tender", win=(14, 84), fb=0, succ=14, pp=15, sp=9,
                     notes="Block planting (4 rows min) for pollination; isolate supersweet types."),
    "okra":     dict(name="Okra", start="indoor", wks=4, tdelay=21, dt=60,
                     cls="tender", win=(21, 63), fb=0, succ=None, pp=3, sp=15,
                     notes="Loves heat; soak seed overnight; pick pods every 2 days."),
    # herbs
    "basil":    dict(name="Basil", start="indoor", wks=5, tdelay=14, dt=50,
                     cls="tender", win=(14, 63), fb=-7, succ=None, pp=2, sp=10,
                     notes="Warmth lover; pinch flowers for leaf production."),
    "cilantro": dict(name="Cilantro", start="direct", wks=None, tdelay=None, dt=40,
                     cls="half", win=(-7, 70), fb=14, succ=14, pp=3, sp=6,
                     notes="Bolts in 5 wks in heat — succession is mandatory."),
    "parsley":  dict(name="Parsley", start="indoor", wks=8, tdelay=-7, dt=75,
                     cls="hardy", win=(-35, 35), fb=21, succ=None, pp=2, sp=8,
                     notes="Slow germinator (3 wks); soak 24h first."),
}

# USDA zone -> (typical last spring frost, typical first fall frost) as month/day.
# Rough national averages — ALWAYS verify locally (±2 weeks of reality).
ZONE_FROST = {
    "3":  (5, 20, 9, 20), "3a": (5, 25, 9, 15), "3b": (5, 18, 9, 22),
    "4":  (5, 10, 10, 1), "4a": (5, 15, 9, 25), "4b": (5, 7, 10, 3),
    "5":  (4, 28, 10, 10), "5a": (5, 2, 10, 5), "5b": (4, 25, 10, 12),
    "6":  (4, 20, 10, 20), "6a": (4, 23, 10, 17), "6b": (4, 18, 10, 22),
    "7":  (4, 10, 10, 30), "7a": (4, 13, 10, 28), "7b": (4, 7, 11, 3),
    "8":  (3, 28, 11, 10), "8a": (4, 1, 11, 7), "8b": (3, 25, 11, 13),
    "9":  (3, 5, 11, 25), "9a": (3, 10, 11, 20), "9b": (2, 25, 12, 5),
    "10": (2, 15, 12, 15),
}

FLAT_SIZES = [72, 50, 32]


# ---------------------------------------------------------------------------
def d(s):
    return dt.date.fromisoformat(s) if s else None


def shift(base, days):
    return base + dt.timedelta(days=days)


def days_until(a, b):
    return (b - a).days


def fmt_date(x):
    return x.isoformat()


def crop_or_die(slug):
    if slug not in CROPS:
        sys.exit(f"error: unknown crop '{slug}'. See: seed_calendar.py crops")
    return CROPS[slug]


# --------------------------- moon phase (folklore) -------------------------
SYNODIC = 29.530588853
NEW_MOON_EPOCH = dt.datetime(2000, 1, 6, 18, 14)


def moon_phase(date):
    """Return (phase_name 0-7, is_waxing). Mean-phase approx, ±1 day."""
    days = (dt.datetime.combine(date, dt.time(12)) - NEW_MOON_EPOCH).total_seconds() / 86400.0
    age = days % SYNODIC
    idx = int((age / SYNODIC) * 8 + 0.5) % 8
    names = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
             "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
    waxing = 0 < age < SYNODIC / 2
    return names[idx], waxing


def moon_note(date, part):
    """part: 'leaf/fruit' (above ground) or 'root' (below ground)."""
    phase, waxing = moon_phase(date)
    wants_waxing = part != "root"
    ok = waxing == wants_waxing
    tag = "matches" if ok else "off-cycle"
    return f"[moon {phase}, {tag} for {'waxing/above-ground' if wants_waxing else 'waning/below-ground'}]"


ROOT_CROPS = {"carrot", "beet", "radish", "turnip", "potato", "onion", "leek", "garlic"}


# --------------------------- event builders -------------------------------
def build_events(slug, last, first, people=1, moon=False):
    """Return list of (date, code, crop, detail) sorted by date."""
    c = crop_or_die(slug)
    ev = []
    n_plants = max(1, round(c["pp"] * people))
    part = "root" if slug in ROOT_CROPS else "leaf/fruit"
    m = (lambda x: moon_note(x, part)) if moon else (lambda x: "")

    def add(date, code, detail):
        if date is None:
            return
        past = " (PAST)" if date < dt.date.today() else ""
        ev.append((date, code, c["name"], detail + past))

    if slug == "garlic":
        add(first - dt.timedelta(days=35), "FALL-PLANT",
            f"plant cloves 2in deep, mulch 4in; {m(first)}")
        nxt = first.replace(year=first.year + 1)
        add(shift(nxt, -30), "HARVEST ~", "next July when tops brown; cure 2 wks")
        return sorted(ev)

    # --- indoor start chain ---
    if c["start"] in ("indoor", "either") and c["wks"]:
        sow = shift(last, -7 * c["wks"])
        cells = math.ceil(n_plants * 1.2)
        trays = {fs: math.ceil(cells / fs) for fs in FLAT_SIZES}
        tray_txt = f"{cells} cells -> {trays[72]} flat(s) of 72 ({trays[50]}x50 / {trays[32]}x32)"
        add(sow, "SOW-INDOORS", f"{tray_txt}; germ 20-25C; {c['notes'].split(';')[0]}. {m(sow)}")
        if slug in ("tomato", "pepper", "eggplant"):
            add(shift(sow, 7 * c["wks"] - 14), "POT-UP", "into 4in pots if crowded")
        tdelay = c["tdelay"] if c["tdelay"] is not None else 0
        tp = shift(last, tdelay)
        if c["start"] == "indoor" or c["tdelay"] is not None:
            add(shift(tp, -7), "HARDEN-OFF", "1h outdoors day 1, double daily x 7d")
            warm = " soil 18C+;" if c["cls"] == "tender" else ""
            add(tp, "TRANSPLANT", f"{n_plants} plants,{warm} spacing {c['sp']}in")
            add(shift(tp, c["dt"]), "HARVEST ~", f"±2 weeks")

    # --- direct sow window (primary + fall) ---
    if c["start"] in ("direct", "either"):
        ws, we = c["win"]
        w_start, w_end = shift(last, ws), shift(last, we)
        if c["start"] == "direct" or c["wks"] is None or c["cls"] in ("hardy", "half"):
            rowft = n_plants * c["sp"] / 12.0
            if c["start"] == "direct":
                add(w_start, "SOW-DIRECT",
                    f"window {fmt_date(w_start)}..{fmt_date(w_end)}; "
                    f"~{rowft:.0f} row-ft for {n_plants} plants. {m(w_start)}")
            else:
                add(w_start, "SOW-DIRECT-OR-START",
                    f"window {fmt_date(w_start)}..{fmt_date(w_end)}. {m(w_start)}")
            add(shift(w_start, c["dt"]), "HARVEST ~", "±2 weeks" if c["dt"] >= 40 else "")

    # --- succession ---
    if c["succ"]:
        fb = c["fb"] if isinstance(c["fb"], int) else 0
        limit = shift(first, fb) if fb is not None else first
        if slug in ("spinach",):
            limit = shift(last, 28)  # stop spring chain when heat arrives
        t = shift(last, c["win"][0])
        k = 1
        while t <= limit and k <= 26:
            if shift(t, c["dt"]) <= limit:
                add(t, f"SOW #{k}", f"succession every {c['succ']}d. {m(t)}")
                k += 1
            t = shift(t, c["succ"])
        # fall successions for bolt-prone greens
        if slug in ("spinach", "arugula", "lettuce"):
            t = shift(first, -45)
            while t <= shift(first, fb - 21 if isinstance(fb, int) else -21):
                add(t, "SOW-FALL", f"fall crop. {m(t)}")
                t = shift(t, c["succ"])

    # --- fall sow-by (roots + brassicas + greens) ---
    if c["start"] == "direct" and c["cls"] in ("hardy", "half"):
        fb = c["fb"] if isinstance(c["fb"], int) else 10
        sowby = shift(shift(first, fb), -(c["dt"] + 7))
        add(sowby, "SOW-BY-FALL", f"last date for fall crop (harvest ~{fmt_date(shift(sowby, c['dt']))})")

    if not ev:
        add(last, "NOTE", f"{c['name']}: see notes — {c['notes']}")
    return sorted(ev)


def plants_needed(slugs, people):
    rows = []
    for s in slugs:
        c = crop_or_die(s)
        n = max(1, round(c["pp"] * people))
        rows.append(dict(slug=s, name=c["name"], plants=n, spacing_in=c["sp"],
                         row_ft=round(n * c["sp"] / 12.0, 1),
                         flat_cells=math.ceil(n * 1.2)))
    return rows


# --------------------------- output helpers -------------------------------
def print_events(events, verbose=True):
    W = (11, 15, 14)
    print(f"{'DATE':<11} {'EVENT':<15} {'CROP':<14} DETAIL")
    print("-" * 78)
    for date, code, crop, detail in events:
        flag = " *" if date < dt.date.today() else ""
        print(f"{fmt_date(date):<11} {code:<15} {crop[:13]:<14} {detail}{flag}")
    if verbose and any(e[0] < dt.date.today() for e in events):
        print("\n* = date already passed — see recovery advice in SKILL.md pitfalls")


# --------------------------- subcommands -----------------------------------
def cmd_crops(args):
    if args.crop:
        s = args.crop
        c = crop_or_die(s)
        print(f"== {c['name']} ({s}) ==")
        for k, v in c.items():
            if k != "name":
                print(f"  {k:10} {v}")
        return
    print(f"{'SLUG':<14} {'START':<8} {'WKS':>4} {'DT':>4} {'CLASS':<8} {'SUCC':>5} "
          f"{'PP':>3} {'SPIN':>4}  NOTES")
    print("-" * 100)
    for s, c in sorted(CROPS.items()):
        print(f"{s:<14} {c['start']:<8} {str(c['wks'] or '-'):>4} {c['dt']:>4} "
              f"{c['cls']:<8} {str(c['succ'] or '-'):>5} {c['pp']:>3} {c['sp']:>4}  "
              f"{c['notes'][:52]}")


def cmd_frost(args):
    z = args.zone.lower()
    if z not in ZONE_FROST:
        sys.exit(f"error: zone '{args.zone}' not in table {sorted(set(k.rstrip('ab') for k in ZONE_FROST))}")
    lm, ld_, fm, fd = ZONE_FROST[z]
    yr = dt.date.today().year
    print(f"Zone {z.upper()} rough frost estimates (VERIFY with local extension data):")
    print(f"  last spring frost ~ {dt.date(yr, lm, ld_)}")
    print(f"  first fall frost  ~ {dt.date(yr, fm, fd)}")
    print(f"  frost-free days   ~ {(dt.date(yr, fm, fd) - dt.date(yr, lm, ld_)).days}")
    print("  Zone = winter-cold average, NOT frost timing; ±2 weeks of reality.")


def cmd_plan(args):
    last, first = d(args.last_frost), d(args.first_frost)
    if first <= last:
        sys.exit("error: first fall frost must be after last spring frost")
    ev = build_events(args.crop, last, first, args.people, args.moon)
    if args.json:
        print(json.dumps([dict(date=fmt_date(x[0]), event=x[1], crop=x[2], detail=x[3])
                          for x in ev], indent=2))
    else:
        print_events(ev)


def cmd_garden(args):
    last, first = d(args.last_frost), d(args.first_frost)
    if first <= last:
        sys.exit("error: first fall frost must be after last spring frost")
    slugs = [s.strip().lower() for s in args.crops.split(",") if s.strip()]
    bad = [s for s in slugs if s not in CROPS]
    if bad:
        sys.exit(f"error: unknown crops {bad}. See: seed_calendar.py crops")
    events = []
    for s in slugs:
        events.extend(build_events(s, last, first, args.people, args.moon))
    events.sort()
    if args.json:
        out = dict(
            last_frost=fmt_date(last), first_frost=fmt_date(first),
            frost_free_days=days_until(last, first),
            plants=plants_needed(slugs, args.people),
            events=[dict(date=fmt_date(x[0]), event=x[1], crop=x[2], detail=x[3])
                    for x in events])
        print(json.dumps(out, indent=2))
        return
    ff = days_until(last, first)
    print(f"GARDEN CALENDAR — last frost {fmt_date(last)}, first frost {fmt_date(first)} "
          f"({ff} frost-free days), feeding {args.people}")
    print("=" * 78)
    print_events(events, verbose=False)
    # tray table
    indoor = [s for s in slugs if CROPS[s]["start"] in ("indoor", "either") and CROPS[s]["wks"]]
    if indoor:
        print("\nSEED-STARTING LOGISTICS (indoor crops)")
        print("-" * 62)
        print(f"{'CROP':<14} {'PLANTS':>6} {'CELLS':>6} {'72s':>4} {'50s':>4} {'32s':>4}")
        tot = dict(cells=0, t72=0, t50=0, t32=0)
        for s in indoor:
            c = CROPS[s]
            n = max(1, round(c["pp"] * args.people))
            cells = math.ceil(n * 1.2)
            t72, t50, t32 = (math.ceil(cells / f) for f in FLAT_SIZES)
            tot["cells"] += cells; tot["t72"] += t72; tot["t50"] += t50; tot["t32"] += t32
            print(f"{c['name'][:13]:<14} {n:>6} {cells:>6} {t72:>4} {t50:>4} {t32:>4}")
        print("-" * 62)
        print(f"{'TOTAL':<14} {'':>6} {tot['cells']:>6} {tot['t72']:>4} {tot['t50']:>4} {tot['t32']:>4}")
    # row-feet table
    print("\nBED/ROW SPACE (in-row spacing x plants)")
    print("-" * 62)
    print(f"{'CROP':<14} {'PLANTS':>6} {'SPACING':>8} {'ROW-FT':>8}")
    total_ft = 0.0
    for r in plants_needed(slugs, args.people):
        total_ft += r["row_ft"]
        print(f"{r['name'][:13]:<14} {r['plants']:>6} {r['spacing_in']:>7}in {r['row_ft']:>8}")
    print("-" * 62)
    print(f"{'TOTAL':<14} {'':>6} {'':>8} {round(total_ft):>8}")
    print(f"(add ~40% for aisles/beds → plan ~{round(total_ft * 1.4)} total row-ft of bed)")


def cmd_succession(args):
    frm, until, first = d(args.from_), d(args.until), d(args.first_frost)
    if until <= frm:
        sys.exit("error: --until must be after --from")
    c = crop_or_die(args.crop)
    if not c["succ"]:
        print(f"{c['name']}: single-planting crop (no succession) — {c['notes']}")
        return
    fb = c["fb"] if isinstance(c["fb"], int) else 0
    limit = min(until, shift(first, fb - c["dt"]))
    t, k = frm, 1
    print(f"SUCCESSION — {c['name']} every {c['succ']}d, {fmt_date(frm)} .. {fmt_date(until)}")
    print(f"stop rule: sow + {c['dt']}d growth must fit before {fmt_date(shift(first, fb))}")
    print("-" * 60)
    while t <= limit:
        harv = shift(t, c["dt"])
        fits = "OK " if harv <= shift(first, fb) else "RISK"
        print(f"  sow #{k:<2} {fmt_date(t)}  → harvest ~{fmt_date(harv)}  [{fits}]")
        t = shift(t, c["succ"])
        k += 1


# --------------------------- cli -------------------------------------------
def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("crops", help="list crop library")
    sp.add_argument("crop", nargs="?", help="detail for one crop slug")
    sp.set_defaults(fn=cmd_crops)

    sp = sub.add_parser("frost", help="rough frost dates by USDA zone")
    sp.add_argument("--zone", required=True, help="e.g. 6b")
    sp.set_defaults(fn=cmd_frost)

    sp = sub.add_parser("plan", help="full timeline for one crop")
    sp.add_argument("--crop", required=True)
    sp.add_argument("--last-frost", required=True, help="YYYY-MM-DD")
    sp.add_argument("--first-frost", required=True, help="YYYY-MM-DD")
    sp.add_argument("--people", type=int, default=1)
    sp.add_argument("--moon", action="store_true", help="annotate folklore moon phases")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(fn=cmd_plan)

    sp = sub.add_parser("garden", help="whole-garden calendar + logistics")
    sp.add_argument("--crops", required=True, help="comma-separated slugs")
    sp.add_argument("--last-frost", required=True)
    sp.add_argument("--first-frost", required=True)
    sp.add_argument("--people", type=int, default=1)
    sp.add_argument("--moon", action="store_true")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(fn=cmd_garden)

    sp = sub.add_parser("succession", help="succession sow schedule")
    sp.add_argument("--crop", required=True)
    sp.add_argument("--from", dest="from_", required=True)
    sp.add_argument("--until", required=True)
    sp.add_argument("--first-frost", required=True)
    sp.set_defaults(fn=cmd_succession)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
