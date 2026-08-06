#!/usr/bin/env python3
"""souxunlei (搜迅雷) parser。

搜索URL: /souxunlei/<hex(关键词UTF-8)>_1_id.html
  关键词转 UTF-8 十六进制，如 战狼2 -> e68898e78bbc32
结果: div.search-item 含 /xunleixiazai/<hash>.html 链接
详情页 hash 即 magnet 的 btih，可直接构造磁力链接，无需进详情页
搜索页 item-bar 已含文件大小(b.blue-pill)与文件数量(b.yellow-pill)，直接提取

依赖: requests, beautifulsoup4 (venv 已装)
统一接口: parse(query, source_cfg) -> [candidate]
"""
import re

from .common import make_session, build_candidate


def parse(query, source_cfg):
    title = query.get("title", "")
    if not title:
        return []
    base = (source_cfg.get("domains") or ["https://www.souxunlei.org"])[0].rstrip("/")
    hex_kw = title.encode("utf-8").hex()
    search_url = f"{base}/souxunlei/{hex_kw}_1_id.html"
    session = make_session()
    try:
        r = session.get(search_url, timeout=15)
        r.raise_for_status()
        r.encoding = "utf-8"
    except Exception:
        return []
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    candidates = []
    seen = set()
    for item in soup.select("div.search-item"):
        a = item.find("a", href=True)
        if not a:
            continue
        href = a.get("href", "")
        name = a.get_text(strip=True)
        m = re.search(r"/xunleixiazai/([a-f0-9]+)\.html", href)
        if not m:
            continue
        hash_ = m.group(1)
        if hash_ in seen:
            continue
        seen.add(hash_)
        # 搜索页 item-bar 已含文件大小(b.blue-pill)与文件数量(b.yellow-pill)，
        # 直接提取，无需访问详情页（少一次请求，更快更稳）
        size = ""
        size_b = item.select_one("b.blue-pill")
        if size_b:
            size = size_b.get_text(strip=True)
        file_count = 0
        cnt_b = item.select_one("b.yellow-pill")
        if cnt_b and cnt_b.get_text(strip=True).isdigit():
            file_count = int(cnt_b.get_text(strip=True))
        cand = build_candidate(
            title=name,
            url=f"magnet:?xt=urn:btih:{hash_}",
            source_cfg=source_cfg,
            link_type="magnet",
            size=size,
            detail_url=href if href.startswith("http") else base + href,
        )
        # 文件数量: 详情页已知集数信息，供 aggregator 兜底（标题无"全N集"时）
        if file_count:
            cand["file_count"] = file_count
        candidates.append(cand)
        if len(candidates) >= 10:
            break
    return candidates
