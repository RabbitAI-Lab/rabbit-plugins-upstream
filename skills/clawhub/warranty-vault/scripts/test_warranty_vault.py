#!/usr/bin/env python3
"""Tests for warranty_vault.py — plain asserts. Run: python3 test_warranty_vault.py"""
import datetime as dt
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(HERE, "warranty_vault.py")
sys.path.insert(0, HERE)
import warranty_vault as wv  # noqa: E402


def run_cli(args, f):
    return subprocess.run([sys.executable, ENGINE] + args + ["--file", f],
                          capture_output=True, text=True)


def check(label, cond):
    assert cond, label
    print("[PASS] %s" % label)


tmp = tempfile.mkdtemp()
V = os.path.join(tmp, "vault.json")

# ---- date math ----
check("months_add basic", wv.months_add(dt.date(2024, 11, 3), 12) == dt.date(2025, 11, 3))
check("months_add month-end clamp", wv.months_add(dt.date(2024, 1, 31), 1) == dt.date(2024, 2, 29))
check("months_add year rollover", wv.months_add(dt.date(2024, 11, 3), 72) == dt.date(2030, 11, 3))

# ---- card program detection ----
check("card amex detected", wv.card_program("Amex Gold") == "amex")
check("card visa infinite detected", wv.card_program("Chase Visa Infinite") == "visa-infinite")
check("card none", wv.card_program(None) is None)
check("card random", wv.card_program("debit card") is None)

# ---- coverage engine ----
d = wv.d  # shorthand
t = wv.today()
recent = dict(id="x", purchased=(t - dt.timedelta(days=100)).isoformat(),
              warranty_mo=24, card="Amex Gold", price=500)
lys = wv.layers_for(recent, "US")
names = [l["name"] for l in lys]
check("US: manufacturer + card perk, no statutory", len(lys) == 2
      and any("manufacturer" in n for n in names) and any("card perk" in n for n in names))
card_ly = [l for l in lys if "card perk" in l["name"]][0]
check("amex perk adds 12mo AFTER mfr end",
      card_ly["end"] == wv.months_add(wv.months_add(d(recent["purchased"]), 24), 12))

lys = wv.layers_for(recent, "UK")
check("UK: statutory layer present", any("statutory" in l["name"] for l in lys))
stat = [l for l in lys if "statutory" in l["name"]][0]
check("UK statutory end = +72mo", stat["end"] == wv.months_add(d(recent["purchased"]), 72))
check("UK <6mo burden reversed", "REVERSED" in stat["note"])

lys = wv.layers_for(recent, "EU")
stat = [l for l in lys if "statutory" in l["name"]][0]
check("EU statutory end = +24mo", stat["end"] == wv.months_add(d(recent["purchased"]), 24))

# long base warranty ineligible for card perk
long_w = dict(recent, warranty_mo=60)
lys = wv.layers_for(long_w, "US")
inelig = [l for l in lys if "card perk" in l["name"]]
check("5yr base warranty ineligible for amex perk", inelig and not inelig[0]["live"]
      and "ineligible" in inelig[0]["evidence"])

# expired warranty
old = dict(recent, purchased=(t - dt.timedelta(days=800)).isoformat(), warranty_mo=12)
lys = wv.layers_for(old, "US")
check("expired mfr warranty not live", all(not l["live"] for l in lys
      if "manufacturer" in l["name"]))

# ---- CLI flow ----
r = run_cli(["add", "--id", "dishwasher", "--name", "Bosch dishwasher",
             "--category", "appliance", "--price", "749",
             "--purchased", "2024-11-03", "--warranty-mo", "12",
             "--receipt", "email order #3391", "--card", "Amex Gold",
             "--jurisdiction", "UK"], V)
check("add dishwasher", r.returncode == 0)
r = run_cli(["add", "--id", "tv", "--name", "LG C4", "--price", "1299",
             "--purchased", "2025-03-14", "--warranty-mo", "12",
             "--extended-mo", "36", "--extended-by", "Geek Squad"], V)
check("add tv with extended", r.returncode == 0)
r = run_cli(["add", "--id", "dishwasher", "--price", "1",
             "--purchased", "2025-01-01"], V)
check("duplicate id rejected", r.returncode != 0)

r = run_cli(["covered", "--id", "tv", "--jurisdiction", "UK"], V)
check("covered shows extended plan live", "extended plan" in r.stdout and "LIVE" in r.stdout)

r = run_cli(["expiring", "--days", "3650"], V)
check("expiring finds items with big window", r.returncode == 0
      and ("ends 2" in r.stdout or "ends 3" in r.stdout))

r = run_cli(["claim", "--id", "dishwasher", "--fault", "Won't drain; E25 error",
             "--jurisdiction", "UK"], V)
check("claim letter cites CRA 2015", "Consumer Rights Act 2015" in r.stdout)
check("claim letter targets retailer for statutory", "RETAILER" in r.stdout)
check("claim letter includes fault", "Won't drain; E25 error" in r.stdout)
check("claim includes checklist", "CHECKLIST" in r.stdout)

r = run_cli(["report", "--json"], V)
data = json.loads(r.stdout)
check("report json: 2 entries, any_live flags", len(data["entries"]) == 2
      and isinstance(data["entries"][0]["any_live"], bool))

r = run_cli(["update", "--id", "dishwasher", "--mark-registered"], V)
check("mark-registered works", r.returncode == 0)
data = json.load(open(V))
ds = [e for e in data["entries"] if e["id"] == "dishwasher"][0]
check("registered = today", ds["registered"] == t.isoformat())

r = run_cli(["list"], V)
check("list shows totals", "total $" in r.stdout and "dishwasher" in r.stdout)

r = run_cli(["remove", "--id", "tv"], V)
data = json.load(open(V))
check("remove works", "tv" not in [e["id"] for e in data["entries"]])

print("\nALL TESTS PASSED")
