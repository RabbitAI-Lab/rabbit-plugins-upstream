#!/usr/bin/env python3
"""Offline smoke tests for freelance_rate.py — stdlib only."""
import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
SCRIPT = HERE / "freelance_rate.py"

spec = importlib.util.spec_from_file_location("fr", SCRIPT)
fr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fr)

passed = failed = 0


def ok(name, cond):
    global passed, failed
    if cond:
        passed += 1
        print(f"  ok  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


def run(args):
    return subprocess.run([sys.executable, str(SCRIPT)] + args,
                          capture_output=True, text=True)


# ── core rate math ───────────────────────────────────────────────────────
r = fr.compute_rate(70000)
ok("rate is positive", r["hourly_rate"] > 0)
ok("revenue ≥ gross ≥ net", r["revenue_needed"] >= r["gross_needed"] >= 70000)
ok("keep ratio < 1", 0 < r["keep_ratio"] < 1)

r_benefits = fr.compute_rate(70000, benefits_load=12000)
ok("benefits raise the rate", r_benefits["hourly_ratio"] if False else
   r_benefits["hourly_rate"] > r["hourly_rate"])

r_overhead = fr.compute_rate(70000, overhead=8000)
ok("overhead raises the rate", r_overhead["hourly_rate"] > r["hourly_rate"])

r_busy = fr.compute_rate(70000, billable_ratio=0.75)
ok("higher billable ratio lowers rate", r_busy["hourly_rate"] < r["hourly_rate"])

r_bench = fr.compute_rate(70000, months_bench=0, bench_loaded=True)
ok("no bench lowers rate", r_bench["hourly_rate"] < r["hourly_rate"])

r_bench2 = fr.compute_rate(70000, months_bench=3)
ok("long bench raises rate", r_bench2["hourly_rate"] > r["hourly_rate"])

# hand-check: 70k net, no extras, keep 0.6787 → gross 103,113; 1012 billable h
r_hand = fr.compute_rate(70000)
keep = 1 - 0.18 - 0.153 * 0.9235
ok("gross matches hand math", abs(r_hand["gross_needed"] - 70000 / keep) < 2)
ok("billable hours = 46*40*0.6*(11/12)",
   abs(r_hand["billable_hours"] - 46 * 40 * 0.6 * (11 / 12)) < 1)

# ── salary replacement ───────────────────────────────────────────────────
s = fr.rate_for_salary(95000)
ok("salary→rate > naive salary/2080", s["hourly_rate"] > 95000 / 2080)
ok("salary→rate multiplier ≥ 2x", s["hourly_rate"] / (95000 / 2080) > 2)

# ── check (inverse) ──────────────────────────────────────────────────────
c = fr.check_rate(100)
ok("check: revenue = rate × billable", abs(c["annual_revenue"] - 100 * c["billable_hours"]) < 1)
ok("check: net < revenue", c["annual_net"] < c["annual_revenue"])
ok("check: equivalent salary > net", c["equivalent_salary"] > c["annual_net"])

# round-trip: rate computed for N net should check back to ≈ N
rt = fr.compute_rate(80000)
back = fr.check_rate(rt["hourly_rate"])
ok("round-trip net ≈ 80k", abs(back["annual_net"] - 80000) < 1500)

# ── project pricing ──────────────────────────────────────────────────────
q = fr.price_project(100, 100, risk_buffer=0.15)
ok("quote = hours × 1.15 × rate", abs(q["fixed_price"] - 11500) < 1)
ok("effective rate ≥ nominal when buffered",
   q["price_per_hour_effective"] >= 100)

q_rush = fr.price_project(100, 100, risk_buffer=0.15, rush=True)
ok("rush premium applied", q_rush["fixed_price"] > q["fixed_price"])

q_cap = fr.price_project(100, 100, risk_buffer=0.15, value_price_cap=10000)
ok("value cap binds", q_cap["fixed_price"] == 10000 and "capped_at" in q_cap)

# ── CLI ──────────────────────────────────────────────────────────────────
r1 = run(["rate", "--target-net", "70000"])
ok("rate cmd exits 0", r1.returncode == 0)
ok("rate prints HOURLY RATE", "HOURLY RATE" in r1.stdout)

r2 = run(["salary", "--salary", "95000"])
ok("salary cmd exits 0", r2.returncode == 0)
ok("salary prints the trap line", "trap" in r2.stdout.lower())

r3 = run(["check", "--rate", "60", "--min-net", "70000"])
ok("check cmd exits 0", r3.returncode == 0)
ok("check flags shortfall", "SHORT" in r3.stdout)

r4 = run(["project", "--hours", "60", "--rate", "100"])
ok("project cmd exits 0", r4.returncode == 0)
ok("project prints QUOTE", "QUOTE" in r4.stdout)

r5 = run(["demo"])
ok("demo runs clean", r5.returncode == 0 and len(r5.stdout) > 300)

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
