#!/usr/bin/env python3
"""Tests for seed_calendar.py — plain asserts. Run: python3 test_seed_calendar.py"""
import datetime as dt
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(HERE, "seed_calendar.py")
sys.path.insert(0, HERE)
import seed_calendar as sc  # noqa: E402


def run_cli(args):
    return subprocess.run([sys.executable, ENGINE] + args,
                          capture_output=True, text=True)


def check(label, cond):
    assert cond, label
    print("[PASS] %s" % label)


LAST = dt.date(2026, 5, 15)
FIRST = dt.date(2026, 10, 5)

# ---- library sanity ----
check("35+ crops in library", len(sc.CROPS) >= 35)
check("every crop has required keys", all(
    {"name", "start", "dt", "cls", "pp", "sp", "notes"} <= set(c) for c in sc.CROPS.values()))
check("indoor crops have wks", all(c.get("wks") for c in sc.CROPS.values()
                                   if c["start"] == "indoor"))

# ---- tomato plan: 7 wks indoor, +14d transplant ----
ev = sc.build_events("tomato", LAST, FIRST, people=1)
codes = [e[1] for e in ev]
check("tomato has SOW-INDOORS", "SOW-INDOORS" in codes)
check("tomato has TRANSPLANT", "TRANSPLANT" in codes)
sow = [e[0] for e in ev if e[1] == "SOW-INDOORS"][0]
tp = [e[0] for e in ev if e[1] == "TRANSPLANT"][0]
check("tomato sow = last_frost - 49d", sow == LAST - dt.timedelta(days=49))
check("tomato transplant = last_frost + 14d", tp == LAST + dt.timedelta(days=14))
check("tomato harvest ~ +65d after transplant",
      any(e[1] == "HARVEST ~" and e[0] == tp + dt.timedelta(days=65) for e in ev))
check("tomato events sorted", ev == sorted(ev))

# ---- pea: direct, hardy, window starts before frost ----
ev = sc.build_events("pea", LAST, FIRST, people=1)
sd = [e for e in ev if e[1].startswith("SOW-DIRECT")]
check("pea has direct sow", bool(sd))
check("pea sow window starts 42d BEFORE last frost", sd[0][0] == LAST - dt.timedelta(days=42))

# ---- garlic: fall plant ----
ev = sc.build_events("garlic", LAST, FIRST)
check("garlic FALL-PLANT 35d before first frost",
      ev[0][1] == "FALL-PLANT" and ev[0][0] == FIRST - dt.timedelta(days=35))

# ---- tray math: 4 people x 3 tomato = 12 plants -> 15 cells -> 1x72 ----
ppl = sc.plants_needed(["tomato"], 4)[0]
check("tomato 4ppl plants=12", ppl["plants"] == 12)
check("tomato 4ppl cells=15 (20% buffer)", ppl["flat_cells"] == 15)

# ---- succession: lettuce ----
ev = sc.build_events("lettuce", LAST, FIRST, people=1)
sows = [e for e in ev if e[1].startswith("SOW #")]
check("lettuce gets multiple succession sows", len(sows) >= 3)
interval = (sows[1][0] - sows[0][0]).days
check("lettuce succession interval 14d", interval == 14)

# ---- succession stop rule: all harvests fit ----
first = dt.date(2026, 10, 5)
for e in sows:
    harv = e[0] + dt.timedelta(days=sc.CROPS["lettuce"]["dt"])
    if not e[1].startswith("SOW-FALL"):
        assert harv <= first + dt.timedelta(days=sc.CROPS["lettuce"]["fb"]), e

# ---- moon phase sanity ----
n, w = sc.moon_phase(dt.date(2026, 1, 18))  # known new moon 2026-01-18
check("moon: 2026-01-18 near new moon", n in ("New Moon", "Waxing Crescent", "Waning Crescent"))

# ---- CLI: garden end-to-end + JSON ----
r = run_cli(["garden", "--crops", "tomato,lettuce,carrot,pea",
             "--last-frost", "2026-05-15", "--first-frost", "2026-10-05",
             "--people", "4", "--json"])
check("CLI garden exits 0", r.returncode == 0)
out = json.loads(r.stdout)
check("JSON has events", len(out["events"]) > 10)
check("JSON plants table has 4 rows", len(out["plants"]) == 4)
check("JSON frost-free days 143", out["frost_free_days"] == 143)
r2 = run_cli(["crops"])
check("CLI crops lists 35+ rows", r2.returncode == 0 and len(r2.stdout.splitlines()) > 35)
r3 = run_cli(["frost", "--zone", "6b"])
check("CLI frost zone 6b works", r3.returncode == 0 and "Zone 6B" in r3.stdout
      and "2026-04-18" in r3.stdout and "187" in r3.stdout)
r4 = run_cli(["succession", "--crop", "radish", "--from", "2026-04-01",
              "--until", "2026-06-01", "--first-frost", "2026-10-05"])
check("CLI succession radish", r4.returncode == 0 and "sow #" in r4.stdout)
r5 = run_cli(["plan", "--crop", "nope", "--last-frost", "2026-05-15",
              "--first-frost", "2026-10-05"])
check("CLI unknown crop exits 1", r5.returncode == 1)

print("\nALL TESTS PASSED")
