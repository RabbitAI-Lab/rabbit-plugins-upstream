#!/usr/bin/env python3
"""Tests for commute_opt.py — plain asserts. Run: python3 test_commute_opt.py"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(HERE, "commute_opt.py")
sys.path.insert(0, HERE)
import commute_opt as co  # noqa: E402


def run_cli(args):
    return subprocess.run([sys.executable, ENGINE] + args,
                          capture_output=True, text=True)


def check(label, cond):
    assert cond, label
    print("[PASS] %s" % label)


# ---- evaluate(): math ----
r = co.evaluate(offpeak=25, distance=15, mode="car", days=5, rate=35)
check("car trips/year = 240", r["trips_per_year"] == 240)
avg_mult = sum(co.PARAMS["profile"]) / 5 * co.PARAMS["mode_rush"]["car"]
check("car avg one-way uses weekday profile", abs(r["avg_one_way_min"] - 25 * avg_mult) < 0.1)
expected_direct = 15 * 2 * 240 * (co.PARAMS["fuel_maint_per_mile"] + co.PARAMS["ownership_per_mile"])
check("car direct cost = miles*rate*trips", abs(r["direct_cost_per_year"] - expected_direct) < 1)
check("time + direct = total", abs(r["total_per_year"]
      - (r["time_cost_per_year"] + r["direct_cost_per_year"])) < 1.5)

r = co.evaluate(30, 8, "transit", 5, 30)
check("transit uses fares not miles", r["direct_cost_per_year"] == 240 * co.PARAMS["transit_fare"])
r = co.evaluate(30, 8, "wfh", 5, 30)
check("wfh is zero", r["hours_per_year"] == 0 and r["total_per_year"] == 0)

# marginal vs loaded
r = co.evaluate(25, 15, "car", 5, 35)
check("car marginal < loaded", r["car_marginal_cost_per_year"] < r["direct_cost_per_year"])

# ---- hybrid optimizer ----
import io, contextlib  # noqa: E402
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    co.cmd_hybrid(type("A", (), {"offpeak": 30.0, "mode": "car", "office_days": 3,
                                 "profile": None})())
out = buf.getvalue()
check("hybrid picks Mon/Thu/Fri for 3 days (smallest multipliers)",
      "best   Mon/Thu/Fri" in out and "← best" in out)
check("hybrid shows MWF penalty", "MWF" in out and "vs best" in out)
check("hybrid lists all 10 subsets", out.count("min/wk") >= 10)

# ---- CLI ----
r = run_cli(["cost", "--offpeak", "25", "--distance", "15", "--mode", "car",
             "--rate", "35", "--json"])
check("CLI cost json ok", r.returncode == 0)
d = json.loads(r.stdout)
check("json fields present", {"hours_per_year", "total_per_year", "weekday_one_way_min",
                              "waking_days_per_decade"} <= set(d))
check("wed is the worst weekday", max(d["weekday_one_way_min"].values())
      == d["weekday_one_way_min"]["Wed"])

r = run_cli(["compare", "--offpeak", "25", "--distance", "8", "--rate", "30"])
check("CLI compare lists 5 modes", r.returncode == 0 and all(
    m in r.stdout for m in ["car", "transit", "bike", "walk", "wfh"]))

r = run_cli(["decide",
             "--option", "Apt A,offpeak=25,distance=12,mode=car,extra_rent=0",
             "--option", "House B,offpeak=42,distance=26,mode=car,extra_rent=-450",
             "--rate", "40", "--years", "5"])
check("CLI decide exits 0", r.returncode == 0)
check("decide shows breakeven rent", "MORE rent savings" in r.stdout or "WINS by" in r.stdout)
check("decide shows waking days", "waking days" in r.stdout)

r = run_cli(["profile", "--offpeak", "25", "--mode", "car"])
check("CLI profile shows Friday lightest", r.returncode == 0
      and r.stdout.index("Fri") and "1.22" not in r.stdout)

r = run_cli(["cost", "--offpeak", "25", "--distance", "15", "--mode", "jetpack"])
check("CLI rejects bad mode", r.returncode != 0)

print("\nALL TESTS PASSED")
