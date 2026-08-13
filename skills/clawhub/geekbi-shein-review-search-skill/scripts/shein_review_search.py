#!/usr/bin/env python3
"""调用极鲸云的 SHEIN 评论搜索接口。"""

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


ENDPOINT = "/api/v1/shein/review/ai-search"
ALLOWED_PARAMS = {
    "goodsId",
    "siteId",
    "specs",
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


def parse_params(raw_params):
    params, values, _ = parse_pairs(raw_params, ALLOWED_PARAMS)
    goods_id = values.get("goodsId", "").strip()
    if not goods_id:
        raise ValueError("商品 ID不能为空")
    if len(goods_id) > 100:
        raise ValueError("商品 ID不能超过 100 个字符")
    if len(values.get("specs", "")) > 300:
        raise ValueError("规格条件不能超过 300 个字符")
    if "siteId" in values:
        parse_int("站点 ID", values["siteId"], minimum=1)
    if "scoreMin" in values:
        parse_int("最低评分", values["scoreMin"], minimum=1, maximum=5)
    if "scoreMax" in values:
        parse_int("最高评分", values["scoreMax"], minimum=1, maximum=5)
    if "helpfulMin" in values:
        parse_int("最小有用数", values["helpfulMin"], minimum=0)
    if "helpfulMax" in values:
        parse_int("最大有用数", values["helpfulMax"], minimum=0)
    validate_page(values)
    validate_sort(values, SORT_FIELDS)
    validate_range_pairs(
        values,
        {"score", "helpful"},
        {"commentTime"},
        {"score", "helpful"},
    )
    return params


def main():
    parser = argparse.ArgumentParser(description="按商品查询 SHEIN 评论并输出 JSON")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--param", action="append", default=[], help="名称=值；必须传商品 ID")
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()

    try:
        params = parse_params(args.param)
        payload = authenticated_json_request(
            build_url(args.base_url, ENDPOINT, params),
            args.base_url,
            args.timeout,
        )
        payload = validate_search_response(payload, "评论查询失败")
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
