#!/usr/bin/env python3
"""Nyaa (nyaa.si) parser。

国际动漫+影视磁力站，反爬弱，requests 直接返回 magnet。
搜索: https://nyaa.si/?q=关键词
结果: table tr，含 a[href*=magnet] 磁力链接 + a[href*=/view/] 标题

依赖: requests, beautifulsoup4 (venv 已装)
统一接口: parse(query, source_cfg) -> [candidate]
"""
import urllib.parse

from .common import make_session, build_candidate

BASE = "https://nyaa.si"


def parse(query, source_cfg):
    title = query.get("title", "")
    if not title:
        return []
    search_url = f"{BASE}/?q={urllib.parse.quote(title)}"
    session = make_session()
    try:
        r = session.get(search_url, timeout=15)
        r.raise_for_status()
    except Exception:
        return []
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    candidates = []
    for tr in soup.select("table tr"):
        mag_a = tr.select_one("a[href*='magnet']")
        if not mag_a:
            continue
        # 标题在 a[href*="/view/"]，取文本最长者（排除 comments 数）
        title_as = [a for a in tr.select("a[href*='/view/']") if a.get_text(strip=True)]
        name = max((a.get_text(strip=True) for a in title_as), key=len, default="")
        if not name:
            continue
        candidates.append(build_candidate(
            title=name,
            url=mag_a["href"],
            source_cfg=source_cfg,
            link_type="magnet",
        ))
        if len(candidates) >= 10:
            break
    return candidates
