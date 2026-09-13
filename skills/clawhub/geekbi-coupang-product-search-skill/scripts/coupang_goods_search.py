#!/usr/bin/env python3
"""调用极鲸云 Coupang 商品搜索接口。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from geekbi_auth import ActionRequired, authenticated_json_request
from coupang_search_common import (
    DEFAULT_BASE_URL,
    build_url,
    parse_int,
    parse_number,
    parse_pairs,
    validate_page,
    validate_range_pairs,
    validate_search_response,
    validate_site,
    validate_sort,
)


ENDPOINT = "/api/v1/coupang/goods/ai-search"
BASE_PARAMS = {
    "keyword", "categoryId", "categoryPath", "categoryPathPrefix", "leafCategoryCode",
    "rootCategoryCode", "displayDeliveryMethod", "siteId", "page", "size", "sort", "order",
}
NUMERIC_RANGE_PARAMS = {"price", "rating", "ratingCount", "pvLast28Day", "salesLast28d"}
INTEGER_RANGE_PARAMS = {"ratingCount", "pvLast28Day", "salesLast28d"}
DATE_RANGE_PARAMS = {"onSaleTime", "createTime", "updateTime"}
ALLOWED_PARAMS = BASE_PARAMS | {
    f"{field}{suffix}"
    for field in NUMERIC_RANGE_PARAMS | DATE_RANGE_PARAMS
    for suffix in ("Min", "Max")
}
SORT_FIELDS = {
    "updateTime", "minItemPrice", "maxItemPrice", "itemCount", "sellerCount",
    "rating", "ratingCount", "pvLast28Day", "salesLast28d", "createTime",
}
DELIVERY_METHODS = {"NORMAL", "ROCKET", "ROCKET_MERCHANT", "COUPANG_GLOBAL", "ROCKET_FRESH"}


def parse_params(raw_params):
    params, values = parse_pairs(raw_params, ALLOWED_PARAMS)
    if len(values.get("keyword", "")) > 300:
        raise ValueError("商品关键词不能超过 300 个字符")
    for field in ("categoryId", "categoryPath", "categoryPathPrefix", "leafCategoryCode", "rootCategoryCode"):
        if len(values.get(field, "")) > 500:
            raise ValueError(f"{field} 不能超过 500 个字符")
    validate_site(values)
    if "displayDeliveryMethod" in values and values["displayDeliveryMethod"] not in DELIVERY_METHODS:
        raise ValueError("displayDeliveryMethod 不在当前支持的配送标记中")
    validate_page(values)
    validate_sort(values, SORT_FIELDS)
    validate_range_pairs(values, NUMERIC_RANGE_PARAMS, DATE_RANGE_PARAMS, INTEGER_RANGE_PARAMS)
    for field in ("ratingMin", "ratingMax"):
        if field in values and not 0 <= parse_number(field, values[field]) <= 5:
            raise ValueError(f"{field} 必须在 0 到 5 之间")
    return params


def main():
    parser = argparse.ArgumentParser(description="查询 Coupang 商品并输出 JSON")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--param", action="append", default=[], help="查询条件，格式为 名称=值")
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        params = parse_params(args.param)
        payload = authenticated_json_request(
            build_url(args.base_url, ENDPOINT, params), args.base_url, args.timeout
        )
        payload = validate_search_response(payload, "Coupang 商品查询失败")
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
