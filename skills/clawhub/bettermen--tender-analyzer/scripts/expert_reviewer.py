#!/usr/bin/env python3
"""
Expert Reviewer Simulator — 多角色评审专家模拟打分引擎
模拟5类评审专家独立评分，输出加权总分和扣分明细
"""

import json
import sys
from typing import Optional
from dataclasses import dataclass, field, asdict


@dataclass
class ExpertRole:
    """评审专家角色定义"""
    name: str
    weight: float
    focus_dimensions: list[str]
    scoring_style: str  # strict / balanced / lenient


# 五类评审专家默认配置
DEFAULT_EXPERTS = [
    ExpertRole("技术专家", 0.30, ["技术"], "strict"),
    ExpertRole("商务专家", 0.25, ["商务"], "balanced"),
    ExpertRole("法律专家", 0.20, ["合规"], "strict"),
    ExpertRole("项目管理专家", 0.15, ["管理", "实施"], "balanced"),
    ExpertRole("质量专家", 0.10, ["技术", "管理", "实施"], "balanced"),
]


@dataclass
class ScoreItem:
    """单项评分"""
    req_id: str
    req_content: str
    dimension: str
    max_score: float
    actual_score: float
    deduction: float
    deduction_reason: str
    improvement_suggestion: str


@dataclass
class ExpertReview:
    """单个专家的评审结果"""
    expert_name: str
    role_weight: float
    total_max: float
    total_score: float
    score_items: list[ScoreItem] = field(default_factory=list)
    comments: list[str] = field(default_factory=list)


def score_requirement(req: dict, expert: ExpertRole, max_score_hint: float = 5.0) -> ScoreItem:
    """
    对单条需求进行评分
    模拟不同专家角色的评分风格
    """
    content = req.get("content", "")
    dim = req.get("category", "技术")
    weight = req.get("weight", max_score_hint)
    req_id = req.get("id", "REQ-???")

    # 基础compliance评分(0.0-1.0)
    base_compliance = _estimate_compliance(content, dim, expert)

    # 根据评分风格调整
    style_modifier = {
        "strict": -0.1,
        "balanced": 0.0,
        "lenient": 0.1,
    }

    # 如果需求在专家关注维度内，评分更严格
    focus_penalty = -0.05 if dim in expert.focus_dimensions else 0.0

    final_compliance = min(1.0, max(0.0,
        base_compliance + style_modifier.get(expert.scoring_style, 0) + focus_penalty
    ))

    actual_score = weight * final_compliance
    deduction = weight - actual_score

    # 生成扣分原因
    reasons = _generate_deduction_reason(content, dim, final_compliance, expert)

    return ScoreItem(
        req_id=req_id,
        req_content=content,
        dimension=dim,
        max_score=weight,
        actual_score=round(actual_score, 2),
        deduction=round(deduction, 2),
        deduction_reason=reasons["reason"],
        improvement_suggestion=reasons["suggestion"],
    )


def _estimate_compliance(content: str, dim: str, expert: ExpertRole) -> float:
    """
    估算需求满足度(0.0-1.0)
    基于关键词数量和质量估算
    """
    # 关键词得分映射
    quality_keywords = {
        "完整": 0.1, "详细": 0.1, "明确": 0.1, "具体": 0.1,
        "ISO": 0.15, "认证": 0.1, "方案": 0.05, "计划": 0.05,
        "不低于": 0.0, "不超过": 0.0, "须": -0.1, "必须": -0.1,
    }

    base_score = 0.65  # 默认中等水平

    for kw, bonus in quality_keywords.items():
        if kw in content:
            base_score += bonus

    # 如果维度和专家关注维度匹配，基础分会稍低
    if dim in expert.focus_dimensions:
        base_score -= 0.05

    return max(0.1, min(0.95, base_score))


def _generate_deduction_reason(content: str, dim: str, compliance: float, expert: ExpertRole) -> dict:
    """生成扣分原因和改进建议"""
    if compliance >= 0.9:
        return {"reason": f"基本满足要求", "suggestion": "保持当前水平"}
    elif compliance >= 0.75:
        return {"reason": f"{dim}维度存在轻微不足", "suggestion": f"补充更多{expert.name}关注的细节"}
    elif compliance >= 0.6:
        return {"reason": f"{dim}维度存在明显不足", "suggestion": f"需从{expert.name}角度重新审视并强化"}
    elif compliance >= 0.4:
        return {"reason": f"{dim}维度严重不足", "suggestion": f"必须重点整改，{expert.name}视角下此项为硬伤"}
    else:
        return {"reason": f"几乎未响应此需求", "suggestion": f"需从零补充完整的{dim}方案内容"}


def run_expert_review(requirements: list[dict], experts: list[ExpertRole] = None) -> dict:
    """
    执行多角色专家评审

    Args:
        requirements: 需求列表
        experts: 专家角色列表(默认使用DEFAULT_EXPERTS)

    Returns:
        完整评审结果
    """
    if experts is None:
        experts = DEFAULT_EXPERTS

    expert_reviews = []
    overall_max = sum(req.get("weight", 5.0) for req in requirements)

    for expert in experts:
        items = []
        total = 0.0
        comments = []

        for req in requirements:
            item = score_requirement(req, expert)
            items.append(item)
            total += item.actual_score

            # 大额扣分项添加专家评论
            if item.deduction >= 2.0:
                comments.append(f"[{expert.name}] {item.req_id}: {item.deduction_reason}")

        review = ExpertReview(
            expert_name=expert.name,
            role_weight=expert.weight,
            total_max=overall_max,
            total_score=round(total, 2),
            score_items=items,
            comments=comments,
        )
        expert_reviews.append(review)

    # 计算加权综合得分
    weighted_score = sum(
        (rev.total_score / rev.total_max) * rev.role_weight
        for rev in expert_reviews
    ) * 100

    # 汇总扣分明细
    all_deductions = []
    for rev in expert_reviews:
        for item in rev.score_items:
            if item.deduction > 0:
                all_deductions.append({
                    "expert": rev.expert_name,
                    "req_id": item.req_id,
                    "content": item.req_content,
                    "dimension": item.dimension,
                    "max_score": item.max_score,
                    "actual_score": item.actual_score,
                    "deduction": item.deduction,
                    "reason": item.deduction_reason,
                    "suggestion": item.improvement_suggestion,
                })

    # 按扣分值降序排列
    all_deductions.sort(key=lambda x: x["deduction"], reverse=True)

    return {
        "overall_score": round(weighted_score, 1),
        "rating": _get_rating(weighted_score),
        "expert_reviews": [asdict(rev) for rev in expert_reviews],
        "deductions": all_deductions,
        "top_improvements": all_deductions[:5],  # Top5改善建议
    }


def _get_rating(score: float) -> str:
    """分数转评级"""
    if score >= 95: return "S — 卓越"
    elif score >= 85: return "A — 优秀"
    elif score >= 75: return "B — 良好"
    elif score >= 65: return "C — 合格"
    elif score >= 55: return "D — 较差"
    else: return "F — 不通过"


def main():
    """CLI和演示"""
    import argparse
    parser = argparse.ArgumentParser(description="Expert Review Simulator")
    parser.add_argument("input", nargs="?", help="JSON file with requirements")
    parser.add_argument("--demo", action="store_true", help="Run demo")
    args = parser.parse_args()

    if args.demo or not args.input:
        sample_reqs = [
            {"id": "REQ-001", "content": "CPU主频≥3.0GHz，内存≥64GB，存储≥1TB SSD", "category": "技术", "weight": 10, "mandatory": True},
            {"id": "REQ-002", "content": "投标总价不超过500万元人民币", "category": "商务", "weight": 30, "mandatory": False},
            {"id": "REQ-003", "content": "★投标人须具备ISO 9001和ISO 27001认证", "category": "资质", "weight": 5, "mandatory": True},
            {"id": "REQ-004", "content": "项目交付周期不超过6个月，含试运行1个月", "category": "管理", "weight": 10, "mandatory": False},
            {"id": "REQ-005", "content": "★知识产权归招标人所有，需签署保密协议", "category": "合规", "weight": 5, "mandatory": True},
            {"id": "REQ-006", "content": "提供7×24小时运维保障，故障响应时间≤30分钟", "category": "实施", "weight": 10, "mandatory": False},
            {"id": "REQ-007", "content": "技术方案需包含高可用架构设计(99.9%可用性)", "category": "技术", "weight": 15, "mandatory": False},
            {"id": "REQ-008", "content": "提供不少于40课时的用户培训方案", "category": "商务", "weight": 5, "mandatory": False},
            {"id": "REQ-009", "content": "近3年内至少3个类似项目业绩(合同金额≥200万)", "category": "资质", "weight": 5, "mandatory": False},
            {"id": "REQ-010", "content": "质保期不少于3年，含免费升级服务", "category": "商务", "weight": 5, "mandatory": False},
        ]
        print("=== Expert Review Simulator Demo ===\n")
        result = run_expert_review(sample_reqs)
        print(f"综合评分: {result['overall_score']}分 — {result['rating']}\n")

        print("各角色评分:")
        for rev in result["expert_reviews"]:
            score_pct = rev["total_score"] / rev["total_max"] * 100
            print(f"  {rev['expert_name']}(权重{rev['role_weight']*100:.0f}%): {score_pct:.1f}分")

        print(f"\n扣分明细 (共{len(result['deductions'])}项):")
        for ded in result["deductions"][:10]:
            print(f"  [{ded['expert']}] {ded['req_id']}: -{ded['deduction']:.1f}分 ({ded['reason']})")

        return

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
        result = run_expert_review(data)
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
