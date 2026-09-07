#!/usr/bin/env python3
"""report_generator.py v2.0.0 — 从 JSON 结果文件生成 Markdown 职业规划报告。

用法：
  python3 scripts/report_generator.py --data-file results.json [--out 报告.md]

数据文件为 JSON 对象，必填字段：
  recommendations: 非空数组，每项须含 title（可用 career_planner.py match 的
                   recommendations 字段直接填充）
可选字段：
  nickname, stage, holland, mbti, anchor, values, city, industry,
  assessment_type (默认 "screening"),
  ai_guide {skills, tools, cert}, actions {today, 1month, 3months, 1year}
每条推荐可选：reason, ai_rating, salary, salary_note, path, expectation, risk,
  score (0-5 整数，默认 3)

退出码：0 成功；2 输入错误（stderr 输出可操作的错误 JSON）。
"""
import argparse
import json
import sys
from datetime import datetime

ENGINE = "ai-era-career-planner v2.0.0"


def err(msg, extra=None):
    out = {"status": "error", "error": msg}
    if extra:
        out.update(extra)
    print(json.dumps(out, ensure_ascii=False, indent=2), file=sys.stderr)
    sys.exit(2)


def clamp_score(v):
    try:
        return max(0, min(5, int(v)))
    except (TypeError, ValueError):
        return 3


def build_recs(recs):
    star, unst = chr(9733), chr(9734)
    lines = []
    for i, r in enumerate(recs, 1):
        sc = clamp_score(r.get("score", 3))
        lines.append("### {0}. 【{1}】 适合指数：{2}{3}".format(
            i, r.get("title"), star * sc, unst * (5 - sc)))
        for k, label in (("reason", "推荐理由"), ("ai_rating", "AI评级"),
                         ("salary", "薪资参考"), ("salary_note", "薪资说明"),
                         ("path", "入门路径"), ("expectation", "3年预期"),
                         ("risk", "潜在风险")):
            if r.get(k):
                lines.append("- **{0}**：{1}".format(label, r[k]))
        lines.append("")
    return "\n".join(lines)


def generate_report(data):
    today = datetime.now().strftime("%Y-%m-%d")
    ai = data.get("ai_guide", {})
    acts = data.get("actions", {})
    vals = data.get("values")
    vals_s = "、".join(vals) if isinstance(vals, list) else data.get("values", "未明确")
    atype = data.get("assessment_type", "screening")
    md = [
        "# 个性化职业规划报告", "",
        "> 生成日期：" + today + "　|　引擎：" + ENGINE, "",
        "## ⚠️ 重要声明（先读这里）", "",
        "> 1. 测评性质：**" + str(atype) + "（筛查性参考）**，不是职业认证测评。"
        "MBTI 重测一致性约 50-65%，霍兰德量表信度约 .91-.95。",
        "> 2. 适合指数为**启发式打分，非预测**（权重：霍兰德0.4 / 价值观0.3 / 职业锚0.3，"
        "缺失维度自动重新归一化；详见 references/assessment.md）。",
        "> 3. 薪资为**因子模型参考区间**（人民币/月），非实时市场数据，以招聘平台实时数据为准。",
        "> 4. 文中标注\"定性\"的判断为方向性观察，不是统计结论。",
        "", "---", "",
        "## 基础档案", "",
        "- 昵称：" + str(data.get("nickname", "未提供")),
        "- 当前阶段：" + str(data.get("stage", "未提供")),
        "- 霍兰德代码：" + str(data.get("holland", "未测评")),
        "- MBTI类型：" + str(data.get("mbti", "未测评")),
        "- 职业锚：" + str(data.get("anchor", "未测评")),
        "- 核心价值观：" + str(vals_s),
        "- 城市：" + str(data.get("city", "未提供")),
        "- 行业：" + str(data.get("industry", "未提供")),
        "", "---", "",
        "## 职业方向推荐", "",
        build_recs(data["recommendations"]),
        "",
        "## AI时代生存指南", "",
        "- 核心技能：" + str(ai.get("skills", "详见推荐方向")),
        "- 必学AI工具：" + str(ai.get("tools", "暂无")),
        "- 建议认证：" + str(ai.get("cert", "暂无")),
        "",
        "## 下一步行动清单", "",
        "- 今天：" + str(acts.get("today", "暂无")),
        "- 1个月内：" + str(acts.get("1month", "暂无")),
        "- 3个月内：" + str(acts.get("3months", "暂无")),
        "- 1年内：" + str(acts.get("1year", "暂无")),
        "", "---", "",
        "由 " + ENGINE + " 生成（" + today + "）",
    ]
    return "\n".join(md)


def validate(data):
    errors = []
    recs = data.get("recommendations")
    if not isinstance(recs, list) or not recs:
        errors.append("recommendations 必须是非空数组（可用 career_planner.py match 的输出填充）")
    else:
        for i, r in enumerate(recs):
            if not isinstance(r, dict) or not r.get("title"):
                errors.append("recommendations[{0}] 必须是含 title 的对象".format(i))
                break
    for field in ("ai_guide", "actions"):
        if data.get(field) is not None and not isinstance(data[field], dict):
            errors.append(field + " 必须是对象")
    if not isinstance(data.get("values", "x"), (list, str)):
        errors.append("values 必须是字符串或字符串数组")
    return errors


def main():
    p = argparse.ArgumentParser(prog="report_generator.py",
                                description="从 JSON 结果文件生成 Markdown 职业规划报告")
    p.add_argument("--data-file", required=True, help="JSON 数据文件路径")
    p.add_argument("--out", default=None, help="输出 .md 路径（缺省打印到 stdout）")
    args = p.parse_args()

    try:
        with open(args.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except OSError as e:
        err("无法读取 --data-file: " + str(e))
    except json.JSONDecodeError as e:
        err("--data-file 不是合法 JSON: " + str(e))
    if not isinstance(data, dict):
        err("--data-file 顶层必须是 JSON 对象")
    errors = validate(data)
    if errors:
        err("data-file 校验失败: " + " | ".join(errors))

    md = generate_report(data)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(json.dumps({"command": "report", "status": "ok", "out": args.out,
                          "bytes": len(md.encode("utf-8"))}, ensure_ascii=False))
    else:
        print(md)
    sys.exit(0)


if __name__ == "__main__":
    main()
