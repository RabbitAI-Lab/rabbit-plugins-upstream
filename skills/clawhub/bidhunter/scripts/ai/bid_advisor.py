#!/usr/bin/env python3
"""
bid_advisor.py - Generate bidding strategy suggestions (BidHunter v2.5).

Uses the structured extraction from a bid document + the user's own
qual_rules (capabilities / red_alerts) to produce a strategy brief:
  - 资质自检（我方能力 vs 门槛，标红缺口）
  - 评分得分点（按权重排优先级）
  - 报价/商务策略提示
  - 时间节点与风险提醒

COMPLIANCE BOUNDARY (v2.5): the assistant ONLY informs and advises.
It does NOT auto-fill quotes, forge qualifications, or write the technical
proposal. Every suggestion is clearly marked "仅供参考，最终决策人工确认".

Usage:
  python3 bid_advisor.py <招标文件.pdf|docx|txt>
"""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from doc_parser import parse as parse_doc
from clause_extractor import extract
from minimax_client import MiniMaxClient, ConfigError

RULES_PATH = os.path.join(os.path.dirname(HERE), "qual_rules.json")
MAX_CHARS = 9000
SYSTEM = (
    "你是资深招投标顾问。基于『招标文件结构化信息』与『投标方自身资质能力』，"
    "输出投标策略建议。只输出 JSON："
    "self_check(资质自检数组, 每项含 item(门槛), our_capable(布尔, 我方是否具备), gap(缺口说明)),"
    "score_focus(评分得分点数组, 字符串),"
    "pricing_tips(报价/商务策略提示数组, 字符串),"
    "timeline(关键时间节点数组, 字符串),"
    "risks(风险提醒数组, 字符串)。"
    "所有内容仅供参考，不代替人工决策，不虚构资质。"
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bid_advisor.py <file>", file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"文件不存在: {path}", file=sys.stderr)
        sys.exit(1)

    text, backend = parse_doc(path)
    if not text:
        print("⚠️ 未能提取文本，请安装解析依赖：pip install PyPDF2 python-docx", file=sys.stderr)
        sys.exit(1)

    # extract clauses (requires key)
    try:
        clauses = extract(text)
    except ConfigError as e:
        print(f"需配置 MiniMax API Key 才能生成策略建议：{e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"条款抽取失败: {e}", file=sys.stderr)
        sys.exit(1)

    # load our capabilities
    our_caps = []
    red_alerts = []
    try:
        with open(RULES_PATH, "r", encoding="utf-8") as f:
            rules = json.load(f)
        for e in rules.get("entities", {}).values():
            our_caps += e.get("capabilities", [])
        red_alerts = rules.get("red_alerts", [])
    except Exception:
        pass

    client = MiniMaxClient.from_config()
    prompt = (
        f"招标文件结构化信息：{json.dumps(clauses, ensure_ascii=False)}\n"
        f"我方资质能力词：{json.dumps(our_caps, ensure_ascii=False)}\n"
        f"我方红色预警（不可投类型）：{json.dumps(red_alerts, ensure_ascii=False)}\n"
        "请生成投标策略建议。"
    )
    try:
        raw = client.chat(prompt, system=SYSTEM, json_mode=True)
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw[raw.find("{"): raw.rfind("}") + 1]
        advice = json.loads(raw)
    except Exception as e:
        print(f"策略生成失败: {e}", file=sys.stderr)
        sys.exit(1)

    print("=" * 54)
    print(f"🧠 投标策略建议 · {os.path.basename(path)}")
    print("=" * 54)
    print("\n【资质自检】")
    for sc in advice.get("self_check", []):
        mark = "✅" if sc.get("our_capable") else "❌ 缺口"
        print(f"  {mark} {sc.get('item','')}  {sc.get('gap','')}")
    print("\n【评分得分点】")
    for s in advice.get("score_focus", []):
        print(f"  · {s}")
    print("\n【报价/商务策略】")
    for s in advice.get("pricing_tips", []):
        print(f"  · {s}")
    print("\n【关键时间节点】")
    for s in advice.get("timeline", []):
        print(f"  · {s}")
    print("\n【风险提醒】")
    for s in advice.get("risks", []):
        print(f"  · {s}")
    print("\n" + "=" * 54)
    print("⚠️ 以上为 AI 建议，仅供参考；最终投标决策与资质真实性由人工确认。")
    print("=" * 54)


if __name__ == "__main__":
    main()
