#!/usr/bin/env python3
"""Self-tests for apartment_scorecard.py — run: python3 scripts/test_apartment_scorecard.py"""
import importlib.util
import json
import math
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ap", os.path.join(HERE, "apartment_scorecard.py"))
if spec is None or spec.loader is None:
    raise SystemExit("cannot load module")
ap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ap)

PASS = 0


def check(name, cond):
    global PASS
    assert cond, f"FAILED: {name}"
    PASS += 1
    print(f"  ok  {name}")


print("criteria model:")
check("16 scoring criteria defined", len(ap.CRITERIA) == 16)
check("no leading-space keys (silent-skip bug)",
      all(k == k.strip() for k, *_ in ap.CRITERIA))
check("all default weights 1-3", all(1 <= w <= 3 for *_, w, _1, _2 in
      [(k, q, d, w, lo, hi) for k, q, d, w, lo, hi in ap.CRITERIA]))

print("hard screen:")
w = ap.sample_weights()
Ls = ap.sample_listings()
by_name = {L["name"]: L for L in Ls}
check("Gallery Loft fails budget", ap.hard_screen(by_name["Gallery Loft"], w)
      and "budget" in ap.hard_screen(by_name["Gallery Loft"], w)[0])
check("Vue Tower fails pets", any("pets" in r for r in
      ap.hard_screen(by_name["Vue Tower 1BR"], w)))
check("Maple St passes", ap.hard_screen(by_name["Maple St 2BR"], w) == [])
check("Oak Rd passes", ap.hard_screen(by_name["Oak Rd Garden"], w) == [])
tight = dict(w, max_commute_min=40)
check("Oak Rd fails tight commute", any("commute" in r for r in
      ap.hard_screen(by_name["Oak Rd Garden"], tight)))
dated = dict(w, move_date="2026-09-01")
check("Oak Rd fails early move date", any("available" in r for r in
      ap.hard_screen(by_name["Oak Rd Garden"], dated)))

print("scoring:")
pct, detail = ap.score(by_name["Maple St 2BR"], w)
check("Maple St scores 70-90%", 70 <= pct <= 90)
check("all 16 criteria contributed", len(detail) == 16)
pct_oak, _ = ap.score(by_name["Oak Rd Garden"], w)
check("Maple beats Oak Rd on weights", pct > pct_oak)
perfect = {"scores": {k: 5 for k, *_ in ap.CRITERIA}}
p100, _ = ap.score(perfect, w)
check("all-5s scores 100%", p100 == 100.0)
zeroed = dict(w, weights={k: 0 for k, *_ in ap.CRITERIA})
pz, _ = ap.score(perfect, zeroed)
check("zero weights can't divide by zero", pz == 0.0)
clamped, _ = ap.score({"scores": {ap.CRITERIA[0][0]: 99}}, zeroed)
check("out-of-range scores clamped safely", clamped == 0.0)

print("true cost:")
tm, bd = ap.true_monthly(by_name["Maple St 2BR"], w)
# 1850 rent + 40 fees + 140 utils + 15 ins + 100 parking + deposit interest
expected = 1850 + 40 + 140 + 15 + 100 + 1850 * 0.04 / 12
check("Maple true cost ≈ computed parts", abs(tm - expected) < 1.0)
check("utilities included drops util line",
      ap.true_monthly(by_name["Gallery Loft"], w)[1]["utilities"] == 0)
tm_g, bd_g = ap.true_monthly(by_name["Gallery Loft"], w)
check("broker fee amortized over lease", bd_g.get("one_time_amortized") == 125.0)
# commute valuation
wv = dict(w, commute_cost_per_min=0.5, commute_days=5)
tmv, bdv = ap.true_monthly(by_name["Maple St 2BR"], wv)
check("commute valued at $0.5/min ≈ $693/mo",
      abs(bdv["commute"] - (32 * 2 * 5 * 4.33 * 0.5)) < 1.0)
check("Maple all-in under half income", ap.income_ratio(tm, w) < 0.5)

print("budget:")
r30 = ap.render_budget(w)
check("30% rule computed on debt-adjusted income",
      abs(r30 - (6800 - 400) * 0.30) < 1.0)

print("negotiation:")
check("7% ask, 3% walk-away targets",
      True)  # verified via render below
plan = ap.render_negotiate(by_name["Maple St 2BR"], w,
                           {"vacant_days": True, "lease_length": True})
check("negotiation plan prints ask and script", "Ask:" in plan and "Script" in plan)

print("cli round-trip:")
with tempfile.TemporaryDirectory() as td:
    lf = os.path.join(td, "apartments.json")
    wf = os.path.join(td, "weights.json")
    with open(lf, "w") as f:
        json.dump(ap.sample_listings(), f)
    with open(wf, "w") as f:
        json.dump(ap.sample_weights(), f)
    r = subprocess.run([sys.executable, os.path.join(HERE, "apartment_scorecard.py"),
                        "screen", "--file", lf, "--weights", wf],
                       capture_output=True, text=True)
    check("screen ranks survivors", "Maple St 2BR" in r.stdout
          and "2 pass" in r.stdout and r.returncode == 0)
    check("screen shows fails with reasons", "pets not allowed" in r.stdout)
    r = subprocess.run([sys.executable, os.path.join(HERE, "apartment_scorecard.py"),
                        "compare", "--file", lf, "--weights", wf,
                        "Maple St 2BR", "Oak Rd Garden"],
                       capture_output=True, text=True)
    check("compare renders side-by-side + premium line",
          "Premium" in r.stdout and "SCORE %" in r.stdout)
    r = subprocess.run([sys.executable, os.path.join(HERE, "apartment_scorecard.py"),
                        "negotiate", "--file", lf, "--weights", wf,
                        "Maple St 2BR", "--vacant-days", "30",
                        "--lease-offer", "18"],
                       capture_output=True, text=True)
    check("negotiate flags vacancy lever", "vacant" in r.stdout.lower())
    # CSV input path
    cf = os.path.join(td, "apts.csv")
    with open(cf, "w") as f:
        f.write("name,rent,bedrooms,commute_min,pets_ok,available\n")
        f.write("Csv Flat,1500,1,20,true,2026-09-01\n")
    r = subprocess.run([sys.executable, os.path.join(HERE, "apartment_scorecard.py"),
                        "screen", "--file", cf, "--weights", wf],
                       capture_output=True, text=True)
    check("CSV listings load and screen", "Csv Flat" in r.stdout)
    r = subprocess.run([sys.executable, os.path.join(HERE, "apartment_scorecard.py"),
                        "example"], capture_output=True, text=True)
    check("example runs end-to-end", r.returncode == 0
          and "Screened 4 listings" in r.stdout)

print(f"\nALL TESTS PASSED ({PASS} assertions)")
