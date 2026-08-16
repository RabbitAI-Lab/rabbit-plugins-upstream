#!/usr/bin/env python3
"""调用极鲸云公开的 Temu AI 商品搜索接口。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode

from geekbi_auth import ActionRequired, authenticated_json_request, response_message


DEFAULT_BASE_URL = "https://openapi.geekbi.com"
ENDPOINT = "/api/v1/temu/goods/ai-search"
BASE_PARAMS = {
    "keyword",
    "catIds",
    "siteId",
    "page",
    "size",
    "sort",
    "order",
    "hostingMode",
}
RANGE_PARAMS = {
    "sold",
    "daySold",
    "weekSold",
    "monthSold",
    "daySoldRate",
    "weekSoldRate",
    "monthSoldRate",
    "sales",
    "daySales",
    "weekSales",
    "monthSales",
    "daySalesRate",
    "weekSalesRate",
    "monthSalesRate",
    "quantity",
    "mallSold",
    "similarNum",
    "price",
    "supplyPrice",
    "goodsScore",
    "reviewNum",
    "onSaleTime",
    "mallOpenTime",
}


def is_allowed_param(key):
    if key in BASE_PARAMS:
        return True
    return any(key == f"{prefix}{suffix}" for prefix in RANGE_PARAMS for suffix in ("Min", "Max"))


def parse_params(raw_params):
    params = []
    for raw_param in raw_params:
        if "=" not in raw_param:
            raise ValueError(f"参数必须使用 key=value 格式: {raw_param}")
        key, value = raw_param.split("=", 1)
        if not key:
            raise ValueError(f"参数名不能为空: {raw_param}")
        if not is_allowed_param(key):
            raise ValueError(f"当前商品搜索 Skill 不支持参数: {key}")
        if key == "siteId":
            try:
                site_id = int(value)
            except ValueError as error:
                raise ValueError("站点 ID 必须是整数") from error
            if site_id < 1:
                raise ValueError("站点 ID 必须大于等于 1")
        params.append((key, value))
    return params


def build_url(base_url, params):
    url = f"{base_url.rstrip('/')}{ENDPOINT}"
    query = urlencode(params)
    return f"{url}?{query}" if query else url


def validate_response(payload):
    if not isinstance(payload, dict):
        raise ValueError("接口响应必须是 JSON 对象")
    if payload.get("code") != 0:
        raise ValueError(response_message(payload, "接口返回失败"))
    if not isinstance(payload.get("data"), dict):
        raise ValueError("成功响应缺少 data 对象")
    return {"code": 0, "data": payload["data"]}


def main():
    parser = argparse.ArgumentParser(description="查询 Temu 商品并输出 JSON")
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"极鲸云服务地址，默认 {DEFAULT_BASE_URL}",
    )
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        help="查询参数，格式为 key=value；列表字段可重复传入",
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
