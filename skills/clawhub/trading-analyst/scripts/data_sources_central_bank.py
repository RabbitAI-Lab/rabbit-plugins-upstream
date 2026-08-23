#!/usr/bin/env python3
"""
[7] CENTRAL BANK GOLD BUYING — World Bank total reserves (FI.RES.TOTL.CD)
proxy for major holders (USA, CHN, RUS, IND, TUR, POL).
Note: WB has no gold-only (FR.RES.GOLD.CD) free series; we track total
official reserves of the top gold holders as a structural-demand proxy and
flag whether the trend is accumulation (gold bid) or drawdown.
Output JSON: {source, status, holders:[{code,year,usd_billions,trend}], aggregate_trend}
"""
import json
from ds_util import fetch, cache_get, cache_put

HOLDERS = ["USA", "CHN", "RUS", "IND", "TUR", "POL"]
URL = "https://api.worldbank.org/v2/country/{c}/indicator/FI.RES.TOTL.CD?format=json&per_page=6&date=2018:2024"

def run():
    cached = cache_get("central_bank", 86400)
    if cached: return cached
    holders = []
    for c in HOLDERS:
        try:
            d = json.loads(fetch(URL.format(c=c), 20))
            rows = [r for r in (d[1] or []) if r.get("value") is not None]
            if not rows: continue
            rows.sort(key=lambda r: r["date"])
            vals = [r["value"] for r in rows[-3:]]
            trend = "rising" if vals[-1] > vals[0] else ("falling" if vals[-1] < vals[0] else "flat")
            holders.append({"code": c, "year": rows[-1]["date"],
                            "usd_billions": round(rows[-1]["value"]/1e9, 1), "trend": trend})
        except Exception:
            pass
    if not holders:
        return {"source": "worldbank", "status": "UNVERIFIED", "reason": "no holder data"}
    ag = "rising" if sum(1 for h in holders if h["trend"] == "rising") >= len(holders)//2 else "mixed"
    out = {"source": "worldbank", "status": "OK", "holders": holders, "aggregate_trend": ag,
           "note": "proxy via total official reserves (gold-only series unavailable free)"}
    cache_put("central_bank", out)
    return out

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
