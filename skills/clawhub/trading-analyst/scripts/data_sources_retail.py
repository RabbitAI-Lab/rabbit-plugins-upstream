#!/usr/bin/env python3
"""
[6] RETAIL / MARKET SENTIMENT — contrarian + fear-greed gauge.
Priority (free-first, data-first):
  1) Myfxbook community outlook (true retail positioning) — needs Firecrawl/key in this env
  2) Fear & Greed Index (alternative.me, FREE, no key) — broad market sentiment proxy
When Myfxbook is blocked, Fear & Greed keeps the layer VERIFIED (honest proxy,
not pure retail positioning — labeled as such).
Output JSON: {source, status, value, classification, interpretation}
"""
import re, json, os
from ds_util import fetch, cache_get, cache_put

FIRECRAWL_KEY = os.environ.get("FIRECRAWL_KEY", "")
FNG_URL = "https://api.alternative.me/fng/?limit=1"

def run():
    cached = cache_get("retail", 3600)
    if cached: return cached
    # --- attempt 1: Myfxbook true retail (via Firecrawl if key present) ---
    if FIRECRAWL_KEY:
        try:
            import urllib.request
            body = json.dumps({"url":"https://www.myfxbook.com/community/outlook","formats":["markdown"]}).encode()
            req = urllib.request.Request("https://api.firecrawl.dev/v1/scrape",
                data=body, headers={"Authorization":f"Bearer {FIRECRAWL_KEY}","Content-Type":"application/json"})
            r = urllib.request.urlopen(req, timeout=25).read().decode()
            md = json.loads(r).get("data",{}).get("markdown","")
            m = re.search(r"XAUUSD.*?(\d{1,3})\s*%.*?(\d{1,3})\s*%", md, re.S)
            if m:
                out = {"source":"myfxbook(firecrawl)","status":"OK",
                       "xau_long_pct":int(m.group(1)),"xau_short_pct":int(m.group(2)),
                       "interpretation":"contrarian_ok" if int(m.group(1))<70 else "retail_crowded_long"}
                cache_put("retail", out); return out
        except Exception:
            pass
    # --- attempt 2: Fear & Greed (FREE, no key) ---
    try:
        t = fetch(FNG_URL, 15)
        d = json.loads(t)
        v = d["data"][0]
        val = int(v["value"]); cls = v["value_classification"]
        interp = "fear_gold_bid" if val < 45 else ("extreme_greed_caution" if val > 75 else "neutral_sentiment")
        out = {"source":"alternative.me(Fear&Greed)","status":"OK","value":val,
               "classification":cls,"interpretation":interp,
               "note":"free market-sentiment proxy; Myfxbook true-retail needs FIRECRAWL_KEY"}
        cache_put("retail", out); return out
    except Exception as e:
        return {"source":"retail","status":"UNVERIFIED","reason":f"Fear&Greed failed: {e}"}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
