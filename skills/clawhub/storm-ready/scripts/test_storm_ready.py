#!/usr/bin/env python3
"""Self-tests for storm_ready.py — run: python3 scripts/test_storm_ready.py"""
import importlib.util
import json
import math
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("sr", os.path.join(HERE, "storm_ready.py"))
sr = importlib.util.module_from_spec(spec)
if spec.loader is None:
    raise SystemExit("cannot load module")
spec.loader.exec_module(sr)

PASS = 0


def check(name, cond):
    global PASS
    assert cond, f"FAILED: {name}"
    PASS += 1
    print(f"  ok  {name}")


print("regions:")
check("8 region profiles defined", len(sr.REGIONS) == 8)
check("gulf demands 14 days", sr.REGIONS["hurricane-gulf"]["water_days"] == 14)
check("generic is the 72h baseline", sr.REGIONS["generic"]["water_days"] == 3)
check("tornado profile mentions safe room",
      "safe room" in sr.REGIONS["tornado"]["note"].lower()
      or "shelter" in sr.REGIONS["tornado"]["note"].lower())

print("checklist construction:")
hh = {"people": 4, "pets": [{"kind": "dog", "weight_lb": 60},
                            {"kind": "cat", "weight_lb": 10}],
      "infants": 0, "medical_devices": ["CPAP"],
      "inventory": {"radio": "have"}}
items = sr.build_checklist(hh, "hurricane-gulf")
ids = {i["id"] for i in items}
check("base items present", {"water-store", "food-store", "radio", "co-alarm",
                             "docs", "cash"} <= ids)
check("pet items appear with pets", {"pet-food", "pet-water", "pet-carrier"} <= ids)
check("medical item appears with CPAP", "med-power" in ids)
check("gulf-specific items included",
      {"plywood-film", "fill-tubs", "evac-decide"} <= ids)
gulf_rel = {i["id"] for i in sr.relevant(items, "hurricane-gulf")}
check("tornado-only items excluded for gulf", "helmets" not in gulf_rel
      and "shelter-room" not in gulf_rel)
tor = sr.build_checklist(hh, "tornado")
check("tornado checklist contains helmets", "helmets" in {i["id"] for i in tor})
check("tornado filtered drops gulf plywood",
      "plywood-film" not in {i["id"] for i in sr.relevant(tor, "tornado")})
ice = sr.build_checklist(hh, "ice-storm")
ice_ids = {i["id"] for i in ice}
check("ice-storm gets heat plan", "heat-room" in ice_ids and "warm-layers" in ice_ids)
wf = sr.build_checklist(hh, "wildfire-wui")
wf_ids = {i["id"] for i in wf}
check("wildfire gets go-bags + N95", "go-bag" in wf_ids and "n95" in wf_ids)
check("all phases valid", all(i["phase"] in sr.PHASES for i in items))
check("all priorities valid", all(i["pri"] in ("P0", "P1", "P2") for i in items))
check("water qty scales with region (14d gulf)",
      any(i["id"] == "water-store" and "56 gal" in str(i["qty"]) for i in items))
base = sr.build_checklist({"people": 1}, "generic")
base_rel = {i["id"] for i in sr.relevant(base, "generic")}
check("generic has no hurricane plywood", "plywood-film" not in base_rel)

print("water math:")
gal = sr.water_report({"people": 2}, "generic")  # 2p × 3d + hygiene
check("2 people 3 days ≥ 9 gal", gal >= 9)
gal14 = sr.water_report({"people": 4, "pets": [{"kind": "dog", "weight_lb": 60}]},
                        "hurricane-gulf")
check("4 people 14 days ≥ 56 gal", gal14 >= 56)
check("pets add water", gal14 > 56)

print("food math:")
kcal = sr.food_report({"people": 3}, "generic")
check("3 people 3 days = 18000 kcal", kcal == 3 * 3 * 2000)

print("power math:")
# direct function call: loads list, battery None
total = sr.power_report({}, ["phone", "radio", "led-lights"], None)
check("phone+radio+lights = 6*2+3*4+10*5 = 74 Wh", total == 74)
full = sr.power_report({}, ["fridge", "cpap"], None)
check("fridge+cpap = 150*8+40*8 = 1520 Wh", full == 1520)
check("load table has medical oxygen concentrator", "oxygen-conc" in sr.LOADS)

print("relevance filter:")
rel = sr.relevant(items, "hurricane-gulf")
rel_ids = {i["id"] for i in rel}
check("filter keeps gulf core items",
      {"water-store", "plywood-film", "fill-tubs"} <= rel_ids)
check("filter drops tornado/ice/wildfire-only items",
      not ({"helmets", "heat-room", "n95"} & rel_ids))
check("filter is a strict subset of built",
      len(rel_ids) < len(ids))

print("cli round-trip:")
with tempfile.TemporaryDirectory() as td:
    pf = os.path.join(td, "profile.json")
    r = subprocess.run([sys.executable, os.path.join(HERE, "storm_ready.py"),
                        "profile", "--file", pf, "--region", "ice-storm",
                        "--people", "3", "--pets", "dog:45"],
                       capture_output=True, text=True)
    check("profile created", r.returncode == 0 and "ice-storm" in r.stdout)
    with open(pf) as f:
        saved = json.load(f)
    check("pets parsed", saved["pets"][0]["kind"] == "dog"
          and saved["pets"][0]["weight_lb"] == 45)
    r = subprocess.run([sys.executable, os.path.join(HERE, "storm_ready.py"),
                        "profile", "--file", pf, "--mark-have", "radio",
                        "first-aid"], capture_output=True, text=True)
    check("mark-have works", r.returncode == 0 and "2 marked have" in r.stdout)
    r = subprocess.run([sys.executable, os.path.join(HERE, "storm_ready.py"),
                        "audit", "--file", pf], capture_output=True, text=True)
    check("audit shows ✓ for marked items", "✓" in r.stdout)
    check("audit flags P0 gaps", "P0 prep gaps" in r.stdout)
    r = subprocess.run([sys.executable, os.path.join(HERE, "storm_ready.py"),
                        "timeline", "--region", "wildfire-wui"],
                       capture_output=True, text=True)
    check("timeline renders phases", "T-72 h" in r.stdout and "after the storm" in r.stdout)
    r = subprocess.run([sys.executable, os.path.join(HERE, "storm_ready.py"),
                        "power", "--list"], capture_output=True, text=True)
    check("power --list shows loads", "oxygen-conc" in r.stdout)
    r = subprocess.run([sys.executable, os.path.join(HERE, "storm_ready.py"),
                        "example"], capture_output=True, text=True)
    check("example runs end-to-end", r.returncode == 0
          and "Preparedness audit" in r.stdout)

print(f"\nALL TESTS PASSED ({PASS} assertions)")
