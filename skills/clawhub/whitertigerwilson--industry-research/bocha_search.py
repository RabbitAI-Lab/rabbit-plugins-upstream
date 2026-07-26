#!/usr/bin/env python3
"""
bocha_search.py — 用 Bocha（博查）API 搜网页
用法：python bocha_search.py "查询词" [数量]
"""
import sys
import os
import json
import time
import requests


def search_bocha(query, n=5, summary=True):
    api_key = os.environ.get("BOCHA_API_KEY", "")
    if not api_key:
        raise RuntimeError("BOCHA_API_KEY 未配，请先 export BOCHA_API_KEY=sk-...")
    url = "https://api.bochaai.com/v1/web-search"
    payload = {
        "query": query,
        "summary": summary,
        "count": n,
        "freshness": "noLimit",
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    t0 = time.time()
    r = requests.post(url, json=payload, headers=headers, timeout=15)
    r.raise_for_status()
    data = r.json()
    elapsed = time.time() - t0

    # 提取结果（Bocha 返回 data.webPages.value）
    results = []
    pages = (data.get("data") or {}).get("webPages") or {}
    values = pages.get("value") or []
    for v in values:
        results.append({
            "title": v.get("name", ""),
            "url": v.get("url", ""),
            "snippet": v.get("snippet", ""),
            "summary": v.get("summary", ""),
            "site": v.get("siteName", ""),
            "date": v.get("datePublished", ""),
        })
    return {
        "query": query,
        "elapsed_s": round(elapsed, 2),
        "count": len(results),
        "results": results,
        "raw": data,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python bocha_search.py \"关键词\" [数量]", file=sys.stderr)
        sys.exit(1)
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    try:
        out = search_bocha(q, n)
        # 隐藏 raw
        out.pop("raw", None)
        print(json.dumps(out, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e), "type": type(e).__name__}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
