#!/usr/bin/env python3
"""
Fixture tests for the coherence gates.

Every fixture is derived from real Simmer market data measured on 17/07/2026.
No network and no SDK needed. Run: python3 tests/test_coherence.py
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from coherence_scanner import (  # noqa: E402
    assess_group,
    detect_partition_family,
    executable_price,
    group_by_event,
    non_negative_margin,
    scan,
)

FAILURES = []


def check(name, cond, detail=""):
    if cond:
        print(f"  pass  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILURES.append(name)


def leg(eid, ename, prob, ask=None, neg_risk=False, fee_bps=0, age=None, mid=None):
    return {
        "id": f"{eid}-{prob}-{ask}",
        "event_id": eid,
        "event_name": ename,
        "current_probability": prob,
        "best_ask": ask,
        "polymarket_neg_risk": neg_risk,
        "fee_rate_bps": fee_bps,
        "quote_age_seconds": age,
        "question": f"leg {prob}",
    }


print("\n1. Phantom arbitrage from missing legs (the expensive mistake)")
# Real data: 27 of 37 legs of the 2028 Democratic nominee event summed to
# 0.308. That is not a 69% arbitrage, it is 10 absent legs. The full 37-leg
# set summed to 1.0015.
partial = [leg("dem", "Democratic Presidential Nominee 2028", 0.308 / 27, ask=0.308 / 27, neg_risk=True) for _ in range(27)]
d = assess_group(partial)
check("refuses to trade an incomplete leg set", d.action == "ABSTAIN", d.reason)
check("names missing legs as the cause", "missing legs" in d.reason, d.reason)

print("\n2. The same event, complete, is efficiently priced")
full = [leg("dem", "Democratic nominee for President in 2028?", 1.0015 / 37, ask=1.0015 / 37, neg_risk=True) for _ in range(37)]
d = assess_group(full)
check("complete but no-edge group abstains", d.action == "ABSTAIN", d.reason)
check("cites cost, not completeness", "no edge after costs" in d.reason, d.reason)

print("\n3. Non-partition bundles are rejected structurally")
# "Spain vs. Argentina - More Markets": 23 unrelated props, midpoint sum 5.44.
bundle = [leg("more", "Spain vs. Argentina - More Markets", 0.2366, ask=0.24) for _ in range(23)]
fam, why = detect_partition_family(bundle)
check("More Markets is not a partition family", fam is None, why)
d = assess_group(bundle)
check("bundle abstains before any arithmetic", d.action == "ABSTAIN", d.reason)
check("rejects on structure", "not a proven partition" in d.reason, d.reason)

print("\n4. Sum alone never proves a partition (no circular reasoning)")
# Sums to a plausible 0.97 but has zero structural evidence.
sneaky = [leg("x", "Some Random Event", 0.485, ask=0.485) for _ in range(2)]
d = assess_group(sneaky)
check("plausible sum without structure still abstains", d.action == "ABSTAIN", d.reason)
check("rejects on structure not price", "not a proven partition" in d.reason, d.reason)

print("\n5. Midpoints are never substituted for asks")
noquote = [leg("gb", "World Cup: Golden Boot Winner", 0.0995, ask=None, neg_risk=True) for _ in range(10)]
check("executable_price returns None without an ask", executable_price(noquote[0]) is None)
d = assess_group(noquote)
check("abstains when quotes are absent", d.action == "ABSTAIN", d.reason)
check("explains midpoints are not tradeable", "not tradeable" in d.reason, d.reason)

print("\n6. A genuine dutch book is taken")
# 4 neg-risk legs at 0.24 ask => 0.96 for a guaranteed 1.00.
real = [leg("ev", "Real Partition", 0.24, ask=0.24, neg_risk=True, age=5.0) for _ in range(4)]
d = assess_group(real)
check("acts on a real coherent set", d.action == "BUY_ALL_LEGS", d.reason)
check("margin is +0.04", d.margin is not None and abs(d.margin - 0.04) < 1e-9, str(d.margin))

print("\n7. Fees can erase a thin edge")
# min_margin is an inclusive floor: margin >= min_margin trades. Fixtures sit
# clearly either side of it, never on it, because an exact-boundary case is
# decided by float noise (0.99 yields margin 0.010000000000000009) and would
# make this test assert nothing meaningful.
thin = [leg("f", "Thin", 0.2481, ask=0.2481, neg_risk=True) for _ in range(4)]
d = assess_group(thin)
check("0.9924 cost, margin 0.0076 under the 0.01 floor, abstains", d.action == "ABSTAIN", d.reason)
feed = [leg("f2", "Fee", 0.24, ask=0.24, neg_risk=True, fee_bps=500) for _ in range(4)]
d = assess_group(feed)
check("500bps fees are charged against the edge", d.executable_sum is not None and d.executable_sum > 0.96, str(d.executable_sum))

print("\n8. A truncated discovery window forces abstention")
d = assess_group(real, window_truncated=True)
check("truncated window abstains even on a good set", d.action == "ABSTAIN", d.reason)
check("names truncation", "truncated" in d.reason, d.reason)

print("\n9. Stale quotes are refused")
stale = [leg("s", "Stale", 0.24, ask=0.24, neg_risk=True, age=9999.0) for _ in range(4)]
d = assess_group(stale)
check("stale quotes abstain", d.action == "ABSTAIN" and "stale" in d.reason, d.reason)

print("\n10. Grouping and ranking")
mixed = real + bundle
groups = group_by_event(mixed)
check("groups split by event_id", len(groups) == 2, str(list(groups)))
ds = scan(mixed)
check("tradeable sorts first", ds[0].tradeable and not ds[1].tradeable)

print("\n11. A negative margin floor is refused")
try:
    scan(mixed, min_margin=-0.02)
    check("negative min_margin raises", False, "no exception")
except ValueError as e:
    check("negative min_margin raises", True)
    check("explains the guaranteed loss", "guaranteed" in str(e), str(e))
try:
    non_negative_margin("-0.02")
    check("CLI rejects a negative floor", False, "no exception")
except argparse.ArgumentTypeError:
    check("CLI rejects a negative floor", True)
check("CLI still accepts a thin positive floor", non_negative_margin("0.005") == 0.005)
check("CLI still accepts zero", non_negative_margin("0") == 0.0)
check("a zero floor does not raise", len(scan(mixed, min_margin=0.0)) == 2)

print("\n" + "=" * 62)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} -> {FAILURES}")
    sys.exit(1)
print("All gates pass.")
sys.exit(0)
