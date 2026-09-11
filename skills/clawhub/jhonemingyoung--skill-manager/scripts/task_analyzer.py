#!/usr/bin/env python3
"""
Task Analyzer — Evaluates task complexity and generates skill recommendation reports

Usage:
    python3 task_analyzer.py --task "Convert CSV to JSON" --skills-json skills.json
    python3 task_analyzer.py --task "Build automated data pipeline" --skills-json skills.json --complex
"""

import argparse
import json
import sys

# Task complexity assessment dimensions
COMPLEXITY_RULES = {
    "simple": {
        "max_steps": 1,
        "max_code_lines": 50,
        "needs_domain_knowledge": False,
        "needs_external_api": False,
        "repeated": False,
        "description": "Single-step operation, simple query, one-time conversion"
    },
    "medium": {
        "max_steps": 3,
        "max_code_lines": 200,
        "needs_domain_knowledge": True,
        "needs_external_api": False,
        "repeated": False,
        "description": "Multi-step workflow, requires domain-specific knowledge"
    },
    "complex": {
        "max_steps": 99,
        "max_code_lines": 9999,
        "needs_domain_knowledge": True,
        "needs_external_api": True,
        "repeated": True,
        "description": "Multi-domain crossover, long workflow, requires professional toolchain"
    }
}

# Task keyword to skill domain mapping
TASK_SKILL_MAP = {
    "document": ["docx", "pdf", "xlsx", "tencent-docs", "kdocs", "youdaonote", "notion"],
    "word": ["docx", "tencent-docs", "kdocs"],
    "excel": ["xlsx", "tencent-docs", "kdocs"],
    "spreadsheet": ["xlsx", "tencent-docs", "kdocs"],
    "email": ["email-skill", "agent-email", "imap-smtp-email", "personal-mail-skill"],
    "mail": ["email-skill", "agent-email", "imap-smtp-email"],
    "map": ["tencentmap-jsapi-gl-skill", "tencentmap-webservice-skill", "baidu-ai-map"],
    "finance": ["hithink-mcp", "tongdaxin-mcp", "qcc-company", "qibook-mcp"],
    "travel": ["chengxin", "flyai", "meituan-travel", "wendao-partner-qclaw-skill"],
    "hotel": ["chengxin", "flyai", "meituan-travel", "wendao-partner-qclaw-skill"],
    "flight": ["chengxin", "flyai", "wendao-partner-qclaw-skill"],
    "meeting": ["tencent-meeting-mcp"],
    "install": ["qclaw-env"],
    "environment": ["qclaw-env"],
    "setup": ["qclaw-env"],
    "schedule": ["qclaw-cron-skill"],
    "reminder": ["qclaw-cron-skill"],
    "cron": ["qclaw-cron-skill"],
    "image": ["qclaw-generate-image"],
    "draw": ["qclaw-generate-image"],
    "ppt": ["aippt"],
    "presentation": ["aippt"],
    "music": ["qqmusic", "tencent-musician-skills"],
    "reading": ["weread-skills"],
    "news": ["tencent-news"],
    "survey": ["tencent-survey"],
    "contract": ["tencent-esign-contract"],
    "legal": ["tencent-esign-contract", "yuandian"],
    "ads": ["tencentads"],
    "advertising": ["tencentads"],
    "delivery": ["meituan-paotui"],
    "food": ["mtunion-product-ai-guide", "meituan-paotui"],
    "cloud": ["weiyun", "cloud-upload-backup", "bdpan-storage"],
    "upload": ["cloud-upload-backup", "weiyun"],
    "notes": ["youdaonote", "notion"],
    "knowledge": ["lexiang-knowledge-base", "ima"],
    "browser": ["xbrowser"],
    "webpage": ["xbrowser"],
    "scrape": ["xbrowser"],
    "persona": ["persona-switch"],
    "clone": ["another_them"],
    "skill": ["find-skills", "qclaw-skill-creator", "skill-manager"],
}


def assess_complexity(task: str, force_complex: bool = False) -> dict:
    """Assess task complexity"""
    if force_complex:
        return {
            "level": "complex",
            "reason": "User specified as complex task",
            "steps_estimated": 5,
            "code_lines_estimated": 300,
        }

    task_lower = task.lower()

    # Simple task signals
    simple_signals = ["convert", "read", "list", "show", "format", "rename", "sort", "count",
                      "查看", "显示", "列出", "查询", "搜索", "转换", "转成", "读取", "排序", "统计"]
    # Complex task signals
    complex_signals = ["build", "deploy", "pipeline", "automate", "system", "framework",
                        "integrate", "architecture", "complete", "end-to-end",
                        "搭建", "构建", "部署", "自动化", "管道", "系统", "平台", "全流程",
                        "集成", "架构", "设计并实现", "完整", "端到端"]
    # Medium task signals
    medium_signals = ["generate", "create", "edit", "process", "analyze", "export",
                      "生成", "创建", "编辑", "处理", "分析", "制作", "导出"]

    simple_score = sum(1 for s in simple_signals if s in task_lower)
    complex_score = sum(1 for s in complex_signals if s in task_lower)
    medium_score = sum(1 for s in medium_signals if s in task_lower)

    # Task length also serves as a complexity signal
    task_length = len(task)

    if complex_score > 0 or (task_length > 100 and medium_score > 1):
        level = "complex"
        reason = f"Detected complex task signals ({complex_score}), long task description"
        steps = 5 + complex_score
        code_lines = 200 + complex_score * 50
    elif medium_score > 0 or simple_score == 0:
        level = "medium"
        reason = f"Detected medium task signals ({medium_score})"
        steps = 2 + medium_score
        code_lines = 50 + medium_score * 30
    else:
        level = "simple"
        reason = f"Detected simple task signals ({simple_score})"
        steps = 1
        code_lines = 20

    return {
        "level": level,
        "reason": reason,
        "steps_estimated": steps,
        "code_lines_estimated": code_lines,
    }


def find_matching_skills(task: str, installed_skills: list) -> dict:
    """Find matching installed skills"""
    task_lower = task.lower()
    matched = []

    # Keyword-based matching
    for keyword, skill_names in TASK_SKILL_MAP.items():
        if keyword in task_lower:
            for sn in skill_names:
                for s in installed_skills:
                    if s["name"] == sn:
                        if s not in matched:
                            matched.append(s)

    # Description-based matching
    for s in installed_skills:
        if s not in matched:
            desc = s["description"].lower()
            task_words = [w for w in task_lower.split() if len(w) > 2]
            for w in task_words:
                if w in desc:
                    if s not in matched:
                        matched.append(s)
                    break

    return {
        "matched": matched,
        "unmatched_count": len(installed_skills) - len(matched),
    }


def estimate_tokens(task: str, complexity: dict, path: str, skill_info: dict = None) -> dict:
    """Estimate token consumption and execution time
    
    path options:
    - "skill": Use existing/recommended skill
    - "builtin": Use built-in tools (web_fetch, exec, browser, etc.)
    - "code": Write a new script
    """
    if path == "skill" and skill_info:
        # Token cost of using an existing skill
        # SKILL.md is typically 2-8KB, average 5KB ≈ 1280 tokens
        skill_md_tokens = 1280
        # Script execution consumes a small amount of tokens
        execution_tokens = 300 + min(skill_info.get("file_count", 5), 20) * 20
        total = skill_md_tokens + execution_tokens
        # Execution time: load SKILL.md + read scripts + execute
        steps = complexity["steps_estimated"]
        time_sec = 10 + steps * 5  # Loading ~10s + ~5s per step
        return {
            "path": "Use existing skill",
            "estimated_tokens": total,
            "breakdown": f"SKILL.md loading≈{skill_md_tokens} + execution≈{execution_tokens}",
            "estimated_time": time_sec,
            "time_breakdown": f"Skill loading≈10s + {steps} steps≈{steps*5}s",
        }
    elif path == "builtin":
        # Using built-in tools (web_fetch / exec / browser, etc.)
        # No SKILL.md loading needed, direct call, lowest token consumption
        tool_call_tokens = 200  # Tool call overhead
        result_parse_tokens = complexity["steps_estimated"] * 150
        retry_tokens = complexity["steps_estimated"] * 100
        total = tool_call_tokens + result_parse_tokens + retry_tokens
        # Execution time: direct call, no loading, fastest
        steps = complexity["steps_estimated"]
        time_sec = 3 + steps * 4  # First call ~3s + ~4s per step
        return {
            "path": "Use built-in tools",
            "estimated_tokens": total,
            "breakdown": f"Tool call≈{tool_call_tokens} + result parsing≈{result_parse_tokens} + retry reserve≈{retry_tokens}",
            "estimated_time": time_sec,
            "time_breakdown": f"Direct call≈3s + {steps} steps≈{steps*4}s",
        }
    else:
        # Token cost of writing a new script
        code_lines = complexity["code_lines_estimated"]
        code_tokens = code_lines * 15  # ~15 tokens per line (including thinking, debugging)
        debug_tokens = int(code_tokens * 0.3)  # 30% extra for debugging
        analysis_tokens = 500 + len(task) * 2  # Requirements analysis and planning
        total = code_tokens + debug_tokens + analysis_tokens
        # Execution time: analysis + generation + debugging + running, slowest
        steps = complexity["steps_estimated"]
        time_sec = 20 + code_lines * 0.5 + steps * 5  # Analysis+generation≈20s + 0.5s per line + 5s debugging per step
        return {
            "path": "Write new script",
            "estimated_tokens": total,
            "breakdown": f"Requirements analysis≈{analysis_tokens} + code generation≈{code_tokens} + debugging≈{debug_tokens}",
            "estimated_time": time_sec,
            "time_breakdown": f"Analysis+generation≈20s + {code_lines} lines≈{int(code_lines*0.5)}s + {steps} steps debugging≈{steps*5}s",
        }


def generate_report(task: str, complexity: dict, matching: dict, installed_skills: list) -> str:
    """Generate analysis report"""
    report = []
    report.append("# 📋 Skill Management Report\n")
    report.append(f"## Current Task Analysis\n")
    report.append(f"- **Task**: {task}")
    report.append(f"- **Complexity**: {complexity['level'].upper()}")
    report.append(f"- **Basis**: {complexity['reason']}")
    report.append(f"- **Estimated steps**: {complexity['steps_estimated']}")
    report.append(f"- **Estimated code lines**: {complexity['code_lines_estimated']}\n")

    report.append(f"## Installed Skills Overview ({len(installed_skills)} total)\n")

    # Risk statistics
    high_risk = [s for s in installed_skills if s["risk_level"] == "high"]
    medium_risk = [s for s in installed_skills if s["risk_level"] == "medium"]

    report.append(f"| Skill | Function | Risk | Match |")
    report.append(f"|-------|----------|------|-------|")
    matched_names = [s["name"] for s in matching["matched"]]
    for s in installed_skills:
        desc = s["description"][:40] + "..." if len(s["description"]) > 40 else s["description"]
        is_matched = "✓" if s["name"] in matched_names else ""
        report.append(f"| {s['name']} | {desc} | {s['risk_level']} | {is_matched} |")

    report.append(f"\n## Match Evaluation\n")
    if matching["matched"]:
        report.append(f"**Matched installed skills ({len(matching['matched'])}):**\n")
        for s in matching["matched"]:
            report.append(f"- **{s['name']}**: {s['description'][:80]}")
            report.append(f"  - Risk: {s['risk_level']} — {'; '.join(s['risk_notes'])}")

        # Token + time comparison — three paths
        report.append(f"\n### Cost Estimation (Token + Execution Time)\n")
        use_skill = estimate_tokens(task, complexity, "skill", matching["matched"][0])
        use_builtin = estimate_tokens(task, complexity, "builtin")
        write_code = estimate_tokens(task, complexity, "code")
        report.append(f"| Path | Est. Tokens | Est. Time | Breakdown |")
        report.append(f"|------|------------|-----------|-----------|")
        report.append(f"| {use_skill['path']} | ~{use_skill['estimated_tokens']} | ~{use_skill['estimated_time']}s | {use_skill['breakdown']} |")
        report.append(f"| {use_builtin['path']} | ~{use_builtin['estimated_tokens']} | ~{use_builtin['estimated_time']}s | {use_builtin['breakdown']} |")
        report.append(f"| {write_code['path']} | ~{write_code['estimated_tokens']} | ~{write_code['estimated_time']}s | {write_code['breakdown']} |")

        # Find token-optimal and time-optimal paths
        options = [
            ("skill", use_skill),
            ("builtin", use_builtin),
            ("code", write_code),
        ]
        best_token = min(options, key=lambda x: x[1]["estimated_tokens"])
        best_time = min(options, key=lambda x: x[1]["estimated_time"])
        if best_token[0] == best_time[0]:
            label_map = {"skill": "Use existing skill", "builtin": "Use built-in tools", "code": "Write new script"}
            report.append(f"\n💡 {label_map[best_token[0]]} optimal: Token≈{best_token[1]['estimated_tokens']}, Time≈{best_token[1]['estimated_time']}s\n")
        else:
            label_map = {"skill": "Use existing skill", "builtin": "Use built-in tools", "code": "Write new script"}
            report.append(f"\n💡 Token optimal: {label_map[best_token[0]]} (≈{best_token[1]['estimated_tokens']} tokens)")
            report.append(f"\n💡 Time optimal: {label_map[best_time[0]]} (≈{best_time[1]['estimated_time']}s)\n")
    else:
        report.append(f"**No matching installed skills found.**\n")

        # Token + time comparison — built-in tools vs write script (no skill match)
        report.append(f"\n### Cost Estimation (Token + Execution Time)\n")
        use_builtin = estimate_tokens(task, complexity, "builtin")
        write_code = estimate_tokens(task, complexity, "code")
        report.append(f"| Path | Est. Tokens | Est. Time | Breakdown |")
        report.append(f"|------|------------|-----------|-----------|")
        report.append(f"| {use_builtin['path']} | ~{use_builtin['estimated_tokens']} | ~{use_builtin['estimated_time']}s | {use_builtin['breakdown']} |")
        report.append(f"| {write_code['path']} | ~{write_code['estimated_tokens']} | ~{write_code['estimated_time']}s | {write_code['breakdown']} |")

        if complexity["level"] == "simple":
            report.append(f"\nTask complexity is **simple** — recommend using built-in tools directly.\n")
        else:
            report.append(f"\nTask complexity is **{complexity['level']}** — try built-in tools or search for external skills.\n")
            report.append(f"\n### Recommended Search Platforms\n")
            report.append(f"1. **SkillHub**: Use `skillhub_install` tool to search")
            report.append(f"2. **skills.sh**: `npx skills find <keyword>`")
            report.append(f"3. **GitHub**: web_search 'openclaw skill <keyword>'")
            report.append(f"4. **npm**: Search for relevant MCP servers\n")

        # Find token-optimal and time-optimal paths
        options = [("builtin", use_builtin), ("code", write_code)]
        best_token = min(options, key=lambda x: x[1]["estimated_tokens"])
        best_time = min(options, key=lambda x: x[1]["estimated_time"])
        label_map = {"builtin": "Use built-in tools", "code": "Write new script"}
        if best_token[0] == best_time[0]:
            report.append(f"💡 {label_map[best_token[0]]} optimal: Token≈{best_token[1]['estimated_tokens']}, Time≈{best_time[1]['estimated_time']}s\n")
        else:
            report.append(f"💡 Token optimal: {label_map[best_token[0]]} (≈{best_token[1]['estimated_tokens']} tokens)\n")
            report.append(f"💡 Time optimal: {label_map[best_time[0]]} (≈{best_time[1]['estimated_time']}s)\n")

    report.append(f"\n## Risk Summary\n")
    report.append(f"- 🟢 Low risk: {len(installed_skills) - len(high_risk) - len(medium_risk)}")
    report.append(f"- 🟡 Medium risk: {len(medium_risk)}")
    report.append(f"- 🔴 High risk: {len(high_risk)}")
    if high_risk:
        report.append(f"\n**High-risk skill details:**\n")
        for s in high_risk:
            report.append(f"- {s['name']}: {'; '.join(s['risk_notes'])}")

    report.append(f"\n## Decision Suggestion\n")
    report.append(f"\n> ⚠️ **Please select an execution path. Nothing will be auto-executed.**\n")
    if complexity["level"] == "simple":
        report.append(f"\n**Available paths:**")
        report.append(f"- Built-in tools direct execution (~{use_builtin['estimated_tokens']} tokens, ~{use_builtin['estimated_time']}s, recommended)")
        report.append(f"- Write new script (~{write_code['estimated_tokens']} tokens, ~{write_code['estimated_time']}s)")
        report.append(f"\n💡 Task is simple — built-in tools suffice. Please confirm before executing.")
    elif matching["matched"]:
        # Has matching skill — compare three paths
        use_skill = estimate_tokens(task, complexity, "skill", matching["matched"][0])
        use_builtin = estimate_tokens(task, complexity, "builtin")
        write_code = estimate_tokens(task, complexity, "code")
        options = [("skill", use_skill), ("builtin", use_builtin), ("code", write_code)]
        best_token = min(options, key=lambda x: x[1]["estimated_tokens"])
        best_time = min(options, key=lambda x: x[1]["estimated_time"])

        def _tag(key):
            if best_token[0] == key and best_time[0] == key:
                return ", Token+time optimal"
            elif best_token[0] == key:
                return ", Token optimal"
            elif best_time[0] == key:
                return ", Time optimal"
            return ""

        report.append(f"\n**Available paths:**")
        report.append(f"- Use installed skill {matching['matched'][0]['name']} (~{use_skill['estimated_tokens']} tokens, ~{use_skill['estimated_time']}s)")
        report.append(f"- Use built-in tools (~{use_builtin['estimated_tokens']} tokens, ~{use_builtin['estimated_time']}s{_tag('builtin')})")
        report.append(f"- Write new script (~{write_code['estimated_tokens']} tokens, ~{write_code['estimated_time']}s{_tag('code')})")

        best_labels = {
            "skill": f"Use installed skill (~{use_skill['estimated_tokens']} tokens, ~{use_skill['estimated_time']}s)",
            "builtin": f"Use built-in tools (~{use_builtin['estimated_tokens']} tokens, ~{use_builtin['estimated_time']}s)",
            "code": f"Write new script (~{write_code['estimated_tokens']} tokens, ~{write_code['estimated_time']}s)",
        }
        if best_token[0] == best_time[0]:
            report.append(f"\n💡 Overall optimal: {best_labels[best_token[0]]}")
        else:
            report.append(f"\n💡 Token optimal: {best_labels[best_token[0]]}")
            report.append(f"💡 Time optimal: {best_labels[best_time[0]]}")
        report.append(f"\nPlease select before executing.")
    else:
        # No matching skill — compare built-in tools vs write script
        use_builtin = estimate_tokens(task, complexity, "builtin")
        write_code = estimate_tokens(task, complexity, "code")
        options = [("builtin", use_builtin), ("code", write_code)]
        best_token = min(options, key=lambda x: x[1]["estimated_tokens"])
        best_time = min(options, key=lambda x: x[1]["estimated_time"])

        def _tag2(key):
            if best_token[0] == key and best_time[0] == key:
                return ", Token+time optimal"
            elif best_token[0] == key:
                return ", Token optimal"
            elif best_time[0] == key:
                return ", Time optimal"
            return ""

        report.append(f"\n**Available paths:**")
        report.append(f"- Use built-in tools (~{use_builtin['estimated_tokens']} tokens, ~{use_builtin['estimated_time']}s{_tag2('builtin')})")
        report.append(f"- Write new script (~{write_code['estimated_tokens']} tokens, ~{write_code['estimated_time']}s{_tag2('code')})")
        if complexity["level"] == "complex":
            report.append(f"- Search external platforms for ready-made skills (Token/time unknown, extra search required)")

        best_labels = {
            "builtin": f"Use built-in tools (~{use_builtin['estimated_tokens']} tokens, ~{use_builtin['estimated_time']}s)",
            "code": f"Write new script (~{write_code['estimated_tokens']} tokens, ~{write_code['estimated_time']}s)",
        }
        if best_token[0] == best_time[0]:
            report.append(f"\n💡 Overall optimal: {best_labels[best_token[0]]}")
        else:
            report.append(f"\n💡 Token optimal: {best_labels[best_token[0]]}")
            report.append(f"💡 Time optimal: {best_labels[best_time[0]]}")
        if complexity["level"] == "complex":
            report.append(f"\n🔍 Task is complex — consider also searching external platforms for ready-made skills as alternatives.")
        report.append(f"\nPlease select before executing.")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Analyze task and recommend skills")
    parser.add_argument("--task", required=True, help="Task description")
    parser.add_argument("--skills-json", help="Path to installed skills JSON file")
    parser.add_argument("--complex", action="store_true", help="Force mark as complex task")
    args = parser.parse_args()

    # Load skills data
    if args.skills_json:
        with open(args.skills_json, "r", encoding="utf-8") as f:
            installed_skills = json.load(f)
    else:
        installed_skills = json.load(sys.stdin)

    # Assess complexity
    complexity = assess_complexity(args.task, args.complex)

    # Find matching skills
    matching = find_matching_skills(args.task, installed_skills)

    # Generate report
    report = generate_report(args.task, complexity, matching, installed_skills)
    print(report)


if __name__ == "__main__":
    main()
