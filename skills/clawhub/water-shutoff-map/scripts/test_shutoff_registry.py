#!/usr/bin/env python3
"""Tests for shutoff_registry.py — plain asserts. Run: python3 test_shutoff_registry.py"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(HERE, "shutoff_registry.py")


def run_cli(args, env_file):
    return subprocess.run([sys.executable, ENGINE] + args + ["--file", env_file],
                          capture_output=True, text=True)


def check(label, cond):
    assert cond, label
    print("[PASS] %s" % label)


tmp = tempfile.mkdtemp()
REG = os.path.join(tmp, "reg.json")

# empty registry
r = run_cli(["list"], REG)
check("empty registry lists ok", r.returncode == 0 and "empty" in r.stdout)
r = run_cli(["validate"], REG)
check("empty registry fails validation", r.returncode == 1 and "missing core entry: main" in r.stdout)

# add main (complete) + toilet (no tool) + heater
r = run_cli(["add", "--id", "main", "--label", "Main shutoff",
             "--location", "Basement east wall behind furnace", "--type", "gate",
             "--direction", "clockwise", "--tool", "crescent-12in",
             "--tested", "2026-08-30", "--notes", "stiff first 2 turns"], REG)
check("add main exits 0", r.returncode == 0)
r = run_cli(["add", "--id", "toilet-1", "--location", "Left wall under hall toilet",
             "--type", "angle-stop", "--direction", "clockwise",
             "--tested", "2026-08-30"], REG)
check("add toilet-1 exits 0", r.returncode == 0)
r = run_cli(["add", "--id", "water-heater", "--location", "Garage cold inlet",
             "--type", "ball", "--direction", "perpendicular",
             "--tool", "none", "--tested", "2026-08-30"], REG)
check("add water-heater exits 0", r.returncode == 0)
r = run_cli(["add", "--id", "main", "--location", "dup"], REG)
check("duplicate id rejected", r.returncode != 0)

# validate: complete now
r = run_cli(["validate"], REG)
check("complete registry validates (exit 0)", r.returncode == 0)

# staleness: fake old tested date
data = json.load(open(REG))
for e in data["entries"]:
    e["tested"] = "2024-01-01"
json.dump(data, open(REG, "w"))
r = run_cli(["validate"], REG)
check("stale tested dates warned", "days ago" in r.stdout)

# seized valve flagged as FIX
data = json.load(open(REG))
data["entries"][0]["notes"] = "seized open — replace"
json.dump(data, open(REG, "w"))
r = run_cli(["validate"], REG)
check("seized valve is a [FIX] problem", "SEIZED" in r.stdout and r.returncode == 1)

# update --mark-tested
r = run_cli(["update", "--id", "main", "--mark-tested"], REG)
check("mark-tested works", r.returncode == 0)
data = json.load(open(REG))
import datetime as dt  # noqa: E402
check("main tested = today", [e for e in data["entries"] if e["id"] == "main"][0]["tested"]
      == dt.date.today().isoformat())

# card output
r = run_cli(["card"], REG)
check("card prints first response", "FIRST RESPONSE" in r.stdout and "ISOLATE THE FIXTURE" in r.stdout)
check("card lists valves", "main" in r.stdout and "toilet-1" in r.stdout)
check("card mentions tools location", "TOOLS LIVE HERE" in r.stdout)

# meta
r = run_cli(["meta", "--tools-location", "kitchen junk drawer, left bin",
             "--plumber", "Roto-Rooter 555-0100", "--insurance", "State Farm 555-9999"], REG)
check("meta saves", r.returncode == 0)
r = run_cli(["card"], REG)
check("card shows plumber/insurance/tools", "Roto-Rooter" in r.stdout
      and "State Farm" in r.stdout and "junk drawer" in r.stdout)

# hunt guides (note: --home comes BEFORE --file on this subparser)
for home in ("basement", "slab", "crawlspace", "condo"):
    r = run_cli(["hunt", "--home", home], REG)
    check(f"hunt {home} prints guide", r.returncode == 0 and "WHERE THINGS HIDE" in r.stdout)

# drill
r = run_cli(["drill"], REG)
check("drill references the main", r.returncode == 0 and "Basement east wall" in r.stdout)

# export json
r = run_cli(["export", "--json"], REG)
data = json.loads(r.stdout)
check("export json parses, 3 entries", len(data["entries"]) == 3)

# remove
r = run_cli(["remove", "--id", "toilet-1"], REG)
data = json.load(open(REG))
check("remove works", r.returncode == 0 and
      "toilet-1" not in [e["id"] for e in data["entries"]])

print("\nALL TESTS PASSED")
