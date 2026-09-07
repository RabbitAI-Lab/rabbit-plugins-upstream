#!/usr/bin/env python3
"""调用极鲸云 Shopee AI 商品搜索接口。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from shopee_search_common import (
    DEFAULT_BASE_URL,
    build_url,
    parse_boolean,
    parse_int,
    parse_pairs,
    validate_page,
    validate_range_pairs,
    validate_search_response,
    validate_sort,
)
from geekbi_auth import ActionRequired, authenticated_json_request


ENDPOINT = "/api/v1/shopee/goods/ai-search"
BASE_PARAMS = {"keyword", "catId", "siteId", "isCross", "page", "size", "sort", "order"}
NUMERIC_RANGE_PARAMS = {
    "monthSold", "monthSales", "totalSold", "totalSales",
    "price", "goodsScore", "reviewNum",
}
INTEGER_RANGE_PARAMS = {"monthSold", "totalSold", "reviewNum"}
DATE_RANGE_PARAMS = {"onSaleTime", "mallOpenTime"}
ALLOWED_PARAMS = BASE_PARAMS | {
    f"{field}{suffix}"
    for field in NUMERIC_RANGE_PARAMS | DATE_RANGE_PARAMS
    for suffix in ("Min", "Max")
}
SORT_FIELDS = {
    "monthSold", "monthSales", "goodsScore", "reviewNum",
    "onSaleTime", "mallOpenTime",
    "totalSold", "totalSales",
}


def parse_params(raw_params):
    params, values = parse_pairs(raw_params, ALLOWED_PARAMS)
    if len(values.get("keyword", "")) > 300:
        raise ValueError("商品关键词不能超过 300 个字符")
    if "siteId" in values:
        parse_int("站点 ID", values["siteId"], minimum=1)
    if "isCross" in values:
        parse_boolean("isCross", values["isCross"])
    validate_page(values)
    validate_sort(values, SORT_FIELDS)
    validate_range_pairs(values, NUMERIC_RANGE_PARAMS, DATE_RANGE_PARAMS, INTEGER_RANGE_PARAMS)
    return params


def main():
    parser = argparse.ArgumentParser(description="查询 Shopee 商品并输出 JSON")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--param", action="append", default=[], help="查询条件，格式为 名称=值")
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        params = parse_params(args.param)
        payload = authenticated_json_request(
            build_url(args.base_url, ENDPOINT, params), args.base_url, args.timeout
        )
        payload = validate_search_response(payload)
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
