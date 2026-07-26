"""
Walmart 类目抓取模块
使用 requests 抓取搜索结果页，解析 __NEXT_DATA__ 获取 TOP 商品主图和基础数据
无需登录态、无需浏览器自动化
"""
import re
import json
import time
import random
import requests
from urllib.parse import quote_plus


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
}


def fetch_walmart_top_products(keyword: str, top_n: int = 10) -> list:
    """抓取 Walmart 搜索结果 TOP 商品"""
    print(f"[Walmart] 开始抓取「{keyword}」 TOP {top_n}", flush=True)
    products = []
    page = 1
    max_pages = (top_n // 40) + 1
    while len(products) < top_n and page <= max_pages:
        page_products = _fetch_search_page(keyword, page)
        if not page_products:
            break
        products.extend(page_products)
        page += 1
        if page <= max_pages:
            time.sleep(random.uniform(1.5, 3.0))
    products = products[:top_n]
    print(f"[Walmart] 抓到 {len(products)} 条商品", flush=True)
    return products


def _fetch_search_page(keyword: str, page: int = 1) -> list:
    url = f"https://www.walmart.com/search?q={quote_plus(keyword)}"
    if page > 1:
        url += f"&page={page}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        if resp.status_code != 200:
            print(f"[Walmart] HTTP {resp.status_code} for page {page}", flush=True)
            return []
    except Exception as e:
        print(f"[Walmart] 请求失败: {e}", flush=True)
        return []
    return _parse_search_html(resp.text)


def _parse_search_html(html: str) -> list:
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
    if not m:
        return _parse_search_html_fallback(html)
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError:
        return _parse_search_html_fallback(html)
    return _extract_items_from_next_data(data)


def _extract_items_from_next_data(data: dict) -> list:
    products = []
    try:
        props = data.get("props", {}).get("pageProps", {})
        initial_data = props.get("initialData", {})
        search_result = initial_data.get("searchResult", {})
        item_stacks = search_result.get("itemStacks", [])
        for stack in item_stacks:
            items = stack.get("items", [])
            for item in items:
                product = {
                    "title": item.get("name") or item.get("title", ""),
                    "url": _build_walmart_url(item),
                    "image": _extract_image(item),
                    "price": _extract_price(item),
                    "rating": _to_float(item.get("averageRating")),
                    "reviews": _to_int(item.get("numberOfReviews")),
                    "seller": item.get("sellerName") or (item.get("seller") or {}).get("name", ""),
                    "item_id": item.get("usItemId") or item.get("id", ""),
                    "platform": "walmart",
                }
                if product["title"]:
                    products.append(product)
    except (KeyError, TypeError, AttributeError):
        pass
    return products


def _parse_search_html_fallback(html: str) -> list:
    products = []
    pattern = r'"usItemId":"(\d+)".*?"name":"([^"]+)".*?"imageUrl":"([^"]+)"'
    for m in re.finditer(pattern, html):
        products.append({
            "title": m.group(2),
            "url": f"https://www.walmart.com/ip/{m.group(1)}",
            "image": m.group(3),
            "price": None,
            "rating": None,
            "reviews": None,
            "seller": "",
            "item_id": m.group(1),
            "platform": "walmart",
        })
    return products


def _build_walmart_url(item: dict) -> str:
    canonical = item.get("canonicalUrl", "")
    if canonical:
        return canonical if canonical.startswith("http") else f"https://www.walmart.com{canonical}"
    item_id = item.get("usItemId") or item.get("id", "")
    return f"https://www.walmart.com/ip/{item_id}" if item_id else ""


def _extract_image(item: dict) -> str:
    img = (item.get("imageInfo") or {}).get("thumbnailUrl", "")
    if not img:
        img = item.get("image", "") or item.get("imageUrl", "")
    if img and "?" not in img:
        img += "?odnHeight=450&odnWidth=450"
    return img


def _extract_price(item: dict):
    price_info = item.get("priceInfo", {}) or {}
    current = price_info.get("currentPrice", {})
    if isinstance(current, dict):
        return _to_float(current.get("price"))
    line_price = price_info.get("linePrice", "")
    if line_price:
        return _to_float(line_price)
    return _to_float(item.get("price"))


def _to_float(v):
    if v is None:
        return None
    try:
        return float(str(v).replace("$", "").replace(",", "").strip())
    except (ValueError, TypeError):
        return None


def _to_int(v):
    if v is None:
        return None
    try:
        return int(float(str(v).replace(",", "").strip()))
    except (ValueError, TypeError):
        return None


if __name__ == "__main__":
    import sys
    kw = sys.argv[1] if len(sys.argv) > 1 else "outdoor furniture"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    products = fetch_walmart_top_products(kw, top_n=n)
    print(json.dumps(products, ensure_ascii=False, indent=2))
