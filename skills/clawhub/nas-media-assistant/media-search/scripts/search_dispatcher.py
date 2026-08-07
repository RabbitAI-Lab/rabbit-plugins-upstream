#!/usr/bin/env python3
"""网页磁力检索调度器（链路1）。

分层检索 + 并行调度网页源 parser，拿磁力/直链/播放页链接，聚合去重评分后输出候选。

设计原则: 网页抓取是脆弱的外围，标题解析才是稳定的核心。
- parser 只抓页面原始文本（标题串 + 链接），不做信息提取。
- aggregator 调 title_parser 统一解析标题串。
- 分层检索: tier-1（常用 2~3 源）优先并行检索 + 评分；结果不足（数量/相关度不够）
  才回退 tier-2 补检索，避免每次都打满全部站点、降低对易失源的依赖。

充足性判定（v2·2026-08）：避免"单源 3 条全单集"被误判为充足。
- 必须 ≥MIN_OK_SOURCES 个 tier-1 源成功返回结果
- 且 ≥1 条高分完整资源（is_single_episode=False 且 quality_score≥HIGH_SCORE_THRESHOLD）
- 否则视为不足，触发 tier-2 回退

网盘分享检索功能已下线（独立项目承接），本调度器仅处理网页磁力/直链。
媒体识别由 media-lookup 技能（链路0·TMDB）按需提供；本技能 title_parser 已能从结果文件名提取年份/清晰度/编码/音轨。

用法:
  search_dispatcher.py '<查询JSON>'
查询JSON 示例:
  {"title":"流浪地球2","type":"movie","year":"2023","quality":"1080p"}

输出:
  {"candidates":[...],"excluded":[...],"from_cache":bool,"link":"web","stats":{...}}
"""
import hashlib
import importlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError as FuturesTimeout

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPTS_DIR)
sys.path.insert(0, SCRIPTS_DIR)

from health_check import HealthChecker  # noqa: E402
from aggregator import aggregate  # noqa: E402

# ---------- 充足性判定阈值（v2）----------
# 至少 2 个 tier-1 源成功返回，才视为"广泛命中"；避免单源零散结果被误判为充足
MIN_OK_SOURCES = 2
# 至少 1 条高分完整资源（非单集 + 评分阈值）；单集/低分不算
HIGH_SCORE_THRESHOLD = 60


def load_config():
    cfg_path = os.path.join(SKILL_DIR, "assets", "config.json")
    if not os.path.exists(cfg_path):
        cfg_path = os.path.join(SKILL_DIR, "assets", "config_template.json")
    with open(cfg_path, encoding="utf-8") as f:
        return json.load(f)


# ---------- 缓存 ----------
def cache_key(query):
    return hashlib.md5(
        json.dumps(query, sort_keys=True, ensure_ascii=False).encode()
    ).hexdigest()


def get_cached(key, cache_dir, ttl=3600):
    p = os.path.join(cache_dir, f"{key}.json")
    if os.path.exists(p) and time.time() - os.path.getmtime(p) < ttl:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return None


def set_cache(key, data, cache_dir):
    os.makedirs(cache_dir, exist_ok=True)
    p = os.path.join(cache_dir, f"{key}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ---------- parser 动态加载 ----------
def load_parser(module_path, func_name="parse"):
    """动态加载 parser 模块的 parse 函数，找不到返回 None。"""
    try:
        mod = importlib.import_module(module_path)
        return getattr(mod, func_name, None)
    except Exception:
        return None


def run_web_source(source_cfg, query):
    """网页源: 动态加载 search_sources.web.<parser_id>.parse。"""
    parser_id = source_cfg.get("parser") or source_cfg.get("id")
    fn = load_parser(f"search_sources.web.{parser_id}")
    if not fn:
        raise RuntimeError(f"parser {parser_id} 未找到或无 parse 函数")
    return fn(query, source_cfg) or []


def _fetch_parallel(sources, query, health, timeout_sec):
    """并行检索一批源，返回 (raw_candidates, source_stats)。"""
    raw = []
    source_stats = {}
    if not sources:
        return raw, source_stats
    with ThreadPoolExecutor(max_workers=max(4, len(sources))) as pool:
        futures = {pool.submit(run_web_source, s, query): s["id"] for s in sources}
        try:
            for fut in as_completed(futures, timeout=timeout_sec):
                sid = futures[fut]
                try:
                    result = fut.result()
                    for c in result:
                        if isinstance(c, dict):
                            c.setdefault("source_type", "web")
                            c.setdefault("source_id", sid)
                    raw.extend(result)
                    health.record(sid, True)
                    source_stats[sid] = {"ok": True, "count": len(result)}
                except Exception as e:
                    health.record(sid, False, str(e))
                    source_stats[sid] = {"ok": False, "error": str(e)}
        except FuturesTimeout:
            for fut, sid in futures.items():
                if not fut.done():
                    fut.cancel()
                    health.record(sid, False, "timeout")
                    source_stats.setdefault(sid, {"ok": False, "error": "timeout"})
    return raw, source_stats


def _partition_tiers(sources, tier1_size):
    """按 priority 升序切分 tier-1 / tier-2。"""
    ordered = sorted(sources, key=lambda s: s.get("priority", 99))
    cut = max(1, int(tier1_size))
    return ordered[:cut], ordered[cut:]


def _tag_tier(raw, tier):
    """给候选打 tier 标记（调试/统计用）。"""
    for c in raw:
        if isinstance(c, dict):
            c["tier"] = tier
    return raw


def _sufficient(raw, source_stats, query, config):
    """判定 tier-1 结果是否充足（v2·避免单源零散结果被误判为充足）。

    判定条件（同时满足）：
    1. ≥MIN_OK_SOURCES 个源成功返回（避免单源误判）
    2. ≥1 条高分完整资源（is_single_episode=False 且 quality_score≥HIGH_SCORE_THRESHOLD）

    Returns:
        (sufficient, t1_count, has_high_quality, ok_sources)
    """
    query_title = query.get("title", "")
    query_year = str(query.get("year", ""))
    query_type = query.get("type", "")
    min_relevance = config.get("min_relevance", 0.6)
    agg = aggregate(raw, query_title, query_year, query_type,
                    top_n=0, min_relevance=min_relevance)
    candidates = agg["candidates"]
    ok_sources = sum(1 for s in source_stats.values() if s.get("ok"))
    has_high_quality = any(
        (not c.get("is_single_episode"))
        and (c.get("quality_score", 0) >= HIGH_SCORE_THRESHOLD)
        for c in candidates
    )
    sufficient = (ok_sources >= MIN_OK_SOURCES) and has_high_quality
    return sufficient, len(candidates), has_high_quality, ok_sources


def _log_dispatch(stage, message, **kv):
    """标准化调度日志（写到 stderr，不污染 JSON 输出）。"""
    payload = {"stage": stage, "msg": message, **kv}
    sys.stderr.write(f"[search_dispatcher] {json.dumps(payload, ensure_ascii=False)}\n")
    sys.stderr.flush()


def dispatch(query, config):
    raw_cache_dir = config.get("cache_dir", os.path.join(SKILL_DIR, ".cache"))
    cache_dir = os.path.expanduser(raw_cache_dir)
    if not os.path.isabs(cache_dir):
        cache_dir = os.path.join(SKILL_DIR, cache_dir)

    key = cache_key(query)
    cached = get_cached(key, cache_dir)
    if cached is not None:
        return dict(cached, from_cache=True)

    raw_health_file = config.get("health_file")
    health_file = os.path.expanduser(raw_health_file) if raw_health_file else None
    health = HealthChecker(health_file)

    # 启用的 + 健康的源（同时记录被跳过的源，便于日志）
    all_sources = config.get("web_sources", [])
    web_sources = []
    skipped_sources = []
    for s in all_sources:
        if not s.get("enabled"):
            skipped_sources.append({"id": s["id"], "reason": "disabled"})
            continue
        if not health.is_healthy(s["id"]):
            reason = health.session_unhealthy_reason(s["id"]) or "persistent_removed"
            skipped_sources.append({"id": s["id"], "reason": reason})
            continue
        web_sources.append(s)

    query_title = query.get("title", "")
    query_year = str(query.get("year", ""))
    query_type = query.get("type", "")
    top_n = config.get("top_n", 3)
    min_relevance = config.get("min_relevance", 0.6)
    timeout_sec = config.get("timeout", 30)
    tier1_size = config.get("tier1_size", 3)

    tier1, tier2 = _partition_tiers(web_sources, tier1_size)

    source_stats = {}
    tiers_searched = ["tier1"]
    started = time.time()

    _log_dispatch(
        "start",
        "开始分层检索",
        query={"title": query_title, "year": query_year, "type": query_type},
        tier1_ids=[s["id"] for s in tier1],
        tier2_ids=[s["id"] for s in tier2],
    )

    # tier-1: 常用源优先并行检索
    raw_t1, stats_t1 = _fetch_parallel(tier1, query, health, timeout_sec)
    _tag_tier(raw_t1, 1)
    source_stats.update(stats_t1)

    # 充足性判定（v2）
    raw_all = list(raw_t1)
    sufficient, t1_count, has_hq, t1_ok_sources = _sufficient(
        raw_t1, stats_t1, query, config
    )

    _log_dispatch(
        "tier1_done",
        "tier-1 检索完成",
        tier1_ids=[s["id"] for s in tier1],
        tier1_count=t1_count,
        tier1_ok_sources=t1_ok_sources,
        has_high_quality=has_hq,
        sufficient=sufficient,
    )

    if not sufficient and tier2:
        # tier-2 回退补检索
        tiers_searched.append("tier2")
        _log_dispatch("tier2_start", "tier-1 不足，回退 tier-2",
                       reason=f"ok_sources={t1_ok_sources}<{MIN_OK_SOURCES} 或 无高分完整资源")
        raw_t2, stats_t2 = _fetch_parallel(tier2, query, health, timeout_sec)
        _tag_tier(raw_t2, 2)
        source_stats.update(stats_t2)
        raw_all.extend(raw_t2)
        _log_dispatch(
            "tier2_done",
            "tier-2 检索完成",
            tier2_ids=[s["id"] for s in tier2],
            tier2_count=len(raw_t2),
        )
    elif not tier2:
        _log_dispatch("tier2_skip", "无 tier-2 源可回退")

    # 聚合: 富集(标题解析) + 去重 + 评分 + 排序 + 硬过滤
    agg_result = aggregate(raw_all, query_title, query_year, query_type,
                            top_n=top_n, min_relevance=min_relevance)

    final = agg_result["candidates"]
    excluded = agg_result["excluded"]
    elapsed = round(time.time() - started, 2)

    result = {
        "candidates": final,
        "excluded": excluded,
        "from_cache": False,
        "link": "web",
        "stats": {
            "raw": len(raw_all),
            "final": len(final),
            "excluded": len(excluded),
            "tiers": tiers_searched,
            "tier1_sufficient": sufficient,
            "tier1_count": t1_count,
            "tier1_ok_sources": t1_ok_sources,
            "elapsed_sec": elapsed,
            "sources": source_stats,
            "skipped_sources": skipped_sources,
        },
    }

    # 来源逐条命中日志（便于对比/调试）
    per_source_log = {}
    for s in source_stats:
        cnt = source_stats[s].get("count", 0) if source_stats[s].get("ok") else 0
        per_source_log[s] = cnt
    _log_dispatch(
        "end",
        "检索完成",
        raw_total=len(raw_all),
        final=len(final),
        tiers=tiers_searched,
        per_source_count=per_source_log,
        elapsed_sec=elapsed,
    )

    set_cache(key, result, cache_dir)
    return result


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "用法: search_dispatcher.py '<查询JSON>'"}))
        sys.exit(1)
    query = json.loads(sys.argv[1])
    config = load_config()
    result = dispatch(query, config)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
