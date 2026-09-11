#!/usr/bin/env python3
"""查询 Mercado Libre 商品详情、近 31 条历史和关联店铺。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from geekbi_auth import ActionRequired, authenticated_json_request
from mercadolibre_search_common import DEFAULT_BASE_URL, build_url, parse_int, validate_object_response


ENDPOINT = "/api/v1/mercadolibre/goods/ai-info"


def build_params(goods_id, site_id):
    if not goods_id.strip():
        raise ValueError("商品 ID 不能为空")
    parse_int("站点 ID", str(site_id), minimum=1)
    return [("goodsId", goods_id.strip()), ("siteId", str(site_id))]


def validate_response(payload):
    result = validate_object_response(payload, "goods", "Mercado Libre 商品详情查询失败")
    if not isinstance(result["data"].get("history"), list):
        raise ValueError("成功响应缺少 history 数组")
    return result


def main():
    parser = argparse.ArgumentParser(description="查询 Mercado Libre 商品详情与历史")
    parser.add_argument("--goods-id", required=True, help="Mercado Libre 商品 ID")
    parser.add_argument("--site-id", type=int, default=1)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        params = build_params(args.goods_id, args.site_id)
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
