#!/usr/bin/env python3
"""
winrate_tracker.py — HONEST performance measurement for gold (XAU/USD) trading.

Reads a trade journal (JSONL) and computes REAL statistics:
  - total trades, wins, losses, break-evens
  - win rate % (the REAL one, not a claim)
  - average R-multiple, expectancy (R), profit factor
  - streak info

This is the anti-90%-claim tool: it tells you what ACTUALLY happened.

Journal format (one JSON per line):
  {"date":"2026-08-20","symbol":"XAUUSD","side":"long","entry":4400,"sl":4345,
   "tp":4545,"exit":4520,"result":"win","r_multiple":2.6}
  result ∈ {win, loss, be}   ; r_multiple = (exit-entry)/(entry-sl) for long,
                              or (entry-exit)/(sl-entry) for short.

Usage:
  python3 winrate_tracker.py --journal memory/trading/journal.jsonl
  python3 winrate_tracker.py --journal memory/trading/journal.jsonl --since 2026-08-01

No network, no destructive ops. Pure math on your real history.
"""
import argparse
import json
import sys
from collections import deque


def load(path):
    rows = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print(f"[warn] journal not found: {path}", file=sys.stderr)
    return rows


def main():
    p = argparse.ArgumentParser(description="Honest gold trading win-rate tracker.")
    p.add_argument("--journal", default="memory/trading/journal.jsonl")
    p.add_argument("--since", default=None, help="Only trades on/after this date (YYYY-MM-DD)")
    args = p.parse_args()

    rows = load(args.journal)
    if args.since:
        rows = [r for r in rows if r.get("date", "") >= args.since]

    if not rows:
        print("No trades found. Journal honestly: 0 trades, no win-rate to claim.")
        return

    wins = [r for r in rows if r.get("result") == "win"]
    losses = [r for r in rows if r.get("result") == "loss"]
    bes = [r for r in rows if r.get("result") == "be"]
    total = len(rows)

    win_rate = 100.0 * len(wins) / total if total else 0

    r_vals = [float(r.get("r_multiple", 0)) for r in rows if r.get("r_multiple") is not None]
    avg_r = sum(r_vals) / len(r_vals) if r_vals else 0
    gross_win = sum(r["r_multiple"] for r in wins)
    gross_loss = sum(abs(r["r_multiple"]) for r in losses)
    profit_factor = (gross_win / gross_loss) if gross_loss else float("inf")
    expectancy = (win_rate / 100.0) * (avg_r if avg_r else 0) - \
                 ((100 - win_rate) / 100.0) * 1.0  # assume 1R loss per loss

    # streak
    streak = 0
    max_win_streak = 0
    max_loss_streak = 0
    cur_win = cur_loss = 0
    for r in rows:
        res = r.get("result")
        if res == "win":
            cur_win += 1; cur_loss = 0
            max_win_streak = max(max_win_streak, cur_win)
        elif res == "loss":
            cur_loss += 1; cur_win = 0
            max_loss_streak = max(max_loss_streak, cur_loss)
        else:
            cur_win = cur_loss = 0

    print("=" * 48)
    print("  HONEST GOLD TRADING PERFORMANCE")
    print("=" * 48)
    print(f"  Trades        : {total}")
    print(f"  Wins / Loss / BE : {len(wins)} / {len(losses)} / {len(bes)}")
    print(f"  REAL win rate : {win_rate:.1f}%")
    print(f"  Avg R-multiple: {avg_r:+.2f}R")
    print(f"  Expectancy    : {expectancy:+.2f}R per trade")
    print(f"  Profit factor : {('∞' if profit_factor == float('inf') else f'{profit_factor:.2f}')}")
    print(f"  Max win streak : {max_win_streak}")
    print(f"  Max loss streak: {max_loss_streak}")
    print("=" * 48)
    if win_rate >= 90:
        print("  ⚠ Note: 90%+ over a small sample is rare & usually not sustainable.")
    elif win_rate < 50:
        print("  Note: win rate < 50% is FINE if R:R is positive (expectancy > 0).")
    print("  This number is REAL (from your journal), not a marketing claim.")


if __name__ == "__main__":
    main()
