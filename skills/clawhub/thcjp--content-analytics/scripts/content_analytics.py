#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""内容效果分析脚本 - 计算播放/完播/互动/转化指标，生成S/A/B/C评级和优化建议
来源: content-analytics SKILL.md §四评级标准
"""

import json

import os
import sys
from datetime import datetime, timedelta
from typing import Any, Optional

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent.parent.parent / "scripts"))
sys.path.insert(0, str(_Path(__file__).resolve().parents[3]))  # T4-4: 添加项目根以支持mcps.shared导入
from mcps.shared.db_logger import get_logger
logger = get_logger("content-analytics", source="skills/content-analytics/scripts/content_analytics.py")
from mcps.shared.atomic_write import atomic_read_json, atomic_write_json

import logging
logger = get_logger("system", source="skills/content-analytics/scripts/content_analytics.py")

MEMORY_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "memory")
ANALYTICS_DIR = os.path.join(os.path.dirname(__file__), "..", "analytics_cache")

WEIGHTS = {
    "views": 0.25,
    "completion_rate": 0.25,
    "engagement_rate": 0.20,
    "conversion_rate": 0.20,
    "share_rate": 0.10,
}

RATING_THRESHOLDS = {
    "S": 90,
    "A": 70,
    "B": 50,
}

VALID_PLATFORMS = [
    # 原有10平台(视频/图文类)
    "douyin", "kuaishou", "xiaohongshu", "shipinhao",
    "bilibili", "tiktok", "baijiahao", "douyin_img",
    "kuaishou_tuwen", "xiaohongshu_video",
    # multi-publisher-mcp 28平台(平台名与发布器注册名一致，不加_mp后缀)
    "juejin", "csdn", "segmentfault", "weibo", "jianshu",
    "toutiao", "zhihu", "douban", "cnblogs", "51cto",
    "oschina", "yuque", "imooc", "xueqiu", "eastmoney",
    "smzdm", "woshipm", "yidian", "sohu",
    "dayu", "netease", "bilibili_col", "douyin_img", "sohufocus",
    "x_twitter", "wordpress", "typecho",
]

def _parse_args() -> dict:
    args = {}
    i = 1
    while i < len(sys.argv):
        if sys.argv[i].startswith("--"):
            key = sys.argv[i][2:]
            if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith("--"):
                args[key] = sys.argv[i + 1]
                i += 2
            else:
                args[key] = True
                i += 1
        else:
            i += 1
    return args

def _compute_score(metrics: dict) -> float:
    score = 0.0
    for key, weight in WEIGHTS.items():
        val = metrics.get(key, 0)
        if key == "views":
            norm = min(val / 10000, 1.0) * 100
        else:
            norm = min(val, 1.0) * 100
        score += norm * weight
    return round(score, 1)

def _get_rating(score: float) -> str:
    if score > RATING_THRESHOLDS["S"]:
        return "S"
    elif score > RATING_THRESHOLDS["A"]:
        return "A"
    elif score > RATING_THRESHOLDS["B"]:
        return "B"
    return "C"

def _generate_suggestions(rating: str, metrics: dict) -> list:
    suggestions = []
    if rating == "C":
        if metrics.get("completion_rate", 0) < 0.3:
            suggestions.append("完播率过低，建议缩短视频时长或优化开头3秒吸引力")
        if metrics.get("engagement_rate", 0) < 0.03:
            suggestions.append("互动率低，建议增加互动引导(提问/投票/评论区互动)")
        if metrics.get("share_rate", 0) < 0.01:
            suggestions.append("分享率低，建议增加实用价值或情感共鸣点")
        if metrics.get("conversion_rate", 0) < 0.01:
            suggestions.append("转化率低，建议优化关注引导和内容价值传递")
    elif rating == "B":
        if metrics.get("completion_rate", 0) < 0.5:
            suggestions.append("完播率有提升空间，建议优化内容节奏")
        if metrics.get("engagement_rate", 0) < 0.05:
            suggestions.append("互动率可提升，建议增加互动设计")
    else:
        suggestions.append("表现优秀，建议总结成功要素并复制模式")
    return suggestions if suggestions else ["数据正常，继续保持当前策略"]

def _read_publish_records(days: int) -> list:
    records = []
    for d in range(days):
        date_str = (datetime.now() - timedelta(days=d)).strftime("%Y-%m-%d")
        log_file = os.path.join(MEMORY_DIR, f"{date_str}.md")
        if not os.path.exists(log_file):
            continue
        with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if "发布" in line and "content_id" in line:
                    try:
                        start = line.index("{")
                        end = line.rindex("}") + 1
                        record = json.loads(line[start:end])
                        records.append(record)
                    except (ValueError, json.JSONDecodeError):
                        continue
    return records

def _fetch_from_postgres(content_id: str, platform: str, tenant_id: str = "") -> Optional[dict]:
    """从postgres-mcp获取内容指标(降级数据源)

    R75.2/E-3修复: 使用db_pool统一连接(替代psycopg2.connect碎片化)
    """
    try:
        from mcps.shared.db_pool import get_connection, return_connection
        conn = get_connection()
        if not conn:
            return None
        try:
            cur = conn.cursor()
            # P0-6: 设置租户上下文确保RLS生效(无tenant_id参数,从环境变量获取)
            cur.execute("SET app.current_tenant = %s", (tenant_id or os.environ.get("JUEJIN_TENANT_ID", ""),))
            # R7修复(P0): content_analytics表不存在(幽灵表),改为查询content_stats + tenant_publish_records JOIN
            # 原查询: SELECT views,likes,comments,shares,follows,complete_views FROM content_analytics WHERE content_id=%s AND platform=%s
            # 根因: content_analytics表从未创建(无CREATE TABLE),查询始终抛异常返回None
            # 修复: content_stats表存在(02_rls_init.sql:209)且由content_stats_collector.py填充
            #       但content_stats无content_id列,通过JOIN tenant_publish_records(content_id↔publish_url)映射
            cur.execute(
                "SELECT cs.view_count, cs.like_count, cs.comment_count, cs.share_count "
                "FROM content_stats cs "
                "INNER JOIN tenant_publish_records tpr ON cs.content_url = tpr.publish_url "
                "WHERE tpr.content_id = %s AND cs.platform = %s "
                "ORDER BY cs.stat_date DESC LIMIT 1",
                (content_id, platform)
            )
            row = cur.fetchone()
            if not row or not row[0] or row[0] == 0:
                # 降级: 直接查tenant_publish_records基础指标(U17数据统计更新)
                cur.execute(
                    "SELECT view_count, like_count, comment_count, share_count "
                    "FROM tenant_publish_records WHERE content_id = %s AND platform = %s "
                    "ORDER BY updated_at DESC LIMIT 1",
                    (content_id, platform)
                )
                row = cur.fetchone()
            if row and row[0] and row[0] > 0:
                views, likes, comments, shares = row
                return {
                    "views": views,
                    "completion_rate": 0,  # content_stats/tenant_publish_records无完播数据
                    "engagement_rate": round((likes + comments + shares) / views, 4) if views > 0 else 0,
                    "conversion_rate": 0,  # content_stats/tenant_publish_records无关注数据
                    "share_rate": round(shares / views, 4) if views > 0 else 0,
                    "likes": likes, "comments": comments, "shares": shares,
                    "_source": "postgres-mcp",
                }
        finally:
            return_connection(conn)
    except Exception as e:
        logger.error(f"content analytics异常: {e}", exc_info=True)
        logger.error(f"[INFO] postgres-mcp查询失败: {e}")
    return None

def _fetch_real_metrics(content_id: str, platform: str, tenant_id: str = "") -> Optional[dict]:
    """从可用数据源聚合真实指标
    数据源优先级(来源:SKILL.md dependencies:postgres-mcp):
    postgres-mcp > analytics_cache > memory发布记录 > content-publisher(version)
    """
    # 优先级1: postgres-mcp(降级数据源)
    result = _fetch_from_postgres(content_id, platform, tenant_id)
    if result:
        return result

    # 优先级2: analytics_cache
    cache_file = os.path.join(ANALYTICS_DIR, f"{content_id}.json")
    if os.path.exists(cache_file):
        cached = atomic_read_json(cache_file)
        if cached is not None:
            if cached.get("metrics") and any(
                v > 0 for v in cached["metrics"].values()
                if isinstance(v, (int, float)) and not isinstance(v, bool)
            ):
                cached["metrics"]["_source"] = "analytics_cache"
                return cached["metrics"]
        else:
            logger.warning("缓存读取失败: safe_read_json返回None")

    # 优先级3: memory发布记录
    records = _read_publish_records(30)
    for rec in records:
        if rec.get("content_id") == content_id:
            m = {
                "views": rec.get("views", 0),
                "completion_rate": rec.get("completion_rate", 0),
                "engagement_rate": rec.get("engagement_rate", 0),
                "conversion_rate": rec.get("conversion_rate", 0),
                "share_rate": rec.get("share_rate", 0),
                "likes": rec.get("likes", 0),
                "comments": rec.get("comments", 0),
                "shares": rec.get("shares", 0),
                "_source": "memory_publish_records",
            }
            if any(v > 0 for v in m.values() if isinstance(v, (int, float)) and not isinstance(v, bool)):
                return m
            break

    # 优先级4: content-publisher(version) (v25.0合并content-versioning)
    versioning_dir = os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "data", "content", "versions"
    )
    if os.path.exists(versioning_dir):
        for fname in os.listdir(versioning_dir):
            if content_id in fname and fname.endswith(".json"):
                vpath = os.path.join(versioning_dir, fname)
                vdata = atomic_read_json(vpath)
                if vdata is not None:
                    if vdata.get("metrics"):
                        m = vdata["metrics"]
                        if any(
                            v > 0 for v in m.values()
                            if isinstance(v, (int, float)) and not isinstance(v, bool)
                        ):
                            m["_source"] = "content_versioning"
                            return m
                else:
                    logger.warning("版本记录读取失败: safe_read_json返回None")

    return None

def analyze(content_id: str, platform: str) -> dict[str, Any]:
    """分析

    Args:
        content_id (str): 参数说明
        platform (str): 参数说明

    Returns:
        dict[str, Any]: 返回值说明
    
    Raises:
        ValueError: 异常说明
    """
    if platform not in VALID_PLATFORMS:
        raise ValueError(f"无效平台: {platform}，有效平台: {', '.join(VALID_PLATFORMS)}")

    metrics = _fetch_real_metrics(content_id, platform)
    if metrics is None:
        score = 0.0
        rating = None
        suggestions = ["无可用数据源，请确保: 1)内容已通过content-publisher发布 2)发布日志包含浏览量/互动数据 3)或配置平台API密钥获取真实数据"]
        metrics = {"views": 0, "completion_rate": 0, "engagement_rate": 0, "conversion_rate": 0, "share_rate": 0, "likes": 0, "comments": 0, "shares": 0, "_source": "no_data"}
        data_source = "no_data"
        warning = "无可用数据源，无法进行业务分析。请参考SKILL.md §五配置平台API"
    else:
        score = _compute_score(metrics)
        rating = _get_rating(score)
        suggestions = _generate_suggestions(rating, metrics)
        data_source = metrics.get("_source", "unknown")
        warning = None

    result = {
        "content_id": content_id,
        "platform": platform,
        "rating": rating,
        "score": score,
        "metrics": metrics,
        "suggestions": suggestions,
        "analyzed_at": datetime.now().isoformat(),
        "data_source": data_source,
    }
    if warning:
        result["warning"] = warning

    os.makedirs(ANALYTICS_DIR, exist_ok=True)
    cache_file = os.path.join(ANALYTICS_DIR, f"{content_id}.json")
    atomic_write_json(cache_file, result, indent=2, ensure_ascii=False)

    return result

def _batch_aggregate_from_memory(content_ids: list, platform: str) -> dict:
    """从memory目录和analytics缓存聚合已有数据，优先于模拟数据
    数据源优先级: analytics_cache/*.json > memory/*.md发布记录 > 空
    """
    aggregated = {}
    for cid in content_ids:
        cache_file = os.path.join(ANALYTICS_DIR, f"{cid}.json")
        if os.path.exists(cache_file):
            cached = atomic_read_json(cache_file)
            if cached is not None:
                if cached.get("metrics") and any(
                    v > 0 for v in cached["metrics"].values()
                    if isinstance(v, (int, float))
                ):
                    aggregated[cid] = cached["metrics"]
                    continue
            else:
                logger.debug("[content-analytics] 解析缓存文件失败，跳过缓存: safe_read_json返回None")

        records = _read_publish_records(30)
        for rec in records:
            if rec.get("content_id") == cid:
                aggregated[cid] = {
                    "views": rec.get("views", 0),
                    "completion_rate": rec.get("completion_rate", 0),
                    "engagement_rate": rec.get("engagement_rate", 0),
                    "conversion_rate": rec.get("conversion_rate", 0),
                    "share_rate": rec.get("share_rate", 0),
                    "likes": rec.get("likes", 0),
                    "comments": rec.get("comments", 0),
                    "shares": rec.get("shares", 0),
                    "note": "从memory发布记录聚合（来源: memory/*.md）",
                }
                break
    return aggregated

def batch(days: int = 1, platforms: Optional[list] = None) -> dict[str, Any]:
    """batch

    Args:
        days (int): 参数说明
        platforms (Optional[list]): 参数说明

    Returns:
        dict[str, Any]: 返回值说明
    """
    records = _read_publish_records(days)
    if not records:
        return {
            "total_analyzed": 0,
            "avg_score": 0,
            "rating_distribution": {"S": 0, "A": 0, "B": 0, "C": 0},
            "top_contents": [],
            "bottom_contents": [],
            "message": f"过去{days}天无发布记录",
        }

    results = []
    content_ids = [
        rec.get("content_id", "")
        for rec in records
        if not platforms or rec.get("platform", "douyin") in platforms
    ]
    memory_metrics = _batch_aggregate_from_memory(content_ids, "douyin")

    for rec in records:
        cid = rec.get("content_id", "")
        plat = rec.get("platform", "douyin")
        if platforms and plat not in platforms:
            continue
        try:
            if cid in memory_metrics:
                metrics = memory_metrics[cid]
                score = _compute_score(metrics)
                rating = _get_rating(score)
                suggestions = _generate_suggestions(rating, metrics)
                r = {
                    "content_id": cid,
                    "platform": plat,
                    "rating": rating,
                    "score": score,
                    "metrics": metrics,
                    "suggestions": suggestions,
                    "analyzed_at": datetime.now().isoformat(),
                    "data_source": "memory_aggregation",
                }
            else:
                r = analyze(cid, plat)
            results.append(r)
        except Exception as e:
            logger.error(f"[content_analytics] 分析异常: {e}")
            continue

    if not results:
        return {
            "total_analyzed": 0,
            "avg_score": 0,
            "rating_distribution": {"S": 0, "A": 0, "B": 0, "C": 0},
            "top_contents": [],
            "bottom_contents": [],
            "message": "无匹配平台的分析结果",
        }

    dist = {"S": 0, "A": 0, "B": 0, "C": 0}
    for r in results:
        dist[r["rating"]] = dist.get(r["rating"], 0) + 1

    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

    return {
        "total_analyzed": len(results),
        "avg_score": round(sum(r["score"] for r in results) / len(results), 1),
        "rating_distribution": dist,
        "top_contents": [{"content_id": r["content_id"], "rating": r["rating"], "score": r["score"]} for r in sorted_results[:3]],
        "bottom_contents": [{"content_id": r["content_id"], "rating": r["rating"], "score": r["score"]} for r in sorted_results[-3:]],
    }

def main():
    """main
    
    Raises:
        ValueError: 异常说明
    """
    try:
        args = _parse_args()
        action = args.get("action", "analyze")

        if action == "analyze":
            content_id = args.get("content")
            platform = args.get("platform", "douyin")
            if not content_id:
                raise ValueError("缺少 --content 参数")
            result = analyze(content_id, platform)
            has_real_data = result.get("data_source") != "no_data"
            output = {"success": has_real_data, "data": result,
                      "error": None if has_real_data else "无可用数据源,无法进行业务分析",
                      "code": None if has_real_data else "NO_DATA_SOURCE"}

        elif action == "batch":
            days = int(args.get("days", "1"))
            plats = args.get("platforms")
            platform_list = plats.split(",") if plats else None
            result = batch(days, platform_list)
            output = {"success": True, "data": result, "error": None, "code": None}

        else:
            raise ValueError(f"无效操作: {action}，支持: analyze, batch")

        print(json.dumps(output, ensure_ascii=False))

    except ValueError as e:
        logger.error(f"content analytics异常: {e}", exc_info=True)
        logger.error(json.dumps({"success": False, "data": {}, "error": str(e), "code": "INVALID_PARAMS"}, ensure_ascii=False))
        sys.exit(1)
    except Exception as e:
        logger.error(f"content analytics异常: {e}", exc_info=True)
        logger.error(json.dumps({"success": False, "data": {}, "error": str(e), "code": "ANALYTICS_ERROR"}, ensure_ascii=False))
        sys.exit(2)

if __name__ == "__main__":
    main()
