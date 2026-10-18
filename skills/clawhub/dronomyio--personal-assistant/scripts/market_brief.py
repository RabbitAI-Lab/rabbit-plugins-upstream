#!/usr/bin/env python3
"""Market news + analysis brief generator (stdlib only).

Usage:
    python3 market_brief.py <us|india> <morning|midday|close|futures>

Data sources (keyless, never invented):
  - Yahoo Finance chart API for index/futures/commodity/FX/crypto quotes
  - Google News RSS for topic headlines per block
  - ~/workspace/briefs/{us,india}/latest.json for watchlist movers (with driver headlines)

Output:
  ~/workspace/briefs/markets/<market>/<slot>-<STAMP>.json
  ~/workspace/briefs/markets/<market>/latest-<slot>.json

Schema:
  {generated_at, market, slot, numbers: [{label, value, chg_pct}],
   blocks: {macro|oil|currency|crypto|sectors: {headlines: [{title, source, published, url}]}},
   movers: {gainers: [...], losers: [...]},  # {ticker, price, chg_pct, driver}
   watch_today: [...],                        # best-effort, clearly labeled
   notes: [...]}

"GIFT Nifty": Yahoo has no reliable symbol. It is stated from RSS context or
marked "unavailable" — never faked.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

BASE = Path.home() / "workspace" / "briefs"
OUT = BASE / "markets"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

# (label, yahoo_symbol)
US_NUMBERS = [
    ("S&P 500", "^GSPC"),
    ("Dow", "^DJI"),
    ("Nasdaq", "^IXIC"),
    ("S&P Futures (ES)", "ES=F"),
    ("Nasdaq Futures (NQ)", "NQ=F"),
    ("WTI Crude", "CL=F"),
    ("Brent", "BZ=F"),
    ("Dollar Index", "DX-Y.NYB"),
    ("VIX", "^VIX"),
    ("Bitcoin", "BTC-USD"),
    ("Ethereum", "ETH-USD"),
    ("Semis (SMH)", "SMH"),
    ("Tech (XLK)", "XLK"),
    ("Energy (XLE)", "XLE"),
    ("Financials (XLF)", "XLF"),
]

INDIA_NUMBERS = [
    ("Nifty 50", "^NSEI"),
    ("Sensex", "^BSESN"),
    ("Bank Nifty", "^NSEBANK"),
    ("USD/INR", "USDINR=X"),
    ("WTI Crude", "CL=F"),
    ("Brent", "BZ=F"),
    ("Bitcoin", "BTC-USD"),
    ("Gold", "GC=F"),
]

# block -> list of RSS query strings
US_TOPICS = {
    "macro": ["Federal Reserve interest rates news", "US inflation CPI news"],
    "oil": ["crude oil price WTI Brent news"],
    "currency": ["US dollar index news"],
    "crypto": ["bitcoin price news", "crypto market news"],
    "sectors": ["AI chips semiconductors stocks news", "stock market today analysis"],
}

INDIA_TOPICS = {
    "macro": ["RBI interest rate news", "India economy inflation news"],
    "oil": ["crude oil prices India news"],
    "currency": ["rupee dollar exchange rate news"],
    "crypto": ["bitcoin price news"],
    "sectors": ["Nifty Sensex market analysis", "Indian stock market sectors news"],
}


def fetch_quote(symbol, timeout=20):
    """Last two daily closes -> price + % change. Returns None on failure."""
    url = ("https://query1.finance.yahoo.com/v8/finance/chart/"
           + urllib.parse.quote(symbol, safe="") + "?interval=1d&range=5d")
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.loads(r.read().decode())
        res = d["chart"]["result"][0]
        closes = [c for c in (res["indicators"]["quote"][0].get("close") or []) if c]
        if len(closes) < 2:
            return None
        last, prev = closes[-1], closes[-2]
        return {"value": round(last, 2),
                "chg_pct": round((last - prev) / prev * 100, 2)}
    except Exception:
        return None


def fetch_rss_headlines(query, timeout=15, limit=5, gl="US"):
    """Keyless Google News RSS. Never raises; empty on failure."""
    url = ("https://news.google.com/rss/search?q=" + urllib.parse.quote(query)
           + f"&hl=en-US&gl={gl}&ceid={gl}:en")
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            root = ET.fromstring(r.read().decode())
        out = []
        for it in root.findall(".//item")[:limit]:
            src = it.find("source")
            out.append({
                "title": (it.findtext("title") or "")[:200],
                "source": src.text if src is not None else "",
                "published": it.findtext("pubDate") or "",
                "url": it.findtext("link") or "",
            })
        time.sleep(0.2)
        return out
    except Exception:
        return []


def load_movers(market, top_n=5):
    """Top gainers/losers from the latest watchlist brief, with driver headlines."""
    try:
        payload = json.loads((BASE / market / "latest.json").read_text())
    except Exception:
        return {"gainers": [], "losers": []}
    movers = payload.get("top_movers", [])
    gainers, losers = [], []
    for m in movers:
        news = m.get("news") or []
        driver = news[0]["title"] if news else "no fresh headline"
        entry = {"ticker": m.get("ticker"), "price": m.get("price"),
                 "chg_pct": m.get("chg_pct"), "driver": driver}
        (gainers if m.get("chg_pct", 0) >= 0 else losers).append(entry)
    return {"gainers": gainers[:top_n], "losers": losers[:top_n]}


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("us", "india") \
            or sys.argv[2] not in ("morning", "midday", "close", "futures"):
        print("usage: market_brief.py <us|india> <morning|midday|close|futures>",
              file=sys.stderr)
        sys.exit(1)
    market, slot = sys.argv[1], sys.argv[2]

    numbers_spec = US_NUMBERS if market == "us" else INDIA_NUMBERS
    numbers = []
    for label, sym in numbers_spec:
        q = fetch_quote(sym)
        time.sleep(0.2)
        if q:
            numbers.append({"label": label, "value": q["value"],
                            "chg_pct": q["chg_pct"]})
        else:
            numbers.append({"label": label, "value": None,
                            "chg_pct": None, "status": "unavailable"})

    topics = US_TOPICS if market == "us" else INDIA_TOPICS
    gl = "US" if market == "us" else "IN"
    blocks = {}
    for block, queries in topics.items():
        seen, heads = set(), []
        for qstr in queries:
            for h in fetch_rss_headlines(qstr, gl=gl):
                key = h["title"].lower()
                if key not in seen and len(heads) < 5:
                    seen.add(key)
                    heads.append(h)
        blocks[block] = {"headlines": heads}

    # watch_today: macro-event flavor from the macro block (best effort, labeled)
    watch_today = [
        {"text": h["title"], "source": h["source"], "url": h["url"],
         "note": "headline-derived; verify before acting"}
        for h in blocks["macro"]["headlines"][:5]
    ]

    movers = load_movers(market)

    notes = []
    if market == "india":
        notes.append("GIFT Nifty futures: Yahoo has no reliable quote symbol; "
                     "overnight view inferred from RSS context only — no number shown.")
    if any(n.get("status") == "unavailable" for n in numbers):
        missing = [n["label"] for n in numbers if n.get("status") == "unavailable"]
        notes.append("Quote fetch failed for: " + ", ".join(missing)
                     + " — marked unavailable, not estimated.")

    payload = {
        "market": market,
        "slot": slot,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "numbers": numbers,
        "blocks": blocks,
        "movers": movers,
        "watch_today": watch_today,
        "notes": notes,
    }
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
    d = OUT / market
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{slot}-{stamp}.json").write_text(json.dumps(payload, indent=1))
    (d / f"latest-{slot}.json").write_text(json.dumps(payload, indent=1))
    ok = sum(1 for n in numbers if n.get("value") is not None)
    heads = sum(len(b["headlines"]) for b in blocks.values())
    print(f"markets/{market} {slot}: {ok}/{len(numbers)} quotes, "
          f"{heads} headlines, "
          f"+{len(movers['gainers'])}/-{len(movers['losers'])} movers")


if __name__ == "__main__":
    main()
