#!/usr/bin/env python3
"""查询 Coupang 类目的完整父链。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from geekbi_auth import ActionRequired, authenticated_json_request
from coupang_search_common import DEFAULT_BASE_URL, build_url, parse_int, validate_envelope


ENDPOINT = "/api/v1/coupang/category/ai-info"


def build_params(category_id, site_id):
    parse_int("类目 ID", str(category_id), minimum=1)
    if site_id != 1:
        raise ValueError("Coupang 当前仅支持韩国站，siteId=1")
    return [("displayItemCategoryId", str(category_id)), ("siteId", str(site_id))]


def validate_response(payload):
    data = validate_envelope(payload, "Coupang 类目路径查询失败")
    if not isinstance(data, dict) or not isinstance(data.get("site"), dict):
        raise ValueError("成功响应缺少站点信息")
    if not isinstance(data.get("path"), list):
        raise ValueError("成功响应缺少类目路径")
    return {"code": 0, "data": data}


def main():
    parser = argparse.ArgumentParser(description="查询 Coupang 类目路径")
    parser.add_argument("--category-id", type=int, required=True, help="displayItemCategoryId")
    parser.add_argument("--site-id", type=int, default=1)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        params = build_params(args.category_id, args.site_id)
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
