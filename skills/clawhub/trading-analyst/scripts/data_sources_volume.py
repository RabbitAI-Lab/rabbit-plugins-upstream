#!/usr/bin/env python3
"""
[3] VOLUME / ORDER FLOW — Yahoo GC=F (COMEX gold futures) daily volume.
Cross-source vs CSV volume. Used to validate S/D zone strength:
high-volume departure = fresh strong zone; low-volume move = suspect.
Output JSON: {source, last_volume, avg_volume_20, volume_trend, signature}
"""
import urllib.request, json, os, sys
from ds_util import fetch, cache_get, cache_put

SYM = "GC=F"
def fetch_series(range="3mo", interval="1d"):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{SYM}?range={range}&interval={interval}"
    d = json.loads(fetch(url, 20))
    r = d["chart"]["result"][0]
    vol = r["indicators"].get("quote", [{}])[0].get("volume", [])
    ts = r.get("timestamp", [])
    closes = r["indicators"].get("quote",[{}])[0].get("close", [])
    return [v for v in vol if v is not None], closes

def run():
    cached = cache_get("volume", 3600)
    if cached: return cached
    vols, closes = fetch_series()
    if not vols:
        return {"source":"yahoo", "status":"UNVERIFIED", "reason":"no volume"}
    last = vols[-1]
    avg20 = sum(vols[-20:]) / len(vols[-20:])
    # volume trend: last 5d avg vs prior 15d
    recent = sum(vols[-5:]) / 5
    prior = sum(vols[-20:-5]) / 15
    trend = "rising" if recent > prior * 1.05 else ("falling" if recent < prior * 0.95 else "flat")
    # signature: volume + price direction last bar
    if len(closes) >= 2:
        up = closes[-1] >= closes[-2]
        sig = ("volume_up_on_" + ("rise" if up else "fall")) if last > avg20 else ("volume_low_on_" + ("rise" if up else "fall"))
    else:
        sig = "n/a"
    # honesty: Yahoo COMEX gold future volume is often sparse/zero on some bars;
    # flag if last volume is implausibly low vs its own 20d average.
    low_flag = last < avg20 * 0.3
    out = {
        "source": "yahoo", "symbol": SYM, "status": "OK",
        "last_volume": int(last), "avg20": int(avg20),
        "volume_vs_avg": round(last / avg20, 2),
        "volume_trend": trend, "signature": sig,
        "warn_low_volume": low_flag,
    }
    cache_put("volume", out)
    return out

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
