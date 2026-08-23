#!/usr/bin/env python3
"""
pattern_scan.py — deteksi Chart Pattern & Divergence (no-ICT).

Dari deret harga (+ RSI opsional) hasilkan sinyal:
  - Double Top / Double Bottom (M/W)  -> reversal
  - Bullish / Bearish RSI Divergence  -> momentum berbalik
  - Breakout / Breakdown S&R sederhana

Input: CSV 2 kolom (date,close) atau --values "..."; RSI via --rsi "..." (opsional).
Cara pakai:
  python3 pattern_scan.py --values "4400,4523,4450,4521,4380"
  python3 pattern_scan.py --values "..." --rsi "..." --tol 0.3

Pure math, no network.
"""
import argparse
import csv
import sys


def load(path):
    out = []
    try:
        with open(path, encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) < 2:
                    continue
                try:
                    out.append(float(row[1]))
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    return out


def double_top_bottom(closes, tol=0.003):
    n = len(closes)
    if n < 5:
        return []
    sig = []
    # cari 2 puncak / 2 lembah terpisah
    for i in range(2, n - 2):
        # double top: high i ~ high j, turun di antaranya
        for j in range(i + 2, n):
            if abs(closes[i] - closes[j]) / closes[i] <= tol:
                mid = min(closes[i + 1:j])
                if closes[i] > mid and closes[j] > mid:
                    sig.append(("DOUBLE_TOP", closes[i], j))
                    break
        # double bottom
        for j in range(i + 2, n):
            if abs(closes[i] - closes[j]) / closes[i] <= tol:
                mid = max(closes[i + 1:j])
                if closes[i] < mid and closes[j] < mid:
                    sig.append(("DOUBLE_BOTTOM", closes[i], j))
                    break
    return sig


def divergence(closes, rsi):
    """Bullish: harga lower low, RSI higher low. Bearish: sebaliknya."""
    if not rsi or len(rsi) != len(closes) or len(closes) < 6:
        return []
    out = []
    # cari 2 lembah/2 puncak harga terakhir
    n = len(closes)
    ll1 = ll2 = None
    for i in range(1, n - 1):
        if closes[i] < closes[i - 1] and closes[i] < closes[i + 1]:
            ll1 = (i, closes[i], rsi[i])
            break
    for i in range(ll1[0] + 1, n - 1) if ll1 else []:
        if closes[i] < closes[i - 1] and closes[i] < closes[i + 1]:
            ll2 = (i, closes[i], rsi[i])
            break
    if ll1 and ll2:
        if ll2[1] < ll1[1] and ll2[2] > ll1[2]:
            out.append(("BULLISH_DIVERGENCE", ll2[0]))
        if ll2[1] > ll1[1] and ll2[2] < ll1[2]:
            out.append(("BEARISH_DIVERGENCE", ll2[0]))
    return out


def main():
    p = argparse.ArgumentParser(description="Scan chart patterns & divergence (no-ICT).")
    p.add_argument("--values", default=None, help="Comma prices")
    p.add_argument("--rsi", default=None, help="Comma RSI same length")
    p.add_argument("--closes", default=None, help="CSV date,close")
    p.add_argument("--tol", type=float, default=0.003, help="Tolerance double top/bottom")
    args = p.parse_args()

    closes = []
    if args.closes:
        closes = load(args.closes)
    elif args.values:
        try:
            closes = [float(x) for x in args.values.split(",")]
        except ValueError:
            print("[error] bad --values", file=sys.stderr)
            sys.exit(1)

    rsi = None
    if args.rsi:
        try:
            rsi = [float(x) for x in args.rsi.split(",")]
        except ValueError:
            rsi = None

    if len(closes) < 5:
        print("[warn] need >=5 prices", file=sys.stderr)
        return

    print(f"Scan {len(closes)} bars. (no-ICT: OB/FVG/BoS diabaikan)")
    dt = double_top_bottom(closes, args.tol)
    for s in dt:
        print(f"  {s[0]} @ {s[1]} (idx {s[2]})")
    dv = divergence(closes, rsi) if rsi else []
    for s in dv:
        print(f"  {s[0]} (idx {s[1]})")
    if not dt and not dv:
        print("  Tidak ada pattern/divergence terdeteksi.")


if __name__ == "__main__":
    main()
