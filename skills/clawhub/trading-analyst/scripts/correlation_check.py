#!/usr/bin/env python3
"""
correlation_check.py — ISI GAP KORELASI (DXY / US10Y / SPX) secara GRATIS.

Fakta: Twelve Data FREE tier TIDAK punya DXY / US10Y / SPX / XAG (semua 404 /
paywalled). Makanya filter korelasi di skill selalu "NOT fetched". Tool ini ambil
dari Yahoo Finance (publik, gratis, tanpa API key) supaya gap tertutup.

Logika korelasi emas (dokumentasi di SKILL.md):
  - DXY     naik  -> emas cenderung TURUN  (inverse)
  - US10Y   naik  -> emas cenderung TURUN  (real yield naik)
  - SPX     naik  -> risk-on -> emas cenderung TURUN (inverse di risk-on)
  - SPX     turun -> risk-off -> emas cenderung NAIK (safe haven)

Output: JSON ke stdout + ringkasan manusia ke stderr.
  - macro_score : -3..+3  (jumlah sinyal bullish makro buat emas)
  - macro_bias   : "bullish"/"bearish"/"neutral" (vs emas)
  - filter       : "CONFIRM" / "NEUTRAL" / "CONFLICT"  vs price_bias yang dikasih
  - per-instrumen: arah + perubahan harian (%)

Usage:
  python3 correlation_check.py
  python3 correlation_check.py --price-bias bullish
  python3 correlation_check.py --pretty

No secrets, no destructive ops. Hanya fetch Yahoo + print.
"""
import argparse
import json
import sys
import urllib.request
import urllib.error

YAHOO = "https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=5d"
# (label, yahoo_symbol, arah_vs_emas)
INSTRUMENTS = [
    ("DXY",   "DX-Y.NYB", "inverse"),
    ("US10Y", "^TNX",     "inverse"),   # ^TNX = yield 10Y dalam %, inverse ke emas
    ("SPX",   "^GSPC",    "inverse_riskon"),
    ("XAG",   "SI=F",     "beta"),      # silver sbg beta emas (proxy GSR)
]


def fetch_yahoo(sym):
    url = YAHOO.format(sym=sym)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode("utf-8"))
        res = d.get("chart", {}).get("result")
        if not res:
            return None
        m = res[0]["meta"]
        price = m.get("regularMarketPrice")
        prev = m.get("previousClose") or m.get("chartPreviousClose")
        if price is None or prev in (None, 0):
            return None
        chg = (price - prev) / prev * 100.0
        return {"price": price, "prev": prev, "chg_pct": chg}
    except (urllib.error.URLError, KeyError, ValueError, TypeError, IndexError) as e:
        print(f"[warn] {sym} fetch failed: {e}", file=sys.stderr)
        return None


def main():
    p = argparse.ArgumentParser(description="Gold intermarket correlation filter (free, Yahoo).")
    p.add_argument("--price-bias", default=None,
                   choices=["bullish", "bearish", "neutral"],
                   help="Price-based bias from S&R+S/D analysis, to compare with macro.")
    p.add_argument("--pretty", action="store_true", help="Print human summary to stdout too.")
    args = p.parse_args()

    macro_score = 0
    detail = {}
    for label, sym, rel in INSTRUMENTS:
        d = fetch_yahoo(sym)
        if not d:
            detail[label] = {"available": False}
            continue
        up = d["chg_pct"] > 0
        # Tentukan apakah instrumen ini BULLISH atau BEARISH buat emas
        if rel == "inverse":
            gold_bull = not up          # instrumen naik -> emas turun
        elif rel == "inverse_riskon":
            gold_bull = not up          # SPX naik (risk-on) -> emas turun
        else:  # beta
            gold_bull = up              # silver naik -> emas cenderung naik
        macro_score += 1 if gold_bull else -1
        detail[label] = {
            "available": True,
            "price": round(d["price"], 4),
            "chg_pct": round(d["chg_pct"], 2),
            "direction": "up" if up else "down",
            "gold_bias": "bullish" if gold_bull else "bearish",
        }

    if macro_score > 0:
        macro_bias = "bullish"
    elif macro_score < 0:
        macro_bias = "bearish"
    else:
        macro_bias = "neutral"

    filt = "NEUTRAL"
    if args.price_bias and args.price_bias != "neutral":
        if macro_bias == args.price_bias:
            filt = "CONFIRM"
        elif macro_bias != "neutral":
            filt = "CONFLICT"

    out = {
        "macro_score": macro_score,
        "macro_bias": macro_bias,
        "filter_vs_price_bias": filt,
        "price_bias_input": args.price_bias,
        "detail": detail,
    }
    print(json.dumps(out, indent=2))
    if args.pretty:
        print("---", file=sys.stderr)
        print(f"Macro score (emas): {macro_score:+d}  -> {macro_bias.upper()}", file=sys.stderr)
        print(f"Filter vs price bias '{args.price_bias}': {filt}", file=sys.stderr)
        for k, v in detail.items():
            if v.get("available"):
                print(f"  {k:6} {v['price']:>10} ({v['chg_pct']:+.2f}%) -> emas {v['gold_bias']}",
                      file=sys.stderr)
            else:
                print(f"  {k:6} n/a", file=sys.stderr)


if __name__ == "__main__":
    main()
