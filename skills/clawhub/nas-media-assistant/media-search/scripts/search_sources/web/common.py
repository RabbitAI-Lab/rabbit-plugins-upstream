#!/usr/bin/env python3
"""网页源 parser 公共工具（仅抓取辅助）。

本文件只负责「把页面拿下来」相关的共享逻辑：UA、连接复用、HTML 抓取。
**不做任何信息提取**——分辨率/年份/编码/音轨/字幕等全部由 title_parser.py
（稳定核心）在聚合层统一解析，与具体网站解耦：网页会失效，但标题名携带的信息始终在。

统一接口: parse(query, source_cfg) -> [候选 dict]
候选只装「网页能直接拿到的原始字段」: title / url / link_type / size / seeders / detail_url，
其中 title 是后续一切信息提取的来源。
"""
import requests
from bs4 import BeautifulSoup

# 统一 User-Agent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": UA}


def make_session():
    """创建带连接池复用的 requests.Session。"""
    s = requests.Session()
    s.headers.update(HEADERS)
    return s


def fetch_html(url, session=None, timeout=15, encoding="utf-8"):
    """抓取页面 HTML。

    Args:
        url: 目标 URL
        session: 可选的 requests.Session（复用连接池）
        timeout: 超时秒数
        encoding: 响应编码

    Returns:
        (html_text, BeautifulSoup) 元组；失败返回 (None, None)
    """
    requester = session or requests
    try:
        r = requester.get(url, timeout=timeout)
        r.raise_for_status()
        if encoding:
            r.encoding = encoding
        return r.text, BeautifulSoup(r.text, "html.parser")
    except Exception:
        return None, None


def build_candidate(title, url, source_cfg, link_type="magnet",
                    source_type="web", size="", detail_url="", seeders=0):
    """构造候选对象——只装网页能直接拿到的原始字段。

    信息提取（年份/分辨率/编码/音轨/字幕/大小/低质判定等）一律不在 parser 做，
    交由 aggregator 调用 title_parser 统一解析，保证「网页解析独立、可替换」。

    Args:
        title: 资源标题串（后续一切信息提取的来源，最重要）
        url: 下载链接（magnet / 直链 / 种子 / 播放页）
        source_cfg: 该源在 config.json 中的配置块
        link_type: magnet|direct|playpage|torrent
        size: 页面显示的大小原文（可选，兜底用）
        detail_url: 详情页 URL（可选）
        seeders: 做种数（可选）
    """
    cand = {
        "title": title,
        "source_type": source_type,
        "link_type": link_type,
        "url": url,
        "credibility": source_cfg.get("credibility", 0.7),
        "source_id": source_cfg.get("id", ""),
    }
    if size:
        cand["size"] = size
    if detail_url:
        cand["detail_url"] = detail_url
    if seeders:
        cand["seeders"] = seeders
    return cand
