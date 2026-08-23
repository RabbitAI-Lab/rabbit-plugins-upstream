#!/usr/bin/env python3
"""
[1] COT REPORT (CFTC) — managed-money / speculative positioning in gold futures.
Smart-money proxy: net long build = bullish confirmation; extreme net long = crowded.
DATA-FIRST: CFTC publishes current files under /dea/newcot/*.txt (legacy deacmesf.txt
is retired/404). Gold = code 088691 (CMX). We parse the disaggregated/legacy columns.
If the live file is unreachable we fall back to Firecrawl-scraped tradingeconomics
(requires FIRECRAWL_KEY), else UNVERIFIED (never fake).
Output JSON: {source, status, report_date, net_managed_money, change, interpretation}
"""
import re, json, os
from ds_util import fetch, cache_get, cache_put

FIRECRAWL_KEY = os.environ.get("FIRECRAWL_KEY", "")
CANDIDATES = [
    "https://www.cftc.gov/dea/newcot/deafut.txt",     # gold futures (CMX)
    "https://www.cftc.gov/dea/newcot/f_disagg.txt",   # financial disaggregated
    "https://www.cftc.gov/dea/newcot/c_disagg.txt",
]
GOLD_CODE = "088691"

def parse_cftc(txt):
    """Return (report_date, net_managed_money, total_long, total_short) for gold row.
    CFTC combined file columns (after '...,088691,CMX,01,088,'):
      noncommercial long, short | commercial long, short |
      nonreportable long, short | ...
    We approximate 'speculative' net = (noncommercial + nonreportable) long - short.
    """
    for line in txt.splitlines():
        if GOLD_CODE not in line:
            continue
        dm = re.search(r"(20\d{2}-\d{2}-\d{2})", line)
        date = dm.group(1) if dm else None
        # the 6 position figures appear right after the code block, each as a
        # space-padded integer; grab the first 6 integers >= 1000 in order.
        ints = [int(m.group(1)) for m in re.finditer(r"(\d{4,7})", line)]
        if len(ints) >= 6:
            ncL, ncS, cL, cS, nrL, nrS = ints[0], ints[1], ints[2], ints[3], ints[4], ints[5]
            net_spec = (ncL + nrL) - (ncS + nrS)
            return date, net_spec, (ncL + cL + nrL), (ncS + cS + nrS)
    return None

def run():
    cached = cache_get("cot", 86400)  # weekly
    if cached: return cached
    # Attempt 1: live CFTC newcot files
    for url in CANDIDATES:
        try:
            txt = fetch(url, 25)
            res = parse_cftc(txt)
            if res:
                date, net, tot_l, tot_s = res
                interp = "bullish" if net > 0 else "bearish"
                out = {"source": "cftc(newcot)", "status": "OK", "report_date": date,
                       "net_managed_money": net, "total_long": tot_l, "total_short": tot_s,
                       "interpretation": interp}
                cache_put("cot", out); return out
        except Exception:
            continue
    # Attempt 2: Firecrawl-scraped tradingeconomics
    if FIRECRAWL_KEY:
        try:
            import urllib.request
            body = json.dumps({"url":"https://tradingeconomics.com/commodity/gold-cot","formats":["markdown"]}).encode()
            req = urllib.request.Request("https://api.firecrawl.dev/v1/scrape",
                data=body, headers={"Authorization":f"Bearer {FIRECRAWL_KEY}","Content-Type":"application/json"})
            md = json.loads(urllib.request.urlopen(req, timeout=25).read().decode()).get("data",{}).get("markdown","")
            m = re.search(r"(?:net position|managed money)[^0-9]{0,40}(-?[\d,]+)", md, re.I)
            if m:
                net = int(m.group(1).replace(",",""))
                out = {"source":"tradingeconomics(firecrawl)","status":"OK","net_position":net,
                       "interpretation":"bullish" if net>0 else "bearish"}
                cache_put("cot", out); return out
        except Exception:
            pass
    return {"source":"cftc","status":"UNVERIFIED",
            "reason":"CFTC newcot unreachable + no Firecrawl key",
            "note":"Weekly smart-money filter — non-blocking for daily analysis."}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
