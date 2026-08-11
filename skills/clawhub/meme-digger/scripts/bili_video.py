#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: Bilibili 视频详情（免登录 API，已实测 2025-08）。

用法:
    python bili_video.py <bvid>

输出: 标题/简介/发布时间/播放/弹幕/硬币/收藏/分享/up主/链接。
"""
import sys
import json
import datetime
import urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def main():
    cover = "--cover" in sys.argv[1:]
    args = [a for a in sys.argv[1:] if a != "--cover"]
    if len(args) < 1:
        print("用法: python bili_video.py <bvid> [--cover]")
        sys.exit(1)
    bvid = args[0].strip()
    url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Referer": "https://www.bilibili.com/"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode("utf-8", errors="replace"))
    except Exception as e:
        print(f"!! 抓取失败: {e}")
        sys.exit(1)
    if d.get("code") != 0:
        print(f"!! API 返回错误: code={d.get('code')} message={d.get('message')}")
        sys.exit(1)
    v = d["data"]
    stat = v.get("stat") or {}
    pub = datetime.datetime.fromtimestamp(v.get("pubdate", 0)).strftime("%Y-%m-%d")
    print(f"# {v.get('title', '')}")
    print(f"- 链接: https://www.bilibili.com/video/{bvid}")
    print(f"- up主: {(v.get('owner') or {}).get('name', '?')}")
    print(f"- 发布时间: {pub}")
    print(f"- 播放: {stat.get('view', '?')}  弹幕: {stat.get('danmaku', '?')}  "
          f"硬币: {stat.get('coin', '?')}  收藏: {stat.get('favorite', '?')}  "
          f"分享: {stat.get('share', '?')}")
    desc = (v.get("desc") or "").strip()
    if desc:
        print(f"- 简介: {desc[:500]}")
    else:
        print("- 简介: (无)")
    if v.get("tname"):
        print(f"- 分区: {v['tname']}")
    if cover and v.get("pic"):
        print(f"- 封面URL: https:{v['pic']}" if v["pic"].startswith("//") else f"- 封面URL: {v['pic']}")


if __name__ == "__main__":
    main()
