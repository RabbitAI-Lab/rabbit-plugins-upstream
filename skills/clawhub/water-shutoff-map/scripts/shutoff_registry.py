#!/usr/bin/env python3
"""
shutoff_registry.py — record, validate, and drill your home's water shutoffs.

Registry: JSON file (default ~/.shutoff-registry.json). Pure stdlib.
"""
import argparse
import datetime as dt
import json
import os
import sys

DEFAULT_FILE = os.path.join(os.path.expanduser("~"), ".shutoff-registry.json")

VALVE_TYPES = ["gate", "ball", "angle-stop", "straight-stop", "meter-key",
               "lever-box", "saddle", "other"]
TOOLS_HINT = "none / screwdriver / crescent-12in / meter-key / channel-locks"

# What a complete home registry should contain (checklist for validate).
EXPECTED = [
    ("main", "house main shutoff"),
    ("water-heater", "water heater cold-inlet stop"),
]

HUNT_GUIDES = {
    "basement": [
        "Pipe comes up through the basement floor, usually near the FRONT wall,",
        "often next to the water meter and a bell-shaped pressure regulator.",
        "Valve within 3-5 ft of entry: gate wheel or ball lever. CW / quarter-turn.",
        "Also check: hose-bib shutoffs along the ceiling/joists, water heater cold inlet,",
        "and the irrigation backflow preventor outside.",
    ],
    "slab": [
        "No basement. Look for a pipe emerging from the slab near the water heater",
        "or in the garage, sometimes inside a small access box/panel.",
        "Check the exterior wall on the street-facing side for a penetration + panel.",
        "Attic manifold if plumbing runs overhead (garage ceiling, attic floor).",
        "Many slab homes' only interior main is at the water heater — buy a meter key.",
    ],
    "crawlspace": [
        "Pipe enters through the crawlspace rim joist or wall; shutoff often right",
        "inside the crawlspace entrance. Bring a headlamp; log the hatch location.",
        "Sometimes there is NO interior main — meter key at the curb is the answer.",
        "While under there: log hose-bib valves and the water heater if it lives there.",
    ],
    "condo": [
        "Unit shutoff is usually behind an access panel: water-heater closet,",
        "under kitchen/bath sink, or a utility closet near the entry door.",
        "Riser valves belong to the building — log the after-hours maintenance number",
        "on your card instead of a valve you can't operate.",
    ],
    "any": [
        "Walk the perimeter: find where the service pipe enters; that's your main.",
        "Under every sink: two straight stops (hot left, cold right).",
        "Behind every toilet: one angle stop on the left wall side.",
        "Behind the washer: red/blue wheels or lever box; check flex-line condition.",
        "Water heater: cold-inlet stop on top. Irrigation: valve box / backflow tower.",
    ],
}

STEPS = [
    "1. ISOLATE THE FIXTURE — angle stop / appliance valve, clockwise (or lever ⟂ pipe).",
    "2. IF YOU CAN'T — house MAIN clockwise. Stiff? wrench. Full-close or leave it.",
    "3. DAMAGE CONTROL — breakers off near water, towels/shop-vac, move valuables,",
    "   then plumber + insurer (mitigation duty starts immediately).",
]


def today():
    return dt.date.today().isoformat()


def load(path):
    if not os.path.exists(path):
        return {"home_type": None, "tools_location": None, "plumber": None,
                "insurance": None, "entries": []}
    with open(path) as f:
        return json.load(f)


def save(reg, path):
    with open(path, "w") as f:
        json.dump(reg, f, indent=2)
    print(f"saved -> {path}")


def find_entry(reg, eid):
    for e in reg["entries"]:
        if e["id"] == eid:
            return e
    return None


# --------------------------- subcommands -----------------------------------
def cmd_add(a):
    reg = load(a.file)
    if find_entry(reg, a.id):
        sys.exit(f"error: id '{a.id}' exists — use 'update'")
    fields = dict(
        id=a.id, label=a.label or a.id, location=a.location, type=a.type,
        direction=a.direction, tool=a.tool, notes=a.notes,
        photo=a.photo, tested=a.tested,
    )
    if a.interactive:
        print(f"-- interactive entry '{a.id}' (blank = keep flag/default) --")
        for k, cur in [("label", fields["label"]), ("location", fields["location"]),
                       ("type", fields["type"]), ("direction", fields["direction"]),
                       ("tool", fields["tool"]), ("tested", fields["tested"]),
                       ("notes", fields["notes"]), ("photo", fields["photo"])]:
            try:
                v = input(f"  {k} [{cur or '-'}]: ").strip()
            except EOFError:
                v = ""
            if v:
                fields[k] = v
        if not fields["location"]:
            print("  (no location — entry saved as UNLOCATED; run update later)")
    missing = [k for k in ("location", "type", "direction") if not fields[k]]
    if missing and not a.interactive:
        sys.exit(f"error: missing required fields: {missing}")
    reg["entries"].append(fields)
    reg["entries"].sort(key=lambda e: e["id"])
    save(reg, a.file)
    if missing:
        print(f"note: incomplete entry ({missing}) — 'validate' will flag it.")


def cmd_update(a):
    reg = load(a.file)
    e = find_entry(reg, a.id)
    if not e:
        sys.exit(f"error: no entry '{a.id}'")
    changed = False
    for k in ("label", "location", "type", "direction", "tool", "notes",
              "photo", "tested"):
        v = getattr(a, k, None)
        if v:
            e[k] = v
            changed = True
    if a.mark_tested:
        e["tested"] = today()
        changed = True
    if not changed:
        sys.exit("nothing to update — pass field flags or --mark-tested")
    save(reg, a.file)


def cmd_remove(a):
    reg = load(a.file)
    e = find_entry(reg, a.id)
    if not e:
        sys.exit(f"error: no entry '{a.id}'")
    reg["entries"].remove(e)
    save(reg, a.file)


def cmd_list(a):
    reg = load(a.file)
    if not reg["entries"]:
        print("(empty registry — see 'hunt' then 'add')")
        return
    print(f"{'ID':<14} {'TYPE':<13} {'DIR':<14} {'TESTED':<11} LOCATION")
    print("-" * 88)
    for e in reg["entries"]:
        print(f"{e['id']:<14} {e.get('type') or '?':<13} {e.get('direction') or '?':<14} "
              f"{e.get('tested') or 'never':<11} {(e.get('location') or 'UNLOCATED')[:38]}")
        if e.get("tool"):
            print(f"{'':<14} tool: {e['tool']}")
        if e.get("notes"):
            print(f"{'':<14} notes: {e['notes'][:60]}")


def staleness(tested):
    if not tested:
        return None
    try:
        d = dt.date.fromisoformat(tested)
        return (dt.date.today() - d).days
    except ValueError:
        return -1


def cmd_validate(a):
    reg = load(a.file)
    problems, warnings = [], []
    ids = [e["id"] for e in reg["entries"]]
    if len(ids) != len(set(ids)):
        problems.append("duplicate ids present")
    for eid, what in EXPECTED:
        if eid not in ids:
            problems.append(f"missing core entry: {eid} ({what})")
    toilets = [e for e in reg["entries"] if "toilet" in e["id"]]
    if not toilets:
        warnings.append("no toilet stops logged (every toilet has one — go look)")
    for e in reg["entries"]:
        if not e.get("location"):
            problems.append(f"{e['id']}: no location")
        if not e.get("direction"):
            problems.append(f"{e['id']}: no close-direction")
        age = staleness(e.get("tested"))
        if age is None:
            warnings.append(f"{e['id']}: never tested (2-min procedure, references §5)")
        elif age < 0:
            warnings.append(f"{e['id']}: unparseable tested date")
        elif age > 365:
            warnings.append(f"{e['id']}: last tested {age} days ago — exercise it")
        if e.get("notes") and "seiz" in e["notes"].lower():
            problems.append(f"{e['id']}: marked SEIZED — schedule replacement")
        if e.get("type") == "gate" and e.get("tool") in (None, "none"):
            warnings.append(f"{e['id']}: gate valve with no tool logged (they get stiff)")
    if not reg.get("tools_location"):
        warnings.append("no tools_location set (wrench + meter key live WHERE?)")
    print(f"registry: {len(reg['entries'])} entries, {a.file}\n")
    for p in problems:
        print(f"  [FIX]   {p}")
    for w in warnings:
        print(f"  [warn]  {w}")
    if not problems and not warnings:
        print("  ✓ complete and current — print the card")
    sys.exit(1 if problems else 0)


def cmd_card(a):
    reg = load(a.file)
    w = 66
    line = "=" * w
    print(line)
    print("WATER EMERGENCY — SHUTOFF CARD".center(w))
    print("(post on fridge / inside pantry door)".center(w))
    print(line)
    print("\nFIRST RESPONSE:")
    for s in STEPS:
        print("  " + s)
    print("\nYOUR VALVES:")
    print(f"  {'ID':<13}{'WHERE':<26}{'CLOSE HOW':<16}TOOL")
    for e in reg["entries"]:
        loc = (e.get("location") or "?")[:25]
        how = f"{e.get('type','?')} {e.get('direction','')}"[:15]
        tool = (e.get("tool") or "none")[:14]
        print(f"  {e['id']:<13}{loc:<26}{how:<16}{tool}")
    print("\nTOOLS LIVE HERE: " + (reg.get("tools_location") or "(unset — fix this)"))
    if reg.get("plumber"):
        print("PLUMBER:        " + str(reg["plumber"]))
    if reg.get("insurance"):
        print("INSURANCE:      " + str(reg["insurance"]))
    print("QUARTERLY DRILL: run 'drill' — 60 seconds, first Sunday of the quarter")
    print(line)
    print("Photos beat text: tape a photo of the MAIN next to this card.")


def cmd_drill(a):
    reg = load(a.file)
    print("QUARTERLY SHUTOFF DRILL — 60 seconds\n")
    print("1) Say out loud where the MAIN is, and which tool closes it.")
    e = find_entry(reg, "main")
    print(f"   registry says: {e['location'] if e else '(NO MAIN ENTRY — fix now)'}")
    print("2) Walk to it. Touch the valve. Trace the pipe in/out with your eyes.")
    print("3) Name the closest fixture stop (toilet/sink) and walk to that one too.")
    print("4) Close+reopen ONE low-stakes angle stop (toilet): 2 full turns CW,")
    print("   flush check, back open. Log it:")
    print("   python3 shutoff_registry.py update <id> --mark-tested")
    print("5) Note anything stiff, dripping, or stripped -> update --notes.")
    print("\nDone. Your future self during a flood says thanks.")


def cmd_hunt(a):
    print(f"WHERE THINGS HIDE — {a.home.upper()} home\n")
    for ln in HUNT_GUIDES.get(a.home, HUNT_GUIDES["any"]):
        print("  " + ln)
    print("\nFound something? -> 'add' it. Full detail: references/locating-shutoffs.md")


def cmd_export(a):
    reg = load(a.file)
    if a.json:
        print(json.dumps(reg, indent=2))
    else:
        print(json.dumps(reg))


def cmd_meta(a):
    reg = load(a.file)
    if a.tools_location:
        reg["tools_location"] = a.tools_location
    if a.plumber:
        reg["plumber"] = a.plumber
    if a.insurance:
        reg["insurance"] = a.insurance
    if a.home_type:
        reg["home_type"] = a.home_type
    save(reg, a.file)
    print(f"meta: tools@{reg.get('tools_location')}, home={reg.get('home_type')}")


# --------------------------- cli -------------------------------------------
def add_shared(sp):
    sp.add_argument("--file", default=DEFAULT_FILE, help="registry JSON path")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("add", help="record a valve")
    add_shared(sp)
    sp.add_argument("--id", required=True, help="short handle, e.g. main, toilet-1")
    sp.add_argument("--label")
    sp.add_argument("--location")
    sp.add_argument("--type", choices=VALVE_TYPES)
    sp.add_argument("--direction", help="clockwise | perpendicular")
    sp.add_argument("--tool", help=TOOLS_HINT)
    sp.add_argument("--tested", help="YYYY-MM-DD you last exercised it")
    sp.add_argument("--notes")
    sp.add_argument("--photo", help="filename of valve photo")
    sp.add_argument("-i", "--interactive", action="store_true")
    sp.set_defaults(fn=cmd_add)

    sp = sub.add_parser("update", help="edit an entry")
    add_shared(sp)
    sp.add_argument("--id", required=True)
    for fld in ("label", "location", "direction", "tool", "notes", "photo", "tested"):
        sp.add_argument(f"--{fld}")
    sp.add_argument("--type", choices=VALVE_TYPES)
    sp.add_argument("--mark-tested", action="store_true")
    sp.set_defaults(fn=cmd_update)

    sp = sub.add_parser("remove", help="delete an entry")
    add_shared(sp)
    sp.add_argument("--id", required=True)
    sp.set_defaults(fn=cmd_remove)

    sp = sub.add_parser("list", help="show the registry")
    add_shared(sp)
    sp.set_defaults(fn=cmd_list)

    sp = sub.add_parser("validate", help="completeness + staleness check")
    add_shared(sp)
    sp.set_defaults(fn=cmd_validate)

    sp = sub.add_parser("card", help="print the fridge card")
    add_shared(sp)
    sp.set_defaults(fn=cmd_card)

    sp = sub.add_parser("drill", help="60-second quarterly rehearsal")
    add_shared(sp)
    sp.set_defaults(fn=cmd_drill)

    sp = sub.add_parser("hunt", help="where shutoffs hide by home type")
    add_shared(sp)
    sp.add_argument("--home", default="any",
                    choices=["basement", "slab", "crawlspace", "condo", "any"])
    sp.set_defaults(fn=cmd_hunt)

    sp = sub.add_parser("export", help="dump registry JSON")
    add_shared(sp)
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(fn=cmd_export)

    sp = sub.add_parser("meta", help="set tools location / plumber / insurance")
    add_shared(sp)
    sp.add_argument("--tools-location")
    sp.add_argument("--plumber")
    sp.add_argument("--insurance")
    sp.add_argument("--home-type")
    sp.set_defaults(fn=cmd_meta)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
