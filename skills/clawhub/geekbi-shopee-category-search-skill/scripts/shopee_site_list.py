#!/usr/bin/env python3
"""实时查询 Shopee 站点并按国家、地区代码或站点 ID 解析。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from shopee_search_common import DEFAULT_BASE_URL
from geekbi_auth import ActionRequired, authenticated_json_request, response_message


ENDPOINT = "/api/v1/shopee/site/ai-list"
COUNTRY_ALIASES = {
    "singapore": "sg", "新加坡": "sg",
    "malaysia": "my", "马来西亚": "my", "馬來西亞": "my",
    "philippines": "ph", "菲律宾": "ph", "菲律賓": "ph",
    "thailand": "th", "泰国": "th", "泰國": "th",
    "vietnam": "vn", "越南": "vn",
    "indonesia": "id", "印度尼西亚": "id", "印度尼西亞": "id", "印尼": "id",
    "taiwan": "tw", "台湾": "tw", "台灣": "tw",
    "brazil": "br", "巴西": "br",
}


def normalize_name(value):
    normalized = value.strip().casefold()
    for suffix in ("站点", "站"):
        if normalized.endswith(suffix):
            normalized = normalized[: -len(suffix)].strip()
            break
    return normalized


def validate_response(payload):
    if not isinstance(payload, dict):
        raise ValueError("站点列表响应必须是 JSON 对象")
    if payload.get("code") != 0:
        raise ValueError(response_message(payload, "Shopee 站点查询失败"))
    if not isinstance(payload.get("data"), list):
        raise ValueError("站点列表响应缺少 data 数组")
    return payload["data"]


def resolve_site(sites, country):
    target = normalize_name(country)
    if not target:
        raise ValueError("国家、地区或站点名称不能为空")
    target = COUNTRY_ALIASES.get(target, target)
    matches = []
    seen = set()
    for site in sites:
        if not isinstance(site, dict):
            continue
        site_id = site.get("siteId")
        if isinstance(site_id, bool) or not isinstance(site_id, int):
            continue
        candidates = {site.get("regionId"), site.get("name"), site.get("cnName"), str(site_id)}
        normalized_candidates = {
            COUNTRY_ALIASES.get(normalize_name(value), normalize_name(value))
            for value in candidates if isinstance(value, str)
        }
        if target not in normalized_candidates:
            continue
        if site_id in seen:
            continue
        seen.add(site_id)
        matches.append(site)
    if not matches:
        raise ValueError("未找到该 Shopee 站点，请确认国家中文名、英文名或地区代码")
    return matches


def main():
    parser = argparse.ArgumentParser(description="实时解析 Shopee 站点")
    parser.add_argument("--country", required=True, help="国家中文名、英文名、地区代码或站点 ID")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args()
    try:
        payload = authenticated_json_request(
            f"{args.base_url.rstrip('/')}{ENDPOINT}", args.base_url, args.timeout
        )
        matches = resolve_site(validate_response(payload), args.country)
    except ActionRequired as error:
        print(json.dumps(error.public_payload(), ensure_ascii=False, indent=2))
        return 2
    except (ValueError, HTTPError, URLError, TimeoutError) as error:
        print(json.dumps({"error": True, "msg": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps({"code": 0, "data": {"matches": matches}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
