#!/usr/bin/env python3
"""Offline smoke tests for salary_negotiator.py — stdlib only."""
import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
SCRIPT = HERE / "salary_negotiator.py"

spec = importlib.util.spec_from_file_location("sn", SCRIPT)
sn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sn)

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


# ── market anchor ────────────────────────────────────────────────────────
a = sn.build_anchor(130000, 160000, 210000, "strong")
ok("strong target above median", a["target"] > 160000)
ok("stretch above target", a["stretch"] > a["target"])
ok("stretch below market max", a["stretch"] < 210000)
ok("anchor has rationale", len(a["rationale"]) > 10)

a_dev = sn.build_anchor(130000, 160000, 210000, "developing")
ok("developing target below strong", a_dev["target"] < a["target"])
ok("medium between developing and strong",
   sn.build_anchor(130000, 160000, 210000, "medium")["target"]
   == 160000)

# ── total comp EV ────────────────────────────────────────────────────────
ev = sn.comp_ev(base=150000, bonus_pct=15, rsu_annual=60000,
                match_pct=4, match_cap=8000)
# base 150k + bonus 150000*.15*.85=19125 + rsu 60000*.9=54000
# + match min(6000, cap 8000)=6000 → 229125
ok("comp EV matches hand math (match under cap)",
   abs(ev["total_ev"] - 229125) < 1)

ev_cap = sn.comp_ev(base=150000, match_pct=4, match_cap=3000)
ok("401k match capped correctly",
   ev_cap["components"]["401k_match"] == 3000)

ev_sign = sn.comp_ev(base=100000, signon=15000, signon_years=3)
ok("sign-on amortized over 3yr",
   ev_sign["components"]["signon_amortized"] == 5000)

ev_opt = sn.comp_ev(base=100000, options=75000)
ok("options discounted to 15% of paper",
   ev_opt["components"]["options_risk_adjusted"] == 11250)

# ── walk-away floor ──────────────────────────────────────────────────────
fl = sn.walk_away_floor(monthly_costs=4200, runway_months=6)
ok("floor grosses up net costs", fl["gross_floor"] > fl["annual_costs"])
ok("floor ≈ 50400/0.78", abs(fl["gross_floor"] - 64600) < 100)

fl2 = sn.walk_away_floor(2000, 3, other_income=500, benefit_gap=200)
ok("other income lowers floor vs no income",
   fl2["gross_floor"] < sn.walk_away_floor(2000, 3)["gross_floor"])
ok("benefit gap raises floor",
   fl2["gross_floor"] > sn.walk_away_floor(2000, 3, other_income=500)["gross_floor"])

# ── package parser ───────────────────────────────────────────────────────
p = sn.parse_pkg("BigCo: base 150k, bonus 15%, rsu 60k/yr, 401k match 4%")
ok("parses base 150k", p["base"] == 150000)
ok("parses bonus 15 as pct", p["bonus_pct"] == 15)
ok("parses rsu 60k", p["rsu_annual"] == 60000)
ok("parses match 4 as pct", p["match_pct"] == 4)

p2 = sn.parse_pkg("Startup: base 130k, options 0.5%, strike 1.50, valuation 60M")
ok("stake options annualized (0.5% × 60M / 4)",
   abs(p2["options"] - 75000) < 1)

p3 = sn.parse_pkg("base 100k, signon 20k, options 80k")
ok("paper options annualized (80k/4)", p3["options"] == 20000)
ok("signon parsed", p3["signon"] == 20000)

# ── compare ──────────────────────────────────────────────────────────────
a_pkg = sn.parse_pkg("base 150k, bonus 15%, rsu 60k/yr, match 4%")
b_pkg = sn.parse_pkg("base 130k, options 0.5%, valuation 60M")
cmp = sn.compare_packages(a_pkg, b_pkg)
ok("BigCo beats startup on EV", cmp["ev_delta"] > 50000)
ok("compare has 3yr cash view", "a_3yr_cash" in cmp and cmp["a_3yr_cash"] > cmp["b_3yr_cash"])

# ── CLI subcommands ──────────────────────────────────────────────────────
r = run(["floor", "--monthly-costs", "4200", "--runway-months", "6"])
ok("floor cmd exits 0", r.returncode == 0)
ok("floor prints $", "$" in r.stdout)

r = run(["offer", "--role", "PM", "--offer-base", "115000",
         "--market-min", "105000", "--market-med", "125000",
         "--market-max", "140000"])
ok("offer cmd exits 0", r.returncode == 0)
ok("offer prints SCRIPT", "SCRIPT" in r.stdout)

r = run(["compare", "--a", "BigCo: base 150k, bonus 15%, rsu 60k/yr, 401k match 4%",
         "--b", "Startup: base 130k, options 0.5%, strike 1.50, valuation 60M"])
ok("compare cmd exits 0", r.returncode == 0)
ok("compare prints TOTAL EV", "TOTAL EV" in r.stdout)

r = run(["raise", "--current", "95000", "--market-med", "115000",
         "--impact", "shipped X", "--ask", "108000"])
ok("raise cmd exits 0", r.returncode == 0)

r = run(["demo"])
ok("demo runs clean", r.returncode == 0 and len(r.stdout) > 500)

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
