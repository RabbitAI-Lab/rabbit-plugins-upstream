#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: Bilibili 搜索（免登录，已实测 2025-08）。

用法:
    python bili_search.py <关键词> [--page N] [--limit N]

输出: 结构化 markdown 列表（标题/up主/日期/bvid/链接）。
"""
import re
import sys
import json
import urllib.parse
import urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Referer": "https://www.bilibili.com/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "text/html,application/xhtml+xml",
    })
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode("utf-8", errors="replace")


def parse_cards(html: str):
    """从搜索页 HTML 提取视频卡片 (bvid, title, author, date)。"""
    cards = []
    # <a href="//www.bilibili.com/video/BVxxx" ...><h3 ... title="标题">
    pat = re.compile(
        r'href="(?:https?:)?//www\.bilibili\.com/video/(BV[0-9A-Za-z]+)/?"'
        r'[^>]*>.*?bili-video-card__info--tit" title="([^"]+)"',
        re.S,
    )
    authors = re.findall(r'bili-video-card__info--author"[^>]*>([^<]+)<', html)
    dates = re.findall(r'bili-video-card__info--date"[^>]*>\s*([^<]+)<', html)
    for i, (bvid, title) in enumerate(pat.findall(html)):
        title = re.sub(r"<em[^>]*>.*?</em>", "", title)  # 去掉关键词高亮
        title = re.sub(r"\s+", " ", title).strip()
        cards.append({
            "bvid": bvid,
            "title": title,
            "author": authors[i].strip() if i < len(authors) else "?",
            "date": dates[i].strip() if i < len(dates) else "?",
        })
    return cards


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    page = 1
    limit = 10
    for a in sys.argv[1:]:
        if a == "--page":
            page = int(sys.argv[sys.argv.index(a) + 1])
        if a == "--limit":
            limit = int(sys.argv[sys.argv.index(a) + 1])
    if not args:
        print("用法: python bili_search.py <关键词> [--page N] [--limit N]")
        sys.exit(1)
    kw = args[0]
    url = ("https://search.bilibili.com/all?keyword="
           + urllib.parse.quote(kw) + f"&page={page}")
    print(f"# B站搜索「{kw}」第 {page} 页")
    try:
        html = fetch(url)
    except Exception as e:
        print(f"!! 抓取失败: {e}\n请改用 web_fetch 工具打开搜索页, 或稍后重试。")
        sys.exit(1)
    cards = parse_cards(html)
    if not cards:
        print("!! 未解析到视频卡片（可能被风控或页面结构变化）。")
        print("   降级: 用 web_fetch 打开 " + url + " 人工读取结果。")
        sys.exit(1)
    for c in cards[:limit]:
        print(f"- {c['title']}  | up: {c['author']} | {c['date']} | https://www.bilibili.com/video/{c['bvid']}")
    print(f"\n共解析 {len(cards)} 条（显示前 {min(limit, len(cards))} 条）。")


if __name__ == "__main__":
    main()
