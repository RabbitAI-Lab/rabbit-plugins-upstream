#!/usr/bin/env python3
"""trading-analyst: position size + R:R calculator (pure math, no API).

Implements the skill's Risk-First rules:
  - risk <= 1% equity/trade
  - R:R >= 1:2
  - SL placed beyond invalidation (here the user supplies entry/SL/TP)
  - move SL to BE after +1R

Usage:
  python3 risk_calc.py --equity 10000 --risk 1 --entry 2300 --sl 2280 --tp 2360
  python3 risk_calc.py --equity 10000 --risk 1 --entry 2300 --sl 2280 --tp 2360 --contract 1

For XAU/USD CFD the per-unit risk depends on contract size (e.g. 1.0 = 1 oz,
or broker micro-lot specs). Pass --contract to scale. No network, no secrets.
"""
import argparse
import sys


def compute(equity, risk_pct, entry, sl, tp, contract=1.0, direction=None):
    risk_amount = equity * (risk_pct / 100.0)
    per_unit = abs(entry - sl) * contract
    if per_unit <= 0:
        raise ValueError("entry and SL must differ (SL cannot equal entry)")
    size = risk_amount / per_unit
    reward_amount = abs(tp - entry) * contract * size
    rr = (abs(tp - entry) / abs(entry - sl)) if abs(entry - sl) > 0 else 0.0
    # direction inferred if not given
    if direction is None:
        direction = "LONG" if tp > entry else "SHORT"
    return {
        "direction": direction,
        "risk_amount": round(risk_amount, 2),
        "per_unit_risk": round(per_unit, 4),
        "position_size": round(size, 4),
        "reward_amount": round(reward_amount, 2),
        "rr": round(rr, 2),
        "risk_pct": risk_pct,
        "be_after": "+1R (move SL to entry)",
    }


def main():
    p = argparse.ArgumentParser(description="trading position-size + R:R calculator")
    p.add_argument("--equity", type=float, required=True, help="account equity")
    p.add_argument("--risk", type=float, required=True, help="risk fraction per trade, e.g. 1 means 1 percent")
    p.add_argument("--entry", type=float, required=True)
    p.add_argument("--sl", type=float, required=True)
    p.add_argument("--tp", type=float, required=True)
    p.add_argument("--contract", type=float, default=1.0, help="units per 1.0 size (XAU: 1 oz)")
    p.add_argument("--direction", choices=["LONG", "SHORT"], default=None)
    args = p.parse_args()

    try:
        r = compute(args.equity, args.risk, args.entry, args.sl, args.tp, args.contract, args.direction)
    except ValueError as e:
        print(f"[risk_calc] ERROR: {e}", file=sys.stderr)
        return 2

    print("POSITION PLAN")
    print(f"  Direction      : {r['direction']}")
    print(f"  Risk amount    : {r['risk_amount']} ({r['risk_pct']}%)")
    print(f"  Per-unit risk  : {r['per_unit_risk']}")
    print(f"  Position size  : {r['position_size']}")
    print(f"  Reward amount  : {r['reward_amount']}")
    print(f"  R:R            : {r['rr']}  (target >= 1:2)")
    print(f"  Management     : {r['be_after']}")

    ok = (r["rr"] >= 2.0) and (r["risk_pct"] <= 1.0)
    print("  Verdict        : " + ("OK - within risk rules" if ok else "REVIEW - R:R<1:2 or risk>1%"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
