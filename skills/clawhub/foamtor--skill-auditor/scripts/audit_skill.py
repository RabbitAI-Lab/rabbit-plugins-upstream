#!/usr/bin/env python3
"""
skill-auditor 自动化验证脚本
自动检测SKILL.md中的关键模式，给出客观基础评分。

用法: python3 audit_skill.py <SKILL.md路径>
输出: JSON格式的评分结果
退出码: 0=全部达标, 1=有缺失项, 2=参数错误
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


def detect_type(content: str, skill_dir: str) -> str:
    """自动判断skill类型"""
    # 工作流型：有步骤流程或门禁表
    if re.search(r'(Step\s*\d|阶段\d|## 步骤|🛑|门禁|G[0-9])', content):
        return "workflow"
    # 工具型：有scripts/目录或CLI命令
    scripts_dir = os.path.join(skill_dir, "scripts")
    if os.path.isdir(scripts_dir) or re.search(r'(scripts/|cli|命令行|argparse)', content, re.I):
        return "tool"
    # 模式型：方法论/思维方式
    if re.search(r'(方法论|思维方式|分析框架|思考框架|心智模型)', content):
        return "pattern"
    # 默认：参考型
    return "reference"


# 类型→适用维度映射
# ✅=必须(2), ⚠️=可选(1), —=跳过(0)
TYPE_DIMENSIONS = {
    "workflow": [2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
    "tool":     [2, 1, 2, 1, 2, 2, 0, 2, 2, 0],
    "reference":[0, 0, 0, 0, 1, 2, 1, 0, 2, 1],
    "pattern":  [1, 0, 0, 1, 0, 2, 0, 0, 2, 0],
}

TYPE_NAMES = {
    "workflow": "工作流型",
    "tool": "工具型",
    "reference": "参考型",
    "pattern": "模式型",
}

DIMENSION_NAMES = [
    "反合理化守卫",
    "阶段门禁",
    "自动化验证",
    "决策流程图",
    "陷阱清单",
    "渐进式加载",
    "三层架构",
    "Runtime Hooks",
    "Context Engineering",
    "Scoped Rules",
]


def check_dimension(idx: int, content: str, skill_dir: str, file_size: int) -> dict:
    """检查单个维度，返回 {score, detail}"""
    # score: "pass" / "partial" / "fail"
    lines = content.split('\n')
    first_200_chars = content[:200]

    if idx == 0:  # 反合理化守卫
        patterns = [r'不是.*借口', r'合理化', r'跳过.*步骤', r'以下理由', r'❌.*→']
        hits = sum(1 for p in patterns if re.search(p, content))
        if hits >= 3:
            return {"score": "pass", "detail": f"检测到{hits}个反合理化模式"}
        elif hits >= 1:
            return {"score": "partial", "detail": f"只检测到{hits}个模式，缺少完整的借口列表"}
        return {"score": "fail", "detail": "未检测到反合理化守卫"}

    elif idx == 1:  # 阶段门禁
        gate_patterns = [r'G[0-9]', r'🛑', r'门禁', r'STOP', r'禁止做.*必须做']
        hits = sum(1 for p in gate_patterns if re.search(p, content))
        if hits >= 2:
            return {"score": "pass", "detail": f"检测到门禁标记"}
        elif hits >= 1:
            return {"score": "partial", "detail": "有停止点但没有结构化门禁表"}
        return {"score": "fail", "detail": "未检测到阶段门禁"}

    elif idx == 2:  # 自动化验证
        scripts_dir = os.path.join(skill_dir, "scripts")
        has_scripts = os.path.isdir(scripts_dir) and len(os.listdir(scripts_dir)) > 0
        mentions_script = bool(re.search(r'(运行.*验证|脚本.*检查|退出码|非零.*退出)', content))
        if has_scripts and mentions_script:
            return {"score": "pass", "detail": f"有scripts/目录且skill中要求运行验证"}
        elif has_scripts or mentions_script:
            return {"score": "partial", "detail": "有脚本或提到验证，但未强制要求"}
        return {"score": "fail", "detail": "无验证脚本，依赖AI自我报告"}

    elif idx == 3:  # 决策流程图
        flow_chars = ['├', '└', '│', '▼', '→', '↓']
        flow_hits = sum(content.count(c) for c in flow_chars)
        has_mermaid = bool(re.search(r'```mermaid', content))
        if flow_hits >= 5 or has_mermaid:
            return {"score": "pass", "detail": f"检测到流程图（{flow_hits}个流程字符）"}
        elif flow_hits >= 2:
            return {"score": "partial", "detail": "有简单流程但不够完整"}
        return {"score": "fail", "detail": "未检测到决策流程图"}

    elif idx == 4:  # 陷阱清单
        trap_pattern = r'⚠️.*[（(]\d{4}'
        traps = re.findall(trap_pattern, content)
        warn_sections = len(re.findall(r'⚠️', content))
        if len(traps) >= 3:
            return {"score": "pass", "detail": f"检测到{len(traps)}条带日期的陷阱"}
        elif warn_sections >= 3:
            return {"score": "partial", "detail": f"有{warn_sections}处⚠️标记但缺少日期"}
        return {"score": "fail", "detail": "未检测到结构化陷阱清单"}

    elif idx == 5:  # 渐进式加载
        has_refs = os.path.isdir(os.path.join(skill_dir, "references"))
        early_trigger = bool(re.search(r'(触发条件|触发词|## Trigger)', content[:500], re.I))
        has_templates = os.path.isdir(os.path.join(skill_dir, "templates"))
        if has_refs and early_trigger:
            return {"score": "pass", "detail": "有references/目录且触发条件前置"}
        elif has_refs or early_trigger:
            return {"score": "partial", "detail": "有分层但不完整"}
        return {"score": "fail", "detail": "所有内容平铺，无分层设计"}

    elif idx == 6:  # 三层架构
        layer_patterns = [r'AGENTS\.md', r'MCP', r'三层', r'工作流层', r'项目上下文']
        hits = sum(1 for p in layer_patterns if re.search(p, content))
        if hits >= 2:
            return {"score": "pass", "detail": "提到了多层架构协作"}
        elif hits >= 1:
            return {"score": "partial", "detail": "提到了其他层但未明确关系"}
        return {"score": "fail", "detail": "未说明与其他层的协作关系"}

    elif idx == 7:  # Runtime Hooks
        hook_patterns = [r'hook', r'拦截', r'事前.*检查', r'runtime', r'钩子']
        hits = sum(1 for p in hook_patterns if re.search(p, content, re.I))
        scripts_dir = os.path.join(skill_dir, "scripts")
        has_hook_script = False
        if os.path.isdir(scripts_dir):
            for f in os.listdir(scripts_dir):
                if 'hook' in f.lower() or 'guard' in f.lower():
                    has_hook_script = True
        if hits >= 2 or has_hook_script:
            return {"score": "pass", "detail": "有runtime hook机制"}
        elif hits >= 1:
            return {"score": "partial", "detail": "提到了hook但未实现"}
        return {"score": "fail", "detail": "纯文本指令，无代码层面强制"}

    elif idx == 8:  # Context Engineering
        size_ok = file_size < 15000  # <5000字 ≈ <15000 bytes (CJK)
        key_first = bool(re.search(r'(触发条件|## Trigger|执行规则|## 规则)', content[:300], re.I))
        if size_ok and key_first:
            return {"score": "pass", "detail": f"文件{file_size}B，关键规则前置"}
        elif size_ok:
            return {"score": "partial", "detail": f"文件{file_size}B合理，但关键规则未前置"}
        return {"score": "fail", "detail": f"文件{file_size}B过大（>{15000}B），或关键规则埋在中间"}

    elif idx == 9:  # Scoped Rules
        scoped_patterns = [r'glob', r'按需加载', r'条件.*加载', r'@import', r'scoped']
        hits = sum(1 for p in scoped_patterns if re.search(p, content, re.I))
        sub_files = sum(1 for d in ['references', 'templates', 'scripts']
                       if os.path.isdir(os.path.join(skill_dir, d)))
        if hits >= 2 and sub_files >= 1:
            return {"score": "pass", "detail": "有条件加载逻辑和子文件"}
        elif hits >= 1 or sub_files >= 2:
            return {"score": "partial", "detail": "有部分条件加载或子文件拆分"}
        return {"score": "fail", "detail": "所有规则始终全部加载"}

    return {"score": "fail", "detail": "未知维度"}


def audit(skill_path: str) -> dict:
    """执行完整审阅"""
    path = Path(skill_path).resolve()
    if not path.exists():
        return {"error": f"文件不存在: {skill_path}"}

    content = path.read_text(encoding="utf-8")
    skill_dir = str(path.parent)
    file_size = len(content.encode("utf-8"))

    skill_type = detect_type(content, skill_dir)
    applicable = TYPE_DIMENSIONS[skill_type]

    results = []
    for i in range(10):
        if applicable[i] == 0:
            continue  # 跳过不适用维度
        result = check_dimension(i, content, skill_dir, file_size)
        result["dimension"] = DIMENSION_NAMES[i]
        result["required"] = applicable[i] == 2
        results.append(result)

    # 统计
    pass_count = sum(1 for r in results if r["score"] == "pass")
    partial_count = sum(1 for r in results if r["score"] == "partial")
    fail_count = sum(1 for r in results if r["score"] == "fail")
    applicable_count = len(results)

    return {
        "skill_name": path.stem,
        "skill_type": TYPE_NAMES[skill_type],
        "type_reason": _type_reason(skill_type, content, skill_dir),
        "applicable_dimensions": applicable_count,
        "total_dimensions": 10,
        "results": results,
        "summary": {
            "pass": pass_count,
            "partial": partial_count,
            "fail": fail_count,
        },
        "improvements": _suggest_improvements(results),
    }


def _type_reason(skill_type: str, content: str, skill_dir: str) -> str:
    """解释类型判断依据"""
    if skill_type == "workflow":
        if re.search(r'G[0-9]|🛑|门禁', content):
            return "检测到门禁表/STOP标记"
        return "检测到步骤流程"
    elif skill_type == "tool":
        if os.path.isdir(os.path.join(skill_dir, "scripts")):
            return "有scripts/目录"
        return "提到CLI/脚本"
    elif skill_type == "pattern":
        return "检测到方法论/分析框架"
    return "无步骤流程和脚本，默认为参考型"


def _suggest_improvements(results: list) -> list:
    """按优先级生成改进建议"""
    improvements = []
    for r in results:
        if r["score"] == "fail" and r["required"]:
            improvements.append({
                "priority": "最高",
                "dimension": r["dimension"],
                "problem": r["detail"],
            })
        elif r["score"] == "partial" and r["required"]:
            improvements.append({
                "priority": "高",
                "dimension": r["dimension"],
                "problem": r["detail"],
            })
        elif r["score"] == "fail" and not r["required"]:
            improvements.append({
                "priority": "中",
                "dimension": r["dimension"],
                "problem": r["detail"],
            })
    return improvements


def format_report(result: dict) -> str:
    """格式化为Markdown报告"""
    if "error" in result:
        return f"❌ {result['error']}"

    lines = [
        f"## Skill审阅报告：{result['skill_name']}",
        f"类型：{result['skill_type']}（{result['type_reason']}）",
        f"适用维度：{result['applicable_dimensions']}/{result['total_dimensions']}",
        "",
        "| # | 维度 | 评分 | 必须 | 说明 |",
        "|---|------|------|------|------|",
    ]

    for i, r in enumerate(result["results"], 1):
        score_icon = {"pass": "✅", "partial": "⚠️", "fail": "❌"}[r["score"]]
        required = "✅" if r["required"] else "—"
        lines.append(f"| {i} | {r['dimension']} | {score_icon} | {required} | {r['detail']} |")

    s = result["summary"]
    lines.extend([
        "",
        f"总分：{s['pass']}✅ {s['partial']}⚠️ {s['fail']}❌（共{result['applicable_dimensions']}项）",
    ])

    if result["improvements"]:
        lines.extend(["", "### 改进建议（按优先级排序）", ""])
        for i, imp in enumerate(result["improvements"], 1):
            lines.append(f"{i}. **[{imp['priority']}]** {imp['dimension']}：{imp['problem']}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="SKILL.md 指令遵循质量检测")
    parser.add_argument("skill_path", help="SKILL.md文件路径")
    parser.add_argument("--json", action="store_true", help="输出JSON格式")
    args = parser.parse_args()

    result = audit(args.skill_path)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_report(result))

    # 退出码
    if "error" in result:
        sys.exit(2)
    fail_required = sum(1 for r in result["results"]
                       if r["score"] == "fail" and r["required"])
    sys.exit(1 if fail_required > 0 else 0)


if __name__ == "__main__":
    main()
