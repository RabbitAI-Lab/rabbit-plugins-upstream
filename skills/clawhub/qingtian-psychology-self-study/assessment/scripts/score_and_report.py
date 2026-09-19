#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""集成封装：读量表 → 计分 → 渲染 HTML 报告 → 保存到指定目录。

用法：
    python3 score_and_report.py <SCALE_ID> <ANSWERS_JSON> <OUT_DIR>

依赖同目录的 scoring_engine.py / report_generator.py（均由量表测评系统提供）。
answers JSON 形如 {"q1": 2, "q2": 0, ...}，值为选项序号（0 起）。
最后一行输出 RESULT_JSON>>>... 供调用方（自学 Skill）解析并写入进度文件。
"""
import sys
import os
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from scoring_engine import load_scale, score
from report_generator import save


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 score_and_report.py <SCALE_ID> <ANSWERS_JSON> <OUT_DIR>")
        sys.exit(1)

    sid, ans_path, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    scale = load_scale(sid)  # 大小写/连字符容错：phq9 / phq-9 / PHQ9 均可
    with open(ans_path, "r", encoding="utf-8") as f:
        answers = json.load(f)

    result = score(scale, answers)

    # 完整性校验：缺题则明确报错退出，避免生成无分数的空白报告误导用户
    missing = result.get("missing_items", [])
    if missing:
        sys.stderr.write(
            "❌ 作答不完整：缺少题目 %s。\n"
            "正确格式：{\"q1\":<选项序号>, \"q2\":<选项序号>, ...}（键为题号 q1..qn，值为选项序号，0 起）。\n"
            "请补全后重试。\n" % ", ".join(missing)
        )
        sys.exit(2)

    # 要点摘要（先于报告，便于对话中即时播报）
    print("=== 计分结果 ===")
    for dim, val in result.get("dimension_scores", {}).items():
        std = result.get("standard_scores", {}).get(dim, "—")
        print(f"  {dim}: 原始分 {val} | 标准分 {std} | 分级 {result.get('bands', {}).get(dim, '—')}")
    if result.get("crisis_flag"):
        print("⚠️ 危机标志触发，请先于分数展示求助资源（见 safety_protocol.md）")

    os.makedirs(out_dir, exist_ok=True)
    path = save(scale, result, out_dir=out_dir)  # 渲染并保存 HTML
    result["report_path"] = path  # 回吐路径，供调用方记录进度
    print(f"HTML 报告已保存：{path}")

    # 回吐 result JSON 供调用方记录进度
    print("RESULT_JSON>>>" + json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
