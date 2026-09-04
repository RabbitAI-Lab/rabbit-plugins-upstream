#!/usr/bin/env python3
"""
diagnose.py — skill-studio 元技能的模式决策树

把"我最想约束 Agent 的哪一种失控"从感觉升级到确定性输出（铁律第 2 条）。
自举：本脚本含错误处理 + 关键数值注释（铁律第 13 条）。

5种模式本质 = 控制 5 类不确定性（见 SOP 第 0.5 节）：
    知识不确定 → Tool Wrapper
    输出不确定 → Generator
    质量不确定 → Reviewer
    输入不确定 → Inversion
    流程不确定 → Pipeline

用法:
    # 交互式（推荐，符合 Inversion 防骚扰上限 6 问）
    python diagnose.py

    # 命令行直接指定
    python diagnose.py --task "生成固定格式技术报告" --uncertainty output
    python diagnose.py --task "按团队规范审查代码" --uncertainty quality

    # 从任务描述自动推断
    python diagnose.py --task "生成固定格式技术报告"

输出: JSON {primary_pattern, secondary_pattern, uncertainty_type, reason, required_dirs, optional_dirs}
"""

import sys
import json
import argparse
from typing import Dict, List, Tuple, Optional

# === 常量（关键数值，铁律第 13 条要求注释说明原因）===
MAX_INTERVIEW_QUESTIONS = 6  # Inversion 防骚扰上限（SOP 熔断第 4 道），超此强制生成假设

# 5类不确定性 → 5种模式映射（SOP 第 0.5 节核心表）
UNCERTAINTY_TO_PATTERN = {
    "knowledge": "Tool Wrapper",
    "output": "Generator",
    "quality": "Reviewer",
    "input": "Inversion",
    "process": "Pipeline",
}

# 每种模式的目录结构（SOP 步骤 3 架构设计表）
# dogfood 改进点2：区分必需（核心契约/脚本）与可选（模板/素材）
PATTERN_REQUIRED_DIRS = {
    "Tool Wrapper": ["references/"],
    "Generator": ["references/"],
    "Reviewer": ["references/"],
    "Inversion": ["references/"],
    "Pipeline": ["references/", "scripts/"],
}
PATTERN_OPTIONAL_DIRS = {
    "Tool Wrapper": ["assets/"],
    "Generator": ["assets/"],
    "Reviewer": [],
    "Inversion": ["assets/"],
    "Pipeline": ["assets/"],
}

# 任务描述关键词 → 不确定性类型（自动推断用）
# 顺序敏感：先匹配更具体的，避免被通用词抢断
KEYWORD_MAP = [
    # (关键词列表, 不确定性类型, 理由)
    (["规范", "标准", "约定", "best practice", "convention", "guideline",
      "团队规范", "代码规范", "API规范"],
     "knowledge", "任务涉及团队/技术栈规范，Agent 需按约定行事"),
    (["报告", "文档", "格式", "模板", "结构", "生成", "起草", "撰写",
      "report", "document", "template"],
     "output", "任务需固定输出结构，防止每次漂移"),
    (["审查", "review", "检查", "审计", "checklist", "评估", "验收",
      "code review", "audit", "lint"],
     "quality", "任务需按统一标准打分/审查/验收"),
    (["规划", "设计", "需求", "收集", "访谈", "问清", "脑补",
      "plan", "design", "requirement", "interview"],
     "input", "任务结果高度依赖用户上下文，需先问清再做"),
    (["流程", "步骤", "工作流", "发布", "部署", "审批", "门槛",
      "pipeline", "workflow", "deploy", "publish", "gate"],
     "process", "任务必须按顺序走，中间不能跳步"),
]

# 访谈问题（Inversion 模式开场，一次一个，防骚扰）
INTERVIEW_QUESTIONS = [
    ("trigger", "什么具体用户请求应该激活这个 skill？（关键词）"),
    ("uncertainty", "最大风险是哪一类？knowledge/output/quality/input/process"),
    ("input_output", "必须严格定义的输入/输出是什么？"),
    ("failure", "信息缺失/校验失败/脚本失败时怎么办？"),
    ("gate", "哪些步骤必须用户确认或质量通过？"),
    ("scope", "这个 skill 的能力边界在哪？避免做所有事"),
]


def infer_uncertainty(task_desc: str) -> Tuple[Optional[str], str]:
    """从任务描述关键词自动推断不确定性类型。"""
    desc_lower = task_desc.lower()
    for keywords, uncertainty, reason in KEYWORD_MAP:
        for kw in keywords:
            if kw.lower() in desc_lower:
                return uncertainty, f"命中关键词 '{kw}'：{reason}"
    return None, "未命中任何关键词，需人工指定"


def select_pattern(uncertainty: str) -> str:
    """不确定性类型 → 主推模式。"""
    return UNCERTAINTY_TO_PATTERN.get(uncertainty, "Tool Wrapper")


def suggest_combination(uncertainty: str, has_gate: bool = False,
                        has_template: bool = False) -> Optional[str]:
    """根据特征建议组合模式（生产形态罕见纯模式）。"""
    primary = select_pattern(uncertainty)
    # 组合规则（SOP 第 2 节组合表）
    if primary == "Inversion" and has_template:
        return "Inversion + Generator"
    if primary == "Tool Wrapper" and uncertainty == "quality":
        return "Tool Wrapper + Reviewer"
    if primary == "Pipeline" and has_gate:
        return "Pipeline + Reviewer"
    if primary == "Pipeline" and has_template:
        return "Pipeline + Inversion + Generator"
    return None


def interactive_interview() -> Dict:
    """交互式访谈，返回收集到的回答。"""
    print("=== diagnose.py 模式诊断访谈 ===")
    print(f"(最多 {MAX_INTERVIEW_QUESTIONS} 问，符合 Inversion 防骚扰上限)\n")
    answers = {}
    for i, (key, question) in enumerate(INTERVIEW_QUESTIONS, 1):
        if i > MAX_INTERVIEW_QUESTIONS:
            break
        ans = input(f"Q{i} {question}\n> ").strip()
        answers[key] = ans
        if key == "uncertainty" and ans.lower() in UNCERTAINTY_TO_PATTERN:
            # 已明确不确定性，可提前收尾（给予恰当自由度）
            print(f"\n(已明确不确定性类型，后续问题可选答，留空跳过)\n")
    return answers


def diagnose(task_desc: str = "", uncertainty: str = "",
             has_gate: bool = False, has_template: bool = False) -> Dict:
    """主诊断函数。返回结构化结果。"""
    # 1. 确定不确定性类型
    reason = ""
    if not uncertainty:
        uncertainty, reason = infer_uncertainty(task_desc)
        if uncertainty is None:
            return {
                "error": "无法自动推断不确定性类型，请用 --uncertainty 指定 "
                         "knowledge/output/quality/input/process",
                "hint": reason,
            }
    else:
        uncertainty = uncertainty.lower()
        if uncertainty not in UNCERTAINTY_TO_PATTERN:
            return {
                "error": f"未知不确定性类型: {uncertainty}",
                "valid_types": list(UNCERTAINTY_TO_PATTERN.keys()),
            }

    # 2. 选主模式
    primary = select_pattern(uncertainty)

    # 3. 建议组合
    combo = suggest_combination(uncertainty, has_gate, has_template)
    secondary = None
    if combo:
        parts = combo.split(" + ")
        if len(parts) > 1 and parts[0] == primary:
            secondary = parts[1]

    # 4. 所需目录（dogfood 改进点2：区分必需/可选）
    required_dirs = PATTERN_REQUIRED_DIRS.get(primary, [])
    optional_dirs = PATTERN_OPTIONAL_DIRS.get(primary, [])

    # 5. 理由
    if not reason:
        reason = f"不确定性类型={uncertainty} → 主推模式={primary}"

    return {
        "primary_pattern": primary,
        "secondary_pattern": secondary,
        "uncertainty_type": uncertainty,
        "reason": reason,
        "required_dirs": required_dirs,
        "optional_dirs": optional_dirs,
        "combination": combo,
        "interview_questions_count": len(INTERVIEW_QUESTIONS),
        "max_interview_questions": MAX_INTERVIEW_QUESTIONS,
    }


def main():
    parser = argparse.ArgumentParser(
        description="skill-studio 模式决策树：5类不确定性 → 5种设计模式")
    parser.add_argument("--task", default="",
                        help="任务描述（用于自动推断不确定性）")
    parser.add_argument("--uncertainty", default="",
                        choices=["", "knowledge", "output", "quality",
                                 "input", "process"],
                        help="不确定性类型（手动指定，跳过推断）")
    parser.add_argument("--has-gate", action="store_true",
                        help="任务含门槛/用户确认节点")
    parser.add_argument("--has-template", action="store_true",
                        help="任务需固定输出模板")
    parser.add_argument("--interactive", action="store_true",
                        help="交互式访谈模式")
    args = parser.parse_args()

    try:
        if args.interactive:
            answers = interactive_interview()
            uncertainty = answers.get("uncertainty", "").lower()
            has_gate = "确认" in answers.get("gate", "") or "门槛" in answers.get("gate", "")
            has_template = "模板" in answers.get("input_output", "") or "格式" in answers.get("input_output", "")
            result = diagnose(answers.get("trigger", ""),
                              uncertainty or "",
                              has_gate, has_template)
            result["interview_answers"] = answers
        else:
            if not args.task and not args.uncertainty:
                parser.error("需提供 --task 或 --uncertainty，或用 --interactive")
            result = diagnose(args.task, args.uncertainty,
                              args.has_gate, args.has_template)
    except KeyboardInterrupt:
        print("\n(访谈中断)")
        sys.exit(130)
    except Exception as e:
        print(f"DIAGNOSE_CRASH: {e}", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0)


if __name__ == '__main__':
    main()
