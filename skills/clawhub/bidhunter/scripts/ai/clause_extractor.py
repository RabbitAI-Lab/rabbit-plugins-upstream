#!/usr/bin/env python3
"""
clause_extractor.py - Extract structured clauses from a bid document (BidHunter v2.0, B1).

Calls MiniMax (OpenAI-compatible) to pull: 项目名称 / 招标单位 / 资质门槛 /
预算 / 投标截止日 / 评分权重 / 关键条款. Returns JSON. Requires MiniMax API key
(configured in ~/.config/bidhunter/ai.json). Without a key it prints a clear
instruction and exits non-zero (does not crash the pipeline).

Usage:
  python3 clause_extractor.py <doc_text_file.txt>     # prints JSON
  echo "文本..." | python3 clause_extractor.py -      # read from stdin
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from minimax_client import MiniMaxClient, ConfigError

MAX_CHARS = 9000
SYSTEM = (
    "你是招投标文件分析专家。请从给定的招标文件文本中提取结构化信息。"
    "只输出 JSON，不要解释。字段："
    "project_name(项目名称), owner(招标单位/采购人),"
    "qualification_requirements(资质门槛列表, 字符串数组),"
    "budget_yuan(预算金额, 整数元, 无法识别填null),"
    "bid_deadline(投标截止日 YYYY-MM-DD, 无法识别填null),"
    "score_weights(评分权重对象, 含 price/tech/business 百分比整数, 无法识别填空对象),"
    "key_clauses(关键商务条款列表, 字符串数组),"
    "has_risk_tendency(是否含有排他/内定倾向条款, 布尔)。"
    "若文本信息不足，对应字段留空或null。"
)


def extract(text):
    client = MiniMaxClient.from_config()
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS] + "\n...（已截断）"
    prompt = f"招标文件文本如下：\n'''{text}'''\n请提取结构化信息。"
    raw = client.chat(prompt, system=SYSTEM, json_mode=True)
    # tolerate code fences
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.strip("`")
        raw = raw[raw.find("{") : raw.rfind("}") + 1]
    return json.loads(raw)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 clause_extractor.py <file.txt|->", file=sys.stderr)
        sys.exit(1)
    src = sys.argv[1]
    if src == "-":
        text = sys.stdin.read()
    else:
        with open(src, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    try:
        data = extract(text)
    except ConfigError as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(json.dumps({"error": f"抽取失败: {e}"}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
