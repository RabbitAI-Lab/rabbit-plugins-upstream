#!/usr/bin/env python3
"""SHEIN 查询脚本共用的参数、请求与响应校验。"""

from datetime import datetime
from math import isfinite
from urllib.parse import urlencode

from geekbi_auth import response_message


DEFAULT_BASE_URL = "https://openapi.geekbi.com"


def parse_pairs(raw_params, allowed_params, repeated_params=()):
    params = []
    values = {}
    repeated = {key: [] for key in repeated_params}
    for raw_param in raw_params:
        if "=" not in raw_param:
            raise ValueError(f"查询条件必须使用 名称=值 格式: {raw_param}")
        key, value = raw_param.split("=", 1)
        if not key:
            raise ValueError("查询条件名不能为空")
        if key not in allowed_params:
            raise ValueError(f"当前查询不支持该条件: {key}")
        if key in repeated:
            repeated[key].append(value)
        elif key in values:
            raise ValueError(f"查询条件不能重复: {key}")
        else:
            values[key] = value
        params.append((key, value))
    return params, values, repeated


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


def parse_number(label, value):
    try:
        parsed = float(value)
    except ValueError as error:
        raise ValueError(f"{label}必须是数字") from error
    if not isfinite(parsed):
        raise ValueError(f"{label}必须是有限数字")
    return parsed


def parse_iso_datetime(label, value):
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"{label}必须使用 ISO 8601 日期时间") from error
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{label}必须包含时区偏移")
    return parsed


def validate_range_pairs(
    values,
    numeric_fields=(),
    date_fields=(),
    integer_fields=(),
    nonnegative_fields=(),
):
    nonnegative_fields = set(nonnegative_fields)
    for field in numeric_fields:
        minimum = values.get(f"{field}Min")
        maximum = values.get(f"{field}Max")
        parser = parse_int if field in integer_fields else parse_number
        parsed_min = parser(f"{field}Min", minimum) if minimum is not None else None
        parsed_max = parser(f"{field}Max", maximum) if maximum is not None else None
        if field in nonnegative_fields:
            if parsed_min is not None and parsed_min < 0:
                raise ValueError(f"{field}Min 不能小于 0")
            if parsed_max is not None and parsed_max < 0:
                raise ValueError(f"{field}Max 不能小于 0")
        if parsed_min is not None and parsed_max is not None and parsed_min > parsed_max:
            raise ValueError(f"{field} 的最小值不能大于最大值")

    for field in date_fields:
        minimum = values.get(f"{field}Min")
        maximum = values.get(f"{field}Max")
        parsed_min = parse_iso_datetime(f"{field}Min", minimum) if minimum is not None else None
        parsed_max = parse_iso_datetime(f"{field}Max", maximum) if maximum is not None else None
        if parsed_min is not None and parsed_max is not None:
            try:
                invalid = parsed_min > parsed_max
            except TypeError as error:
                raise ValueError(f"{field} 上下限必须使用一致的时区格式") from error
            if invalid:
                raise ValueError(f"{field} 的最早时间不能晚于最晚时间")


def validate_page(values):
    page = parse_int("页码", values.get("page", "1"), minimum=1)
    size = parse_int("每页数量", values.get("size", "20"), minimum=1, maximum=200)
    if page * size > 10000:
        raise ValueError("查询最多翻到前 10000 条，请缩小筛选范围")


def validate_sort(values, sort_fields):
    if "sort" in values and values["sort"] not in sort_fields:
        raise ValueError(f"当前查询不支持排序字段: {values['sort']}")
    if "order" in values and values["order"] not in {"asc", "desc"}:
        raise ValueError("排序方向只支持 asc 或 desc")


def build_url(base_url, endpoint, params):
    url = f"{base_url.rstrip('/')}{endpoint}"
    query = urlencode(params)
    return f"{url}?{query}" if query else url


def validate_search_response(payload, failure_message):
    if not isinstance(payload, dict):
        raise ValueError("接口响应必须是 JSON 对象")
    if payload.get("code") != 0:
        raise ValueError(response_message(payload, failure_message))
    data = payload.get("data")
    if not isinstance(data, dict):
        raise ValueError("成功响应缺少 data 对象")
    if not isinstance(data.get("total"), int) or not isinstance(data.get("list"), list):
        raise ValueError("成功响应缺少 total 或 list")
    if not isinstance(data.get("site"), dict):
        raise ValueError("成功响应缺少 site 对象")
    return {"code": 0, "data": data}
