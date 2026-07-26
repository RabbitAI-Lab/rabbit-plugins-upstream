#!/usr/bin/env python3
"""
stablecoin-depeg-monitor: Real-time stablecoin peg monitoring.
Detects deviations from $1.00 across DEX and CEX venues, scores risk,
and surfaces arbitrage windows.

Usage:
    python3 depeg_monitor.py check
    python3 depeg_monitor.py check USDC
    python3 depeg_monitor.py watch
    python3 depeg_monitor.py history USDC
    python3 depeg_monitor.py arb
"""
import argparse
import json
import os
import random
import sys
import time
from datetime import datetime, timezone
from typing import Optional


STABLES = ["USDT", "USDC", "DAI", "FRAX", "TUSD", "BUSD", "USDP", "GUSD"]
THRESHOLD_BPS = int(os.environ.get("STABLECOIN_THRESHOLD_BPS", "50"))
POLL_INTERVAL = int(os.environ.get("STABLECOIN_POLL_INTERVAL", "60"))


def fetch_mock_venue_prices(stable: str) -> dict:
    """
    In production, hit Curve subgraph, Binance, Coinbase, Uniswap TWAPs.
    For local/CI runs, synthesize realistic prices with a small noise band
    plus an optional stress offset driven by a deterministic seed.
    """
    seed = sum(ord(c) for c in stable) + int(time.time() // 30)
    rng = random.Random(seed)
    # Most stables sit within ±5 bps; allow occasional wobble.
    base = 1.0
    if stable == "USDT" and rng.random() < 0.05:
        base -= rng.uniform(0.002, 0.012)
    if stable == "USDC" and rng.random() < 0.03:
        base += rng.uniform(0.001, 0.006)
    venues = {
        "binance": round(base + rng.uniform(-0.0008, 0.0008), 5),
        "coinbase": round(base + rng.uniform(-0.0008, 0.0008), 5),
        "kraken": round(base + rng.uniform(-0.0008, 0.0008), 5),
        "curve_3pool": round(base + rng.uniform(-0.0015, 0.0015), 5),
        "uniswap_v3": round(base + rng.uniform(-0.002, 0.002), 5),
    }
    liquidity = {
        "binance": rng.uniform(50_000_000, 200_000_000),
        "coinbase": rng.uniform(20_000_000, 90_000_000),
        "curve_3pool": rng.uniform(40_000_000, 150_000_000) * (1.0 if abs(base - 1.0) < 0.005 else 0.4),
        "uniswap_v3": rng.uniform(5_000_000, 25_000_000),
    }
    return {"venues": venues, "liquidity": liquidity}


def mid_price(prices: dict) -> float:
    return sum(prices.values()) / len(prices)


def deviation_bps(price: float) -> float:
    return (price - 1.0) * 10_000


def classify(dev_bps: float) -> str:
    if abs(dev_bps) < 10:
        return "PEGGED"
    if abs(dev_bps) < THRESHOLD_BPS:
        return "WOBBLE"
    return "DEPEG"


def check_stable(stable: str) -> dict:
    data = fetch_mock_venue_prices(stable)
    mid = mid_price(data["venues"])
    dev = deviation_bps(mid)
    status = classify(dev)
    return {
        "stable": stable,
        "mid_price": round(mid, 5),
        "deviation_bps": round(dev, 2),
        "status": status,
        "venues": {k: round(v, 5) for k, v in data["venues"].items()},
        "venue_spread_bps": round(
            (max(data["venues"].values()) - min(data["venues"].values())) * 10_000, 2
        ),
        "liquidity_usd": {k: round(v, 0) for k, v in data["liquidity"].items()},
        "total_liquidity_usd": round(sum(data["liquidity"].values()), 0),
        "threshold_bps": THRESHOLD_BPS,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def cmd_check(target: Optional[str]) -> None:
    stables = [target.upper()] if target else STABLES
    results = [check_stable(s) for s in stables]
    print(json.dumps({"results": results, "count": len(results)}, indent=2))


def cmd_watch() -> None:
    print(f"# Polling every {POLL_INTERVAL}s | threshold ±{THRESHOLD_BPS}bps", file=sys.stderr)
    try:
        while True:
            results = [check_stable(s) for s in STABLES]
            alerts = [r for r in results if r["status"] != "PEGGED"]
            line = json.dumps({
                "ts": datetime.now(timezone.utc).isoformat(),
                "alerts": alerts,
                "all": results,
            })
            print(line, flush=True)
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        sys.exit(0)


def cmd_history(stable: str) -> None:
    """
    Synthesize a 30-day stability summary. Production would query
    on-chain events, Curve trade logs, and CEX klines.
    """
    stable = stable.upper()
    rng = random.Random(sum(ord(c) for c in stable))
    n_samples = 30 * 24
    samples = []
    base = 1.0
    for i in range(n_samples):
        drift = rng.gauss(0, 0.0005)
        # Occasional stress event
        if rng.random() < 0.002:
            drift += rng.choice([-0.005, 0.003])
        base = max(0.85, min(1.15, base + drift))
        samples.append(base)
    max_dev = max(samples) - 1.0
    min_dev = min(samples) - 1.0
    avg_dev = sum(samples) / len(samples) - 1.0
    out = {
        "stable": stable,
        "window_days": 30,
        "samples": n_samples,
        "max_premium_bps": round(max_dev * 10_000, 2),
        "max_discount_bps": round(min_dev * 10_000, 2),
        "avg_deviation_bps": round(avg_dev * 10_000, 2),
        "depeg_events": sum(1 for p in samples if abs(p - 1.0) > THRESHOLD_BPS / 10_000),
        "stability_score": round(1.0 - min(1.0, abs(avg_dev) * 100), 4),
    }
    print(json.dumps(out, indent=2))


def cmd_arb() -> None:
    """
    Find venues where the same stable is trading at materially different
    prices — classic depeg-arb surface.
    """
    opps = []
    for s in STABLES:
        r = check_stable(s)
        prices = r["venues"]
        hi = max(prices.items(), key=lambda kv: kv[1])
        lo = min(prices.items(), key=lambda kv: kv[1])
        spread_bps = (hi[1] - lo[1]) * 10_000
        if spread_bps >= 5:
            opps.append({
                "stable": s,
                "buy_venue": lo[0],
                "buy_price": lo[1],
                "sell_venue": hi[0],
                "sell_price": hi[1],
                "spread_bps": round(spread_bps, 2),
                "edge_per_100k_usd": round((hi[1] - lo[1]) * 100_000, 2),
            })
    opps.sort(key=lambda o: o["spread_bps"], reverse=True)
    print(json.dumps({"opportunities": opps, "count": len(opps)}, indent=2))


def main() -> int:
    p = argparse.ArgumentParser(description="Stablecoin depeg monitor")
    sub = p.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("check", help="Check peg status")
    p1.add_argument("stable", nargs="?", help="Specific symbol, e.g. USDC")

    p2 = sub.add_parser("watch", help="Stream live updates")

    p3 = sub.add_parser("history", help="Historical stability window")
    p3.add_argument("stable", help="Specific symbol, e.g. USDC")

    p4 = sub.add_parser("arb", help="Find arbitrage opportunities")

    args = p.parse_args()
    if args.cmd == "check":
        cmd_check(args.stable)
    elif args.cmd == "watch":
        cmd_watch()
    elif args.cmd == "history":
        cmd_history(args.stable)
    elif args.cmd == "arb":
        cmd_arb()
    return 0


if __name__ == "__main__":
    sys.exit(main())
