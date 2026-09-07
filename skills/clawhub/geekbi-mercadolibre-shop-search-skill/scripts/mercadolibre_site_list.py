#!/usr/bin/env python3
"""实时查询 Mercado Libre 站点并按国家、地区代码或站点 ID 解析。"""

import argparse
import json
import sys
from urllib.error import HTTPError, URLError

from geekbi_auth import ActionRequired, authenticated_json_request, response_message
from mercadolibre_search_common import DEFAULT_BASE_URL


ENDPOINT = "/api/v1/mercadolibre/site/ai-list"


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
        raise ValueError(response_message(payload, "Mercado Libre 站点查询失败"))
    if not isinstance(payload.get("data"), list):
        raise ValueError("站点列表响应缺少 data 数组")
    return payload["data"]


def resolve_site(sites, country):
    target = normalize_name(country)
    if not target:
        raise ValueError("国家、地区或站点名称不能为空")
    matches = []
    seen = set()
    for site in sites:
        if not isinstance(site, dict):
            continue
        site_id = site.get("siteId")
        if isinstance(site_id, bool) or not isinstance(site_id, int):
            continue
        candidates = {site.get("regionId"), site.get("name"), site.get("cnName"), str(site_id)}
        if target not in {normalize_name(value) for value in candidates if isinstance(value, str)}:
            continue
        if site_id not in seen:
            matches.append(site)
            seen.add(site_id)
    if not matches:
        raise ValueError("未找到该 Mercado Libre 站点，请确认国家中文名、英文名或地区代码")
    return matches


def main():
    parser = argparse.ArgumentParser(description="实时解析 Mercado Libre 站点")
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
