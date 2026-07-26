"""
Copyright (c) 2026 Allen. MIT License.
"""
"""
高德地图 API 调用封装 —— 5000 次/月免费额度自动追踪
=====================================================

用法:
  python3 scripts/gaode_api.py --keyword "甜茶馆" --city "拉萨"

  # 仅查看剩余配额
  python3 scripts/gaode_api.py --check

环境变量(推荐自行申请替换):
  AMAP_KEY='你的高德Web服务Key'   # 内置了一个免费测试 Key，建议换成你自己的
"""

import json
import os
import sys
import time
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote

USAGE_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "gaode_api_usage.json")
USAGE_FILE = os.path.abspath(USAGE_FILE)
# 内置免费测试 Key（每月 5000 次免费额度）
# 建议部署时 export AMAP_KEY='你自己的key' 覆盖
DEFAULT_KEY = "24ac143852d686c1d0b8bd5c8ed59498"
MONTHLY_LIMIT = 5000
BASE_URL = "https://restapi.amap.com/v3/place/text"


def get_current_month() -> str:
    return datetime.now().strftime("%Y-%m")


def load_usage() -> dict:
    if not os.path.exists(USAGE_FILE):
        return {"month": get_current_month(), "call_count": 0, "monthly_limit": MONTHLY_LIMIT}
    with open(USAGE_FILE, "r") as f:
        data = json.load(f)
    if data["month"] != get_current_month():
        data["month"] = get_current_month()
        data["call_count"] = 0
    data["monthly_limit"] = MONTHLY_LIMIT
    return data


def save_usage(data: dict):
    os.makedirs(os.path.dirname(USAGE_FILE), exist_ok=True)
    with open(USAGE_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def call_place_api(keyword: str, city: str, key: str) -> dict:
    params = {
        "key": key,
        "keywords": keyword,
        "city": city,
        "offset": "5",
        "page": "1",
        "extensions": "all",
    }
    url = f"{BASE_URL}?{urlencode(params, quote_via=quote)}"
    req = Request(url, headers={"User-Agent": "QuXizang/1.0"})
    with urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def format_result(raw: dict, keyword: str, city: str, remaining: int) -> dict:
    if raw.get("status") != "1" or raw.get("count") == "0":
        return {
            "found": False,
            "message": f"高德地图在{city}没找到「{keyword}」相关结果",
            "remaining_quota": remaining,
        }

    results = []
    for poi in raw.get("pois", [])[:5]:
        results.append({
            "name": poi.get("name", ""),
            "address": poi.get("address", ""),
            "phone": poi.get("tel", ""),
            "rating": poi.get("biz_ext", {}).get("rating", ""),
            "type": poi.get("type", ""),
        })

    return {
        "found": True,
        "results": results,
        "count": len(results),
        "source": "高德地图实时搜索",
        "disclaimer": "这是用高德实时查到的，信息仅供参考",
        "remaining_quota": remaining,
    }


def cli_main():
    key = os.environ.get("AMAP_KEY", "24ac143852d686c1d0b8bd5c8ed59498")

    if "--check" in sys.argv:
        usage = load_usage()
        remaining = MONTHLY_LIMIT - usage["call_count"]
        print(f"📊 高德 API 本月已用: {usage['call_count']} / {MONTHLY_LIMIT} 次")
        print(f"   剩余额度: {remaining} 次")
        print(f"   统计月份: {usage['month']}")
        return

    import argparse
    parser = argparse.ArgumentParser(description="高德地图 API 调用封装（5000次/月限额）")
    parser.add_argument("--keyword", required=True, help="搜索关键词（如：甜茶馆、藏餐厅）")
    parser.add_argument("--city", default="拉萨", help="城市名（默认：拉萨）")
    parser.add_argument("--check", action="store_true", help="仅查看剩余配额")
    args = parser.parse_args()

    usage = load_usage()
    remaining = MONTHLY_LIMIT - usage["call_count"]

    if usage["call_count"] >= MONTHLY_LIMIT:
        print(json.dumps({
            "found": False,
            "message": f"本月 5000 次免费额度已用完（{usage['month']}），下月 1 号自动重置。当前推荐只能从内置商户和高德备选中匹配。",
            "remaining_quota": 0,
        }, ensure_ascii=False))
        sys.exit(0)

    raw = call_place_api(args.keyword, args.city, key)

    usage["call_count"] += 1
    save_usage(usage)

    result = format_result(raw, args.keyword, args.city, remaining - 1)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    cli_main()
