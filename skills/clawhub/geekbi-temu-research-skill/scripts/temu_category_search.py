#!/usr/bin/env python3
"""调用极鲸云的 Temu 类目搜索接口。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode

from geekbi_auth import ActionRequired, authenticated_json_request, response_message


DEFAULT_BASE_URL = "https://openapi.geekbi.com"
ENDPOINT = "/api/v1/temu/category/ai-search"
BASE_PARAMS = {
    "keyword",
    "siteId",
    "catLevel",
    "parentCatId",
    "page",
    "size",
    "sort",
    "order",
}
RANGE_PARAMS = {
    "dsr",
    "totalSold",
    "avgPrice",
    "totalSales",
    "itemCount",
    "semiManagedItemCount",
    "mallCount",
    "semiManagedMallCount",
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
SORT_FIELDS = RANGE_PARAMS | {"catLevel", "createTime", "updateTime"}
INTEGER_PARAMS = {
    "siteId",
    "catLevel",
    "parentCatId",
    "page",
    "size",
}


def is_allowed_param(key):
    if key in BASE_PARAMS:
        return True
    return any(key == f"{prefix}{suffix}" for prefix in RANGE_PARAMS for suffix in ("Min", "Max"))


def parse_positive_int(label, value, maximum=None):
    try:
        parsed = int(value)
    except ValueError as error:
        raise ValueError(f"{label}必须是整数") from error
    if parsed < 1:
        raise ValueError(f"{label}必须大于等于 1")
    if maximum is not None and parsed > maximum:
        raise ValueError(f"{label}最大值为 {maximum}")


def parse_nonnegative_int(label, value):
    try:
        parsed = int(value)
    except ValueError as error:
        raise ValueError(f"{label}必须是整数") from error
    if parsed < 0:
        raise ValueError(f"{label}必须大于等于 0")


def parse_number(label, value):
    try:
        float(value)
    except ValueError as error:
        raise ValueError(f"{label}必须是数字") from error


def parse_params(raw_params):
    params = []
    single_values = {}
    for raw_param in raw_params:
        if "=" not in raw_param:
            raise ValueError(f"查询条件必须使用 名称=值 格式: {raw_param}")
        key, value = raw_param.split("=", 1)
        if not key:
            raise ValueError("查询条件名不能为空")
        if not is_allowed_param(key):
            raise ValueError(f"当前类目搜索不支持该查询条件: {key}")
        params.append((key, value))
        single_values[key] = value

    if "sort" in single_values and single_values["sort"] not in SORT_FIELDS:
        raise ValueError(f"当前类目搜索不支持该排序方式: {single_values['sort']}")
    if "order" in single_values and single_values["order"] not in ("asc", "desc"):
        raise ValueError("排序方向只支持升序或降序")
    if "keyword" in single_values and len(single_values["keyword"]) > 300:
        raise ValueError("类目关键词不能超过 300 个字符")

    integer_labels = {
        "siteId": "站点 ID",
        "catLevel": "类目层级",
        "parentCatId": "父类目 ID",
        "page": "页码",
        "size": "每页数量",
    }
    for key in INTEGER_PARAMS.intersection(single_values):
        if key == "parentCatId":
            parse_nonnegative_int(integer_labels[key], single_values[key])
            continue
        maximum = 200 if key == "size" else None
        if key == "catLevel":
            maximum = 4
        parse_positive_int(integer_labels[key], single_values[key], maximum)

    for key, value in single_values.items():
        if any(key == f"{prefix}{suffix}" for prefix in RANGE_PARAMS for suffix in ("Min", "Max")):
            parse_number("区间筛选值", value)
    return params


def build_url(base_url, params):
    url = f"{base_url.rstrip('/')}{ENDPOINT}"
    query = urlencode(params)
    return f"{url}?{query}" if query else url


def validate_response(payload):
    if not isinstance(payload, dict):
        raise ValueError("接口响应必须是 JSON 对象")
    if payload.get("code") != 0:
        raise ValueError(response_message(payload, "类目查询失败"))
    if not isinstance(payload.get("data"), dict):
        raise ValueError("成功响应缺少数据对象")
    return {"code": 0, "data": payload["data"]}


def main():
    parser = argparse.ArgumentParser(description="查询 Temu 类目并输出 JSON")
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"极鲸云服务地址，默认 {DEFAULT_BASE_URL}",
    )
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        help="查询条件，格式为 名称=值",
    )
    parser.add_argument("--timeout", type=float, default=30, help="请求超时秒数")
    args = parser.parse_args()

    try:
        params = parse_params(args.param)
        payload = authenticated_json_request(
            build_url(args.base_url, params),
            args.base_url,
            args.timeout,
        )
        payload = validate_response(payload)
    except ActionRequired as error:
        print(json.dumps(error.public_payload(), ensure_ascii=False, indent=2))
        return 2
    except (ValueError, HTTPError, URLError, TimeoutError) as error:
        print(
            json.dumps({"error": True, "msg": str(error)}, ensure_ascii=False),
            file=sys.stderr,
        )
        return 1

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
