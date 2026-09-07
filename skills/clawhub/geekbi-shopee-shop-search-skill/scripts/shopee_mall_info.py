#!/usr/bin/env python3
"""查询 Shopee 店铺详情。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from shopee_search_common import DEFAULT_BASE_URL, build_url, parse_int, validate_object_response
from geekbi_auth import ActionRequired, authenticated_json_request


ENDPOINT = "/api/v1/shopee/mall/ai-info"


def build_params(mall_id, site_id):
    if not mall_id.strip():
        raise ValueError("店铺 ID 不能为空")
    parse_int("站点 ID", str(site_id), minimum=1)
    return [("mallId", mall_id.strip()), ("siteId", str(site_id))]


def main():
    parser = argparse.ArgumentParser(description="查询 Shopee 店铺详情")
    parser.add_argument("--mall-id", required=True, help="Shopee 店铺或卖家 ID")
    parser.add_argument("--site-id", type=int, default=1)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        params = build_params(args.mall_id, args.site_id)
        payload = authenticated_json_request(
            build_url(args.base_url, ENDPOINT, params), args.base_url, args.timeout
        )
        payload = validate_object_response(payload, "mall", "Shopee 店铺查询失败")
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
