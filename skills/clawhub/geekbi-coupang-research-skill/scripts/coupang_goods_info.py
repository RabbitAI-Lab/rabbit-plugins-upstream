#!/usr/bin/env python3
"""查询 Coupang 商品、规格和近 31 条历史。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from geekbi_auth import ActionRequired, authenticated_json_request
from coupang_search_common import DEFAULT_BASE_URL, build_url, validate_object_response


ENDPOINT = "/api/v1/coupang/goods/ai-info"


def build_params(product_id, item_id, site_id):
    if not product_id.strip():
        raise ValueError("商品 ID 不能为空")
    if site_id != 1:
        raise ValueError("Coupang 当前仅支持韩国站，siteId=1")
    params = [("productId", product_id.strip()), ("siteId", str(site_id))]
    if item_id:
        if not item_id.strip():
            raise ValueError("规格 ID 不能为空")
        params.append(("itemId", item_id.strip()))
    return params


def validate_response(payload):
    result = validate_object_response(payload, "goods", "Coupang 商品详情查询失败")
    data = result["data"]
    if not isinstance(data.get("items"), list) or not isinstance(data.get("history"), list):
        raise ValueError("成功响应缺少 items 或 history 数组")
    if "itemHistory" in data and not isinstance(data["itemHistory"], list):
        raise ValueError("itemHistory 必须是数组")
    return result


def main():
    parser = argparse.ArgumentParser(description="查询 Coupang 商品详情、规格与历史")
    parser.add_argument("--product-id", required=True, help="Coupang productId")
    parser.add_argument("--item-id", help="可选；传入后返回该规格及规格历史")
    parser.add_argument("--site-id", type=int, default=1)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        params = build_params(args.product_id, args.item_id, args.site_id)
        payload = authenticated_json_request(
            build_url(args.base_url, ENDPOINT, params), args.base_url, args.timeout
        )
        payload = validate_response(payload)
    except ActionRequired as error:
        print(json.dumps(error.public_payload(), ensure_ascii=False, indent=2))
        return 2
    except (ValueError, HTTPError, URLError, TimeoutError) as error:
        print(json.dumps({"error": True, "msg": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
