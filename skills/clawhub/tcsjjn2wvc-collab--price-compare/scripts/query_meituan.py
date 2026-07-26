#!/usr/bin/env python3
"""
美团联盟API查询脚本
API规则:
  - 外卖: platform=1, bizLine=0, topiId=2
  - 搜索: topiId=0
  - 团购: platform=2, bizLine=1, topiId=3
官方文档: https://open.meituan.com/
"""
import os
import hashlib
import time
import json
import sys
import requests

APP_KEY = os.environ.get("MEITUAN_APPKEY", "e04be35c176a4a5d8400b46c29ec4132")
APP_SECRET = os.environ.get("MEITUAN_APPSECRET", "0af8998613c54f7e9cb3ededb7203031")
CALLBACK_KEY = os.environ.get("MEITUAN_CALLBACK_KEY", "25d9esTrBn")
MEDIA_NAME = "券汇省"
CALLBACK_URL = "https://mini.juanshenghui.com/callback/meiTu"


def generate_sign(params, app_secret):
    """生成美团联盟API签名"""
    sorted_keys = sorted(params.keys())
    sign_str = app_secret
    for k in sorted_keys:
        if k != "sign" and params[k] is not None:
            sign_str += f"{k}{params[k]}"
    sign_str += app_secret
    return hashlib.md5(sign_str.encode("utf-8")).hexdigest().upper()


def query_meituan_waimai(keyword="", city_id=1, page=1, page_size=20):
    """
    查询美团外卖商家/商品
    platform=1, bizLine=0, topiId=2（外卖）
    """
    params = {
        "appKey": APP_KEY,
        "timestamp": int(time.time()),
        "platform": 1,
        "bizLine": 0,
        "topiId": 2,
        "keyword": keyword,
        "cityId": city_id,
        "pageNo": page,
        "pageSize": page_size,
    }
    params["sign"] = generate_sign(params, APP_SECRET)
    url = "https://open.meituan.com/api/promotion/waimai/query"

    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        return {"error": "美团查询超时", "code": -1}
    except requests.exceptions.ConnectionError:
        return {"error": "无法连接美团API", "code": -1}
    except Exception as e:
        return {"error": str(e), "code": -1}


def query_meituan_search(keyword, page=1, page_size=20):
    """
    美团联盟综合搜索
    topiId=0 表示搜索
    """
    params = {
        "appKey": APP_KEY,
        "timestamp": int(time.time()),
        "topiId": 0,
        "keyword": keyword,
        "pageNo": page,
        "pageSize": page_size,
    }
    params["sign"] = generate_sign(params, APP_SECRET)
    url = "https://open.meituan.com/api/promotion/search"

    try:
        resp = requests.get(url, params=params, timeout=15)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def query_meituan_tuangou(keyword="", city_id=1, page=1, page_size=20):
    """
    美团团购搜索
    platform=2, bizLine=1, topiId=3（团购）
    """
    params = {
        "appKey": APP_KEY,
        "timestamp": int(time.time()),
        "platform": 2,
        "bizLine": 1,
        "topiId": 3,
        "keyword": keyword,
        "cityId": city_id,
        "pageNo": page,
        "pageSize": page_size,
    }
    params["sign"] = generate_sign(params, APP_SECRET)
    url = "https://open.meituan.com/api/promotion/tuangou/query"

    try:
        resp = requests.get(url, params=params, timeout=15)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_meituan_coupons():
    """获取美团可领红包/优惠券列表"""
    params = {
        "appKey": APP_KEY,
        "timestamp": int(time.time()),
        "couponType": 1,  # 1=红包, 2=优惠券
    }
    params["sign"] = generate_sign(params, APP_SECRET)
    url = "https://open.meituan.com/api/promotion/coupon/list"

    try:
        resp = requests.get(url, params=params, timeout=15)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def format_result(data):
    """标准化美团返回数据"""
    formatted = []
    if data.get("error"):
        return formatted

    items = data.get("data", {}).get("list", data.get("data", {}).get("items", []))
    if not items and isinstance(data.get("data"), list):
        items = data["data"]

    for item in items[:10]:
        price = float(item.get("price", item.get("currentPrice", item.get("sellPrice", 0))))
        coupon = float(item.get("couponAmount", item.get("couponAmountCent", 0)))
        # couponAmountCent 可能是分单位
        if coupon > 1000:
            coupon = coupon / 100

        after_price = round(price - coupon, 2)
        if after_price < 0:
            after_price = 0.01

        formatted.append({
            "platform": "美团",
            "title": item.get("title", item.get("name", item.get("goodsName", ""))),
            "price": price,
            "origin_price": float(item.get("originPrice", item.get("originalPrice", price))),
            "coupon_amount": coupon,
            "after_price": after_price,
            "url": item.get("link", item.get("h5Link", item.get("couponH5Link", ""))),
            "shop": item.get("shopName", item.get("poiName", "")),
            "rating": float(item.get("rating", item.get("wmPoiScore", 0))),
            "monthly_sales": int(item.get("monthSales", item.get("sales", 0))),
            "delivery_time": item.get("deliveryTime", item.get("delivery_time", "")),
        })
    return formatted


if __name__ == "__main__":
    keyword = sys.argv[1] if len(sys.argv) > 1 else "快餐"

    print("=" * 50)
    print(f"美团外卖查询: {keyword}")
    print("=" * 50)
    data = query_meituan_waimai(keyword)
    results = format_result(data)
    print(f"共找到 {len(results)} 条结果\n")
    print(json.dumps(results, ensure_ascii=False, indent=2))

    print("\n" + "=" * 50)
    print("美团可领红包")
    print("=" * 50)
    coupons = get_meituan_coupons()
    print(json.dumps(coupons, ensure_ascii=False, indent=2))
