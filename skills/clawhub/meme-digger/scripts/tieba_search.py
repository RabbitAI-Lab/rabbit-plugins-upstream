#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""meme-digger: 贴吧搜索（最佳努力通道，贴吧风控严格）。

用法:
    python tieba_search.py <关键词>

Cookie 获取优先级（任一即可）:
1. 本 skill 的 config/cookies.json (推荐, 格式见 cookies.json.example)
2. 环境变量 TIEBA_COOKIE

策略（按顺序尝试）:
1. 有 cookie 时请求贴吧 v3 搜索接口(JSON), 返回真实帖子列表。
2. 无 cookie 时尝试 wap 接口 → 检测「百度安全验证」→ 明确告知被拦截,
   并输出降级建议。

脚本永不崩溃，永远输出可执行的下一步。
"""
import sys
import os
import json
import urllib.parse
import urllib.request

import common


def load_cookie() -> str:
    """从 config/cookies.json 或环境变量读取贴吧 cookie。"""
    return common.load_cookies()["tieba"]

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
MOBILE_UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
             "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1")


def fetch(url: str, headers: dict) -> str:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode("utf-8", errors="replace")


def blocked(body: str) -> bool:
    return "安全验证" in body or "百度安全" in body or "verify" in body.lower()


def main():
    if len(sys.argv) < 2:
        print("用法: python tieba_search.py <关键词>")
        sys.exit(1)
    kw = sys.argv[1].strip()
    q = urllib.parse.quote(kw)
    cookie = load_cookie()

    if cookie:
        print(f"# 贴吧搜索「{kw}」（使用 TIEBA_COOKIE）")
        # 贴吧 v3 搜索接口（JSON）
        api = (f"https://c.tieba.baidu.com/c/f/search"
               f"?kw=&ie=utf-8&qw={q}&rn=20")
        try:
            body = fetch(api, {"User-Agent": MOBILE_UA, "Cookie": cookie})
            d = json.loads(body)
            posts = d.get("data", {}).get("post_list") or []
            if posts:
                for p in posts[:10]:
                    print(f"- {p.get('title','')[:60]} | 楼层:{p.get('floor')} "
                          f"| 赞:{p.get('agree')} | https://tieba.baidu.com/p/{p.get('post_id')}")
                print(f"\n共 {len(posts)} 条。")
                return
            print(f"!! 接口无结果（code={d.get('error_code')}）。")
        except Exception as e:
            print(f"!! 接口失败: {e}")
    else:
        print(f"# 贴吧搜索「{kw}」（未设置 TIEBA_COOKIE）")

    # 兜底: 尝试 wap 搜索页
    wap = f"https://tieba.baidu.com/mo/q/m?word={q}"
    try:
        body = fetch(wap, {"User-Agent": MOBILE_UA})
        if blocked(body):
            print("!! 被百度安全验证拦截（当前 IP 无 cookie 无法访问贴吧）。")
        else:
            print("!! wap 页可访问但未解析到帖子（页面结构可能变化）。")
    except Exception as e:
        print(f"!! wap 访问失败: {e}")

    print("""
降级方案（任选其一，按可用性排序）:
1. 若 agent 有 web_search 工具: 用 `site:tieba.baidu.com <关键词>` 搜索,
   再对命中的帖子 URL 用 web_fetch 抓取正文。
2. 用 web_fetch 打开 https://tieba.baidu.com/f?kw=<吧名> 浏览吧内热帖。
3. 请用户从浏览器 F12 → Network → 任意贴吧请求的 Cookie 复制到环境变量
   TIEBA_COOKIE 后重试本脚本（最可靠）。
""")


if __name__ == "__main__":
    main()
