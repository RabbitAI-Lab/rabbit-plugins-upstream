#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_geopolitics.py — 模块 B 地缘 / 风险事件采集（P0）

「盘前雷达」skill 的数据采集层之一。
基于 GDELT DOC 2.0 API（全球新闻事件库，65 语言，完全免费、无需 key、可再分发），
按主题拉取地缘风险相关新闻，输出结构化事件信号。

设计原则：
  1. 纯标准库（urllib），零第三方依赖。
  2. 仅使用 GDELT（可自由再分发），规避 ACLED 等 NC 许可源。
  3. 遵守 GDELT 限流：同一 IP 约 1 req / 5s，主题间 sleep。
  4. http 优先（实测比 https 稳定），失败自动切 https 并重试。
  5. 只取「标题 + 来源 + 链接」，不转载新闻全文，规避时政新闻转载红线。

用法：
  python3 fetch_geopolitics.py            # 打印 JSON 到 stdout
  python3 fetch_geopolitics.py --pretty   # 美化打印
"""

import json
import sys
import time
import urllib.request
import urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
TIMEOUT = 20

# 主题 -> GDELT DOC 2.0 query（英文关键词，覆盖 65 语言新闻）
THEMES = {
    "conflict": {
        "label": "冲突/战争",
        "query": "(war OR conflict OR invasion OR missile OR airstrike OR ceasefire)",
    },
    "trade": {
        "label": "贸易/制裁",
        "query": '(tariff OR "trade war" OR sanctions OR export controls)',
    },
    "mideast": {
        "label": "中东/能源通道",
        "query": '("middle east" OR hormuz OR "red sea" OR suez) AND (oil OR shipping OR strait)',
    },
}


def doc_query(query, maxrecords=8, scheme="http"):
    """调用 GDELT DOC 2.0，返回文章列表（失败返回 None）。"""
    params = {
        "query": query,
        "mode": "artlist",
        "format": "json",
        "maxrecords": str(maxrecords),
        "sort": "datedesc",
    }
    url = f"{scheme}://api.gdeltproject.org/api/v2/doc/doc?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read()
        data = json.loads(raw.decode("utf-8", "ignore"))
        return data.get("articles", [])
    except Exception:
        return None


def fetch_theme(key, cfg, scheme="http"):
    """拉取单个主题，带 http->https 降级与重试。返回结构化 dict。"""
    for sc in ([scheme] if scheme else []) + ["http", "https"]:
        arts = doc_query(cfg["query"], maxrecords=8, scheme=sc)
        if arts is not None:
            break
    if arts is None:
        return {
            "label": cfg["label"],
            "query": cfg["query"],
            "count": 0,
            "articles": [],
            "error": "fetch_failed",
        }

    articles = []
    countries = {}
    languages = {}
    for a in arts:
        item = {
            "title": (a.get("title") or "").strip(),
            "url": a.get("url") or "",
            "time": a.get("seendate") or "",
            "country": a.get("sourcecountry") or "",
            "language": a.get("language") or "",
            "domain": a.get("domain") or "",
        }
        articles.append(item)
        c = item["country"]
        l = item["language"]
        if c:
            countries[c] = countries.get(c, 0) + 1
        if l:
            languages[l] = languages.get(l, 0) + 1

    return {
        "label": cfg["label"],
        "query": cfg["query"],
        "count": len(articles),
        "articles": articles,
        "countries": dict(sorted(countries.items(), key=lambda x: -x[1])),
        "languages": dict(sorted(languages.items(), key=lambda x: -x[1])),
    }


def collect():
    """采集全部地缘主题，返回结构化 dict。"""
    themes = {}
    for key, cfg in THEMES.items():
        themes[key] = fetch_theme(key, cfg)
        # 遵守 GDELT 限流（约 1 req / 5s）
        time.sleep(5.5)
    return themes


def main():
    pretty = "--pretty" in sys.argv
    themes = collect()
    total = sum(t["count"] for t in themes.values())
    out = {
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "GDELT DOC 2.0 (free, no key, redistributable)",
        "total_articles": total,
        "themes": themes,
    }
    if pretty:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
