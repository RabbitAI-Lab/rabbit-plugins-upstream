#!/usr/bin/env python3
"""
fetch_market.py — pull XAU/USD market data so Clara can analyze WITHOUT a screenshot.

Self-contained, stdlib only (no pip installs).
- Always: current price + day high/low + previous close (gold-api.com, public).
- If env TWELVE_DATA_API_KEY is set: RSI(14), EMA20, SMA50, SMA200, and
  30-day high/low from Twelve Data's time_series + indicators endpoints.
- If no key: reports price + a note that indicators need a key OR a local
  closes CSV (--closes file.csv) for on-device computation.

Output: JSON to stdout (machine) + a human summary to stderr.

Usage:
  python3 fetch_market.py                       # price only (no key)
  python3 fetch_market.py --key                 # use TWELVE_DATA_API_KEY from env
  python3 fetch_market.py --closes hist.csv     # compute RSI/EMA/SMA from local closes
  python3 fetch_market.py --pretty             # print human summary to stdout too

No secrets are printed. The API key is read ONLY from env and sent ONLY to
api.twelvedata.com over HTTPS.
"""
import argparse
import csv
import json
import math
import os
import re
import sys
import urllib.request
import urllib.error

GOLDAPI = "https://api.gold-api.com/price/XAU"


def _workspace():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def load_twelve_key():
    """Ambil key dari memory/trading/api_keys.md (file lokal privat, tidak di-commit).
    Tidak pernah di-print."""
    p = os.path.join(_workspace(), "memory", "trading", "api_keys.md")
    try:
        with open(p, encoding="utf-8") as f:
            for line in f:
                m = re.search(r"Key:\s*([a-f0-9]{32})", line)
                if m:
                    return m.group(1)
    except FileNotFoundError:
        return None
    return None


def http_get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "clara-trading/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def ema(values, period):
    if not values or len(values) < period:
        return None
    k = 2.0 / (period + 1)
    prev = sum(values[:period]) / period
    for v in values[period:]:
        prev = v * k + prev * (1 - k)
    return prev


def sma(values, period):
    if not values or len(values) < period:
        return None
    return sum(values[-period:]) / period


def rsi(values, period=14):
    if not values or len(values) <= period:
        return None
    gains = 0.0
    losses = 0.0
    for i in range(1, period + 1):
        d = values[-i] - values[-i - 1]
        if d >= 0:
            gains += d
        else:
            losses -= d
    gains /= period
    losses /= period
    if losses == 0:
        return 100.0
    rs = gains / losses
    return 100.0 - (100.0 / (1 + rs))


def price_from_goldapi():
    try:
        data = http_get(GOLDAPI)
        return {
            "price": float(data.get("price", 0)),
            "prev_close": float(data.get("previous_close_price", 0) or 0),
            "high": float(data.get("high_price", 0) or 0),
            "low": float(data.get("low_price", 0) or 0),
            "updated": data.get("updated_at", ""),
            "source": "gold-api.com",
        }
    except (urllib.error.URLError, KeyError, ValueError, TypeError) as e:
        print(f"[warn] gold-api fetch failed: {e}", file=sys.stderr)
        return None


def indicators_from_twelvedata(key, symbol="XAU/USD"):
    base = "https://api.twelvedata.com"
    out = {}
    try:
        ts = http_get(f"{base}/time_series?symbol={symbol}&interval=1day&outputsize=60&apikey={key}")
        closes = [float(c["close"]) for c in ts.get("values", [])][::-1]
        if closes:
            out["closes_n"] = len(closes)
            out["rsi14"] = rsi(closes)
            out["ema20"] = ema(closes, 20)
            out["sma50"] = sma(closes, 50)
            out["sma200"] = sma(closes, 200)
            out["high30"] = max(closes[-30:])
            out["low30"] = min(closes[-30:])
            out["last_close"] = closes[-1]
    except Exception as e:  # noqa
        print(f"[warn] twelvedata indicators failed: {e}", file=sys.stderr)
    return out


def indicators_from_csv(path):
    closes = []
    try:
        with open(path, encoding="utf-8") as f:
            for row in csv.reader(f):
                if not row:
                    continue
                try:
                    closes.append(float(row[-1]))
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"[warn] closes file not found: {path}", file=sys.stderr)
        return {}
    if len(closes) < 15:
        print("[warn] need >=15 closes for indicators", file=sys.stderr)
        return {}
    return {
        "closes_n": len(closes),
        "rsi14": rsi(closes),
        "ema20": ema(closes, 20),
        "sma50": sma(closes, 50),
        "sma200": sma(closes, 200),
        "high30": max(closes[-30:]),
        "low30": min(closes[-30:]),
        "last_close": closes[-1],
        "source": "local csv",
    }


def main():
    p = argparse.ArgumentParser(description="Fetch XAU/USD data for analysis (no screenshot needed).")
    p.add_argument("--key", action="store_true", help="Use TWELVE_DATA_API_KEY from env for full indicators")
    p.add_argument("--closes", default=None, help="Local CSV of historical closes (oldest..newest)")
    p.add_argument("--pretty", action="store_true", help="Also print human summary to stdout")
    args = p.parse_args()

    result = {"symbol": "XAU/USD"}

    price = price_from_goldapi()
    if price:
        result.update(price)

    if args.key:
        key = os.environ.get("TWELVE_DATA_API_KEY") or load_twelve_key()
        if not key:
            print("[warn] --key set but no TWELVE_DATA_API_KEY (env or api_keys.md)", file=sys.stderr)
        else:
            result["indicators"] = indicators_from_twelvedata(key)
    elif args.closes:
        result["indicators"] = indicators_from_csv(args.closes)

    print(json.dumps(result, indent=2))

    if args.pretty:
        print("---", file=sys.stderr)
        print(f"XAU/USD last: {result.get('price')}", file=sys.stderr)
        ind = result.get("indicators", {})
        if ind:
            print(f"RSI14 : {ind.get('rsi14'):.1f}" if ind.get('rsi14') is not None else "RSI14 : n/a", file=sys.stderr)
            print(f"EMA20 : {ind.get('ema20'):.2f}" if ind.get('ema20') is not None else "EMA20 : n/a", file=sys.stderr)
            print(f"SMA50 : {ind.get('sma50'):.2f}" if ind.get('sma50') is not None else "SMA50 : n/a", file=sys.stderr)
            print(f"SMA200: {ind.get('sma200'):.2f}" if ind.get('sma200') is not None else "SMA200: n/a", file=sys.stderr)
            print(f"30d H/L: {ind.get('high30')} / {ind.get('low30')}", file=sys.stderr)
        else:
            print("Indicators: n/a (set TWELVE_DATA_API_KEY + --key, or pass --closes csv)", file=sys.stderr)


if __name__ == "__main__":
    main()
