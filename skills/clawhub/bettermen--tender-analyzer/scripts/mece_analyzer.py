#!/usr/bin/env python3
"""
MECE Multi-Dimensional Analyzer — MECE原则多维度分析引擎
基于6大维度24+子维度对需求清单进行结构化展开
"""

import json
import sys
from typing import Optional

# MECE 6大维度定义
MECE_DIMENSIONS = {
    "技术": {
        "weight_range": [0.25, 0.40],
        "sub_dimensions": [
            "技术方案完整性",
            "技术方案先进性",
            "技术参数符合度",
            "技术创新性",
            "技术路线成熟度",
        ],
    },
    "商务": {
        "weight_range": [0.25, 0.40],
        "sub_dimensions": [
            "报价合理性",
            "付款条件",
            "质保与售后服务",
            "培训方案",
            "交付周期",
        ],
    },
    "资质": {
        "weight_range": [0.10, 0.20],
        "sub_dimensions": [
            "企业资质等级",
            "人员资质",
            "业绩案例",
            "财务状况",
            "信誉记录",
        ],
    },
    "管理": {
        "weight_range": [0.10, 0.15],
        "sub_dimensions": [
            "项目组织架构",
            "进度计划",
            "质量管理体系",
            "风险管理",
            "沟通与变更管理",
        ],
    },
    "合规": {
        "weight_range": [0.10, 0.15],
        "sub_dimensions": [
            "实质性条款响应",
            "知识产权与保密",
            "免责条款",
            "违约责任",
            "废标项检测",
        ],
    },
    "实施": {
        "weight_range": [0.10, 0.15],
        "sub_dimensions": [
            "交付计划",
            "资源配置",
            "验收标准",
            "运维保障",
            "应急预案",
        ],
    },
}

# 子维度到维度的映射
SUB_TO_PARENT = {}
for dim_name, dim_info in MECE_DIMENSIONS.items():
    for sub in dim_info["sub_dimensions"]:
        SUB_TO_PARENT[sub] = dim_name


def classify_requirement(req: dict) -> str:
    """
    根据需求内容自动分类到MECE维度
    基于关键词匹配 + 规则引擎
    """
    content = req.get("content", "") + req.get("category", "")
    req_id = req.get("id", "")

    # 关键词映射表
    keyword_map = {
        "技术": [
            "技术方案", "技术参数", "技术指标", "性能", "架构", "算法",
            "接口", "协议", "兼容性", "扩展性", "安全性", "可靠性",
            "CPU", "内存", "存储", "网络", "软件", "硬件", "系统",
            "精度", "分辨率", "响应时间", "吞吐量", "并发", "QPS",
        ],
        "商务": [
            "报价", "价格", "预算", "费用", "成本", "付款", "结算",
            "质保", "售后", "保修", "服务", "培训", "交付", "交货",
            "税率", "发票", "合同金额",
        ],
        "资质": [
            "资质", "资格", "证书", "认证", "ISO", "执照", "许可",
            "业绩", "案例", "合同", "人员", "项目经理", "工程师",
            "审计", "财务", "纳税", "社保", "注册资金",
        ],
        "管理": [
            "项目经理", "组织架构", "进度", "计划", "里程碑",
            "质量管理", "风险", "应急预案", "沟通", "变更",
            "周报", "月报", "会议",
        ],
        "合规": [
            "知识产权", "专利", "著作权", "保密", "违约", "赔偿",
            "不可抗力", "法律", "法规", "政策", "合规", "审计",
        ],
        "实施": [
            "实施", "部署", "安装", "调试", "验收", "运维",
            "SLA", "服务级别", "故障", "恢复", "灾备",
            "资源配置", "人员安排",
        ],
    }

    # 评分计数
    scores = {dim: 0 for dim in MECE_DIMENSIONS}
    for dim, keywords in keyword_map.items():
        for kw in keywords:
            if kw in content:
                scores[dim] += 1

    # 寻找最高分维度
    best_dim = max(scores, key=scores.get)
    if scores[best_dim] == 0:
        # 无法自动分类时，使用已有的 category
        cat = req.get("category", "技术")
        if cat in MECE_DIMENSIONS:
            return cat
        return "技术"  # 默认归入技术维度

    return best_dim


def analyze_mece(requirements: list[dict]) -> dict:
    """
    对需求清单进行MECE多维度分析

    Args:
        requirements: 需求列表，每条包含 id, content, category, weight, type 等字段

    Returns:
        MECE分析结果，包含维度分布、交叉影响、隐含需求、改进建议
    """
    total_items = len(requirements)
    if total_items == 0:
        return {"error": "No requirements to analyze"}

    # 初始化维度桶
    dim_buckets = {dim: [] for dim in MECE_DIMENSIONS}

    # 分类需求到维度
    for req in requirements:
        dim = classify_requirement(req)
        dim_buckets[dim].append(req)

    # 计算各维度统计
    dimension_stats = {}
    total_weight = sum(req.get("weight", 0) for req in requirements)

    for dim_name, dim_info in MECE_DIMENSIONS.items():
        items = dim_buckets[dim_name]
        dim_weight = sum(item.get("weight", 0) for item in items)
        dim_stats = {
            "count": len(items),
            "percentage": round(len(items) / total_items * 100, 1) if total_items > 0 else 0,
            "weight": dim_weight,
            "weight_percentage": round(dim_weight / total_weight * 100, 1) if total_weight > 0 else 0,
            "mandatory_count": sum(1 for item in items if item.get("mandatory")),
            "high_risk_count": sum(1 for item in items if item.get("risk_level") in ("high", "critical")),
            "items": items,
        }
        dimension_stats[dim_name] = dim_stats

    # 生成交叉影响分析
    cross_impact = _generate_cross_impact(dimension_stats)

    # 识别隐含需求
    implicit_requirements = _identify_implicit(requirements, dimension_stats)

    # 生成改进建议
    improvement_suggestions = _generate_suggestions(dimension_stats)

    return {
        "total_items": total_items,
        "total_weight": total_weight,
        "dimension_stats": dimension_stats,
        "cross_impact": cross_impact,
        "implicit_requirements": implicit_requirements,
        "improvement_suggestions": improvement_suggestions,
        "radar_data": {
            "dimensions": list(MECE_DIMENSIONS.keys()),
            "item_counts": [dimension_stats[d]["count"] for d in MECE_DIMENSIONS],
            "weights": [dimension_stats[d]["weight"] for d in MECE_DIMENSIONS],
        },
    }


def _generate_cross_impact(dim_stats: dict) -> list:
    """生成维度间交叉影响分析"""
    impacts = []
    pairs = [
        ("技术", "商务", "技术方案复杂度直接影响报价水平；配置选型同时受预算约束"),
        ("技术", "实施", "技术架构决定部署难度和交付周期；技术验证是验收的前提"),
        ("技术", "资质", "技术能力需要资质证明；专利/软著是技术实力的背书"),
        ("商务", "管理", "付款节奏与项目进度关联；成本控制影响管理投入"),
        ("商务", "合规", "合同条款约束商务条件；违约条款限制商务灵活性"),
        ("商务", "实施", "交付周期影响现金流；运维成本需要在商务报价中体现"),
        ("资质", "合规", "资质证书是合规的前提；无资质无法通过资格审查"),
        ("管理", "实施", "进度管理决定交付时间；质量管理影响验收结果"),
        ("管理", "合规", "项目管理流程需要合规；变更管理需符合合同要求"),
    ]
    for dim1, dim2, desc in pairs:
        if dim1 in dim_stats and dim2 in dim_stats:
            impacts.append({
                "dimensions": [dim1, dim2],
                "description": desc,
                "strength": "high" if dim_stats[dim1]["count"] > 3 and dim_stats[dim2]["count"] > 3 else "medium",
            })
    return impacts


def _identify_implicit(requirements: list, dim_stats: dict) -> list:
    """识别隐含需求（招标文件未明确但行业惯例需要）"""
    implicit = []
    implicit_id = 1

    # 检查各维度关键覆盖
    checks = [
        ("技术", "技术方案完整性", "技术方案中是否包含架构设计和详细技术路线"),
        ("技术", "技术方案完整性", "是否明确的测试方案和测试用例"),
        ("商务", "报价合理性", "报价是否包含全部税费和运费"),
        ("商务", "质保与售后服务", "质保期满后的服务费用安排"),
        ("管理", "质量管理体系", "质量管理是否符合ISO 9001标准"),
        ("管理", "风险管理", "是否识别了所有关键路径风险"),
        ("合规", "知识产权与保密", "开源软件使用声明和许可证合规"),
        ("实施", "验收标准", "验收测试的标准和用例明细"),
        ("实施", "运维保障", "故障响应SLA的具体指标(MTTR/MTBF)"),
    ]

    existing_content = {req.get("content", "") for req in requirements}

    for dim, sub, desc in checks:
        # 简化的检查逻辑：内容中是否包含相关关键词
        found = False
        keywords = desc[:4]
        for content in existing_content:
            if any(kw in content for kw in keywords):
                found = True
                break

        if not found:
            implicit.append({
                "id": f"IMPL-{implicit_id:03d}",
                "dimension": dim,
                "sub_dimension": sub,
                "description": desc,
                "type": "行业惯例",
                "importance": "high",
            })
            implicit_id += 1

    return implicit


def _generate_suggestions(dim_stats: dict) -> list:
    """生成改进建议"""
    suggestions = []
    for dim_name, stats in dim_stats.items():
        if stats["count"] == 0:
            suggestions.append({
                "dimension": dim_name,
                "issue": f"{dim_name}维度无需求覆盖",
                "suggestion": f"需补充{dim_name}相关方案内容",
                "priority": "P0",
            })
        if stats["mandatory_count"] > 0:
            suggestions.append({
                "dimension": dim_name,
                "issue": f"{dim_name}维度含{stats['mandatory_count']}条实质性要求(★条款)",
                "suggestion": "确保所有★条款完全响应，任何偏离可能导致废标",
                "priority": "P0",
            })
    return suggestions


def main():
    """CLI入口：接收JSON格式的需求清单，输出MECE分析结果"""
    if len(sys.argv) < 2:
        # 示例模式
        sample_reqs = [
            {"id": "REQ-001", "content": "CPU主频不低于3.0GHz", "category": "技术", "weight": 5, "mandatory": False},
            {"id": "REQ-002", "content": "总报价不超过预算500万元", "category": "商务", "weight": 30, "mandatory": True},
            {"id": "REQ-003", "content": "投标人须具备ISO 9001认证", "category": "资质", "weight": 5, "mandatory": True},
            {"id": "REQ-004", "content": "项目交付周期不超过6个月", "category": "管理", "weight": 10, "mandatory": False},
            {"id": "REQ-005", "content": "★知识产权归招标人所有", "category": "合规", "weight": 5, "mandatory": True, "risk_level": "critical"},
            {"id": "REQ-006", "content": "提供7×24小时运维保障", "category": "实施", "weight": 5, "mandatory": False},
        ]
        print("=== MECE Analyzer Demo ===")
        result = analyze_mece(sample_reqs)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # 从文件或stdin读取JSON
    import argparse
    parser = argparse.ArgumentParser(description="MECE Multi-Dimensional Analyzer")
    parser.add_argument("input", nargs="?", help="JSON file path or '-' for stdin")
    parser.add_argument("--demo", action="store_true", help="Run demo with sample data")
    args = parser.parse_args()

    if args.demo:
        sample_reqs = [
            {"id": "REQ-001", "content": "CPU主频不低于3.0GHz", "category": "技术", "weight": 5},
            {"id": "REQ-002", "content": "总报价不超过预算500万元", "category": "商务", "weight": 30, "mandatory": True},
        ]
        result = analyze_mece(sample_reqs)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if args.input == "-":
        data = json.loads(sys.stdin.read())
    elif args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        print("No input provided. Use --demo for sample run.")
        sys.exit(1)

    result = analyze_mece(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
