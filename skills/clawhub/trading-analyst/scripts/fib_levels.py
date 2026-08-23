#!/usr/bin/env python3
"""
fib_levels.py — hitung level Fibonacci Retracement & Extension (no-ICT).

Dari satu swing high & swing low, hasilkan level S/R potensial:
  Retracement : 23.6% 38.2% 50% 61.8% 78.6%
  Extension    : 127.2% 161.8% (target profit di luar struktur)

Cara pakai:
  python3 fib_levels.py --high 4523 --low 4028          # retracement naik
  python3 fib_levels.py --high 4523 --low 4028 --dir down  # retracement turun

Pure math, no network. Output JSON + ringkasan.
"""
import argparse
import json
import sys

RETR = [0.236, 0.382, 0.5, 0.618, 0.786]
EXT = [1.272, 1.618]


def main():
    p = argparse.ArgumentParser(description="Fibonacci retracement/extension levels.")
    p.add_argument("--high", type=float, required=True, help="Swing high")
    p.add_argument("--low", type=float, required=True, help="Swing low")
    p.add_argument("--dir", choices=["up", "down"], default="up",
                   help="arah move awal (up = harga naik dari low ke high)")
    args = p.parse_args()

    if args.high <= args.low:
        print("[error] high harus > low", file=sys.stderr)
        sys.exit(1)

    rng = args.high - args.low
    out = {"high": args.high, "low": args.low, "dir": args.dir,
           "retracement": {}, "extension": {}}
    print(f"Swing: high={args.high} low={args.low} range={rng:.2f} dir={args.dir}")
    print("\n== RETRACEMENT (level S/R saat pullback) ==")
    for r in RETR:
        if args.dir == "up":
            lvl = args.high - rng * r
        else:
            lvl = args.low + rng * r
        out["retracement"][f"{int(r*1000)/10}%"] = round(lvl, 2)
        print(f"  {int(r*1000)/10:>5}%  ->  {lvl:.2f}")
    print("\n== EXTENSION (target profit) ==")
    for e in EXT:
        if args.dir == "up":
            lvl = args.high + rng * (e - 1)
        else:
            lvl = args.low - rng * (e - 1)
        out["extension"][f"{int(e*1000)/10}%"] = round(lvl, 2)
        print(f"  {int(e*1000)/10:>5}%  ->  {lvl:.2f}")
    print("\n" + json.dumps(out))


if __name__ == "__main__":
    main()
