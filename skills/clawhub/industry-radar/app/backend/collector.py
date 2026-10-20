"""
M2 多源采集器：从 RSS / Atom 源拉取条目。

设计要点
--------
* 使用 requests 抓取原始字节（可自定义 UA / 超时 / 代理），再交给 feedparser 解析，
  避免 feedparser 直接联网时无法控制超时。
* 单源异常隔离：任一源失败只记录日志，不影响其它源（多源冗余原则）。
* 支持 HTTP 与 HTTPS；自动纠正源 URL。
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, Dict, List

import feedparser
import requests

import net_guard
from config import (
    MAX_ARTICLES_PER_SOURCE, MAX_FETCH_BYTES, REQUEST_TIMEOUT, USER_AGENT,
)

log = logging.getLogger("industryradar.collector")

_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
}


def _entry_time(entry) -> str:
    for key in ("published_parsed", "updated_parsed"):
        t = entry.get(key)
        if t:
            try:
                dt = datetime(*t[:6], tzinfo=timezone.utc)
                return dt.strftime("%Y-%m-%d %H:%M:%S")
            except Exception:  # noqa: BLE001
                pass
    return ""


def _entry_content(entry) -> str:
    """提取条目内嵌正文（若源提供）。"""
    if entry.get("content"):
        try:
            return entry["content"][0].get("value", "") or ""
        except Exception:  # noqa: BLE001
            pass
    return entry.get("summary", "") or entry.get("description", "") or ""


def fetch_source(source: Dict[str, Any]) -> List[Dict[str, Any]]:
    """抓取单个源，返回标准化条目列表。失败返回空列表。"""
    url = source.get("url", "")
    if not url:
        return []
    # 源地址虽来自内置配置，仍统一走出站校验，避免配置被改写后横向访问内网
    if not net_guard.is_fetchable(url):
        return []
    try:
        resp = net_guard.safe_get(
            url, headers=_HEADERS, timeout=REQUEST_TIMEOUT, max_bytes=MAX_FETCH_BYTES,
        )
        resp.raise_for_status()
        raw = resp.content
    except Exception as exc:  # noqa: BLE001
        log.warning("source fetch failed: %s (%s)", source.get("name", url), exc)
        return []

    try:
        parsed = feedparser.parse(raw)
    except Exception as exc:  # noqa: BLE001
        log.warning("feed parse failed: %s (%s)", source.get("name", url), exc)
        return []

    items: List[Dict[str, Any]] = []
    for e in parsed.entries[:MAX_ARTICLES_PER_SOURCE]:
        link = e.get("link", "") or ""
        title = (e.get("title", "") or "").strip()
        if not title or not link:
            continue
        items.append({
            "title": title,
            "url": link,
            "source_name": source.get("name", ""),
            "source_category": source.get("category", ""),
            "published_at": _entry_time(e),
            "raw_content": _entry_content(e),
        })
    log.info("source %s -> %d items", source.get("name", url), len(items))
    return items


def collect(sources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """并发采集多个源（线程池，免费源通常 <10 个，开销可控）。"""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    enabled = [s for s in sources if s.get("enabled", True)]
    out: List[Dict[str, Any]] = []
    if not enabled:
        return out

    with ThreadPoolExecutor(max_workers=min(8, len(enabled))) as pool:
        futures = {pool.submit(fetch_source, s): s for s in enabled}
        for fut in as_completed(futures):
            try:
                out.extend(fut.result())
            except Exception as exc:  # noqa: BLE001
                log.warning("collector task error: %s", exc)
    return out