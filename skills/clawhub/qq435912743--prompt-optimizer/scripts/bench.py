#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bench.py — 两个 prompt 的启发式基准对比，选优。

对比维度：清晰度 / 具体性 / 结构 / 约束强度 / 输出格式明确度。
纯本地规则，无需外部 API。

用法:
  python bench.py --a p1.md --b p2.md --task "..." --out bench.json
"""
import os, sys, json, argparse, re


def load(p):
    if os.path.isfile(p):
        return open(p, encoding="utf-8").read()
    return p


def score(text):
    dims = {}
    # 清晰度：是否有明确角色/任务标记
    dims["清晰度"] = 1.0 if re.search(r"(角色|任务|目标|你是一位|你是)", text) else 0.3
    # 具体性：长度适中 + 关键词密度（指令动词）
    verbs = len(re.findall(r"(请|必须|不要|步骤|首先|然后|最后|输出|返回)", text))
    dims["具体性"] = min(1.0, 0.4 + verbs / 20.0)
    # 结构：是否有分级标题/编号
    dims["结构"] = 1.0 if re.search(r"(#|\d+\.|一、|（\d）)", text) else 0.3
    # 约束强度：显式约束词
    cons = len(re.findall(r"(必须|不要|禁止|约束|限制|不得)", text))
    dims["约束强度"] = min(1.0, 0.3 + cons / 8.0)
    # 输出格式明确度
    dims["输出格式"] = 1.0 if re.search(r"(输出格式|JSON|Markdown|表格|代码块|返回格式)", text) else 0.3
    overall = sum(dims.values()) / len(dims)
    return overall, dims


def main():
    ap = argparse.ArgumentParser(description="prompt 基准对比")
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--task", default="")
    ap.add_argument("--out")
    args = ap.parse_args()

    ta, da = score(load(args.a))
    tb, db = score(load(args.b))

    winner = "A" if ta > tb else ("B" if tb > ta else "平局")
    report = {
        "task": args.task,
        "A": {"overall": round(ta, 3), "dims": {k: round(v, 3) for k, v in da.items()}},
        "B": {"overall": round(tb, 3), "dims": {k: round(v, 3) for k, v in db.items()}},
        "winner": winner,
    }
    out = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(out)
        print(f"✅ 对比完成 winner={winner} A={round(ta,3)} B={round(tb,3)} -> {args.out}")
    else:
        print(out)


if __name__ == "__main__":
    main()
