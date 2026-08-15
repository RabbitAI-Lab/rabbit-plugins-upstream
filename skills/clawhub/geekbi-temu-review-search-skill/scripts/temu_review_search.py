#!/usr/bin/env python3
"""调用极鲸云的 Temu 评论搜索接口。"""

import argparse
import json
import sys
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode

from geekbi_auth import ActionRequired, authenticated_json_request, response_message


DEFAULT_BASE_URL = "https://openapi.geekbi.com"
ENDPOINT = "/api/v1/temu/review/ai-search"
ALLOWED_PARAMS = {
    "goodsId",
    "siteId",
    "skuId",
    "scoreMin",
    "scoreMax",
    "helpfulMin",
    "helpfulMax",
    "commentTimeMin",
    "commentTimeMax",
    "sort",
    "order",
    "page",
    "size",
}
SORT_FIELDS = {"commentTime", "helpful", "score", "createTime"}


def parse_int(label, value, minimum=None, maximum=None):
    try:
        parsed = int(value)
    except ValueError as error:
        raise ValueError(f"{label}必须是整数") from error
    if minimum is not None and parsed < minimum:
        raise ValueError(f"{label}不能小于 {minimum}")
    if maximum is not None and parsed > maximum:
        raise ValueError(f"{label}不能大于 {maximum}")
    return parsed


def parse_iso_datetime(value):
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("评论时间必须使用 ISO 8601 日期时间") from error


def parse_params(raw_params):
    params = []
    values = {}
    for raw_param in raw_params:
        if "=" not in raw_param:
            raise ValueError(f"查询条件必须使用 名称=值 格式: {raw_param}")
        key, value = raw_param.split("=", 1)
        if key not in ALLOWED_PARAMS:
            raise ValueError(f"当前评论搜索不支持该查询条件: {key}")
        if key in values:
            raise ValueError(f"评论查询条件不能重复: {key}")
        params.append((key, value))
        values[key] = value

    goods_id = values.get("goodsId", "").strip()
    if not goods_id:
        raise ValueError("商品 ID不能为空")
    if len(goods_id) > 100:
        raise ValueError("商品 ID不能超过 100 个字符")
    if "skuId" in values and len(values["skuId"]) > 100:
        raise ValueError("SKU ID不能超过 100 个字符")
    if "siteId" in values:
        parse_int("站点 ID", values["siteId"], minimum=1)

    score_min = parse_int("最低评分", values["scoreMin"], 1, 5) if "scoreMin" in values else None
    score_max = parse_int("最高评分", values["scoreMax"], 1, 5) if "scoreMax" in values else None
    if score_min is not None and score_max is not None and score_min > score_max:
        raise ValueError("最低评分不能大于最高评分")

    helpful_min = parse_int("最小有用数", values["helpfulMin"], minimum=0) if "helpfulMin" in values else None
    helpful_max = parse_int("最大有用数", values["helpfulMax"], minimum=0) if "helpfulMax" in values else None
    if helpful_min is not None and helpful_max is not None and helpful_min > helpful_max:
        raise ValueError("最小有用数不能大于最大有用数")

    for key in ("commentTimeMin", "commentTimeMax"):
        if key in values:
            parse_iso_datetime(values[key])
    if "commentTimeMin" in values and "commentTimeMax" in values:
        start = datetime.fromisoformat(values["commentTimeMin"].replace("Z", "+00:00"))
        end = datetime.fromisoformat(values["commentTimeMax"].replace("Z", "+00:00"))
        try:
            invalid_range = start > end
        except TypeError as error:
            raise ValueError("评论时间上下限必须使用一致的时区格式") from error
        if invalid_range:
            raise ValueError("最早评论时间不能晚于最晚评论时间")

    if "sort" in values and values["sort"] not in SORT_FIELDS:
        raise ValueError(f"当前评论搜索不支持该排序方式: {values['sort']}")
    if "order" in values and values["order"] not in ("asc", "desc"):
        raise ValueError("排序方向只支持升序或降序")

    page = parse_int("页码", values.get("page", "1"), minimum=1)
    size = parse_int("每页数量", values.get("size", "20"), minimum=1, maximum=200)
    if page * size > 10000:
        raise ValueError("评论查询最多翻到前 10000 条，请缩小筛选范围")
    return params


def build_url(base_url, params):
    query = urlencode(params)
    return f"{base_url.rstrip('/')}{ENDPOINT}?{query}"


def validate_response(payload):
    if not isinstance(payload, dict):
        raise ValueError("接口响应必须是 JSON 对象")
    if payload.get("code") != 0:
        raise ValueError(response_message(payload, "评论查询失败"))
    data = payload.get("data")
    if not isinstance(data, dict):
        raise ValueError("成功响应缺少数据对象")
    if not isinstance(data.get("total"), int) or not isinstance(data.get("list"), list):
        raise ValueError("评论响应数据格式不完整")
    return {"code": 0, "data": data}


def main():
    parser = argparse.ArgumentParser(description="按商品查询 Temu 评论并输出 JSON")
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"极鲸云服务地址，默认 {DEFAULT_BASE_URL}",
    )
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        help="查询条件，格式为 名称=值；必须传入商品 ID",
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
