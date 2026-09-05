#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_news_cn.py — 模块 C+ 国内权威新闻源采集（P1）

「盘前雷达」skill 的数据采集层之一。
分层采集国内权威新闻，为盘前「政策定调 + 题材催化 + 消息面」提供信号底座：
  ① 官媒层（政策定调、权威性最高）：新华网 / 人民网 / 中新网官方 RSS
  ② 快讯层（盘中催化、题材催化）：东方财富 7x24 快讯 + 新浪财经滚动新闻

设计原则：
  1. 纯标准库（urllib + xml.etree），零第三方依赖。
  2. 只取「标题 + 摘要 + 链接 + 来源」，**不转载、不展示新闻全文**，规避时政新闻转载红线。
  3. 情绪打分不在本脚本做（交给 score_and_report.py），本脚本只做可信采集。

用法：
  python3 fetch_news_cn.py            # 打印 JSON 到 stdout
  python3 fetch_news_cn.py --pretty   # 美化打印
  python3 fetch_news_cn.py --limit 10 # 每类取前 N 条（默认 15）
"""

import json
import sys
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
TIMEOUT = 15

# ① 官媒 RSS（无 key，标题+链接引用）
# 注意：新华网 RSS 停更于 2022、人民网 RSS 停更于 2025、澎湃 RSS 已失效，
# 国内官媒中仅「中新网（中新社）」系列 RSS 仍在实时更新，故官媒层以中新网为主。
OFFICIAL_RSS = [
    ("中新网-滚动", "http://www.chinanews.com.cn/rss/scroll-news.xml"),
    ("中新网-财经", "https://www.chinanews.com.cn/rss/finance.xml"),
    ("中新网-国内", "http://www.chinanews.com.cn/rss/china.xml"),
    ("中新网-国际", "http://www.chinanews.com.cn/rss/world.xml"),
    ("中新网-社会", "http://www.chinanews.com.cn/rss/society.xml"),
]

# ② 快讯层
EASTMONEY_FLASH = "https://np-listapi.eastmoney.com/comm/web/getFastNewsList"
SINA_ROLL = "https://feed.mix.sina.com.cn/api/roll/get"


def _get(url, gbk=False, referer=None):
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        raw = resp.read()
    return raw.decode("gbk" if gbk else "utf-8", "ignore")


def _fmt_time(pub_date):
    """RFC 822 时间 -> '%m-%d %H:%M'，解析失败返回原字符串。"""
    if not pub_date:
        return ""
    try:
        dt = parsedate_to_datetime(pub_date)
        return dt.strftime("%m-%d %H:%M")
    except (TypeError, ValueError):
        return pub_date


def _parse_rss(xml_text):
    """解析 RSS 2.0，返回 [{title, url, time, desc}]。"""
    items = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return items
    for item in root.iter("item"):
        title = ""
        url = ""
        pub_date = ""
        desc = ""
        for child in item:
            tag = child.tag.split("}")[-1]  # 去掉命名空间前缀
            text = (child.text or "").strip()
            if tag == "title":
                title = text
            elif tag == "link":
                url = text
            elif tag in ("pubDate", "date", "pubdate"):
                pub_date = text
            elif tag == "description":
                desc = text
        if title:
            items.append({
                "title": title,
                "url": url,
                "time": _fmt_time(pub_date),
                "desc": desc[:120] if desc else "",
            })
    return items


def fetch_official(limit=15):
    """采集官媒 RSS。"""
    result = {}
    for name, url in OFFICIAL_RSS:
        try:
            xml_text = _get(url)
            items = _parse_rss(xml_text)[:limit]
            result[name] = items
        except Exception:
            result[name] = []
    return result


def fetch_eastmoney_flash(limit=15):
    """采集东财 7x24 快讯。"""
    req_trace = str(int(time.time() * 1000))
    params = {
        "client": "web",
        "biz": "web_724",
        "fastColumn": "102",
        "sortEnd": "",
        "pageSize": str(limit),
        "req_trace": req_trace,
    }
    url = EASTMONEY_FLASH + "?" + urllib.parse.urlencode(params)
    try:
        data = json.loads(_get(url))
        news = data.get("data", {}).get("fastNewsList", [])
        return [
            {
                "title": (n.get("title") or "").strip(),
                "summary": (n.get("summary") or "").strip()[:150],
                "time": n.get("showTime") or "",
            }
            for n in news
        ]
    except Exception:
        return []


def fetch_sina_roll(limit=15):
    """采集新浪财经滚动新闻（7x24）。"""
    params = {
        "pageid": "153",
        "lid": "2516",
        "num": str(limit),
        "page": "1",
    }
    url = SINA_ROLL + "?" + urllib.parse.urlencode(params)
    try:
        data = json.loads(_get(url, referer="https://finance.sina.com.cn"))
        rows = data.get("result", {}).get("data", [])
        return [
            {
                "title": (r.get("title") or "").strip(),
                "url": r.get("url") or "",
                "time": time.strftime("%m-%d %H:%M", time.localtime(int(r.get("intime", 0)))) if r.get("intime") else "",
            }
            for r in rows
        ]
    except Exception:
        return []


def collect(limit=15):
    return {
        "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "官媒RSS(中新网) + 东财7x24快讯 + 新浪滚动 (free, no key)",
        "note": "只采集标题/摘要/链接，不转载新闻全文",
        "official_media": fetch_official(limit=limit),
        "eastmoney_flash": fetch_eastmoney_flash(limit=limit),
        "sina_roll": fetch_sina_roll(limit=limit),
    }


def main():
    args = sys.argv[1:]
    pretty = "--pretty" in args
    limit = 15
    if "--limit" in args:
        limit = int(args[args.index("--limit") + 1])

    out = collect(limit=limit)
    if pretty:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
