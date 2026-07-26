#!/usr/bin/env python3
"""
好单库 - 淘宝商品搜索脚本
API文档: http://v2.api.haodanku.com
接口: /supersearch/apikey/{apikey}/keyword/{keyword}/back/{back}/min_id/{min_id}
注意: 关键词需两次URL编码；需联系好单库开通supersearch权限
"""
import os
import sys
import json
import urllib.parse
import requests

APIKEY = os.environ.get("HAODANKU_APIKEY", "F52D1486CC51")
BASE_URL = "http://v2.api.haodanku.com"


def double_url_encode(keyword):
    """关键词两次URL编码（好单库要求）"""
    return urllib.parse.quote(urllib.parse.quote(keyword, safe=""), safe="")


def query_taobao(keyword, back=20, min_id=1):
    """
    搜索淘宝商品
    :param keyword: 搜索关键词
    :param back: 返回数量，仅支持 1/2/5/10/20/50/100
    :param min_id: 分页ID，首次传1
    :return: API原始响应
    """
    if back not in [1, 2, 5, 10, 20, 50, 100]:
        back = 20  # 默认值

    encoded_keyword = double_url_encode(keyword)
    path = f"/supersearch/apikey/{APIKEY}/keyword/{encoded_keyword}/back/{back}/min_id/{min_id}"
    url = BASE_URL + path

    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        return {"error": "好单库查询超时", "code": -1}
    except requests.exceptions.ConnectionError:
        return {"error": "无法连接好单库服务", "code": -1}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP错误: {e.response.status_code}", "code": -1}
    except json.JSONDecodeError:
        return {"error": "好单库返回格式异常", "code": -1}
    except Exception as e:
        return {"error": f"好单库查询异常: {str(e)}", "code": -1}


def format_result(data):
    """
    标准化输出格式
    兼容好单库supersearch和普通search两种返回格式
    """
    results = []

    # 错误处理
    if data.get("error"):
        return results

    if data.get("code") != 200 and data.get("code") != 0 and data.get("code") != 1:
        return results

    items = data.get("data", [])
    # data可能是列表（supersearch）或字典含content字段
    if isinstance(items, dict):
        items = items.get("content", items.get("items", []))
    if not isinstance(items, list):
        return results

    for item in items[:10]:
        price = float(item.get("itemprice", item.get("price", 0)))
        coupon_money = float(item.get("couponmoney", item.get("coupon_money", 0)))
        after_price = round(price - coupon_money, 2)
        if after_price < 0:
            after_price = 0.01

        results.append({
            "platform": "淘宝",
            "title": item.get("itemtitle", item.get("title", "")),
            "price": price,
            "coupon_money": coupon_money,
            "after_price": after_price,
            "url": item.get("coupon_link", item.get("itemurl", "")),
            "shop": item.get("shopname", item.get("shop_title", "")),
            "sales": int(item.get("itemsale", item.get("volume", 0))),
            "image": item.get("itempic", item.get("pic_url", "")),
        })
    return results


if __name__ == "__main__":
    keyword = sys.argv[1] if len(sys.argv) > 1 else "手机"
    print(f"🔍 好单库搜索: {keyword}")
    data = query_taobao(keyword)
    results = format_result(data)
    print(f"共找到 {len(results)} 条结果\n")
    print(json.dumps(results, ensure_ascii=False, indent=2))
