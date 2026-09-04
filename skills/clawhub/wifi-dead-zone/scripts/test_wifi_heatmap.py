#!/usr/bin/env python3
"""Self-tests for wifi_heatmap.py — run: python3 scripts/test_wifi_heatmap.py"""
import importlib.util
import json
import math
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("wifi", os.path.join(HERE, "wifi_heatmap.py"))
wifi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wifi)

PASS = 0


def check(name, cond):
    global PASS
    assert cond, f"FAILED: {name}"
    PASS += 1
    print(f"  ok  {name}")


print("physics:")
# FSPL at 1 m: 5 GHz ~ 46.5 dB, 2.4 GHz ~ 40 dB
f5 = wifi.fspl_1m(5.0)
f24 = wifi.fspl_1m(2.4)
check("FSPL(1m, 5GHz) ≈ 46-48 dB", 45 < f5 < 48)
check("FSPL(1m, 2.4GHz) ≈ 39-41 dB", 39 < f24 < 41)
check("2.4 GHz loses less than 5 GHz at 10 m",
      wifi.path_loss(10, "2.4", []) < wifi.path_loss(10, "5", []))
# doubling distance at exponent 2.6 ≈ 7.8 dB
d1 = wifi.path_loss(5, "5", [])
d2 = wifi.path_loss(10, "5", [])
check("5→10 m adds ~7-9 dB (log-distance)", 7 < (d2 - d1) < 9)
# one drywall adds 3 dB
check("drywall adds 3 dB", wifi.path_loss(5, "5", [{"material": "drywall", "segment": []}])
      - wifi.path_loss(5, "5", []) == 3.0)
# materials override respected
check("material override works",
      wifi.path_loss(5, "5", [{"material": "drywall", "segment": []}], {"drywall": 6.0})
      - wifi.path_loss(5, "5", []) == 6.0)

print("link grades:")
check("grade thresholds", wifi.link_quality(-50)[0] == "excellent"
      and wifi.link_quality(-67)[0] == "good"
      and wifi.link_quality(-72)[0] == "workable"
      and wifi.link_quality(-80)[0] == "weak"
      and wifi.link_quality(-90)[0] == "dead")
check("bandwidth falls with RSSI",
      wifi.bandwidth_estimate(-50, "5", 80) > wifi.bandwidth_estimate(-75, "5", 80))

print("geometry:")
check("segment crossing detected",
      wifi.segments_intersect((0, 0), (10, 10), (0, 10), (10, 0)))
check("parallel segments don't cross",
      not wifi.segments_intersect((0, 0), (10, 0), (0, 5), (10, 5)))
wall = [{"material": "brick", "segment": [[5, -1], [5, 11]]}]
hit = wifi.walls_on_path((0, 0), (10, 0), wall)
miss = wifi.walls_on_path((0, 0), (4, 0), wall)
check("wall on path counted once", len(hit) == 1 and hit[0]["material"] == "brick")
check("path not reaching wall unaffected", len(miss) == 0)

print("channels:")
best, alts, why = wifi.channel_plan("2.4", [6, 6, 6, 1])
check("2.4 GHz avoids crowded 6", best == 11 or best == 1)
best, alts, why = wifi.channel_plan("2.4", [1, 6, 11])
check("2.4 GHz picks a legal channel", best in (1, 6, 11))
best, alts, why = wifi.channel_plan("5", [36, 40, 44, 48])
check("5 GHz avoids occupied 36-block", best != 36)
best, alts, why = wifi.channel_plan("6", [])
check("6 GHz returns PSC 37", best == 37)

print("analysis pipeline:")
home = wifi.sample_home()
rows = wifi.analyze(home)
check("all rooms analyzed", len(rows) == len(home["rooms"]))
check("sorted worst-first", rows[0]["rssi"] == min(r["rssi"] for r in rows))
check("RSSI values plausible (-95..-25)", all(-95 < r["rssi"] < -25 for r in rows))
check(" PHY estimates present", all(r["phy_mbps"] > 0 for r in rows))
tips = wifi.advice(home, rows)
check("advice mentions router move for corner router",
      any("MOVE ROUTER" in t for t in tips))
rec_xy, _ = wifi.best_placement(home)
cur_worst = wifi.worst_room_rssi(home, *wifi.router_xy(home))
rec_worst = wifi.worst_room_rssi(home, *rec_xy)
check("recommended spot ≥ current for worst room", rec_worst >= cur_worst)

print("survey + compare round-trip:")
with tempfile.TemporaryDirectory() as td:
    hf = os.path.join(td, "home.json")
    with open(hf, "w") as f:
        json.dump(wifi.sample_home(), f)
    r = subprocess.run([sys.executable, os.path.join(HERE, "wifi_heatmap.py"),
                        "survey", "--home", hf, "--room", "kitchen",
                        "--rssi", "-58", "--band", "5", "--where", "counter"],
                       capture_output=True, text=True)
    check("survey records measurement", "Recorded" in r.stdout and r.returncode == 0)
    with open(hf) as f:
        saved = json.load(f)
    check("measurement persisted", saved["measurements"]["kitchen"][-1]["rssi"] == -58)
    r = subprocess.run([sys.executable, os.path.join(HERE, "wifi_heatmap.py"),
                        "compare", "--home", hf], capture_output=True, text=True)
    check("compare renders table", "Model vs measured" in r.stdout and "delta" in r.stdout.lower()
          or "Delta" in r.stdout)
    r = subprocess.run([sys.executable, os.path.join(HERE, "wifi_heatmap.py"),
                        "plan", "--home", hf], capture_output=True, text=True)
    check("plan renders heatmap", "Heatmap" in r.stdout and "@" in r.stdout)

print("cli:")
r = subprocess.run([sys.executable, os.path.join(HERE, "wifi_heatmap.py"), "example"],
                   capture_output=True, text=True)
check("example runs end-to-end", r.returncode == 0 and "Per-room signal" in r.stdout)
check("example shows before/after", "recommended spot" in r.stdout)

print(f"\nALL TESTS PASSED ({PASS} assertions)")
