#!/usr/bin/env python3
"""
bing_search.py — 0 依赖、0 API key 的 Bing 网页搜索抓取器
用法：python bing_search.py "查询关键词" [结果数]
"""
import sys
import re
import json
import time
import urllib.parse
import requests

HDRS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


def search_bing(query, n=5):
    """抓 Bing 搜索结果 HTML，正则提取"""
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}&setlang=zh-Hans"
    r = requests.get(url, headers=HDRS, timeout=10)
    r.raise_for_status()
    html = r.text
    # 找 h2 内的链接和标题（Bing 结果格式）
    h2_pattern = r'<h2[^>]*>\s*<a[^>]*href="([^"]+)"[^>]*h="ID=SERP[^"]*">\s*(.*?)\s*</a>\s*</h2>'
    blocks = re.findall(h2_pattern, html, re.S)
    out = []
    for link, raw_title in blocks[:n]:
        title = re.sub(r"<[^>]+>", "", raw_title).strip()
        # 找摘要：在 <h2> 后面的 <p>
        out.append({"title": title, "url": link})
    return out, html


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python bing_search.py \"关键词\" [数量]", file=sys.stderr)
        sys.exit(1)
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    try:
        t0 = time.time()
        res, raw = search_bing(q, n)
        print(json.dumps({
            "query": q,
            "elapsed_s": round(time.time() - t0, 1),
            "count": len(res),
            "results": res,
        }, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e), "type": type(e).__name__}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
