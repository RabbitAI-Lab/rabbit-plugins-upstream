#!/usr/bin/env python3
"""
gambar_sr.py — hitung Support & Resistance dari deret harga (closes) lokal.

Bantu Clara identifikasi level S&R tanpa chart:
  - Swing high / swing low (puncak & lembah berulang)
  - Angka bundar (psikologis, kelipatan 50/100)
  - High/Low periode

Input: CSV dengan kolom harga di kolom terakhir (oldest..newest), satu harga per baris,
atau arg --values "4500,4520,...".

Usage:
  python3 gambar_sr.py --closes history.csv
  python3 gambar_sr.py --values "4400,4525,4545,4730,4182" --round-step 50

Output: daftar level S&R + zona (dengan jarak ke harga terakhir).
No network, no destructive ops.
"""
import argparse
import csv
import sys


def load_closes(path):
    out = []
    try:
        with open(path, encoding="utf-8") as f:
            for row in csv.reader(f):
                if not row:
                    continue
                try:
                    out.append(float(row[-1]))
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"[warn] file not found: {path}", file=sys.stderr)
    return out


def round_levels(closes, step=50):
    levels = set()
    for p in closes:
        levels.add(round(p / step) * step)
    return sorted(levels)


def swing_levels(closes, window=3):
    highs, lows = [], []
    for i in range(window, len(closes) - window):
        seg = closes[i - window:i + window + 1]
        if closes[i] == max(seg):
            highs.append(closes[i])
        if closes[i] == min(seg):
            lows.append(closes[i])
    return sorted(set(highs)), sorted(set(lows))


def main():
    p = argparse.ArgumentParser(description="Compute Support & Resistance from price series.")
    p.add_argument("--closes", default=None, help="CSV of closes (oldest..newest)")
    p.add_argument("--values", default=None, help="Comma-separated prices")
    p.add_argument("--round-step", type=float, default=50, help="Round-number step (default 50)")
    p.add_argument("--window", type=int, default=3, help="Swing window")
    args = p.parse_args()

    closes = []
    if args.closes:
        closes = load_closes(args.closes)
    elif args.values:
        try:
            closes = [float(x) for x in args.values.split(",")]
        except ValueError:
            print("[error] invalid --values", file=sys.stderr)
            sys.exit(1)

    if len(closes) < 5:
        print("[warn] need >=5 prices for meaningful S&R", file=sys.stderr)
        return

    last = closes[-1]
    print(f"Last price: {last}")
    print(f"Period high: {max(closes)}  low: {min(closes)}")

    print("\n== Round-number S&R (step {}==".format(int(args.round_step)))
    for lv in round_levels(closes, args.round_step):
        tag = "RESISTANCE" if lv >= last else "SUPPORT"
        print(f"  {tag:11} {lv}")

    highs, lows = swing_levels(closes, args.window)
    print("\n== Swing Highs (resistance candidates) ==")
    for h in highs:
        if h >= last:
            print(f"  R  {h}")
    print("\n== Swing Lows (support candidates) ==")
    for l in lows:
        if l <= last:
            print(f"  S  {l}")


if __name__ == "__main__":
    main()
