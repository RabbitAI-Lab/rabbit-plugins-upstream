#!/usr/bin/env python3
"""A/B测试框架exec脚本 - 支持创建实验/记录结果/计算显著性/计算样本量"""

import argparse
import json
import math
import os
import sys
from datetime import datetime
from typing import Any

from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent.parent.parent / "scripts"))
sys.path.insert(0, str(_Path(__file__).resolve().parents[3]))  # T4-4: 添加项目根以支持mcps.shared导入
from mcps.shared.db_logger import get_logger
from mcps.shared.db_pool import get_connection, return_connection
logger = get_logger("ab-testing", source="skills/ab-testing/scripts/ab_testing.py")  # P2-06: 从_lazy激活
from mcps.shared.atomic_write import atomic_read_json, atomic_write_json


def json_out(success: bool, data: dict[str, Any] | None = None,
             error: str | None = None, code: str | None = None) -> None:
    """统一JSON输出

    Args:
        success (bool): 参数说明
        data (dict[str, Any] | None): 参数说明
        error (str | None): 参数说明
        code (str | None): 参数说明
    """
    print(json.dumps({"success": success, "data": data or {},
                       "error": error, "code": code}, ensure_ascii=False))


def get_data_dir() -> str:
    """获取数据存储目录(统一为SKILL.md定义的memory/ab-tests/)

    Returns:
        str: 返回值说明
    """
    # 查找项目根目录(向上找到JueJin)
    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_dir = os.path.join(base, "memory", "ab_tests")
    os.makedirs(data_dir, exist_ok=True)
    return data_dir


def cmd_create(args: argparse.Namespace) -> None:
    """创建A/B测试实验

    Args:
        args (argparse.Namespace): 参数说明
    
    Raises:
        ValueError: 异常说明
    """
    try:
        name = args.name
        metric = args.metric
        variants = [v.strip() for v in args.variants.split(",")]
        if len(variants) < 2:
            json_out(False, error="至少需要2个变体", code="INVALID_VARIANTS")
            sys.exit(1)
        # P0-V2-02: 可选解析variant_contents(变体→内容URL列表)
        variant_contents: dict[str, list[str]] = {}
        if hasattr(args, "variant_contents") and args.variant_contents:
            try:
                parsed = json.loads(args.variant_contents)
                if not isinstance(parsed, dict):
                    raise ValueError("variant_contents必须是JSON对象")
                for v in variants:
                    urls = parsed.get(v, [])
                    if urls:
                        variant_contents[v] = urls
            except json.JSONDecodeError as e:
                json_out(False, error=f"variant_contents JSON解析失败: {e}", code="INVALID_JSON")
                sys.exit(1)
        # 生成测试ID
        today = datetime.now().strftime("%Y%m%d")
        data_dir = get_data_dir()
        existing = [f for f in os.listdir(data_dir) if f.startswith(f"ab_test_{today}")]
        seq = len(existing) + 1
        test_id = f"ab_test_{today}_{seq:02d}"
        # 构建实验数据
        test_data: dict[str, Any] = {
            "test_id": test_id, "name": name, "metric": metric,
            "variants": {v: {"samples": 0, "conversions": 0} for v in variants},
            "results": [], "status": "running",
            "created_at": datetime.now().isoformat()
        }
        if variant_contents:
            test_data["variant_contents"] = variant_contents
        filepath = os.path.join(data_dir, f"{test_id}.json")
        atomic_write_json(filepath, test_data, indent=2, ensure_ascii=False)
        json_out(True, data={"test_id": test_id, "name": name, "metric": metric,
                              "variants": variants, "status": "running"})
    except ValueError as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="INVALID_PARAMS")
        sys.exit(1)
    except Exception as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="CREATE_ERROR")
        sys.exit(2)


def cmd_result(args: argparse.Namespace) -> None:
    """记录实验结果

    Args:
        args (argparse.Namespace): 参数说明
    """
    try:
        test_id = args.test_id
        variant = args.variant
        value = float(args.value)
        data_dir = get_data_dir()
        filepath = os.path.join(data_dir, f"{test_id}.json")
        if not os.path.exists(filepath):
            json_out(False, error=f"测试不存在: {test_id}", code="TEST_NOT_FOUND")
            sys.exit(1)
        test_data = atomic_read_json(filepath)
        if variant not in test_data["variants"]:
            json_out(False, error=f"变体不存在: {variant}", code="INVALID_VARIANTS")
            sys.exit(1)
        # 追加结果记录
        test_data["results"].append({
            "variant": variant, "value": value,
            "timestamp": datetime.now().isoformat()
        })
        # 更新变体统计
        test_data["variants"][variant]["samples"] += 1
        if value > 0:
            test_data["variants"][variant]["conversions"] += 1
        atomic_write_json(filepath, test_data, indent=2, ensure_ascii=False)
        json_out(True, data={"test_id": test_id, "variant": variant,
                              "value": value, "total_samples": test_data["variants"][variant]["samples"]})
    except ValueError as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="INVALID_PARAMS")
        sys.exit(1)
    except Exception as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="RESULT_ERROR")
        sys.exit(2)


def cmd_significance(args: argparse.Namespace) -> None:
    """计算Z检验显著性

    Args:
        args (argparse.Namespace): 参数说明
    """
    try:
        test_id = args.test_id
        data_dir = get_data_dir()
        filepath = os.path.join(data_dir, f"{test_id}.json")
        if not os.path.exists(filepath):
            json_out(False, error=f"测试不存在: {test_id}", code="TEST_NOT_FOUND")
            sys.exit(1)
        test_data = atomic_read_json(filepath)
        variants = list(test_data["variants"].keys())
        if len(variants) < 2:
            json_out(False, error="至少需要2个变体才能计算显著性", code="INSUFFICIENT_SAMPLE")
            sys.exit(1)
        # 取前两个变体做Z检验
        v_a, v_b = variants[0], variants[1]
        stats_a = test_data["variants"][v_a]
        stats_b = test_data["variants"][v_b]
        n_a, c_a = stats_a["samples"], stats_a["conversions"]
        n_b, c_b = stats_b["samples"], stats_b["conversions"]
        if n_a < 30 or n_b < 30:
            json_out(False, error="样本量不足(每变体至少30)", code="INSUFFICIENT_SAMPLE")
            sys.exit(1)
        p_a = c_a / n_a
        p_b = c_b / n_b
        p_pool = (c_a + c_b) / (n_a + n_b)
        # Z检验
        se = math.sqrt(p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b))
        if se == 0:
            z_score = 0.0
        else:
            z_score = (p_b - p_a) / se
        # 近似p值(双侧检验)
        p_value = 2 * (1 - _norm_cdf(abs(z_score)))
        confidence = 1 - p_value
        significant = p_value < 0.05
        lift = ((p_b - p_a) / p_a * 100) if p_a > 0 else 0.0
        json_out(True, data={
            "test_id": test_id, "variant_a": v_a, "variant_b": v_b,
            "rate_a": round(p_a, 4), "rate_b": round(p_b, 4),
            "z_score": round(z_score, 4), "p_value": round(p_value, 6),
            "confidence": round(confidence, 4), "significant": significant,
            "lift": f"{lift:+.1f}%"
        })
    except ValueError as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="INVALID_PARAMS")
        sys.exit(1)
    except Exception as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="SIGNIFICANCE_ERROR")
        sys.exit(2)


def cmd_sample_size(args: argparse.Namespace) -> None:
    """计算所需样本量

    Args:
        args (argparse.Namespace): 参数说明
    """
    try:
        baseline = float(args.baseline_rate)
        mde = float(args.mde)
        confidence = float(args.confidence)
        if not (0 < baseline < 1):
            json_out(False, error="基线转化率须在(0,1)之间", code="INVALID_PARAMS")
            sys.exit(1)
        if not (0 < mde < 1):
            json_out(False, error="最小检测效果须在(0,1)之间", code="INVALID_PARAMS")
            sys.exit(1)
        # Z值映射
        z_map = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
        z_alpha = z_map.get(confidence, 1.96)
        z_beta = 0.842  # 统计功效80%
        p2 = baseline * (1 + mde)
        p_avg = (baseline + p2) / 2
        n = ((z_alpha * math.sqrt(2 * p_avg * (1 - p_avg)) +
              z_beta * math.sqrt(baseline * (1 - baseline) + p2 * (1 - p2))) ** 2) / \
            (p2 - baseline) ** 2
        n = math.ceil(n)
        json_out(True, data={
            "baseline_rate": baseline, "mde": mde, "confidence": confidence,
            "sample_per_variant": n, "total_sample": n * 2
        })
    except ValueError as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="INVALID_PARAMS")
        sys.exit(1)
    except Exception as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="SAMPLE_SIZE_ERROR")
        sys.exit(2)


# 假设生成模板(规则驱动,不依赖LLM)
_HYPOTHESIS_TEMPLATES = {
    "content": {
        "metric_default": "conversion_rate",
        "template": "假设: 变体{variant}的{metric}显著优于基线,提升幅度≥{mde_pct}%",
        "variants_hint": ["模板A(基线)", "模板B(实验)"],
    },
    "strategy": {
        "metric_default": "reply_rate",
        "template": "假设: 变体{variant}的{metric}显著优于基线,提升幅度≥{mde_pct}%",
        "variants_hint": ["策略A(基线)", "策略B(实验)"],
    },
    "pricing": {
        "metric_default": "purchase_rate",
        "template": "假设: 变体{variant}的{metric}显著优于基线,提升幅度≥{mde_pct}%",
        "variants_hint": ["定价A(基线)", "定价B(实验)"],
    },
}


def cmd_hypothesis(args: argparse.Namespace) -> None:
    """自动生成A/B测试假设(规则模板驱动,补全假设生成环节)

    Args:
        args (argparse.Namespace): 参数说明
    """
    try:
        test_type = args.test_type
        baseline_rate = float(args.baseline_rate)
        mde = float(args.mde)
        if test_type not in _HYPOTHESIS_TEMPLATES:
            json_out(False, error=f"不支持的测试类型: {test_type}, 可选: content/strategy/pricing",
                     code="INVALID_PARAMS")
            sys.exit(1)
        if not (0 < baseline_rate < 1):
            json_out(False, error="基线转化率须在(0,1)之间", code="INVALID_PARAMS")
            sys.exit(1)
        if not (0 < mde < 1):
            json_out(False, error="最小检测效果须在(0,1)之间", code="INVALID_PARAMS")
            sys.exit(1)
        tpl = _HYPOTHESIS_TEMPLATES[test_type]
        metric = args.metric or tpl["metric_default"]
        mde_pct = round(mde * 100, 1)
        hypotheses = []
        for variant in tpl["variants_hint"]:
            hypotheses.append({
                "variant": variant,
                "hypothesis": tpl["template"].format(variant=variant, metric=metric, mde_pct=mde_pct),
                "metric": metric,
                "expected_lift_pct": mde_pct,
            })
        # 计算所需样本量(复用样本量计算逻辑)
        z_alpha = 1.96  # 95%置信
        z_beta = 0.842
        p2 = baseline_rate * (1 + mde)
        p_avg = (baseline_rate + p2) / 2
        n = ((z_alpha * math.sqrt(2 * p_avg * (1 - p_avg)) +
              z_beta * math.sqrt(baseline_rate * (1 - baseline_rate) + p2 * (1 - p2))) ** 2) / \
            (p2 - baseline_rate) ** 2
        sample_per_variant = math.ceil(n)
        json_out(True, data={
            "test_type": test_type, "metric": metric,
            "baseline_rate": baseline_rate, "mde": mde,
            "hypotheses": hypotheses,
            "sample_per_variant": sample_per_variant,
            "auto_assign_strategy": "uniform",  # 均匀分流
            "status": "hypothesis_ready",
        })
    except ValueError as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="INVALID_PARAMS")
        sys.exit(1)
    except Exception as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="HYPOTHESIS_ERROR")
        sys.exit(2)


def cmd_decide(args: argparse.Namespace) -> None:
    """根据显著性结果自动给出决策建议(补全决策环节)

    Args:
        args (argparse.Namespace): 参数说明
    """
    try:
        test_id = args.test_id
        data_dir = get_data_dir()
        filepath = os.path.join(data_dir, f"{test_id}.json")
        if not os.path.exists(filepath):
            json_out(False, error=f"测试不存在: {test_id}", code="TEST_NOT_FOUND")
            sys.exit(1)
        test_data = atomic_read_json(filepath)
        variants = list(test_data["variants"].keys())
        if len(variants) < 2:
            json_out(False, error="至少需要2个变体才能决策", code="INSUFFICIENT_SAMPLE")
            sys.exit(1)
        # 复用显著性计算
        v_a, v_b = variants[0], variants[1]
        stats_a = test_data["variants"][v_a]
        stats_b = test_data["variants"][v_b]
        n_a, c_a = stats_a["samples"], stats_a["conversions"]
        n_b, c_b = stats_b["samples"], stats_b["conversions"]
        # 决策规则
        if n_a < 30 or n_b < 30:
            decision = "continue_collect"
            reason = f"样本量不足(A={n_a}, B={n_b}, 阈值=30),继续收集数据"
            winner = None
        else:
            p_a = c_a / n_a
            p_b = c_b / n_b
            p_pool = (c_a + c_b) / (n_a + n_b)
            se = math.sqrt(p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b))
            z_score = 0.0 if se == 0 else (p_b - p_a) / se
            p_value = 2 * (1 - _norm_cdf(abs(z_score)))
            lift = ((p_b - p_a) / p_a * 100) if p_a > 0 else 0.0
            if p_value < 0.05 and abs(lift) >= 10:
                if p_b > p_a:
                    decision = "ship_variant_b"
                    reason = f"B显著优于A(p={p_value:.4f}, lift={lift:+.1f}%),采纳B"
                    winner = v_b
                else:
                    decision = "keep_variant_a"
                    reason = f"A显著优于B(p={p_value:.4f}, lift={lift:+.1f}%),保留A"
                    winner = v_a
            elif p_value < 0.05 and abs(lift) < 10:
                decision = "no_practical_diff"
                reason = f"统计显著但提升幅度<10%(lift={lift:+.1f}%),无实际意义,保留A"
                winner = v_a
            else:
                decision = "continue_collect"
                reason = f"未达统计显著(p={p_value:.4f}),继续收集数据"
                winner = None
        # 更新测试状态(若已得出结论)
        if decision in ("ship_variant_b", "keep_variant_a", "no_practical_diff"):
            test_data["status"] = "completed"
            test_data["winner"] = winner
            atomic_write_json(filepath, test_data, indent=2, ensure_ascii=False)
        json_out(True, data={
            "test_id": test_id,
            "decision": decision,
            "reason": reason,
            "winner": winner,
            "current_samples": {"A": n_a, "B": n_b},
        })
    except ValueError as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="INVALID_PARAMS")
        sys.exit(1)
    except Exception as e:
        logger.error(f"ab testing异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="DECIDE_ERROR")
        sys.exit(2)


def _norm_cdf(x: float) -> float:
    """标准正态分布CDF近似计算(Abramowitz & Stegun)"""
    t = 1.0 / (1.0 + 0.2316419 * x)
    d = 0.3989422804014327  # 1/sqrt(2*pi)
    p = d * math.exp(-x * x / 2) * (
        0.319381530 * t - 0.356563782 * t**2 + 1.781477937 * t**3
        - 1.821255978 * t**4 + 1.330274429 * t**5)
    return 1.0 - p


def cmd_compare(args: argparse.Namespace) -> None:
    """P0-V2-02: 从content_stats自动采集A/B测试数据并对比表现

    读取测试JSON中各变体的content_urls,查询content_stats获取真实互动数据,
    聚合后进行Z检验显著性对比。
    统一入口: PG查询通过_pg_query工具(规则18)

    Args:
        args (argparse.Namespace): 参数说明
    """
    try:
        test_id = args.test_id
        tenant_id = args.tenant_id
        data_dir = get_data_dir()
        filepath = os.path.join(data_dir, f"{test_id}.json")
        if not os.path.exists(filepath):
            json_out(False, error=f"测试不存在: {test_id}", code="TEST_NOT_FOUND")
            sys.exit(1)
        test_data = atomic_read_json(filepath)

        variants = list(test_data["variants"].keys())
        if len(variants) < 2:
            json_out(False, error="至少需要2个变体才能对比", code="INSUFFICIENT_VARIANTS")
            sys.exit(1)

        # P0-V2-02: 从content_stats自动采集数据
        # 测试JSON中可选存储variant_contents: {"variantA": ["url1","url2"], "variantB": ["url3"]}
        variant_contents = test_data.get("variant_contents", {})
        variant_metrics: dict[str, dict[str, Any]] = {}

        if variant_contents and tenant_id:
            # 从PG content_stats查询各变体内容的互动数据
            sys.path.insert(0, str(_Path(__file__).resolve().parent.parent.parent.parent / "scripts"))
            try:
                import psycopg2
                import psycopg2.extras
                conn_str = os.environ.get("POSTGRES_CONNECTION_STRING") or os.environ.get("DATABASE_URL", "")
                if not conn_str:
                    json_out(False, error="数据库连接字符串未配置", code="DB_NOT_CONFIGURED")
                    sys.exit(1)
                # R75.2: 使用db_pool统一连接池(替代psycopg2.connect碎片化)
                conn = get_connection()
                try:
                    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                        for variant in variants:
                            urls = variant_contents.get(variant, [])
                            if not urls:
                                variant_metrics[variant] = {"views": 0, "likes": 0, "comments": 0, "shares": 0, "favorites": 0, "count": 0}
                                continue
                            placeholders = ",".join(["%s"] * len(urls))
                            cur.execute(f"""
                                SELECT
                                    COALESCE(SUM(view_count), 0) as views,
                                    COALESCE(SUM(like_count), 0) as likes,
                                    COALESCE(SUM(comment_count), 0) as comments,
                                    COALESCE(SUM(share_count), 0) as shares,
                                    COALESCE(SUM(favorite_count), 0) as favorites,
                                    COUNT(*) as count
                                FROM content_stats
                                WHERE tenant_id = %s AND content_url IN ({placeholders})
                            """, [tenant_id] + urls)
                            row = cur.fetchone()
                            variant_metrics[variant] = {
                                "views": int(row["views"] or 0),
                                "likes": int(row["likes"] or 0),
                                "comments": int(row["comments"] or 0),
                                "shares": int(row["shares"] or 0),
                                "favorites": int(row["favorites"] or 0),
                                "count": int(row["count"] or 0),
                            }
                finally:
                    return_connection(conn)
            except ImportError:
                json_out(False, error="psycopg2未安装", code="PSYCOPG2_MISSING")
                sys.exit(1)
        else:
            # 无variant_contents时,使用手动记录的results数据
            for variant in variants:
                results = [r for r in test_data.get("results", []) if r.get("variant") == variant]
                values = [r.get("value", 0) for r in results]
                variant_metrics[variant] = {
                    "views": len(values),
                    "likes": sum(1 for v in values if v > 0),
                    "comments": 0,
                    "shares": 0,
                    "favorites": 0,
                    "count": len(values),
                    "avg_value": round(sum(values) / len(values), 4) if values else 0,
                }

        # 对比前两个变体
        v_a, v_b = variants[0], variants[1]
        m_a = variant_metrics[v_a]
        m_b = variant_metrics[v_b]

        # 计算各指标的提升幅度
        comparison: dict[str, Any] = {}
        for metric in ["views", "likes", "comments", "shares", "favorites"]:
            val_a = m_a.get(metric, 0)
            val_b = m_b.get(metric, 0)
            lift = ((val_b - val_a) / val_a * 100) if val_a > 0 else 0.0
            comparison[metric] = {
                "variant_a": val_a,
                "variant_b": val_b,
                "lift_pct": round(lift, 1),
            }

        # Z检验(基于likes/view作为转化率)
        n_a = m_a.get("views", 0)
        c_a = m_a.get("likes", 0)
        n_b = m_b.get("views", 0)
        c_b = m_b.get("likes", 0)
        if n_a >= 30 and n_b >= 30:
            p_a = c_a / n_a if n_a > 0 else 0
            p_b = c_b / n_b if n_b > 0 else 0
            p_pool = (c_a + c_b) / (n_a + n_b) if (n_a + n_b) > 0 else 0
            se = math.sqrt(p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b)) if n_a > 0 and n_b > 0 else 0
            z_score = 0.0 if se == 0 else (p_b - p_a) / se
            p_value = 2 * (1 - _norm_cdf(abs(z_score)))
            significance = {
                "z_score": round(z_score, 4),
                "p_value": round(p_value, 6),
                "significant": p_value < 0.05,
                "confidence": round(1 - p_value, 4),
                "rate_a": round(p_a, 4),
                "rate_b": round(p_b, 4),
            }
        else:
            significance = {
                "z_score": 0.0,
                "p_value": 1.0,
                "significant": False,
                "confidence": 0.0,
                "rate_a": 0.0,
                "rate_b": 0.0,
                "note": f"样本量不足(A={n_a}, B={n_b}, 阈值=30)",
            }

        json_out(True, data={
            "test_id": test_id,
            "variant_a": v_a,
            "variant_b": v_b,
            "metrics_a": m_a,
            "metrics_b": m_b,
            "comparison": comparison,
            "significance": significance,
            "data_source": "content_stats" if variant_contents and tenant_id else "manual_results",
        })
    except ValueError as e:
        logger.error(f"ab testing compare异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="INVALID_PARAMS")
        sys.exit(1)
    except Exception as e:
        logger.error(f"ab testing compare异常: {e}", exc_info=True)
        json_out(False, error=str(e), code="COMPARE_ERROR")
        sys.exit(2)


def main() -> None:
    """main"""
    parser = argparse.ArgumentParser(description="A/B测试框架")
    sub = parser.add_subparsers(dest="command")
    # 创建实验
    p_create = sub.add_parser("create", help="创建A/B测试实验")
    p_create.add_argument("--name", required=True, help="实验名称")
    p_create.add_argument("--metric", required=True, help="核心指标")
    p_create.add_argument("--variants", required=True, help="变体列表,逗号分隔")
    p_create.add_argument("--variant-contents", default=None, help="P0-V2-02: 变体内容URL映射JSON,如{\"A\":[\"url1\"],\"B\":[\"url2\"]}")
    # 记录结果
    p_result = sub.add_parser("result", help="记录实验结果")
    p_result.add_argument("--test-id", required=True, help="测试ID")
    p_result.add_argument("--variant", required=True, help="变体名称")
    p_result.add_argument("--value", required=True, help="结果值")
    # 计算显著性
    p_sig = sub.add_parser("significance", help="计算Z检验显著性")
    p_sig.add_argument("--test-id", required=True, help="测试ID")
    # 计算样本量
    p_ss = sub.add_parser("sample_size", help="计算所需样本量")
    p_ss.add_argument("--baseline-rate", required=True, help="基线转化率")
    p_ss.add_argument("--mde", required=True, help="最小检测效果")
    p_ss.add_argument("--confidence", default="0.95", help="置信度(默认0.95)")
    # 生成假设(P3-02新增:补全假设生成环节)
    p_hyp = sub.add_parser("hypothesis", help="自动生成A/B测试假设")
    p_hyp.add_argument("--test-type", required=True, help="测试类型: content/strategy/pricing")
    p_hyp.add_argument("--baseline-rate", required=True, help="基线转化率(0-1)")
    p_hyp.add_argument("--mde", required=True, help="最小检测效果(0-1)")
    p_hyp.add_argument("--metric", default=None, help="核心指标(可选,默认按类型选择)")
    # 自动决策(P3-02新增:补全决策环节)
    p_dec = sub.add_parser("decide", help="根据显著性结果自动给出决策建议")
    p_dec.add_argument("--test-id", required=True, help="测试ID")
    # P0-V2-02新增: 从content_stats自动采集数据对比A/B表现
    p_cmp = sub.add_parser("compare", help="从content_stats自动采集数据对比A/B表现")
    p_cmp.add_argument("--test-id", required=True, help="测试ID")
    p_cmp.add_argument("--tenant-id", required=True, help="租户ID(用于查询content_stats)")
    args = parser.parse_args()
    if args.command == "create":
        cmd_create(args)
    elif args.command == "result":
        cmd_result(args)
    elif args.command == "significance":
        cmd_significance(args)
    elif args.command == "sample_size":
        cmd_sample_size(args)
    elif args.command == "hypothesis":
        cmd_hypothesis(args)
    elif args.command == "decide":
        cmd_decide(args)
    elif args.command == "compare":
        cmd_compare(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
