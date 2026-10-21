#!/usr/bin/env python3
"""高德 POI × 飞猪酒店联动：一句话定位 + 查真实库存 + 出预订链接。

高德负责把任意地名解析成坐标并验证该地点真实存在（飞猪 --poi-name 只锚得住头部景区），
飞猪负责实时房价、房态和可点击的预订链接。
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request

GAODE_BASE = "http://82.156.169.110/poi/v1"

# 作为"目的地"优先的非住宿类目；住宿服务是我们要订的对象，不该当目的地
DEST_CATS = {
    "科教文化服务", "体育休闲服务", "风景名胜", "购物服务",
    "餐饮服务", "交通设施服务", "生活服务",
}


def gaode_get(path, params, key):
    url = GAODE_BASE + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-API-Key": key})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


def gaode_search(q, city, key, page_size=10):
    return gaode_get("/search", {"q": q, "city": city, "page_size": page_size}, key)


def gaode_nearby(lng, lat, key, radius_m=1000, category="餐饮服务", page_size=5):
    return gaode_get("/nearby", {
        "lng": lng, "lat": lat, "radius_m": radius_m,
        "category": category, "page_size": page_size,
    }, key)


def flyai_search_hotel(dest, keywords, checkin, checkout,
                       stars=None, max_price=None, sort="distance_asc",
                       anchor="key-words"):
    """anchor: 'key-words' 用 --key-words（通用），'poi-name' 用 --poi-name（头部景区锚定更准）"""
    flag = "--key-words" if anchor == "key-words" else "--poi-name"
    cmd = ["flyai", "search-hotel", "--dest-name", dest,
           flag, keywords,
           "--check-in-date", checkin, "--check-out-date", checkout,
           "--sort", sort]
    if stars:
        cmd += ["--hotel-stars", stars]
    if max_price:
        cmd += ["--max-price", str(max_price)]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
    if res.returncode != 0:
        sys.stderr.write(res.stderr)
        sys.exit(res.returncode)
    return json.loads(res.stdout)


def pick_destination(items):
    """从高德候选里挑出真正的目的地，避开同名酒店。"""
    if not items:
        return None
    for it in items:
        if it.get("cat") in DEST_CATS:
            return it
    # 退而求其次：取第一个非住宿的
    for it in items:
        if it.get("cat") != "住宿服务":
            return it
    return items[0]


def fmt_hotel_card(h):
    lines = []
    pic = h.get("mainPic")
    if pic:
        lines.append(f"![]({pic})")
    name = h.get("name", "")
    price = h.get("price", "")
    star = h.get("star", "")
    score = h.get("rate", "")
    poi = h.get("interestsPoi", "")
    lines.append(f"### {name}")
    meta = [x for x in [star, f"{score}分" if score and score != "0" else None,
                        price, poi] if x]
    lines.append(" · ".join(meta))
    detail = h.get("detailUrl")
    if detail:
        lines.append(f"[点击预订]({detail})")
    return "\n\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="高德×飞猪一句话订酒店")
    ap.add_argument("--city", required=True, help="城市，如 北京")
    ap.add_argument("--place", required=True, help="目的地/景点名，如 798艺术区")
    ap.add_argument("--check-in", required=True, help="入住日期 YYYY-MM-DD")
    ap.add_argument("--check-out", required=True, help="退房日期 YYYY-MM-DD")
    ap.add_argument("--stars", default=None, help="星级，如 4,5")
    ap.add_argument("--max-price", type=int, default=None, help="每晚最高价")
    ap.add_argument("--sort", default="distance_asc",
                    help="排序：distance_asc/rate_desc/price_asc/price_desc")
    ap.add_argument("--enrich-nearby", action="store_true",
                    help="附上目的地周边餐饮（高德富化）")
    ap.add_argument("--top", type=int, default=5, help="展示酒店数")
    args = ap.parse_args()

    key = os.environ.get("GAODE_POI_KEY")
    if not key:
        sys.stderr.write("缺少环境变量 GAODE_POI_KEY（高德 POI REST key）\n")
        sys.exit(2)

    # 1. 高德解析目的地：验证存在 + 拿坐标 + 拿规范名
    sr = gaode_search(args.place, args.city, key)
    dest = pick_destination(sr.get("items", []))
    if not dest:
        print(f"# 未在{args.city}找到「{args.place}」\n\n高德返回 {sr.get('total', 0)} 条，无可用目的地候选。")
        sys.exit(1)

    # 用规范名喂飞猪；若高德只找到住宿类 POI 说明是泛名词（如"西湖"），
    # 回退用用户原始输入 + poi-name 模式，飞猪对头部景区用 --poi-name 锚更准
    if dest.get("cat") == "住宿服务":
        keyword = args.place
        anchor = "poi-name"
    else:
        keyword = dest["name"]
        anchor = "key-words"

    display_name = args.place if anchor == "poi-name" else dest["name"]
    print(f"# {args.city} · {display_name} 附近酒店\n")
    print(f"基于高德 POI 定位：{dest['name']}（{dest.get('cat','')}）"
          f"坐标 {dest['lng']},{dest['lat']}，{dest.get('address','')}\n")

    # 2. 飞猪查真实库存
    hj = flyai_search_hotel(args.city, keyword,
                            args.check_in, args.check_out,
                            stars=args.stars, max_price=args.max_price,
                            sort=args.sort, anchor=anchor)
    hotels = hj.get("data", {}).get("itemList", [])[:args.top]
    if not hotels:
        print("飞猪暂无匹配库存，换个关键词或扩大星级/价格范围再试。")
        if hj.get("systemMessage"):
            print(f"\n{hj['systemMessage']}")
        return

    print(f"## 飞猪实时库存（{args.check_in} → {args.check_out}）\n")
    for h in hotels:
        print(fmt_hotel_card(h))
        print("\n---\n")

    # 3. 高德富化：目的地周边餐饮
    if args.enrich_nearby:
        try:
            nb = gaode_nearby(dest["lng"], dest["lat"], key)
            items = nb.get("items", [])
            if items:
                print("## 周边餐饮（高德，1km 内）\n")
                for it in items[:5]:
                    r = it.get("rating")
                    rs = f"{r}分" if r else "暂无评分"
                    print(f"- **{it['name']}** · {it.get('cat','')} · {rs} · {it.get('address','')}")
        except Exception as e:
            sys.stderr.write(f"周边富化失败：{e}\n")

    if hj.get("systemMessage"):
        print(f"\n{hj['systemMessage']}")


if __name__ == "__main__":
    main()
