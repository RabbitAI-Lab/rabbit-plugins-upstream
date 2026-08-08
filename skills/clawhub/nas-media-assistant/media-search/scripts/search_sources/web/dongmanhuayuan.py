#!/usr/bin/env python3
"""dongmanhuayuan (动漫花园) parser。

搜索: https://www.dongmanhuayuan.com/dosearch/?key=关键词
结果页: 含 /detail/xxx.html 详情链接
详情页: /detail/xxx.html 含 magnet 链接

依赖: requests, beautifulsoup4 (venv 已装)
统一接口: parse(query, source_cfg) -> [candidate]
"""
import urllib.parse

from .common import make_session, build_candidate

DETAIL_LIMIT = 3


def parse(query, source_cfg):
    title = query.get("title", "")
    if not title:
        return []
    base = (source_cfg.get("domains") or ["https://www.dongmanhuayuan.com"])[0].rstrip("/")
    search_url = f"{base}/dosearch/?key={urllib.parse.quote(title)}"
    session = make_session()
    try:
        r = session.get(search_url, timeout=15)
        r.raise_for_status()
    except Exception:
        return []
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    items = []
    seen = set()
    for a in soup.select("a[href*='/detail/']"):
        href = a.get("href", "")
        if not href or href in seen:
            continue
        seen.add(href)
        name = a.get_text(strip=True) or a.get("title", "")
        if not name:
            continue
        items.append((href, name))
        if len(items) >= 10:
            break
    candidates = []
    for i, (href, name) in enumerate(items):
        full = href if href.startswith("http") else base + href
        cand = build_candidate(
            title=name,
            url=full,
            source_cfg=source_cfg,
            link_type="playpage",
        )
        if i < DETAIL_LIMIT:
            link = _fetch_detail_link(full, session)
            if link:
                cand["url"] = link["url"]
                cand["link_type"] = link["type"]
        candidates.append(cand)
    return candidates


def _fetch_detail_link(detail_url, session):
    try:
        r = session.get(detail_url, timeout=15)
        r.raise_for_status()
    except Exception:
        return None
    import re
    m = re.search(r"magnet:\?xt=urn:btih:[a-zA-Z0-9]+", r.text)
    if m:
        return {"url": m.group(0), "type": "magnet"}
    return None
