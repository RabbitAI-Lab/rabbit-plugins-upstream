#!/usr/bin/env python3
"""Calculate an auditable five-factor GEO brand score from normalized metrics."""

from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path
import sys
from typing import Any


FORMULA_VERSION = "五指标综合口径 v1"
METHOD_ID = "template_five_factor_v1"
WEIGHTS = {
    "品牌提及率": Decimal("0.55"),
    "全量 Top3 覆盖率": Decimal("0.20"),
    "平均排名质量": Decimal("0.10"),
    "正面/中性情感": Decimal("0.10"),
    "提及强度": Decimal("0.05"),
}


def decimal_number(value: Any, label: str) -> Decimal:
    if isinstance(value, bool) or value is None:
        raise ValueError(f"{label}必须是数字")
    try:
        number = Decimal(str(value))
    except Exception as exc:
        raise ValueError(f"{label}必须是数字") from exc
    if not number.is_finite():
        raise ValueError(f"{label}必须是有限数字")
    return number


def count(metrics: dict[str, Any], key: str, label: str) -> int:
    value = metrics.get(key)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{label}必须是非负整数")
    return value


def percentage(numerator: int, denominator: int) -> Decimal:
    if denominator == 0:
        return Decimal("0")
    return Decimal(numerator) / Decimal(denominator) * Decimal("100")


def rounded(value: Decimal, places: str = "0.01") -> float:
    return float(value.quantize(Decimal(places), rounding=ROUND_HALF_UP))


def calculate_brand_score(metrics: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(metrics, dict):
        raise ValueError("评分输入必须是对象")

    successful_answers = count(metrics, "successful_answers", "成功回答数")
    mentioning_answers = count(
        metrics, "brand_mentioning_answers", "品牌提及回答数"
    )
    valid_segments = count(
        metrics, "valid_recommendation_segments", "有效推荐段数"
    )
    top3_segments = count(metrics, "brand_top3_segments", "品牌 Top3 段数")
    ranked_segments = count(metrics, "brand_ranked_segments", "品牌进榜段数")
    brand_context_answers = count(
        metrics, "brand_context_answers", "品牌语境回答数"
    )
    nonnegative_context_answers = count(
        metrics, "nonnegative_context_answers", "正面或中性回答数"
    )
    brand_mentions = count(metrics, "brand_mentions", "品牌提及次数")

    if successful_answers < 1:
        raise ValueError("成功回答数必须大于零，空任务不得生成品牌得分")
    if mentioning_answers > successful_answers:
        raise ValueError("品牌提及回答数不得大于成功回答数")
    if ranked_segments > valid_segments:
        raise ValueError("品牌进榜段数不得大于有效推荐段数")
    if top3_segments > ranked_segments:
        raise ValueError("品牌 Top3 段数不得大于品牌进榜段数")
    if brand_context_answers > mentioning_answers:
        raise ValueError("品牌语境回答数不得大于品牌提及回答数")
    if nonnegative_context_answers > brand_context_answers:
        raise ValueError("正面或中性回答数不得大于品牌语境回答数")
    if mentioning_answers == 0 and brand_mentions != 0:
        raise ValueError("品牌未被任何回答提及时，品牌提及次数必须为零")
    if mentioning_answers > 0 and brand_mentions < mentioning_answers:
        raise ValueError("品牌提及次数不得小于品牌提及回答数")

    average_rank_value = metrics.get("average_rank")
    if ranked_segments == 0:
        if average_rank_value not in (None, ""):
            raise ValueError("品牌未进榜时平均排名必须为空")
        average_rank = None
        rank_quality = Decimal("0")
    else:
        average_rank = decimal_number(average_rank_value, "平均排名")
        if average_rank < 1:
            raise ValueError("平均排名不得小于 1")
        rank_quality = max(
            Decimal("0"),
            min(
                Decimal("100"),
                (Decimal("5") - average_rank) / Decimal("4") * Decimal("100"),
            ),
        )

    component_scores = {
        "品牌提及率": percentage(mentioning_answers, successful_answers),
        "全量 Top3 覆盖率": percentage(top3_segments, valid_segments),
        "平均排名质量": rank_quality,
        "正面/中性情感": percentage(
            nonnegative_context_answers, brand_context_answers
        ),
        "提及强度": (
            min(
                Decimal("100"),
                Decimal(brand_mentions)
                / Decimal(mentioning_answers)
                / Decimal("10")
                * Decimal("100"),
            )
            if mentioning_answers
            else Decimal("0")
        ),
    }
    weighted_score = sum(
        (component_scores[name] * weight for name, weight in WEIGHTS.items()),
        Decimal("0"),
    )
    final_score = int(weighted_score.quantize(Decimal("1"), rounding=ROUND_HALF_UP))

    components = {
        name: {
            "标准分": rounded(component_scores[name]),
            "权重": f"{int(weight * 100)}%",
            "加权贡献": rounded(component_scores[name] * weight),
        }
        for name, weight in WEIGHTS.items()
    }
    audit_summary: dict[str, Any] = {
        "成功回答数": successful_answers,
        "品牌提及回答数": mentioning_answers,
        "有效推荐段数": valid_segments,
        "品牌 Top3 段数": top3_segments,
        "品牌进榜段数": ranked_segments,
        "平均排名": float(average_rank) if average_rank is not None else None,
        "品牌语境回答数": brand_context_answers,
        "正面或中性回答数": nonnegative_context_answers,
        "品牌提及次数": brand_mentions,
    }
    return {
        "公式版本": FORMULA_VERSION,
        "品牌得分": final_score,
        "指标": components,
        "审计摘要": audit_summary,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metrics", type=Path, help="UTF-8 JSON normalized metrics")
    args = parser.parse_args()
    try:
        metrics = json.loads(args.metrics.read_text(encoding="utf-8"))
        result = calculate_brand_score(metrics)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
