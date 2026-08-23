#!/usr/bin/env python3
"""Shared helpers for data_sources_*.py — fetch + cache + key load.
Data-first: every fetch is real urllib; failures degrade to UNVERIFIED (never fake)."""
import urllib.request, json, os, time, re

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "ds_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

def fetch(url, timeout=20, binary=False, headers=None):
    import ssl
    h = dict(UA)
    if headers: h.update(headers)
    req = urllib.request.Request(url, headers=h)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        data = r.read()
        return data if binary else data.decode("utf-8", "ignore")

def load_twelve_key():
    import re
    p = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "memory", "trading", "api_keys.md")
    try:
        for line in open(p).read().splitlines():
            if "Key:" in line:
                m = re.search(r"Key:\s*([0-9a-fA-F]{32})", line)
                if m:
                    return m.group(1)
    except Exception:
        pass
    return os.environ.get("TWELVE_DATA_API_KEY", "")

def cache_get(name, ttl=600):
    fp = os.path.join(CACHE_DIR, name + ".json")
    if os.path.exists(fp):
        try:
            c = json.load(open(fp))
            if time.time() - c.get("_ts", 0) < ttl:
                return c
        except Exception:
            pass
    return None

def cache_put(name, obj):
    fp = os.path.join(CACHE_DIR, name + ".json")
    obj = dict(obj); obj["_ts"] = time.time()
    try: json.dump(obj, open(fp, "w"))
    except Exception: pass

def simple_sentiment(text, bull_words, bear_words):
    t = text.lower()
    b = sum(t.count(w) for w in bull_words)
    x = sum(t.count(w) for w in bear_words)
    score = b - x
    if score > 0: return "bullish", score
    if score < 0: return "bearish", score
    return "neutral", 0
