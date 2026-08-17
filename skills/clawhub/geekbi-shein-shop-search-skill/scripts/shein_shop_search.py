#!/usr/bin/env python3
"""调用极鲸云的 SHEIN 店铺搜索接口。"""

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


ENDPOINT = "/api/v1/shein/mall/ai-search"
BASE_PARAMS = {
    "keyword",
    "catIds",
    "siteId",
    "hostingMode",
    "page",
    "size",
    "sort",
    "order",
}
NUMERIC_RANGE_PARAMS = {
    "mallSold",
    "mallSales",
    "totalSold",
    "totalSales",
    "mallStar",
    "reviewNum",
    "goodsNum",
    "followerNum",
    "avgPrice",
    "daySold",
    "weekSold",
    "monthSold",
    "daySales",
    "weekSales",
    "monthSales",
    "daySoldRate",
    "weekSoldRate",
    "monthSoldRate",
    "daySalesRate",
    "weekSalesRate",
    "monthSalesRate",
    "dayItemCount",
    "weekItemCount",
    "monthItemCount",
    "dayItemCountRate",
    "weekItemCountRate",
    "monthItemCountRate",
    "dayFollower",
    "weekFollower",
    "monthFollower",
    "dayFollowerRate",
    "weekFollowerRate",
    "monthFollowerRate",
}
INTEGER_RANGE_PARAMS = {
    "mallSold",
    "totalSold",
    "reviewNum",
    "goodsNum",
    "followerNum",
    "daySold",
    "weekSold",
    "monthSold",
    "dayItemCount",
    "weekItemCount",
    "monthItemCount",
    "dayFollower",
    "weekFollower",
    "monthFollower",
}
NONNEGATIVE_RANGE_PARAMS = {
    "mallSold",
    "mallSales",
    "mallStar",
    "reviewNum",
    "goodsNum",
    "followerNum",
    "avgPrice",
    "daySold",
    "weekSold",
    "monthSold",
    "totalSold",
    "daySales",
    "weekSales",
    "monthSales",
    "totalSales",
    "dayItemCount",
    "weekItemCount",
    "monthItemCount",
    "dayFollower",
    "weekFollower",
    "monthFollower",
}
DATE_RANGE_PARAMS = {"mallOpenTime"}
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
        raise ValueError("店铺关键词不能超过 300 个字符")
    if "siteId" in values:
        parse_int("站点 ID", values["siteId"], minimum=1)
    if "hostingMode" in values:
        parse_int("托管模式", values["hostingMode"], minimum=0, maximum=2)
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
    parser = argparse.ArgumentParser(description="查询 SHEIN 店铺并输出 JSON")
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
        payload = validate_search_response(payload, "店铺查询失败")
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
