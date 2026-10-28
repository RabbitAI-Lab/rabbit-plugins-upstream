#!/usr/bin/env python3
"""Market brief engine v1 — price/volume movers scan (stdlib only).

Data: Yahoo Finance chart API (no key needed). Reads tickers from
~/workspace/news-assistant/watchlist.md ("## US stocks" / "## Indian stocks"
sections; entries may carry share quantities like "TICKER1 (40)").

Output: ~/workspace/briefs/<market>/<STAMP>.json and latest.json with
top movers (>=2% move or >=2x average volume), full snapshot, and any
unresolved tickers.

Usage:
    python3 brief_engine.py --market us|india [--tickers AAPL,MSFT] [--top 20]
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

BASE = Path.home() / "workspace" / "briefs"
WATCH = Path.home() / "workspace" / "news-assistant" / "watchlist.md"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}


def load_tickers(market):
    sec = "US stocks" if market == "us" else "Indian stocks"
    text = WATCH.read_text()
    items, cur = [], None
    for line in text.splitlines():
        m = re.match(r"##(?!#)\s+(.+)", line)
        if m:
            cur = m.group(1).strip()
        elif cur and cur.startswith(sec) and re.match(r"\s*-\s+", line):
            item = re.sub(r"^\s*-\s+", "", line).strip()
            if not item or item.startswith("_") or "_(" in item:
                continue
            for p in item.split(","):
                p = p.strip()
                if not p:
                    continue
                mm = re.match(r"([A-Za-z0-9.\-]+)(?:\s*\((\d+)[^)]*\))?", p)
                if mm:
                    items.append({
                        "ticker": mm.group(1),
                        "qty": int(mm.group(2)) if mm.group(2) else None,
                    })
    return items


def fetch_quote(symbol, timeout=20):
    url = ("https://query1.finance.yahoo.com/v8/finance/chart/"
           + urllib.parse.quote(symbol, safe="") + "?interval=1d&range=1mo")
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.loads(r.read().decode())
        res = d["chart"]["result"][0]
        meta = res["meta"]
        q = res["indicators"]["quote"][0]
        closes = [c for c in (q.get("close") or []) if c]
        vols = [v for v in (q.get("volume") or []) if v]
        if len(closes) < 2:
            return None
        prev, last = closes[-2], closes[-1]
        hist_vol = vols[-11:-1]
        avgvol = sum(hist_vol) / len(hist_vol) if hist_vol else 0
        vol = vols[-1] if vols else 0
        return {
            "price": round(last, 2),
            "prev_close": round(prev, 2),
            "chg_pct": round((last - prev) / prev * 100, 2),
            "volume": vol,
            "avg_volume_10d": int(avgvol),
            "vol_ratio": round(vol / avgvol, 2) if avgvol else None,
            "currency": meta.get("currency"),
            "exchange": meta.get("exchangeName"),
        }
    except Exception as e:
        return {"error": str(e)[:120]}


def fetch_news(ticker, market, timeout=15, limit=3):
    """Top headlines per ticker via Google News RSS (keyless). Never raises."""
    q = f"{ticker} stock" + (" NSE" if market == "india" else "")
    url = ("https://news.google.com/rss/search?q=" + urllib.parse.quote(q)
           + "&hl=en-US&gl=US&ceid=US:en")
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--market", required=True, choices=["us", "india"])
    ap.add_argument("--tickers", default=None)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--delay", type=float, default=0.25)
    a = ap.parse_args()

    if a.tickers:
        items = [{"ticker": t.strip(), "qty": None} for t in a.tickers.split(",") if t.strip()]
    else:
        items = load_tickers(a.market)
    if not items:
        print(f"no tickers found for market={a.market}", file=sys.stderr)
        sys.exit(1)

    out, misses = [], []
    for it in items:
        t = it["ticker"]
        if a.market == "us":
            syms = [t]
        else:
            syms = [t + ".NS", t + ".BO", t]
            # Broker series suffixes (e.g. FOO-BZ, BAR-RR) are not
            # Yahoo symbols; fall back to the base ticker.
            if "-" in t:
                base = t.split("-")[0]
                syms[3:3] = [base + ".NS", base + ".BO"]
        q = None
        for s in syms:
            q = fetch_quote(s)
            if q and "error" not in q:
                q["symbol"] = s
                break
            time.sleep(0.1)
        time.sleep(a.delay)
        if not q or "error" in q:
            misses.append(t)
            continue
        q["ticker"] = t
        q["qty"] = it["qty"]
        q["news"] = fetch_news(t, a.market)
        out.append(q)

    movers = sorted(
        [x for x in out if abs(x["chg_pct"]) >= 2.0 or (x["vol_ratio"] or 0) >= 2.0],
        key=lambda x: abs(x["chg_pct"]),
        reverse=True,
    )
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%MZ")
    payload = {
        "market": a.market,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "universe": len(items),
        "resolved": len(out),
        "unresolved": misses,
        "top_movers": movers[:a.top],
        "snapshot": out,
    }
    d = BASE / a.market
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{stamp}.json").write_text(json.dumps(payload, indent=1))
    (d / "latest.json").write_text(json.dumps(payload, indent=1))
    print(f"{a.market}: {len(out)}/{len(items)} resolved, {len(movers)} movers, misses={misses[:10]}")
    for m in movers[:10]:
        qty = f" x{m['qty']}" if m["qty"] else ""
        print(f"  {m['ticker']:14} {m['chg_pct']:+7.2f}% volx{m['vol_ratio']}{qty}")


if __name__ == "__main__":
    main()
