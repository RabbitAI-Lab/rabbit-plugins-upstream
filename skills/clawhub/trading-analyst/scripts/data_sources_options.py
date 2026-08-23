#!/usr/bin/env python3
"""
[5] OPTIONS POSITIONING — CBOE put/call ratio (broad risk sentiment).
Gold-specific options OI (GC=F chain) is 401-gated without key; CBOE's public
put/call ratio is free and a proven fear gauge: high P/C = risk-off = gold bid.
CBOE page is JS-rendered but embeds a JSON with escaped quotes:
  \"TOTAL PUT/CALL RATIO\",\"value\":\"0.72\"
Output JSON: {source, pcr_total, status, gold_interpretation}
"""
import re, json
from ds_util import fetch, cache_get, cache_put

URL = "https://www.cboe.com/us/options/market_statistics/daily/?mkt=cone"

def run():
    cached = cache_get("options", 3600)
    if cached: return cached
    try:
        t = fetch(URL, 20)
    except Exception as e:
        return {"source":"cboe","status":"UNVERIFIED","reason":str(e)}
    # CBOE embeds JSON with escaped quotes; unescape so we can match normally.
    un = t.replace('\\"', '"')
    pcr = None
    m = re.search(r'"TOTAL PUT/CALL RATIO"[^}]*?"value"\s*:\s*"(\d+\.\d+)"', un, re.I)
    if m:
        try: pcr = float(m.group(1))
        except ValueError: pcr = None
    # fallback: plain HTML table row
    if pcr is None:
        m2 = re.search(r'TOTAL PUT/CALL RATIO</td>\s*<td[^>]*>(\d+\.\d+)</td>', t, re.I)
        if m2:
            try: pcr = float(m2.group(1))
            except ValueError: pcr = None
    if pcr is None:
        return {"source":"cboe","status":"UNVERIFIED","reason":"no ratio parsed"}
    interp = "fear_high_gold_bid" if pcr > 1.0 else ("complacency_gold_vulnerable" if pcr < 0.7 else "balanced")
    out = {"source":"cboe","status":"OK","pcr_total":pcr,"gold_interpretation":interp}
    cache_put("options", out)
    return out

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
