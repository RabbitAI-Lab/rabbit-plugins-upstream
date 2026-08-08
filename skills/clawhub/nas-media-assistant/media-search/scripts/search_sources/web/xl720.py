#!/usr/bin/env python3
"""xl720 (迅雷电影天堂) parser。

搜索: https://www.xl720.com/?s=关键词
结果: h2.entry-title > a[href][title]
详情页: /thunder/数字.html 含 magnet 与 thunder 链接

依赖: requests, beautifulsoup4 (venv 已装)
统一接口: parse(query, source_cfg) -> [candidate]
"""
import re
import urllib.parse

from .common import make_session, build_candidate

DETAIL_LIMIT = 3  # 只抓前 N 个详情页拿真实下载链接，控制请求数


def parse(query, source_cfg):
    title = query.get("title", "")
    if not title:
        return []
    base = (source_cfg.get("domains") or ["https://www.xl720.com"])[0].rstrip("/")
    search_url = f"{base}/?s={urllib.parse.quote(title)}"
    session = make_session()
    try:
        r = session.get(search_url, timeout=15)
        r.raise_for_status()
    except Exception:
        return []
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    candidates = []
    for i, a in enumerate(soup.select(".entry-title a")):
        if i >= 10:
            break
        href = a.get("href", "")
        name = a.get("title") or a.get_text(strip=True)
        if not href or not name:
            continue
        cand = build_candidate(
            title=name,
            url=href,
            source_cfg=source_cfg,
            link_type="playpage",
        )
        if i < DETAIL_LIMIT:
            link = _fetch_detail_link(href, session)
            if link:
                cand["url"] = link["url"]
                cand["link_type"] = link["type"]
        candidates.append(cand)
    return candidates


def _fetch_detail_link(detail_url, session):
    """从详情页提取优先 magnet，其次 thunder。复用传入 session 连接池。"""
    try:
        r = session.get(detail_url, timeout=15)
        r.raise_for_status()
    except Exception:
        return None
    m = re.search(r"magnet:\?xt=urn:btih:[a-zA-Z0-9]+", r.text)
    if m:
        return {"url": m.group(0), "type": "magnet"}
    t = re.search(r"thunder://[A-Za-z0-9+/=]+", r.text)
    if t:
        return {"url": t.group(0), "type": "torrent"}
    return None
