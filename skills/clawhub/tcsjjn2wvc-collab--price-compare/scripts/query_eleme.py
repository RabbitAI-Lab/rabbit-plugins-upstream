#!/usr/bin/env python3
"""
饿了么联盟API查询脚本
方式1: 折淘客代理 (已有Appkey: 8cbd7852d5fc4c04a956049683c2a645, sid: 187029)
方式2: 饿了么联盟直连 (AppKey: 2ec59ae85af24f8da79e6bbe1f5d3312, AppSecret待提供)

优先使用折淘客代理（已有权限）
"""
import os
import sys
import json
import hashlib
import time
import requests

# 折淘客配置（优先使用环境变量）
ZHETAOKE_APPKEY = os.environ.get("ZHETAOKE_APPKEY", "8cbd7852d5fc4c04a956049683c2a645")
ZHETAOKE_SID = os.environ.get("ZHETAOKE_SID", "187029")
ELEME_ENDPOINT = "https://api.zhetaoke.com:10001/api/open_eleme_generateLink.ashx"

# 饿了么联盟直连配置
ELM_APPKEY = os.environ.get("ELEME_APPKEY", "2ec59ae85af24f8da79e6bbe1f5d3312")
ELM_APPSECRET = os.environ.get("ELEME_APPSECRET", "")  # ⚠️ 待提供，PDF标注"待提供"


def query_eleme_zhetaoke(keyword="", page=1, page_size=20):
    """
    通过折淘客代理查询饿了么商品/红包
    折淘客是饿了么的API代理，无需直连AppSecret
    """
    params = {
        "appkey": ZHETAOKE_APPKEY,
        "sid": ZHETAOKE_SID,
        "keyword": keyword,
        "page": page,
        "page_size": page_size,
    }
    try:
        resp = requests.get(ELEME_ENDPOINT, params=params, timeout=15)
        return resp.json()
    except requests.exceptions.Timeout:
        return {"error": "饿了么查询超时（折淘客代理）"}
    except requests.exceptions.ConnectionError:
        return {"error": "无法连接饿了么服务（折淘客代理）"}
    except Exception as e:
        return {"error": f"饿了么查询异常: {str(e)}"}


def get_eleme_coupons_zhetaoke():
    """
    通过折淘客获取饿了么可领红包
    """
    params = {
        "appkey": ZHETAOKE_APPKEY,
        "sid": ZHETAOKE_SID,
        "type": "coupon_list",
    }
    try:
        resp = requests.get(ELEME_ENDPOINT, params=params, timeout=15)
        data = resp.json()
        # 折淘客返回的result字段是JSON字符串，需二次解析
        if isinstance(data.get("result"), str):
            try:
                data["result"] = json.loads(data["result"])
            except json.JSONDecodeError:
                pass
        return data
    except Exception as e:
        return {"error": str(e)}


def generate_eleme_sign(params, app_secret):
    """
    饿了么联盟直连签名（备用，待AppSecret后启用）
    签名算法参考饿了么开放平台文档
    """
    if not app_secret:
        raise ValueError("饿了么AppSecret未配置")
    sorted_keys = sorted(params.keys())
    sign_str = ""
    for k in sorted_keys:
        if k != "sign" and params[k] is not None:
            sign_str += f"{k}{params[k]}"
    sign_str = app_secret + sign_str + app_secret
    return hashlib.md5(sign_str.encode("utf-8")).hexdigest().upper()


def query_eleme_direct(keyword="", page=1, page_size=20):
    """
    饿了么联盟直连查询（需要AppSecret）
    当前状态：⚠️ AppSecret待提供，请优先使用折淘客代理
    """
    if not ELM_APPSECRET:
        return {
            "error": "饿了么联盟直连AppSecret未配置",
            "hint": "请优先使用折淘客代理（query_eleme_zhetaoke），或提供AppSecret后启用直连",
            "status": "PENDING_APPSECRET"
        }
    # TODO: 饿了么联盟API直连签名逻辑
    params = {
        "app_key": ELM_APPKEY,
        "timestamp": int(time.time()),
        "keyword": keyword,
        "page_no": page,
        "page_size": page_size,
    }
    params["sign"] = generate_eleme_sign(params, ELM_APPSECRET)

    url = "https://openapi.ele.me/goods/search"
    try:
        resp = requests.get(url, params=params, timeout=15)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def format_result(data):
    """
    标准化饿了么返回数据
    兼容折淘客代理格式和饿了么直连格式
    """
    formatted = []

    # 折淘客代理返回格式
    result = data.get("result", {})
    if isinstance(result, str):
        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            result = {}

    items = result.get("items", result.get("data", []))
    if not items and isinstance(result, list):
        items = result

    for item in items[:10]:
        price = float(item.get("price", item.get("current_price", 0)))
        coupon = float(item.get("coupon_amount", item.get("coupon_money", 0)))
        after_price = round(price - coupon, 2)
        if after_price < 0:
            after_price = 0.01  # 最低0.01

        formatted.append({
            "platform": "饿了么",
            "title": item.get("title", item.get("name", item.get("goods_name", ""))),
            "price": price,
            "origin_price": float(item.get("origin_price", item.get("original_price", price))),
            "coupon_amount": coupon,
            "after_price": after_price,
            "url": item.get("url", item.get("link", item.get("h5_link", ""))),
            "shop": item.get("shop_name", item.get("shopName", item.get("store_name", ""))),
            "rating": float(item.get("rating", 0)),
            "monthly_sales": int(item.get("monthly_sales", item.get("sales", 0))),
        })
    return formatted


def get_status():
    """
    返回饿了么接口状态
    """
    return {
        "zhetaoke_proxy": {
            "available": True,
            "appkey": ZHETAOKE_APPKEY[:8] + "****" if ZHETAOKE_APPKEY else "未配置",
            "sid": ZHETAOKE_SID,
        },
        "eleme_direct": {
            "available": bool(ELM_APPSECRET),
            "appkey": ELM_APPKEY[:8] + "****" if ELM_APPKEY else "未配置",
            "status": "就绪" if ELM_APPSECRET else "⚠️ AppSecret待提供",
        }
    }


if __name__ == "__main__":
    keyword = sys.argv[1] if len(sys.argv) > 1 else "快餐"

    print("=" * 50)
    print("饿了么接口状态")
    print("=" * 50)
    print(json.dumps(get_status(), ensure_ascii=False, indent=2))
    print()

    print(f"=== 饿了么比价查询：{keyword} ===")
    data = query_eleme_zhetaoke(keyword)
    results = format_result(data)
    print(json.dumps(results, ensure_ascii=False, indent=2))
