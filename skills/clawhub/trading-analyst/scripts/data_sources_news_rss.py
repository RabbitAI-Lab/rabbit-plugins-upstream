#!/usr/bin/env python3
"""
[4] NEWS SENTIMENT (NLP) — FXStreet + Investing RSS.
Reads article titles/descriptions, scores bull/bear keywords for GOLD/USD/Fed/rates.
Returns gold_bias + score + top headlines. Complements FXStreet calendar (news_check.py).
Graceful: if both RSS fail -> UNVERIFIED.
"""
import urllib.request, json, re
from ds_util import fetch, cache_get, cache_put, simple_sentiment

FEEDS = {
    "investing": "https://www.investing.com/rss/news.rss",
    "fxstreet": "https://www.fxstreet.com/rss/news",
    "dailyfx": "https://www.dailyfx.com/rss",
}
BULL = ["gold rises","gold gains","gold jumps","gold climbs","fed dovish","rate cut","easing",
        "dovish","weak dollar","dollar falls","safe haven","geopolitical","stimulus","inflation hedge",
        "gold bull","record high gold","buy gold","bullion"]
BEAR = ["gold falls","gold drops","gold slides","gold weakens","fed hawkish","rate hike","hawkish",
        "strong dollar","dollar rises","sell gold","gold bear","profit taking","outflow","tightening"]

def parse_rss(xml):
    items = re.findall(r"<item>(.*?)</item>", xml, re.S) or re.findall(r"<entry>(.*?)</entry>", xml, re.S)
    out = []
    for it in items[:15]:
        title = re.search(r"<title[^>]*>(.*?)</title>", it, re.S)
        desc = re.search(r"<description[^>]*>(.*?)</description>", it, re.S)
        def cdata(t):
            if not t: return ""
            m = re.search(r"<!\[CDATA\[(.*?)\]\]>", t, re.S)
            if m: t = m.group(1)
            return re.sub(r"<[^>]+>", "", t).strip()
        t = cdata(title.group(1)) if title else ""
        d = cdata(desc.group(1)) if desc else ""
        text = t or d
        if text:
            out.append(text[:200])
    return out

def run():
    cached = cache_get("news_rss", 900)  # 15 min
    if cached: return cached
    heads = []
    per_feed = {}
    for name, url in FEEDS.items():
        try:
            xml = fetch(url, 15)
            items = parse_rss(xml)
            per_feed[name] = "ok" if items else "empty"
            heads.extend(items)
        except Exception as e:
            per_feed[name] = f"FAIL:{type(e).__name__}"
    if not heads:
        return {"source":"rss","status":"UNVERIFIED","reason":"all feeds failed","per_feed":per_feed}
    blob = " ".join(heads)
    bias, score = simple_sentiment(blob, BULL, BEAR)
    # gold-specific: count gold mentions vs fed/dollar
    gold_mentions = len(re.findall(r"gold|bullion|xau", blob, re.I))
    out = {
        "source":"rss","status":"OK","gold_bias":bias,"score":score,
        "gold_mentions":gold_mentions,"headlines_total":len(heads),
        "top_headlines": heads[:8],
        "per_feed_status":{k:("ok" if isinstance(v,list) else v) for k,v in per_feed.items()},
    }
    cache_put("news_rss", out)
    return out

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
