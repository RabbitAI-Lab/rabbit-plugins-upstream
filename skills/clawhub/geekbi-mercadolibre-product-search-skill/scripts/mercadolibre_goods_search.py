#!/usr/bin/env python3
"""调用极鲸云 Mercado Libre AI 商品搜索接口。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from geekbi_auth import ActionRequired, authenticated_json_request
from mercadolibre_search_common import (
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


ENDPOINT = "/api/v1/mercadolibre/goods/ai-search"
BASE_PARAMS = {
    "keyword", "catId", "siteId", "shippedFrom", "full", "crossBorder",
    "page", "size", "sort", "order",
}
NUMERIC_RANGE_PARAMS = {
    "totalSold", "totalSales", "price", "goodsScore", "reviewNum", "mallSold",
}
INTEGER_RANGE_PARAMS = {"totalSold", "reviewNum", "mallSold"}
DATE_RANGE_PARAMS = {"onSaleTime", "mallOpenTime"}
ALLOWED_PARAMS = BASE_PARAMS | {
    f"{field}{suffix}"
    for field in NUMERIC_RANGE_PARAMS | DATE_RANGE_PARAMS
    for suffix in ("Min", "Max")
}
SORT_FIELDS = {
    "updateTime", "daySold", "totalSold", "totalSales",
    "price", "goodsScore", "reviewNum", "onSaleTime", "mallOpenTime", "mallSold",
}


def parse_params(raw_params):
    params, values = parse_pairs(raw_params, ALLOWED_PARAMS)
    if len(values.get("keyword", "")) > 300:
        raise ValueError("商品关键词不能超过 300 个字符")
    if len(values.get("shippedFrom", "")) > 100:
        raise ValueError("发货地不能超过 100 个字符")
    if "siteId" in values:
        parse_int("站点 ID", values["siteId"], minimum=1)
    for field in ("full", "crossBorder"):
        if field in values:
            parse_boolean(field, values[field])
    validate_page(values)
    validate_sort(values, SORT_FIELDS)
    validate_range_pairs(values, NUMERIC_RANGE_PARAMS, DATE_RANGE_PARAMS, INTEGER_RANGE_PARAMS)
    return params


def main():
    parser = argparse.ArgumentParser(description="查询 Mercado Libre 商品并输出 JSON")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--param", action="append", default=[], help="查询条件，格式为 名称=值")
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        params = parse_params(args.param)
        payload = authenticated_json_request(
            build_url(args.base_url, ENDPOINT, params), args.base_url, args.timeout
        )
        payload = validate_search_response(payload, "Mercado Libre 商品查询失败")
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
