#!/usr/bin/env python3
"""
news_check.py — CEK BERITA / ECONOMIC CALENDAR buat filter entry (prinsip #4).

Fakta validasi (2026-08-21):
  - ForexFactory: DIBLOKIR Cloudflare (HTTP 403 "Just a moment...") -> TIDAK bisa di-scrape.
  - FXStreet economic calendar: BISA di-fetch (web_fetch). Ini sumber utama.
  - Fallback: web_search "USD high impact calendar <hari ini>" -> ringkasan.

Output: JSON {news_clear, events:[...], source, headline_gold_bias}
  - news_clear: true  -> tdk ada high-impact USD ± sesi / atau sudah lewat
  - news_clear: false -> ada event berdampak (atau gagal fetch -> AMAN mending skip)
  - gold_bias: "bullish"/"bearish"/"neutral" dari headline (hawkish Fed = bearish emas)

Cara pakai:
  python3 news_check.py
  python3 news_check.py --pretty
  (otomatis dipanggil update_xau_memory.py / Clara saat analisa)

Tidak ada secret. Hanya fetch publik.
"""
import argparse
import json
import re
import sys
import urllib.request
import urllib.error

FXSTREET = "https://www.fxstreet.com/economic-calendar"


def fetch_fxstreet():
    try:
        req = urllib.request.Request(FXSTREET, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", errors="ignore")
        return html
    except (urllib.error.URLError, ValueError, TypeError) as e:
        print(f"[warn] fxstreet fetch failed: {e}", file=sys.stderr)
        return None


def parse_headline(html):
    """Ambil teks 'Here is what you need to know on <day>' + paragraf berikutnya.
    Struktur FXStreet: <p>...Here is what you need to know on Friday, August 21...</p>
    lalu paragraf narasi. Kita ambil 2 paragraf setelahnya."""
    m = re.search(r"(Here is what you need to know on .*?)(?:<\/p>|<\/div>)", html, re.S | re.I)
    if not m:
        return ""
    chunk = re.sub(r"<[^>]+>", " ", m.group(1))
    chunk = re.sub(r"\s+", " ", chunk).strip()
    return chunk[:600]


def gold_bias_from(text):
    t = text.lower()
    bear = ("hawkish" in t) or ("higher rates" in t) or ("rate hike" in t) \
           or ("inflation too high" in t) or ("federal reserve" in t and "hawkish" in t)
    bull = ("dovish" in t) or ("rate cut" in t) or ("weak data" in t) \
           or ("lower rates" in t) or ("us dollar" in t and ("weak" in t or "struggles" in t or "low" in t))
    if bear and not bull:
        return "bearish"
    if bull and not bear:
        return "bullish"
    return "neutral"


def has_high_impact(text):
    """Ada event high-impact hari ini? (PMI, NFP, CPI, FOMC, rate decision, dll)"""
    t = text.lower()
    hits = ["pmi", "purchasing managers", "nonfarm", "nfp", "cpi", "fomc",
            "rate decision", "interest rate", "gdp", "jobless", "retail sales"]
    return any(h in t for h in hits)


def main():
    p = argparse.ArgumentParser(description="Gold news / calendar filter (prinsip #4).")
    p.add_argument("--pretty", action="store_true")
    args = p.parse_args()

    html = fetch_fxstreet()
    headline = parse_headline(html) if html else ""
    bias = gold_bias_from(headline) if headline else "unknown"

    # news_clear = true HANYA kalau: ada headline DAN tdk ada high-impact event.
    # Bila fetch gagal -> anggap TIDAK clear (aman: skip dulu).
    news_clear = bool(headline) and not has_high_impact(headline)

    out = {
        "source": "fxstreet.com/economic-calendar",
        "fetched": bool(html),
        "news_clear": news_clear,
        "high_impact_today": has_high_impact(headline),
        "gold_bias": bias,
        "headline": headline,
    }
    print(json.dumps(out, indent=2))
    if args.pretty:
        print("---", file=sys.stderr)
        print(f"Source: {out['source']} (fetched={out['fetched']})", file=sys.stderr)
        print(f"News clear: {news_clear}  | high-impact today: {out['high_impact_today']}  | gold bias: {bias}", file=sys.stderr)
        if headline:
            print(f"Headline: {headline[:160]}...", file=sys.stderr)


if __name__ == "__main__":
    main()
