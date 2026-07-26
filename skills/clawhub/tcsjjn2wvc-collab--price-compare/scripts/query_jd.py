#!/usr/bin/env python3
"""
京东联盟商品查询脚本
API: jd.union.open.goods.query
官方文档: https://union.jd.com/openplatform/api
"""
import os
import hashlib
import time
import requests
import json
import sys

APP_KEY = os.environ.get("JD_APPKEY", "0577957bee925536b09ac062dfda3db8")
APP_SECRET = os.environ.get("JD_APPSECRET", "44560303245f4ae19cccc1360e30f51c")
AUTH_KEY = os.environ.get("JD_AUTH_KEY", "6ef3fbb8dfe5d8e2f712b99abc77faa9375c84f0b3276421b8f6d11403b7da4bd2a116baf402fc46")


def generate_sign(params, app_secret):
    """生成京东联盟API签名（MD5大写）"""
    sorted_params = sorted(params.items())
    sign_str = app_secret
    for k, v in sorted_params:
        if v is not None:
            sign_str += f"{k}{v}"
    sign_str += app_secret
    return hashlib.md5(sign_str.encode("utf-8")).hexdigest().upper()


def query_jd_products(keyword, page=1, page_size=20):
    """
    查询京东商品（关键词搜索）
    接口: jd.union.open.goods.query
    """
    goods_req = {
        "keyword": keyword,
        "pageIndex": page,
        "pageSize": min(page_size, 50),
    }
    params = {
        "app_key": APP_KEY,
        "method": "jd.union.open.goods.query",
        "timestamp": str(int(time.time() * 1000)),
        "format": "json",
        "v": "1.0",
        "sign_method": "md5",
        "param_json": json.dumps({"goodsReqDTO": goods_req}, ensure_ascii=False),
    }
    params["sign"] = generate_sign(params, APP_SECRET)

    url = "https://api.jd.com/routerjson"
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        return {"error": "京东查询超时", "error_response": {"code": -1}}
    except requests.exceptions.ConnectionError:
        return {"error": "无法连接京东API", "error_response": {"code": -1}}
    except Exception as e:
        return {"error": str(e), "error_response": {"code": -1}}


def query_jd_coupons(keyword=""):
    """
    获取京东可领优惠券
    接口: jd.union.open.coupon.query
    """
    coupon_req = {"keyword": keyword} if keyword else {}
    params = {
        "app_key": APP_KEY,
        "method": "jd.union.open.coupon.query",
        "timestamp": str(int(time.time() * 1000)),
        "format": "json",
        "v": "1.0",
        "sign_method": "md5",
        "param_json": json.dumps({"couponReq": coupon_req}, ensure_ascii=False),
    }
    params["sign"] = generate_sign(params, APP_SECRET)

    url = "https://api.jd.com/routerjson"
    try:
        resp = requests.get(url, params=params, timeout=10)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def format_result(data):
    """
    标准化京东商品返回数据
    兼容京东联盟多种返回结构
    """
    results = []

    # 错误处理
    if data.get("error"):
        return results

    # 解析京东联盟响应
    resp_key = "jd_union_open_goods_query_responce"
    response = data.get(resp_key, data.get("jd_union_open_goods_query_response", {}))
    if not response:
        return results

    result_code = response.get("code", response.get("resultCode", ""))
    if str(result_code) != "200" and str(result_code) != "0":
        return results

    # 京东API返回的商品列表
    query_result = response.get("queryResult", response.get("data", {}))
    if isinstance(query_result, str):
        try:
            query_result = json.loads(query_result)
        except json.JSONDecodeError:
            return results

    items = query_result.get("data", query_result.get("goodsRespList", []))
    if not isinstance(items, list):
        return results

    for item in items[:10]:
        # 兼容不同字段名
        price_info = item.get("priceInfo", item.get("couponInfo", {}))
        if isinstance(price_info, str):
            try:
                price_info = json.loads(price_info)
            except json.JSONDecodeError:
                price_info = {}

        price = float(price_info.get("price", item.get("price", 0)))
        coupon_list = price_info.get("couponList", [])
        coupon_amount = 0
        if coupon_list:
            coupon_amount = max(float(c.get("discount", 0)) for c in coupon_list)

        after_price = round(price - coupon_amount, 2)
        if after_price < 0:
            after_price = 0.01

        shop_info = item.get("shopInfo", {})
        if isinstance(shop_info, str):
            try:
                shop_info = json.loads(shop_info)
            except json.JSONDecodeError:
                shop_info = {}

        results.append({
            "platform": "京东",
            "title": item.get("skuName", item.get("goodsName", "")),
            "sku_id": item.get("skuId", item.get("materialUrl", "")),
            "price": price,
            "coupon_amount": coupon_amount,
            "after_price": after_price,
            "url": f"https://item.jd.com/{item.get('skuId', '')}.html",
            "shop": shop_info.get("shopName", item.get("shopName", "")),
            "sales": int(item.get("inOrderCount30Days", item.get("sales", 0))),
            "image": item.get("imageInfo", {}).get("imageList", [{}])[0].get("url", "") if isinstance(item.get("imageInfo"), dict) else "",
            "commission": float(price_info.get("commission", 0)),
        })
    return results


if __name__ == "__main__":
    keyword = sys.argv[1] if len(sys.argv) > 1 else "手机"
    print(f"🔍 京东搜索: {keyword}")
    data = query_jd_products(keyword)
    results = format_result(data)
    print(f"共找到 {len(results)} 条结果\n")
    print(json.dumps(results, ensure_ascii=False, indent=2))
