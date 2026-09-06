#!/usr/bin/env python3
"""
storm_ready.py — household severe-weather preparedness audit and planner.

Tells you what your household is missing for the storms your region actually
gets, sizes water/food/power for your people and pets (real math, not generic
lists), and prints phase-by-phase checklists from 72 hours out to recovery.

Commands:
  regions              list region profiles and what each demands
  profile              show/edit household profile (people, pets, needs)
  audit                gap analysis: what you have vs what your region demands
  water                water storage + purification math for your household
  food                 no-cook food plan, calories and rotation
  power                outage power plan: loads, battery/generator sizing
  timeline             countdown checklist by phase (72h/48h/24h/12h/during/after)
  example              self-contained demo (gulf-coast hurricane household)

Data file (override with --file): ~/.storm-ready.json
Pure stdlib. Guidance follows FEMA/Ready.gov conventions; quantities adapt to
YOUR household, that's the point.
"""
import argparse
import datetime as dt
import json
import math
import os
import sys

DEFAULT_FILE = os.path.expanduser("~/.storm-ready.json")

# ---------------------------------------------------------------- regions
# Each profile: hazards, water_days, food_days, checklist key items.
# Water: Ready.gov baseline 1 gal/person/day ×3 days; hurricane counties
# (FL/HI) and boil-prone areas recommend 14; earthquake country 14.
REGIONS = {
    "hurricane-gulf": {
        "hazards": ["wind", "storm-surge", "flooding", "multi-day-outage"],
        "water_days": 14, "food_days": 14,
        "note": "Grid can be down 1-3 weeks; municipal water may lose pressure "
                "or get a boil notice. 14-day water/food is the county-standard.",
    },
    "hurricane-atlantic": {
        "hazards": ["wind", "flooding", "multi-day-outage"],
        "water_days": 7, "food_days": 7,
        "note": "Days-long outages common inland after landfall; 7-day kit.",
    },
    "tornado": {
        "hazards": ["tornado", "severe-thunderstorm", "short-outage"],
        "water_days": 3, "food_days": 3,
        "note": "Warning is minutes, not days. Priorities: shelter kit, helmets, "
                "shoes, whistle — and know your safe room BEFORE the season.",
    },
    "ice-storm": {
        "hazards": ["ice", "cold-indoor", "short-outage", "co-risk"],
        "water_days": 3, "food_days": 5,
        "note": "Cold inside the house is the killer. Priorities: safe heat for "
                "one room, CO alarm, insulation layers — and NEVER run a grill "
                "or generator indoors.",
    },
    "atmospheric-river": {
        "hazards": ["flooding", "landslide", "boil-notice"],
        "water_days": 7, "food_days": 5,
        "note": "Flooding contaminates municipal supply; boil notices follow. "
                "Elevate stores, know sandbag sources, keep a water filter.",
    },
    "wildfire-wui": {
        "hazards": ["wildfire", "evacuation", "smoke", "psps-outage"],
        "water_days": 3, "food_days": 3,
        "note": "This is a GO kit, not a shelter kit: documents, meds, N95s, "
                "hard drives — packed by May, car facing out, gas above half.",
    },
    "blizzard-plains": {
        "hazards": ["snow", "cold-indoor", "stranded", "short-outage"],
        "water_days": 3, "food_days": 7,
        "note": "You may be snowed IN for days: heat, food you can cook if power "
                "dies, and a vehicle kit if you must drive.",
    },
    "generic": {
        "hazards": ["short-outage"],
        "water_days": 3, "food_days": 3,
        "note": "Baseline 72-hour household kit (Ready.gov standard).",
    },
}

# ---------------------------------------------------------------- checklist
# id: (phase, priority, item, quantity fn(household) or None, region tags)
# phase: prep (any time) | p72 | p48 | p24 | p12 | during | after
# priority: P0 life-safety | P1 hardship-reducer | P2 convenience
def build_checklist(hh, region_key="generic"):
    """Return list of dicts for a household profile hh in region_key."""
    reg = REGIONS.get(region_key, REGIONS["generic"])
    people = hh.get("people", 1)
    pets = hh.get("pets", [])
    days_w = hh.get("water_days_override") or reg["water_days"]
    days_f = hh.get("food_days_override") or reg["food_days"]
    dogs = sum(1 for p in pets if p.get("kind") == "dog")
    cats = sum(1 for p in pets if p.get("kind") == "cat")
    pet_lb = sum(p.get("weight_lb", 20) for p in pets)
    items = []

    def add(cid, phase, pri, item, qty=None, regions=None):
        items.append({"id": cid, "phase": phase, "pri": pri,
                      "item": item, "qty": qty, "regions": regions or []})

    # --- always (base kit) ---
    add("water-store", "prep", "P0", "Stored drinking water (see `water` cmd)",
        f"{days_w * people} gal ({people} people × {days_w} days)")
    add("water-purify", "prep", "P0",
        "Water purification: unscented bleach (fresh) AND filter/boil path", "1 bottle")
    add("food-store", "prep", "P0", "No-cook food, rotates with pantry (see `food` cmd)",
        f"{days_f * people} person-days ({people} × {days_f}d × 2000 kcal)")
    add("radio", "prep", "P0", "NOAA weather radio (hand-crank or battery)", "1")
    add("flashlights", "prep", "P0", "Flashlights/headlamps + spare batteries",
        max(2, people))
    add("first-aid", "prep", "P0", "First-aid kit sized for household", "1")
    add("meds-7d", "prep", "P0", "7+ day buffer of every prescription med", "per person")
    add("whistle", "prep", "P0", "Whistle per person (signal beats shouting)", people)
    add("co-alarm", "prep", "P0", "CO alarm with battery backup (if ANY fuel device)",
        "1 per level")
    add("fire-ext", "prep", "P1", "ABC fire extinguisher", "1")
    add("cash", "prep", "P0", "Cash in small bills (ATMs/card readers die)", "$100-300")
    add("docs", "prep", "P0",
        "Document go-binder or encrypted copy: IDs, deeds/lease, insurance, "
        "medical lists, vet records, photos of every room", "1")
    add("sanitation", "prep", "P1",
        "Sanitation: trash bags, bucket toilet line, hygiene supplies", "1 set")
    add("phone-backup", "prep", "P1", "Charged power banks", f"{max(1, people // 2)}+")
    add("contacts-card", "prep", "P1",
        "Paper contact list + out-of-area check-in contact", "1")
    # infants / medical
    if hh.get("infants"):
        add("formula", "prep", "P0", "Formula + sterile water + bottles",
            f"{hh['infants']} × 7 days")
    if hh.get("medical_devices"):
        add("med-power", "prep", "P0",
            f"Backup power for medical devices ({', '.join(hh['medical_devices'])}) "
            "— see `power`; register with utility for priority restoration",
            "sized in `power`")
    # pets
    if pets:
        add("pet-food", "prep", "P0", "Pet food (sealed, rotated)",
            f"{days_f or 3} days × {dogs} dog/{cats} cat")
        add("pet-water", "prep", "P0", "Pet water",
            f"~{math.ceil(pet_lb)} lb of animal ≈ {math.ceil(pet_lb)} oz/day")
        add("pet-meds", "prep", "P1", "Pet meds + shot records copy", "1 set")
        add("pet-carrier", "prep", "P0", "Carrier per animal", len(pets))
        add("pet-calming", "prep", "P2", "Anxiety vest/thunder shirt if noise-phobic", "1")

    # --- region-specific prep ---
    add("shelter-room", "prep", "P0",
        "Designated safe room known to everyone (lowest floor, interior, no windows)",
        "1", ["tornado"])
    add("helmets", "prep", "P0",
        "Bike/sports helmets in the safe room (head injuries are the tornado killer)",
        people, ["tornado"])
    add("shoes-safe-room", "prep", "P0",
        "Closed shoes + work gloves at each bed (post-tornado glass)", people,
        ["tornado", "hurricane-gulf", "hurricane-atlantic"])
    add("plywood-film", "prep", "P1",
        "Window protection measured, cut, LABELED, and staged (plywood or film)",
        "all windows", ["hurricane-gulf", "hurricane-atlantic"])
    add("sandbag-source", "prep", "P1",
        "Known sandbag pickup point + plan to elevate stores", "1",
        ["atmospheric-river", "hurricane-gulf"])
    add("heat-room", "prep", "P0",
        "One-room heat plan: safely vented heater OR indoor-safe option + "
        "door draft stoppers + rugs", "1", ["ice-storm", "blizzard-plains"])
    add("warm-layers", "prep", "P0", "Sleeping bags/blankets rated for indoor cold",
        people, ["ice-storm", "blizzard-plains"])
    add("n95", "prep", "P0", "N95 masks per person (smoke)", people, ["wildfire-wui"])
    add("go-bag", "prep", "P0",
        "GO bags packed per person: 3 days clothes, meds, chargers, copies of "
        "documents — grab-and-go in 10 minutes", people, ["wildfire-wui", "hurricane-gulf"])
    add("car-kit", "prep", "P1",
        "Vehicle kit: blanket, water, snacks, shovel, jumper cables, phone charger",
        "1", ["blizzard-plains", "wildfire-wui", "ice-storm"])
    add("evac-route", "prep", "P0",
        "Two evacuation routes agreed + meeting point if separated", "1",
        ["wildfire-wui", "hurricane-gulf", "hurricane-atlantic", "flooding"])
    add("utility-shutoff", "prep", "P0",
        "Everyone knows gas/water/main-breaker shutoff locations and tools",
        "1", ["hurricane-gulf", "hurricane-atlantic", "atmospheric-river", "ice-storm"])

    # --- countdown phases ---
    add("fill-tubs", "p72", "P0",
        "Fill bathtubs + washing machine (flush/toilet water) BEFORE pressure drops",
        None, ["hurricane-gulf", "hurricane-atlantic", "atmospheric-river"])
    add("freeze-bottles", "p72", "P1",
        "Freeze water bottles; fill freezer gaps (ice keeps food 48h, bottles "
        "become drinking water)", None,
        ["hurricane-gulf", "hurricane-atlantic", "ice-storm", "blizzard-plains"])
    add("gas-car", "p72", "P0", "Vehicles fueled; never below half a tank in season",
        None, ["hurricane-gulf", "hurricane-atlantic", "wildfire-wui", "blizzard-plains"])
    add("cash-out", "p72", "P1", "Withdraw a week of cash", None,
        ["hurricane-gulf", "hurricane-atlantic", "ice-storm"])
    add("rx-fill", "p72", "P0", "Refill every prescription you can (emergency fills)",
        None, ["hurricane-gulf", "hurricane-atlantic", "wildfire-wui"])
    add("laundry-dishes", "p72", "P2", "All laundry and dishes done (clean clothes "
        "matter more than you'd think)", None,
        ["hurricane-gulf", "hurricane-atlantic", "atmospheric-river"])
    add("charge-everything", "p48", "P0", "Charge phones, power banks, laptops, "
        "medical devices; top off vehicle tanks", None, [])
    add("propane-ice", "p48", "P1", "Propane/butane for camp stove + ice chests; "
        "dry ice plan for freezer", None,
        ["hurricane-gulf", "hurricane-atlantic", "ice-storm"])
    add("gen-test", "p48", "P0", "Test generator OUTDOORS ≥20 ft from any window; "
        "stock fuel + stabilizer; test transfer setup", None,
        ["hurricane-gulf", "hurricane-atlantic", "ice-storm", "blizzard-plains"])
    add("yard-missiles", "p48", "P0",
        "Bring in/tie down EVERYTHING outdoors: furniture, trampolines, bins — "
        "they become missiles", None,
        ["hurricane-gulf", "hurricane-atlantic", "tornado"])
    add("window-cover", "p24", "P0", "Install window protection; tape does nothing",
        None, ["hurricane-gulf", "hurricane-atlantic"])
    add("fridge-cold", "p24", "P1", "Fridge to coldest setting; group frozen goods "
        "together; freeze gel packs", None,
        ["hurricane-gulf", "hurricane-atlantic", "ice-storm"])
    add("water-containers", "p24", "P0", "Fill every clean container (see `water` "
        "target); bathtubs if surge/flood risk", None,
        ["hurricane-gulf", "hurricane-atlantic", "atmospheric-river"])
    add("evac-decide", "p24", "P0",
        "Evacuation DECISION: if in an evacuation zone or surge zone and officials "
        "say go — GO. Leaving early is the only reliable hurricane survival move",
        None, ["hurricane-gulf", "hurricane-atlantic"])
    add("pet-plan-storm", "p24", "P0", "Pets inside, carriers staged, vet records "
        "in go-binder (shelters require them)", None,
        ["hurricane-gulf", "hurricane-atlantic", "wildfire-wui"])
    add("shelter-move", "p12", "P0", "Move to safe room/shelter; helmets on, shoes "
        "on, whistle, radio, water", None, ["tornado", "hurricane-gulf"])
    add("fridge-limit", "during", "P1",
        "Keep fridge/freezer CLOSED: unopened fridge holds 4h, full freezer 48h",
        None, [])
    add("co-rule", "during", "P0",
        "NO grills/generators/charcoal indoors or in garages — CO kills silently "
        "every storm", None, [])
    add("candles-no", "during", "P1", "Flashlights not candles (fire + gas leaks)",
        None, [])
    add("water-notify", "during", "P1",
        "Treat tap as unsafe until utility clears it (boil/filter/bleach)", None,
        ["hurricane-gulf", "atmospheric-river", "flooding"])
    add("flood-water", "during", "P0",
        "NEVER drive or walk through flood water: 6 in moving water takes a car, "
        "12 in takes an SUV — Turn Around Don't Drown", None, [])
    add("downed-lines", "during", "P0",
        "Assume every downed line is live; keep 30 ft and report", None, [])
    add("photo-damage", "after", "P0",
        "Photograph ALL damage before cleanup; call insurance ASAP; keep receipts "
        "for every repair/hotel/meal", None, [])
    add("food-toss", "after", "P0",
        "Toss refrigerated food after 4h above 40°F; when in doubt throw it out",
        None, [])
    add("generator-reports", "after", "P1",
        "File utility outage report and check on isolated neighbors", None, [])
    add("fema-assist", "after", "P1",
        "DisasterAssistance.gov + SBA loans open after declarations — apply "
        "within the window", None, [])
    return items


# ---------------------------------------------------------------- default profile
def default_profile():
    return {
        "region": "generic",
        "people": 2,
        "pets": [],
        "infants": 0,
        "medical_devices": [],
        "inventory": {},   # checklist id -> status: have | partial | missing
    }


def load_file(path, create=False):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    if create:
        prof = default_profile()
        with open(path, "w") as f:
            json.dump(prof, f, indent=2)
        return prof
    return None


# ---------------------------------------------------------------- water math
GAL_PER_L = 0.264172

def water_report(hh, region_key):
    reg = REGIONS[region_key]
    people = hh.get("people", 1)
    pets = hh.get("pets", [])
    days = hh.get("water_days_override") or reg["water_days"]
    pet_lb = sum(p.get("weight_lb", 20) for p in pets)
    pet_oz = pet_lb * 1.0        # ~1 oz per lb per day common guidance
    pet_gal = pet_oz / 128.0
    drink = people * days        # 1 gal/person/day drinking+basic
    hygiene = 0.5 * people * days  # extra if you want to wash
    print(f"Water plan — {region_key} ({days}-day standard)")
    print(f"  Drinking/basic (1 gal × person × day): {drink} gal "
          f"({drink * 3.785:.0f} L)")
    if pets:
        print(f"  Pets ({pet_lb:.0f} lb total, ~1 oz/lb/day): {pet_oz:.0f} oz/day "
              f"→ {pet_gal * days:.1f} gal over {days} days")
    print(f"  Hygiene cushion (+50%, optional): {hygiene:.0f} gal")
    total = drink + pet_gal * days + hygiene
    print(f"  TOTAL: {math.ceil(total)} gal ({math.ceil(total) * 3.785:.0f} L)")
    print(f"\n  Storage: {math.ceil(total / 7)} × 7-gal aquatainers, or "
          f"{math.ceil(total / 2.5)} × 2.5-gal jugs, or "
          f"{math.ceil(total * 4 / 24)} × 24-bottle cases")
    print("\n  Purification fallbacks (if stored water runs out):")
    print("   • Boil: rolling boil 1 min (3 min above 6,500 ft) — most reliable")
    print("   • Unscented household bleach (5-6%): 8 drops/gal (6 per 2 L),")
    print("     mix, wait 30 min; slight chlorine smell = OK; none = repeat")
    print("   • Filter: hollow-fiber pump/straw for bacteria/protozoa (NOT viruses)")
    print("   • Never drink flood water without boiling + bleach")
    print("\n  Rotation: tap-water containers every 6-12 months; commercially")
    print("  bottled water: check the date, keep out of sunlight.")
    return math.ceil(total)


# ---------------------------------------------------------------- food math
def food_report(hh, region_key):
    reg = REGIONS[region_key]
    people = hh.get("people", 1)
    days = hh.get("food_days_override") or reg["food_days"]
    kcal_day = 2000
    total_kcal = people * days * kcal_day
    print(f"Food plan — {region_key} ({days}-day standard)")
    print(f"  Target: {people} people × {days} days × {kcal_day:,} kcal = "
          f"{total_kcal:,} kcal")
    print("\n  Build from the pantry (rotate what you already eat):")
    print("   • Canned protein: beans, tuna, chicken, chili (~250 kcal/can)")
    print("   • Canned meals: soups, ravioli (~300 kcal/can) — eat first, they're heavy")
    print("   • Grains: crackers, instant oats, rice (cook later), dry cereal")
    print("   • Nut butters + nuts + trail mix: calorie-dense, no prep (~170/oz)")
    print("   • Comfort + electrolytes: powdered drink mix, coffee/tea, cookies")
    if any(h in ("ice-storm", "blizzard-plains") for h in reg["hazards"]):
        print("   • Your region can strand you WITH a working stove top:")
        print("     keep pasta/sauce/rice you can cook if only gas survives")
    print(f"\n  Rule-of-thumb basket: {people * days} cans meals + "
          f"{people * days // 2} cans protein + {people * days // 3} lb grains/nuts")
    print("  Special: infant formula, pet food (see audit), low-sodium if needed")
    print("\n  Fridge discipline when power dies: unopened = 4 h; full freezer = "
          "48 h. Thermometer in each so you're guessing less.")
    return total_kcal


# ---------------------------------------------------------------- power math
LOADS = {
    "phone":      {"w": 6,    "h": 2,   "note": "daily top-up"},
    "radio":      {"w": 3,    "h": 4,   "note": "NOAA weather radio"},
    "led-lights": {"w": 10,   "h": 5,   "note": "couple of lamps"},
    "laptop":     {"w": 45,   "h": 3,   "note": "work from home"},
    "fridge":     {"w": 150,  "h": 8,   "note": "duty-cycled: 150 W × ~33%"},
    "freezer":    {"w": 150,  "h": 8,   "note": "duty-cycled similarly"},
    "cpap":       {"w": 40,   "h": 8,   "note": "no humidifier; humidifier ~2×"},
    "oxygen-conc":{"w": 350,  "h": 24,  "note": "MEDICAL — also have O2 bottles"},
    "fans":       {"w": 55,   "h": 10,  "note": "summer airflow matters"},
    "router-modem":{"w": 18,  "h": 24,  "note": "keep internet alive (fiber often survives)"},
    "med-device-generic": {"w": 100, "h": 12, "note": "placeholder for other devices"},
}


def power_report(hh, loads_selected, battery_wh=None):
    print("Power plan — daily energy for selected loads:")
    total = 0.0
    peak = 0
    print(f"  {'load':<16}{'watts':>7}{'h/day':>7}{'Wh/day':>8}  note")
    for key in loads_selected:
        if key not in LOADS:
            print(f"  {key:<16} UNKNOWN — see `power --list` for keys")
            continue
        ld = LOADS[key]
        wh = ld["w"] * ld["h"]
        total += wh
        peak += ld["w"] if key not in ("fridge", "freezer") else ld["w"] * 3.5
        print(f"  {key:<16}{ld['w']:>7}{ld['h']:>7}{wh:>8}  {ld['note']}")
    print(f"  {'TOTAL':<16}{'':>7}{'':>7}{total:>8.0f}")
    print(f"\n  Peak (surge-aware, compressor start ×3.5): {peak:.0f} W —")
    print("  inverter/generator must EXCEED this or breakers trip.")
    usable = 0.85  # inverter losses + DoD
    for bank in (500, 1000, 2000, 3000, 5000):
        days = bank * usable / total if total else 0
        print(f"  {bank}-Wh power station runs this ≈ {days:.1f} days")
    if battery_wh:
        days = battery_wh * usable / total
        print(f"\n  Your {battery_wh}-Wh bank: {days:.1f} days of the above.")
    print("\n  Rules that keep people alive:")
    print("   • Generator: OUTDOORS only, ≥20 ft from windows/vents, dry,")
    print("     CO alarm indoors always; 3-4 day fuel with stabilizer, run dry")
    print("     before storage; transfer switch or heavy-duty interlock for house")
    print("     circuits — backfeeding a dryer outlet kills linemen.")
    print("   • Solar panels recharge small banks fine; a 100 W panel yields")
    print("     ~300-500 Wh/day of sun — matches phones/radio/CPAP, not fridges.")
    print("   • Medical devices: register with your utility (priority restore),")
    print("     size battery for 3× daily need, and keep a mechanical fallback.")
    return total


# ---------------------------------------------------------------- printing
PHASES = ["prep", "p72", "p48", "p24", "p12", "during", "after"]
PHASE_LABEL = {
    "prep": "anytime prep", "p72": "T-72 h", "p48": "T-48 h", "p24": "T-24 h",
    "p12": "T-12 h", "during": "during the storm", "after": "after the storm",
}
PRI_ORDER = {"P0": 0, "P1": 1, "P2": 2}


def relevant(items, region_key):
    return [i for i in items if not i["regions"] or region_key in i["regions"]]


def print_audit(hh, region_key):
    reg = REGIONS[region_key]
    items = relevant(build_checklist(hh, region_key), region_key)
    inv = hh.get("inventory", {})
    print(f"Preparedness audit — {region_key}")
    print(f"  hazards: {', '.join(reg['hazards'])}")
    print(f"  standard: {reg['water_days']}-day water, {reg['food_days']}-day food")
    print(f"  {reg['note']}\n")
    missing_p0 = []
    for ph in PHASES:
        rows = [i for i in items if i["phase"] == ph]
        if not rows:
            continue
        print(f"[{PHASE_LABEL[ph]}]")
        for i in sorted(rows, key=lambda x: PRI_ORDER[x["pri"]]):
            status = inv.get(i["id"], "missing")
            mark = {"have": "✓", "partial": "~", "missing": "✗"}[status]
            qty = f" — {i['qty']}" if i["qty"] else ""
            print(f"  {mark} {i['pri']} {i['item']}{qty}")
            if status != "have" and i["pri"] == "P0" and ph == "prep":
                missing_p0.append(i["id"])
        print()
    print(f"P0 prep gaps: {len(missing_p0)} "
          + (f"({', '.join(missing_p0)})" if missing_p0 else "— nice.")
          + "  Fix these first.")
    print("Mark what you have:  storm_ready.py profile --mark-have water-store")
    return missing_p0


def print_timeline(region_key):
    items = relevant(build_checklist({"people": 1}), region_key)
    print(f"Storm countdown — {region_key}\n")
    for ph in PHASES[1:]:
        rows = [i for i in items if i["phase"] == ph]
        if not rows:
            continue
        print(f"── {PHASE_LABEL[ph]} " + "─" * max(0, 40 - len(PHASE_LABEL[ph])))
        for i in sorted(rows, key=lambda x: PRI_ORDER[x["pri"]]):
            print(f"  {i['pri']}  {i['item']}")
        print()


# ---------------------------------------------------------------- commands
def cmd_regions(args):
    print("Region profiles:\n")
    for key, r in REGIONS.items():
        print(f"  {key:<20} water {r['water_days']}d | food {r['food_days']}d")
        print(f"  {'':<20} {r['note']}\n")


def cmd_profile(args):
    path = args.file
    hh = load_file(path, create=True)
    if args.region:
        if args.region not in REGIONS:
            print(f"Unknown region '{args.region}' — see `regions` command.")
            sys.exit(1)
        hh["region"] = args.region
    if args.people:
        hh["people"] = args.people
    if args.pets is not None:
        hh["pets"] = []
        for spec in args.pets.split(","):
            kind, w = spec.strip().split(":")
            hh["pets"].append({"kind": kind, "weight_lb": float(w)})
    if args.mark_have or args.mark_partial or args.mark_missing:
        for cid in (args.mark_have or []):
            hh.setdefault("inventory", {})[cid] = "have"
        for cid in (args.mark_partial or []):
            hh.setdefault("inventory", {})[cid] = "partial"
        for cid in (args.mark_missing or []):
            hh.setdefault("inventory", {})[cid] = "missing"
    with open(path, "w") as f:
        json.dump(hh, f, indent=2)
    print(f"Profile at {path}:")
    print(f"  region: {hh.get('region')}")
    print(f"  people: {hh.get('people')}")
    print(f"  pets:   {hh.get('pets')}")
    inv = hh.get("inventory", {})
    have = sum(1 for v in inv.values() if v == "have")
    print(f"  inventory: {have} marked have, {len(inv)} tracked total")


def cmd_audit(args):
    hh = load_file(args.file, create=True)
    region = args.region or hh.get("region", "generic")
    print_audit(hh, region)


def cmd_water(args):
    hh = load_file(args.file, create=True)
    water_report(hh, args.region or hh.get("region", "generic"))


def cmd_food(args):
    hh = load_file(args.file, create=True)
    food_report(hh, args.region or hh.get("region", "generic"))


def cmd_power(args):
    if args.list:
        print("Known loads (key: watts, hours/day, note):")
        for k, v in LOADS.items():
            print(f"  {k:<18}{v['w']:>5} W × {v['h']:>2} h = {v['w'] * v['h']:>5} Wh  {v['note']}")
        return
    hh = load_file(args.file, create=True)
    loads = args.loads.split(",") if args.loads else ["phone", "radio", "led-lights", "router-modem"]
    power_report(hh, [l.strip() for l in loads], args.battery_wh)


def cmd_timeline(args):
    region = args.region or "generic"
    if region not in REGIONS:
        print("Unknown region — see `regions`.")
        sys.exit(1)
    print_timeline(region)


def cmd_example(args):
    hh = {
        "region": "hurricane-gulf", "people": 4,
        "pets": [{"kind": "dog", "weight_lb": 60}, {"kind": "cat", "weight_lb": 10}],
        "infants": 0, "medical_devices": ["CPAP"],
        "inventory": {"radio": "have", "first-aid": "have", "flashlights": "have"},
    }
    print("=== EXAMPLE: Gulf-coast family of 4 + 60 lb dog + cat, CPAP user ===\n")
    print_audit(hh, "hurricane-gulf")
    print("=" * 70 + "\n")
    water_report(hh, "hurricane-gulf")
    print("\n" + "=" * 70 + "\n")
    power_report(hh, ["fridge", "phone", "radio", "led-lights", "router-modem", "cpap"],
                 battery_wh=2000)
    print("\n" + "=" * 70 + "\n")
    print_timeline("hurricane-gulf")


def main():
    ap = argparse.ArgumentParser(
        prog="storm_ready.py",
        description="Household severe-weather preparedness audit and planner. Pure stdlib.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("regions", help="list region profiles")
    sub.add_parser("example", help="self-contained demo")

    p = sub.add_parser("audit", help="gap analysis for your household")
    p.add_argument("--file", default=DEFAULT_FILE)
    p.add_argument("--region", help="override profile region")
    p = sub.add_parser("water", help="water storage + purification math")
    p.add_argument("--file", default=DEFAULT_FILE)
    p.add_argument("--region", help="override profile region")
    p = sub.add_parser("food", help="food plan and calories")
    p.add_argument("--file", default=DEFAULT_FILE)
    p.add_argument("--region", help="override profile region")
    p = sub.add_parser("timeline", help="countdown checklist by phase")
    p.add_argument("--region", help="override profile region")
    p = sub.add_parser("profile", help="show/edit household profile")
    p.add_argument("--file", default=DEFAULT_FILE)
    p.add_argument("--region", help="one of: " + " ".join(REGIONS))
    p.add_argument("--people", type=int)
    p.add_argument("--pets", help='"dog:60,cat:10" weight in lb')
    p.add_argument("--mark-have", nargs="+", metavar="ID")
    p.add_argument("--mark-partial", nargs="+", metavar="ID")
    p.add_argument("--mark-missing", nargs="+", metavar="ID")

    p = sub.add_parser("power", help="outage power plan")
    p.add_argument("--file", default=DEFAULT_FILE)
    p.add_argument("--loads", help="comma list (see --list)")
    p.add_argument("--battery-wh", type=int)
    p.add_argument("--list", action="store_true", help="list known loads")

    args = ap.parse_args()
    handlers = {"regions": cmd_regions, "profile": cmd_profile, "audit": cmd_audit,
                "water": cmd_water, "food": cmd_food, "power": cmd_power,
                "timeline": cmd_timeline, "example": cmd_example}
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
