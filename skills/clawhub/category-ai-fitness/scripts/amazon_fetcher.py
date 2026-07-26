"""
Amazon 类目抓取模块
使用 LinkFox tool-gateway API（amazon/search 接口）
单次调用直接返回 ~60 条商品，含 imageUrl、价格、评分、月销、品牌等
"""
import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_URL = "https://tool-gateway.linkfox.com/amazon/search"


def fetch_amazon_top_products(keyword: str, top_n: int = 10, amazon_domain: str = "amazon.com",
                               sort: str = "relevanceblender", language: str = None,
                               timeout: int = 90) -> list:
    """
    抓取 Amazon 关键词搜索 TOP 商品（基于 LinkFox API）
    返回: [{title, url, image, rating, reviews, monthly_sales, price, asin, brand, ...}, ...]
    """
    api_key = os.getenv("LINKFOXAGENT_API_KEY")
    if not api_key:
        raise RuntimeError("缺少 LINKFOXAGENT_API_KEY 环境变量")

    print(f"[Amazon] LinkFox 搜索「{keyword}」 TOP {top_n}", flush=True)

    payload = {"keyword": keyword, "amazonDomain": amazon_domain}
    if sort:
        payload["sort"] = sort
    if language:
        payload["language"] = language

    data = json.dumps(payload).encode("utf-8")
    req = Request(
        API_URL,
        data=data,
        headers={
            "Authorization": api_key,
            "Content-Type": "application/json",
            "User-Agent": "category-ai-fitness/1.0",
        },
        method="POST",
    )

    try:
        with urlopen(req, timeout=timeout) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8") if e.fp else ""
        print(f"[Amazon] HTTP {e.code}: {body[:200]}", flush=True)
        return []
    except URLError as e:
        print(f"[Amazon] 连接失败: {e.reason}", flush=True)
        return []
    except Exception as e:
        print(f"[Amazon] 请求异常: {e}", flush=True)
        return []

    if isinstance(result, dict) and result.get("errcode") != 200:
        print(f"[Amazon] 业务错误: {result.get('errcode')} - {result.get('errmsg', '')}", flush=True)
        return []

    products = result.get("products", []) or []
    print(f"[Amazon] LinkFox 返回 {len(products)} 条，截取 TOP {top_n}", flush=True)
    products = products[:top_n]
    return [_normalize(p) for p in products]


def _normalize(p: dict) -> dict:
    """统一字段命名"""
    return {
        "title": p.get("title", ""),
        "url": p.get("asinUrl", ""),
        "image": p.get("imageUrl", ""),
        "rating": _to_float(p.get("rating")),
        "reviews": _to_int(p.get("ratings")),
        "monthly_sales": p.get("monthlySalesUnits") or p.get("monthlySales"),
        "monthly_sales_revenue": _to_float(p.get("monthlySalesRevenue")),
        "price": _to_float(p.get("extractedPrice") or p.get("price")),
        "currency": p.get("currency", "$"),
        "asin": p.get("asin", ""),
        "brand": p.get("brand", ""),
        "weight": p.get("weight", ""),
        "dimension": p.get("dimension", ""),
        "available_date": p.get("availableDate", ""),
        "fulfillment": p.get("fulfillment", ""),
        "seller_nation": p.get("sellerNation", ""),
        "is_sponsored": bool(p.get("sponsored", False)),
        "badges": p.get("badges", ""),
        "position": p.get("position", 0),
        "platform": "amazon",
    }


def enrich_with_images(products: list, max_workers: int = 3) -> list:
    """LinkFox 已经返回 imageUrl，无需额外抓取"""
    return products


def _to_float(v):
    if v is None or v == "":
        return None
    try:
        return float(str(v).replace("$", "").replace(",", "").strip())
    except (ValueError, TypeError):
        return None


def _to_int(v):
    if v is None or v == "":
        return None
    try:
        return int(float(str(v).replace(",", "").strip()))
    except (ValueError, TypeError):
        return None


if __name__ == "__main__":
    import sys
    kw = sys.argv[1] if len(sys.argv) > 1 else "yoga mat"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    products = fetch_amazon_top_products(kw, top_n=n)
    print(json.dumps(products, ensure_ascii=False, indent=2))
