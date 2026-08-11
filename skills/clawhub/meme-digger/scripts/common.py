#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: 共享模块（UA / cookie 加载 / 带重试的抓取）。

所有采集脚本 import 本模块，避免重复代码。
cookie 来源优先级: config/cookies.json > 环境变量 BILI_COOKIE / TIEBA_COOKIE
"""
import os
import json
import time
import urllib.request

CONFIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config")
CONFIG_FILE = os.path.join(CONFIG_DIR, "cookies.json")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
MOBILE_UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
             "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 "
             "Mobile/15E148 Safari/604.1")


def load_cookies() -> dict:
    """返回 {"bilibili": str, "tieba": str}，可均为空串。"""
    out = {"bilibili": "", "tieba": ""}
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, encoding="utf-8") as f:
                d = json.load(f)
            out["bilibili"] = (d.get("bilibili") or {}).get("cookie", "").strip()
            out["tieba"] = (d.get("tieba") or {}).get("cookie", "").strip()
        except Exception:
            pass
    out["bilibili"] = out["bilibili"] or os.environ.get("BILI_COOKIE", "").strip()
    out["tieba"] = out["tieba"] or os.environ.get("TIEBA_COOKIE", "").strip()
    return out


def save_cookies(bili: str = None, tieba: str = None) -> dict:
    """写入 config/cookies.json（保留未修改项）。"""
    os.makedirs(CONFIG_DIR, exist_ok=True)
    d = {}
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            d = {}
    d.setdefault("bilibili", {"cookie": ""})
    d.setdefault("tieba", {"cookie": ""})
    if bili is not None:
        d["bilibili"]["cookie"] = bili.strip()
    if tieba is not None:
        d["tieba"]["cookie"] = tieba.strip()
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    return d


def fetch(url: str, referer: str = "https://www.bilibili.com/",
          cookie: str = "", mobile: bool = False,
          retries: int = 2, timeout: int = 15) -> str:
    """带重试的抓取。重试间指数退避。"""
    ua = MOBILE_UA if mobile else UA
    headers = {"User-Agent": ua, "Accept-Language": "zh-CN,zh;q=0.9"}
    if referer:
        headers["Referer"] = referer
    if cookie:
        headers["Cookie"] = cookie
    last = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception as e:
            last = e
            if attempt < retries:
                time.sleep(1.5 * (2 ** attempt))
    raise last
