#!/usr/bin/env python3
"""查询 Mercado Libre 当前 ES 商品样本中的直接子类目。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from geekbi_auth import ActionRequired, authenticated_json_request
from mercadolibre_search_common import DEFAULT_BASE_URL, build_url, parse_int, validate_envelope


ENDPOINT = "/api/v1/mercadolibre/category/ai-list"


def build_params(parent_cat_id, site_id):
    if not parent_cat_id.strip():
        raise ValueError("父类目 ID 不能为空")
    parse_int("站点 ID", str(site_id), minimum=1)
    return [("parentCatId", parent_cat_id.strip()), ("siteId", str(site_id))]


def validate_response(payload):
    data = validate_envelope(payload, "Mercado Libre 类目列表查询失败")
    if not isinstance(data, dict) or not isinstance(data.get("site"), dict):
        raise ValueError("成功响应缺少站点信息")
    if not isinstance(data.get("list"), list):
        raise ValueError("成功响应缺少类目列表")
    return {"code": 0, "data": data}


def main():
    parser = argparse.ArgumentParser(description="查询 Mercado Libre 子类目")
    parser.add_argument("--parent-cat-id", default="0")
    parser.add_argument("--site-id", type=int, default=1)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        params = build_params(args.parent_cat_id, args.site_id)
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
