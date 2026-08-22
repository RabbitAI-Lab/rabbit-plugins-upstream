#!/usr/bin/env python3
"""
wechat_js_render.py — 处理 JS 动态渲染的微信公众号文章

当 curl_cffi 抓不到 #js_content 时，用此脚本尝试：
1. 在页面中搜索嵌入的 JSON 数据
2. 提取所有可见文本作为兜底
3. 尝试不同 User-Agent

用法:
  python3 wechat_js_render.py "https://mp.weixin.qq.com/s/..."
"""

import argparse
import json
import re
import sys
import time
from urllib.parse import urlparse

try:
    from curl_cffi import requests as curl_requests
    HAS_CURL_CFFI = True
except ImportError:
    import requests
    HAS_CURL_CFFI = False


def fetch_with_strategy(url: str, headers: dict = None) -> tuple:
    """尝试多种策略抓取页面"""
    strategies = []

    # 策略 1: curl_cffi 模拟 Chrome
    if HAS_CURL_CFFI:
        try:
            resp = curl_requests.get(url, headers=headers or {}, timeout=15,
                                     impersonate="chrome120")
            strategies.append(("curl_cffi_chrome", resp.status_code, len(resp.text)))
            if resp.status_code == 200:
                return resp.text, "curl_cffi_chrome", strategies
        except Exception as e:
            strategies.append(("curl_cffi_chrome", "error", str(e)[:50]))

    # 策略 2: curl_cffi 模拟 Safari
    if HAS_CURL_CFFI:
        try:
            resp = curl_requests.get(url, headers=headers or {}, timeout=15,
                                     impersonate="safari15_5")
            strategies.append(("curl_cffi_safari", resp.status_code, len(resp.text)))
            if resp.status_code == 200:
                return resp.text, "curl_cffi_safari", strategies
        except Exception as e:
            strategies.append(("curl_cffi_safari", "error", str(e)[:50]))

    # 策略 3: 标准 requests
    try:
        import requests as std_requests
        resp = std_requests.get(url, headers=headers or {}, timeout=15)
        strategies.append(("standard_requests", resp.status_code, len(resp.text)))
        if resp.status_code == 200:
            return resp.text, "standard_requests", strategies
    except Exception as e:
        strategies.append(("standard_requests", "error", str(e)[:50]))

    return None, "all_failed", strategies


def extract_from_html(html: str) -> dict:
    """从 HTML 中尽可能提取内容"""
    result = {
        "title": None,
        "author": None,
        "pub_time": None,
        "content": None,
        "method": "unknown",
    }

    # 方法 1: 标准 #js_content (已有 reader 脚本处理)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    js_content = soup.find(id="js_content")
    if js_content:
        text = js_content.get_text("\n", strip=True)
        if len(text) > 50:
            result["content"] = text
            result["method"] = "js_content_id"

    # 方法 2: 从 script 中提取变量
    patterns = [
        (r'var\s+msg_title\s*=\s*[\'"]([^\'"]+)[\'"]', "title"),
        (r'var\s+nickname\s*=\s*[\'"]([^\'"]+)[\'"]', "author"),
        (r'var\s+create_time\s*=\s*[\'"]([^\'"]+)[\'"]', "pub_time"),
        (r'var\s+msg_cdn_url\s*=\s*[\'"]([^\'"]+)[\'"]', "cdn_url"),
    ]
    for pattern, field in patterns:
        if not result.get(field):
            m = re.search(pattern, html)
            if m:
                result[field] = m.group(1)

    # 方法 3: 从 JSON-like 数据中提取
    if not result.get("title"):
        m = re.search(r'"title"\s*:\s*"([^"]+)"', html)
        if m:
            result["title"] = m.group(1)
    if not result.get("author"):
        m = re.search(r'"nickname"\s*:\s*"([^"]+)"', html)
        if m:
            result["author"] = m.group(1)

    # 方法 4: 从 rich_media 相关元素提取
    if not result.get("content"):
        content_selectors = [
            "#js_content",
            ".rich_media_content",
            "#js_article",
            ".rich_media_area_primary",
            "article",
        ]

        for selector in content_selectors:
            try:
                if selector.startswith("#"):
                    elem = soup.find(id=selector[1:])
                elif selector.startswith("."):
                    elem = soup.find(class_=selector[1:])
                else:
                    elem = soup.find(selector)
                if elem:
                    text = elem.get_text("\n", strip=True)
                    if len(text) > 100:
                        result["content"] = text
                        result["method"] = selector
                        break
            except:
                continue

    # 方法 5: 从 page content 变量提取 (JSON格式)
    if not result.get("content"):
        m = re.search(r'window\.__page_content\s*=\s*[\'"](.+?)[\'"]\s*;', html, re.DOTALL)
        if not m:
            m = re.search(r'var\s+page_content\s*=\s*[\'"](.+?)[\'"]\s*;', html, re.DOTALL)
        if m:
            try:
                decoded = m.group(1).encode().decode('unicode_escape')
                result["content"] = decoded
                result["method"] = "page_content_var"
            except:
                pass

    # 方法 6: 兜底 - 提取 body 中所有文本
    if not result.get("content"):
        body = soup.find("body")
        if body:
            # 移除 script 和 style
            for tag in body(["script", "style", "nav", "footer", "header"]):
                tag.decompose()
            text = body.get_text("\n", strip=True)
            # 清理
            text = re.sub(r'\n{3,}', '\n\n', text)
            text = text.strip()
            if len(text) > 100:
                result["content"] = text
                result["method"] = "body_text_fallback"

    return result


def main():
    parser = argparse.ArgumentParser(description="微信JS渲染文章抓取")
    parser.add_argument("url", help="微信公众号文章链接")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    # 清理 URL
    url = args.url
    parsed = urlparse(url)
    clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    if parsed.query:
        # 只保留必要的参数
        params = {}
        for k, v in [p.split("=", 1) for p in parsed.query.split("&") if "=" in p]:
            if k in ["__biz", "mid", "idx", "sn"]:
                params[k] = v
        if params:
            clean_url += "?" + "&".join(f"{k}={v}" for k, v in params.items())

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://mp.weixin.qq.com/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    }

    # 抓取
    html, strategy, attempts = fetch_with_strategy(clean_url, headers)

    if not html:
        print(json.dumps({
            "error": "all_strategies_failed",
            "attempts": attempts,
            "source_url": url,
        }, indent=2, ensure_ascii=False))
        return

    # 解析
    result = extract_from_html(html)

    # 输出
    output = {
        "title": result.get("title", ""),
        "author": result.get("author", ""),
        "pub_time": result.get("pub_time", ""),
        "content": result.get("content", ""),
        "source_url": url,
        "strategy": strategy,
        "extract_method": result.get("method", "unknown"),
        "content_length": len(result.get("content") or ""),
        "attempts": attempts,
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
