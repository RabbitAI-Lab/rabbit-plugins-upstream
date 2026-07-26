#!/usr/bin/env python3
"""
综合比价引擎 - 并行查询所有平台，汇总比价结果
输出标准化JSON，供Skill和小程序使用

用法:
  python compare_all.py <关键词> [城市ID]
  python compare_all.py 螺蛳粉 1
  python compare_all.py --coupons   # 只看红包
"""
import json
import sys
import os
import argparse
import concurrent.futures

# 动态导入各平台查询模块
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

AVAILABLE_PLATFORMS = {}

# 京东
try:
    from query_jd import query_jd_products, format_result as fmt_jd, query_jd_coupons
    AVAILABLE_PLATFORMS["jd"] = True
except ImportError:
    AVAILABLE_PLATFORMS["jd"] = False

# 淘宝（好单库）
try:
    from query_taobao import query_taobao, format_result as fmt_tb
    AVAILABLE_PLATFORMS["taobao"] = True
except ImportError:
    AVAILABLE_PLATFORMS["taobao"] = False

# 美团
try:
    from query_meituan import (
        query_meituan_waimai, query_meituan_search,
        get_meituan_coupons, format_result as fmt_mt
    )
    AVAILABLE_PLATFORMS["meituan"] = True
except ImportError:
    AVAILABLE_PLATFORMS["meituan"] = False

# 饿了么
try:
    from query_eleme import query_eleme_zhetaoke, get_eleme_coupons_zhetaoke, format_result as fmt_elm
    AVAILABLE_PLATFORMS["eleme"] = True
except ImportError:
    AVAILABLE_PLATFORMS["eleme"] = False


def compare_all(keyword, city_id=1, page_size=20):
    """
    综合比价：并行查询所有平台
    返回标准化结果列表，按到手价排序
    """
    all_results = []
    errors = []

    def safe_fetch(name, fetch_fn, format_fn):
        try:
            data = fetch_fn()
            return format_fn(data)
        except Exception as e:
            errors.append({"platform": name, "error": str(e)})
            return []

    tasks = []

    if AVAILABLE_PLATFORMS.get("jd"):
        tasks.append(("京东", lambda: query_jd_products(keyword, page_size=page_size), fmt_jd))

    if AVAILABLE_PLATFORMS.get("taobao"):
        tasks.append(("淘宝", lambda: query_taobao(keyword, back=min(page_size, 100)), fmt_tb))

    if AVAILABLE_PLATFORMS.get("meituan"):
        tasks.append(("美团外卖", lambda: query_meituan_waimai(keyword, city_id=city_id, page_size=page_size), fmt_mt))
        tasks.append(("美团搜索", lambda: query_meituan_search(keyword, page_size=page_size), fmt_mt))

    if AVAILABLE_PLATFORMS.get("eleme"):
        tasks.append(("饿了么", lambda: query_eleme_zhetaoke(keyword, page_size=page_size), fmt_elm))

    # 并行查询
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = {}
        for name, fetch_fn, format_fn in tasks:
            futures[executor.submit(safe_fetch, name, fetch_fn, format_fn)] = name

        for future in concurrent.futures.as_completed(futures, timeout=30):
            name = futures[future]
            try:
                results = future.result(timeout=20)
                all_results.extend(results)
            except concurrent.futures.TimeoutError:
                errors.append({"platform": name, "error": "查询超时(30s)"})
            except Exception as e:
                errors.append({"platform": name, "error": str(e)})

    # 按到手价排序
    all_results.sort(key=lambda x: float(x.get("after_price", x.get("price", 999999))))

    # 去重（基于标题相似度简单去重）
    seen_titles = set()
    deduped = []
    for item in all_results:
        title_key = item.get("title", "")[:20]
        if title_key not in seen_titles:
            seen_titles.add(title_key)
            deduped.append(item)
    all_results = deduped

    return {
        "keyword": keyword,
        "city_id": city_id,
        "count": len(all_results),
        "results": all_results[:50],  # 最多50条
        "best": all_results[0] if all_results else None,
        "platforms_available": {k: v for k, v in AVAILABLE_PLATFORMS.items() if v},
        "errors": errors if errors else [],
    }


def get_all_coupons():
    """汇总各平台可领红包"""
    summary = {}

    # 美团红包
    if AVAILABLE_PLATFORMS.get("meituan"):
        try:
            mt_data = get_meituan_coupons()
            coupons = mt_data.get("data", {}).get("coupons", mt_data.get("data", []))
            if isinstance(coupons, dict):
                coupons = coupons.get("list", [])
            summary["美团"] = _format_coupons(coupons)
        except Exception as e:
            summary["美团"] = {"error": str(e), "count": 0}

    # 饿了么红包（折淘客代理）
    if AVAILABLE_PLATFORMS.get("eleme"):
        try:
            elm_data = get_eleme_coupons_zhetaoke()
            coupons = elm_data.get("result", {}).get("coupons", [])
            if isinstance(coupons, str):
                try:
                    coupons = json.loads(coupons)
                except json.JSONDecodeError:
                    coupons = []
            summary["饿了么"] = _format_coupons(coupons)
        except Exception as e:
            summary["饿了么"] = {"error": str(e), "count": 0}

    # 京东红包
    if AVAILABLE_PLATFORMS.get("jd"):
        try:
            jd_data = query_jd_coupons()
            coupons = jd_data.get("data", {}).get("coupons", [])
            summary["京东"] = _format_coupons(coupons)
        except Exception as e:
            summary["京东"] = {"error": str(e), "count": 0}

    return summary


def _format_coupons(coupons):
    """格式化红包/优惠券"""
    if not coupons or not isinstance(coupons, list):
        return {"count": 0, "coupons": [], "max_amount": 0}

    formatted = []
    max_amount = 0
    for c in coupons[:10]:
        amount = float(c.get("amount", c.get("discount", c.get("value", 0))))
        max_amount = max(max_amount, amount)
        formatted.append({
            "id": c.get("id", c.get("couponId", c.get("batchId", ""))),
            "name": c.get("name", c.get("title", c.get("couponName", ""))),
            "amount": round(amount, 2),
            "condition": c.get("condition", c.get("limitText", "无门槛")),
            "expire": c.get("expire", c.get("endTime", c.get("validTime", ""))),
            "url": c.get("url", c.get("link", c.get("h5Link", ""))),
        })

    return {
        "count": len(coupons),
        "max_amount": round(max_amount, 2),
        "coupons": formatted,
    }


def format_for_display(result):
    """格式化为终端展示格式"""
    lines = []
    lines.append("=" * 60)
    lines.append(f"🔍 比价结果：{result['keyword']}")
    lines.append(f"📊 可用平台：{', '.join(result.get('platforms_available', {}).keys())}")
    lines.append(f"📦 共找到 {result['count']} 个商品\n")

    for i, item in enumerate(result["results"][:15], 1):
        platform = item.get("platform", "未知")
        title = item.get("title", "")[:40]
        price = item.get("price", 0)
        after = item.get("after_price", price)
        coupon = item.get("coupon_amount", 0)
        shop = item.get("shop", "")[:15]

        rank_icon = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"【{i}】"
        lines.append(f"{rank_icon} {platform} | {title}")
        if float(coupon) > 0:
            lines.append(f"   💰 ¥{price} → 券¥{coupon} → 到手 ¥{after}")
        else:
            lines.append(f"   💰 ¥{price}")
        if shop:
            lines.append(f"   🏪 {shop}")
        lines.append("")

    best = result.get("best")
    if best:
        lines.append("-" * 60)
        lines.append(f"🏆 最便宜: {best.get('platform')} {best.get('title', '')[:30]}")
        lines.append(f"   到手价: ¥{best.get('after_price', best.get('price', 0))}")

    if result.get("errors"):
        lines.append("-" * 60)
        lines.append("⚠️ 以下平台查询出错:")
        for err in result["errors"]:
            lines.append(f"   {err['platform']}: {err['error']}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="全网比价引擎")
    parser.add_argument("keyword", nargs="?", default="手机", help="搜索关键词")
    parser.add_argument("--city", type=int, default=1, help="城市ID（外卖用）")
    parser.add_argument("--size", type=int, default=20, help="每页数量")
    parser.add_argument("--coupons", action="store_true", help="只看红包")
    parser.add_argument("--json", action="store_true", help="JSON格式输出")
    args = parser.parse_args()

    if args.coupons:
        print("🎁 各平台可领红包汇总\n")
        coupons = get_all_coupons()
        print(json.dumps(coupons, ensure_ascii=False, indent=2))
        return

    result = compare_all(args.keyword, city_id=args.city, page_size=args.size)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_for_display(result))


if __name__ == "__main__":
    main()
