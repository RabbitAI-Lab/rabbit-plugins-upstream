"""
类目 AI 改图适配度分析器 - CLI 入口
"""
import argparse
import datetime
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def _load_openclaw_env():
    """从 ~/.openclaw/openclaw.json 读取环境变量回填到 os.environ"""
    cfg_path = Path.home() / ".openclaw" / "openclaw.json"
    if not cfg_path.exists():
        return
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        env = cfg.get("env", {}) or cfg.get("envs", {}) or {}
        if not env and "providers" in cfg:
            for p in cfg.get("providers", []):
                env.update(p.get("env", {}) or {})
        for k, v in cfg.items():
            if isinstance(v, str) and k.isupper():
                env.setdefault(k, v)
        for k, v in env.items():
            if k not in os.environ and isinstance(v, str):
                os.environ[k] = v
    except Exception as e:
        print(f"[Config] 读取 openclaw.json 失败: {e}", flush=True)


_load_openclaw_env()

from category_parser import load_categories
from amazon_fetcher import fetch_amazon_top_products, enrich_with_images
from walmart_fetcher import fetch_walmart_top_products
from vision_analyzer import analyze_images_batch, download_image, CACHE_DIR as IMG_CACHE_DIR
from scorer import score_category
from excel_writer import write_excel


def analyze_one_category(cat: dict, top_n: int, amazon_only: bool, walmart_only: bool) -> dict:
    """对单个类目跑全流程：抓取→视觉分析→打分"""
    keyword = cat["search_keyword"]
    platform = cat["platform"]
    print(f"\n=== 类目: {cat['raw']} (平台: {platform}, 搜索词: {keyword}) ===", flush=True)

    products = []

    if not walmart_only and platform in ("amazon", "both"):
        try:
            amz_products = fetch_amazon_top_products(keyword, top_n=top_n)
            amz_products = enrich_with_images(amz_products)
            products.extend(amz_products)
        except Exception as e:
            print(f"[Amazon] 抓取失败: {e}", flush=True)

    if not amazon_only and platform in ("walmart", "both"):
        try:
            wm_products = fetch_walmart_top_products(keyword, top_n=top_n)
            products.extend(wm_products)
        except Exception as e:
            print(f"[Walmart] 抓取失败: {e}", flush=True)

    if not products:
        print(f"[Skip] 类目「{keyword}」未抓到任何商品", flush=True)
        return {**_base_row(cat), **_empty_score()}

    image_urls = [p.get("image", "") for p in products if p.get("image")]
    print(f"[Vision] 开始分析 {len(image_urls)} 张主图...", flush=True)

    for url in image_urls:
        download_image(url)

    vision_results = analyze_images_batch(image_urls, max_workers=4)

    score = score_category(products, vision_results)

    rep_images = []
    for p, v in zip(products, vision_results):
        if v and "error" not in v and p.get("image"):
            rep_images.append(p["image"])
        if len(rep_images) >= 3:
            break

    row = {
        **_base_row(cat),
        **score,
        "representative_images": rep_images,
    }
    print(f"[Result] {cat['raw']} → {row['decision']} ({row['reason']})", flush=True)
    return row


def _base_row(cat: dict) -> dict:
    return {
        "raw_input": cat["raw"],
        "platform": cat["platform"],
        "keyword": cat["search_keyword"],
        "fetched_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    }


def _empty_score() -> dict:
    return {
        "scene_fitness": 0,
        "ai_difficulty": "无数据",
        "infringement_risk": "无数据",
        "must_modify_image": False,
        "strategy": "无数据",
        "decision": "❌无数据",
        "reason": "未抓到任何商品",
        "dominant_form": "unknown",
        "lifestyle_ratio": 0,
        "white_ratio": 0,
        "median_price": None,
        "median_sales": None,
        "sample_count": 0,
        "representative_images": [],
    }


def main():
    parser = argparse.ArgumentParser(description="类目 AI 改图适配度分析器")
    parser.add_argument("--input", "-i", required=True, help="输入类目 Excel/CSV 文件")
    parser.add_argument("--output", "-o", default=None, help="输出 Excel 路径")
    parser.add_argument("--top-n", type=int, default=10, help="每类目抓取商品数（默认10）")
    parser.add_argument("--amazon-only", action="store_true", default=True, help="只跑 Amazon (默认)")
    parser.add_argument("--include-walmart", action="store_true", help="同时抓 Walmart (需要登录态/代理，默认关闭)")
    parser.add_argument("--walmart-only", action="store_true", help="只跑 Walmart")
    parser.add_argument("--limit", type=int, default=None, help="只跑前N个类目（测试用）")
    args = parser.parse_args()

    categories = load_categories(args.input)
    if args.limit:
        categories = categories[:args.limit]
    print(f"共 {len(categories)} 个类目待分析", flush=True)

    amazon_only = args.amazon_only and not args.include_walmart
    walmart_only = args.walmart_only

    rows = []
    for i, cat in enumerate(categories, 1):
        print(f"\n[{i}/{len(categories)}]", flush=True)
        row = analyze_one_category(cat, args.top_n, amazon_only, walmart_only)
        rows.append(row)

    if args.output:
        out_path = args.output
    else:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        out_dir = Path(__file__).parent.parent / "output"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = str(out_dir / f"category_fitness_report_{ts}.xlsx")

    write_excel(rows, out_path, IMG_CACHE_DIR)
    print(f"\n✅ 完成！报告已保存: {out_path}", flush=True)


if __name__ == "__main__":
    main()
