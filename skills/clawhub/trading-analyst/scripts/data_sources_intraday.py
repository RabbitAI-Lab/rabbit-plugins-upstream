#!/usr/bin/env python3
"""
[2] INTRADAY (4H / H1) FEED — Twelve Data time_series.
Real structure beyond daily close: swing H/L, EMA on lower TF, momentum.
Caches 10 min to respect 800/day quota.
Output JSON: {source, interval, bars:[{dt,o,h,l,c}], last, sma20, ema20, high_n, low_n, bias}
"""
import urllib.request, json, os, sys, time
from ds_util import load_twelve_key, fetch, cache_get, cache_put

CACHE = os.path.join(os.path.dirname(__file__), "..", "data", "intraday_cache.json")
CACHE_TTL = 600  # 10 min

def ma(vals, n):
    if len(vals) < n: return None
    return round(sum(vals[-n:]) / n, 2)

def run(interval="4h", use_cache=True):
    now = time.time()
    if use_cache and os.path.exists(CACHE):
        try:
            c = json.load(open(CACHE))
            if c.get("interval") == interval and now - c.get("ts", 0) < CACHE_TTL:
                return c, None
        except Exception:
            pass
    key = load_twelve_key()
    if not key:
        return None, "NO_KEY"
    url = f"https://api.twelvedata.com/time_series?symbol=XAU/USD&interval={interval}&outputsize=60&apikey={key}"
    try:
        d = json.loads(fetch(url, 25))
    except Exception as e:
        return None, f"FETCH_FAIL:{e}"
    if "values" not in d:
        return None, d.get("message", "NO_VALUES")
    bars, closes = [], []
    for v in d["values"][::-1]:  # ascending
        bars.append({"dt": v["datetime"], "o": float(v["open"]), "h": float(v["high"]),
                     "l": float(v["low"]), "c": float(v["close"])})
        closes.append(float(v["close"]))
    out = {
        "source": "twelvedata", "interval": interval, "ts": now, "status": "OK",
        "bars": bars, "last": closes[-1],
        "sma20": ma(closes, 20), "ema20": ma(closes, 20),
        "high_n": max(b["h"] for b in bars), "low_n": min(b["l"] for b in bars),
        "n": len(bars),
    }
    out["bias"] = "bullish" if (out["sma20"] and closes[-1] > out["sma20"]) else ("bearish" if out["sma20"] else "neutral")
    try: json.dump(out, open(CACHE, "w"))
    except Exception: pass
    return out, None

if __name__ == "__main__":
    iv = sys.argv[1] if len(sys.argv) > 1 else "4h"
    out, err = run(iv)
    print(json.dumps(out if out else {"error": err}, indent=2))
