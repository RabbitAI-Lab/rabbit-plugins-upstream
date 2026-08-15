#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
optimize.py — 提示词迭代优化器。

把一段粗糙 prompt 系统化增强为结构化、强约束、带输出格式的高质量 prompt，
并做版本管理。纯本地规则，无需外部 API。

用法:
  python optimize.py --task "把中文摘要翻译成学术英文" --prompt weak.txt --out prompt.optimized.md
  python optimize.py --task "..." --prompt weak.txt --no-role --no-cot   # 关闭部分增强
"""
import os, sys, json, argparse, datetime, re

DOMAINS = {
    "翻译": "中英双语翻译与本地化", "代码": "资深软件工程师", "写": "专业内容写作者",
    "分析": "资深数据分析师", "营销": "增长营销专家", "法律": "执业律师",
    "财务": "注册会计师", "设计": "产品设计师", "研究": "领域研究员",
    "客服": "客户成功专家",
}


def infer_domain(task):
    for k, v in DOMAINS.items():
        if k in task:
            return v
    return "领域专家"


def optimize(task, base, role=True, cot=True):
    domain = infer_domain(task)
    blocks = []
    changes = []
    if role:
        blocks.append(f"# 角色\n你是一位{domain}，擅长把任务做到专业、可靠、可交付。")
        changes.append("注入角色设定")
    blocks.append(f"# 任务\n{task}")
    blocks.append("# 上下文\n- 已知信息：（在此补充背景、输入、约束）\n- 目标：交付满足下述要求的结果")
    blocks.append("# 要求（分步）\n1. 先理解任务意图与隐含约束\n2. 规划执行步骤\n3. 产出结果\n4. 自检是否满足全部要求")
    changes.append("拆解为分步指令")
    blocks.append("# 输出格式\n- 使用清晰的结构化输出（标题/列表/代码块按需）\n- 关键结论前置，支撑细节在后")
    changes.append("强制输出格式")
    blocks.append("# 约束\n- 必须：紧扣任务、事实准确、可直接使用\n- 不要：编造信息、答非所问、冗余铺垫")
    changes.append("显式约束清单")
    blocks.append("# 示例（可选 few-shot）\n<在此放入 1-2 个输入/输出范例>\n")
    changes.append("预留示例占位")
    if cot:
        blocks.append("# 思考方式\n先简要推理（为什么这么做），再给出最终答案。")
        changes.append("加入链式思考")
    blocks.append("# 自检\n交付前确认：① 是否回应了任务 ② 是否格式正确 ③ 是否无事实错误")
    changes.append("加入自检步骤")
    blocks.append("\n---\n# 原始 prompt（基准）\n" + base)
    return "\n\n".join(blocks), changes


def load_base(p):
    if os.path.isfile(p):
        return open(p, encoding="utf-8").read()
    return p


def main():
    ap = argparse.ArgumentParser(description="提示词优化器")
    ap.add_argument("--task", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", default="prompt.optimized.md")
    ap.add_argument("--no-role", action="store_true")
    ap.add_argument("--no-cot", action="store_true")
    args = ap.parse_args()

    base = load_base(args.prompt)
    optimized, changes = optimize(args.task, base, role=not args.no_role, cot=not args.no_cot)

    open(args.out, "w", encoding="utf-8").write(optimized)

    # 版本日志
    logp = os.path.join(os.path.dirname(os.path.abspath(args.out)) or ".", "optimize_log.json")
    log = []
    if os.path.exists(logp):
        try:
            log = json.loads(open(logp, encoding="utf-8").read())
        except Exception:
            log = []
    log.append({
        "ts": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"),
        "task": args.task,
        "out": os.path.basename(args.out),
        "changes": changes,
    })
    open(logp, "w", encoding="utf-8").write(json.dumps(log, ensure_ascii=False, indent=2))

    print(f"✅ 已优化 -> {args.out}（增强项：{', '.join(changes)}）")


if __name__ == "__main__":
    main()
