#!/usr/bin/env python3
"""调用极鲸云的 SHEIN 关键词搜索接口。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from geekbi_auth import ActionRequired, authenticated_json_request
from shein_search_common import (
    DEFAULT_BASE_URL,
    build_url,
    parse_int,
    parse_pairs,
    validate_page,
    validate_range_pairs,
    validate_search_response,
    validate_sort,
)


ENDPOINT = "/api/v1/shein/keyword/ai-search"
BASE_PARAMS = {"keyword", "catIds", "siteId", "page", "size", "sort", "order"}
NUMERIC_RANGE_PARAMS = {
    "dsr",
    "totalSold",
    "avgPrice",
    "totalSales",
    "itemCount",
    "semiManagedItemCount",
    "mallCount",
    "semiManagedMallCount",
    "sold",
    "sales",
    "daySold",
    "weekSold",
    "monthSold",
    "daySoldRate",
    "weekSoldRate",
    "monthSoldRate",
    "daySales",
    "weekSales",
    "monthSales",
    "daySalesRate",
    "weekSalesRate",
    "monthSalesRate",
    "dayItemCount",
    "weekItemCount",
    "monthItemCount",
    "dayItemCountRate",
    "weekItemCountRate",
    "monthItemCountRate",
    "dayMallCount",
    "weekMallCount",
    "monthMallCount",
    "dayMallCountRate",
    "weekMallCountRate",
    "monthMallCountRate",
}
INTEGER_RANGE_PARAMS = {
    "totalSold",
    "itemCount",
    "semiManagedItemCount",
    "mallCount",
    "semiManagedMallCount",
    "sold",
    "daySold",
    "weekSold",
    "monthSold",
    "dayItemCount",
    "weekItemCount",
    "monthItemCount",
    "dayMallCount",
    "weekMallCount",
    "monthMallCount",
}
NONNEGATIVE_RANGE_PARAMS = {
    "dsr",
    "totalSold",
    "avgPrice",
    "totalSales",
    "itemCount",
    "semiManagedItemCount",
    "mallCount",
    "semiManagedMallCount",
    "sold",
    "sales",
    "daySold",
    "weekSold",
    "monthSold",
    "daySales",
    "weekSales",
    "monthSales",
    "dayItemCount",
    "weekItemCount",
    "monthItemCount",
    "dayMallCount",
    "weekMallCount",
    "monthMallCount",
}
DATE_RANGE_PARAMS = {"firstOnSaleTime"}
ALLOWED_PARAMS = BASE_PARAMS | {
    f"{field}{suffix}"
    for field in NUMERIC_RANGE_PARAMS | DATE_RANGE_PARAMS
    for suffix in ("Min", "Max")
}
SORT_FIELDS = NUMERIC_RANGE_PARAMS | DATE_RANGE_PARAMS | {"createTime", "updateTime"}


def parse_params(raw_params):
    params, values, repeated = parse_pairs(
        raw_params,
        ALLOWED_PARAMS,
        repeated_params={"catIds"},
    )
    if len(values.get("keyword", "")) > 300:
        raise ValueError("关键词不能超过 300 个字符")
    if "siteId" in values:
        parse_int("站点 ID", values["siteId"], minimum=1)
    for value in repeated["catIds"]:
        parse_int("类目 ID", value, minimum=1)
    validate_page(values)
    validate_sort(values, SORT_FIELDS)
    validate_range_pairs(
        values,
        NUMERIC_RANGE_PARAMS,
        DATE_RANGE_PARAMS,
        INTEGER_RANGE_PARAMS,
        NONNEGATIVE_RANGE_PARAMS,
    )
    return params


def main():
    parser = argparse.ArgumentParser(description="查询 SHEIN 关键词并输出 JSON")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--param", action="append", default=[], help="名称=值；类目可重复传入")
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()

    try:
        params = parse_params(args.param)
        payload = authenticated_json_request(
            build_url(args.base_url, ENDPOINT, params),
            args.base_url,
            args.timeout,
        )
        payload = validate_search_response(payload, "关键词查询失败")
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
