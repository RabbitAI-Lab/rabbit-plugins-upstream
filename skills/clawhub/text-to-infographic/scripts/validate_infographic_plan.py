#!/usr/bin/env python3
"""validate_infographic_plan.py — 信息图 plan 校验器（布局语义 + 结构 + 文本预算）。

实现《校验规则规格 v0.1》A 层（布局语义）为主，结构检查与 C 层文本预算内置；
B 层（数值 vs 原文）在提供 --source 时启用。

判级：ERROR（阻塞渲染）/ WARN（建议修）/ INFO（提示）。
退出码：存在 ERROR → 1，否则 0。

用法:
    python3 validate_infographic_plan.py plan.json [--source source.txt] [--json]
"""
import json
import re
import sys

ERROR, WARN, INFO = "ERROR", "WARN", "INFO"
LAYOUTS = {"flywheel", "fishbone", "sankey", "pyramid", "timeline", "dashboard"}
HEX_COLOR_RE = re.compile(r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')
TEMPORAL_WORDS = ("先", "然后", "接着", "随后", "之后", "再", "最终", "导致", "因此", "从而")
TIME_PAT = re.compile(r"(\d{4}|\d{1,2}月|\d{1,2}日|Q[1-4]|第\s*[一二三四五六七八九十\d]+\s*[步周月阶段天年]|周[一二三四五六日末]|早期|中期|后期|现在|未来)")


def check(plan, findings):
    layout = plan.get("layout")
    blocks = plan.get("blocks", [])
    ids = [b.get("id") for b in blocks]
    rels = plan.get("relations", [])

    # ---- 结构基线
    if plan.get("version") != "1.0":
        findings.append(ERROR, "version 必须为 1.0")
    if layout not in LAYOUTS:
        findings.append(ERROR, f"layout 必须是 {sorted(LAYOUTS)} 之一")
    # ---- 安全：accent 颜色只放行十六进制（与渲染器边界一致，防止 CSS/SVG 注入）
    vs = plan.get("visual_system") or {}
    if vs.get("accent") is not None:
        if not isinstance(vs["accent"], str) or not HEX_COLOR_RE.match(vs["accent"]):
            findings.append(ERROR, f"visual_system.accent 必须是十六进制颜色（#RGB 或 #RRGGBB），收到: {vs['accent']!r}")
    if len(blocks) < 2:
        findings.append(ERROR, "blocks 至少 2 个")
    if len(ids) != len(set(ids)):
        findings.append(ERROR, "block id 存在重复")
    for r in rels:
        if r.get("from") not in ids or r.get("to") not in ids:
            findings.append(ERROR, f"relation 引用了不存在的 block: {r}")

    for b in blocks:
        if not b.get("title"):
            findings.append(ERROR, f"block {b.get('id')} 缺 title")
        if len(b.get("title", "")) > 24:
            findings.append(WARN, f"block {b.get('id')} 标题超过 24 字（C 层文本预算）")
        if len(b.get("text", "")) > 120:
            findings.append(WARN, f"block {b.get('id')} 正文超过 120 字（C 层文本预算）")

    # ---- A3 timeline 缺时标
    if layout == "timeline":
        for b in blocks:
            if not b.get("time") or not TIME_PAT.search(b.get("time", "")):
                findings.append(ERROR, f"timeline 节点 {b.get('id')} 缺可解析时间标记")

    # ---- A4 pyramid 层级过少
    if layout == "pyramid" and len(blocks) < 3:
        findings.append(WARN, f"pyramid 仅 {len(blocks)} 层（<3 将退化为列表）")

    # ---- A5 flywheel 未闭环
    if layout == "flywheel":
        if not rels:
            findings.append(ERROR, "flywheel 缺 relations（飞轮必须闭环）")
        else:
            edges = {(r["from"], r["to"]) for r in rels}
            start = ids[0]
            cur, seen, closed = start, {start}, False
            for _ in range(len(ids)):
                nxt = next((t for f, t in edges if f == cur), None)
                if nxt is None:
                    break
                if nxt == start:
                    closed = len(seen) == len(ids)
                    break
                if nxt in seen:
                    break
                seen.add(nxt)
                cur = nxt
            if not closed:
                findings.append(ERROR, "flywheel relations 未构成覆盖全部 block 的闭环")

    # ---- A6 fishbone 多头
    if layout == "fishbone":
        heads = [b for b in blocks if b.get("role") == "head"]
        if len(heads) == 0:
            findings.append(WARN, "fishbone 无 role=head 的块（默认取第一个 block 为 head，建议显式标注）")
        elif len(heads) > 1:
            findings.append(ERROR, f"fishbone 有 {len(heads)} 个 head（必须恰好 1 个）")

    # ---- A7 sankey 不守恒
    if layout == "sankey":
        weighted = [r for r in rels if r.get("weight") is not None]
        if not weighted:
            findings.append(ERROR, "sankey 的 relations 全部缺 weight")
        else:
            if len(weighted) < len(rels):
                findings.append(ERROR, "sankey 存在缺 weight 的 relation")
            for bid in ids:
                inflow = sum(r["weight"] for r in weighted if r["to"] == bid)
                outflow = sum(r["weight"] for r in weighted if r["from"] == bid)
                if inflow and outflow and abs(inflow - outflow) / max(inflow, outflow) > 0.01:
                    findings.append(ERROR, f"sankey 节点 {bid} 流量不守恒：入 {inflow} ≠ 出 {outflow}")

    # ---- A8 dashboard 缺元数据
    if layout == "dashboard":
        for b in blocks:
            if not b.get("metric"):
                findings.append(WARN, f"dashboard 卡 {b.get('id')} 缺 metric")
            if not b.get("value"):
                findings.append(ERROR, f"dashboard 卡 {b.get('id')} 缺 value")
            if not b.get("unit"):
                findings.append(ERROR, f"dashboard 卡 {b.get('id')} 缺 unit（无单位的数字等于没说）")
            if not b.get("time"):
                findings.append(WARN, f"dashboard 卡 {b.get('id')} 缺时间范围")

    # ---- A1 并列误作流程（timeline 轻量启发）
    if layout == "timeline" and len(blocks) >= 3:
        flat = all(not any(w in (b.get("text") or "") or w in (b.get("title") or "")
                           for w in TEMPORAL_WORDS) for b in blocks)
        same_shape = len({len(b.get("text") or "") // 20 for b in blocks}) == 1
        if flat and same_shape:
            findings.append(WARN, "疑似并列内容被表达为时间线（A1）：全文无时序连接词且各条目同构")


def check_source(plan, source_text, findings):
    """B 层：数值可溯源 + 引用完整性。"""
    for b in plan.get("blocks", []):
        ref = b.get("source_ref")
        if ref and ref not in source_text:
            findings.append(ERROR, f"block {b.get('id')} source_ref 在原文中找不到（B5）")
        v = b.get("value")
        if v is not None:
            vs = str(v)
            if vs not in source_text and not any(ch.isdigit() and ch in source_text for ch in vs):
                findings.append(WARN, f"block {b.get('id')} 数值 {vs} 未能在原文定位（B1）")


class Findings:
    def __init__(self):
        self.items = []

    def append(self, level, msg):
        self.items.append({"level": level, "message": msg})

    @property
    def has_error(self):
        return any(x["level"] == ERROR for x in self.items)


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    args = [a for a in args if a != "--json"]
    if not args:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    plan = json.loads(open(args[0], encoding="utf-8").read())
    source_text = ""
    if "--source" in args:
        i = args.index("--source")
        source_text = open(args[i + 1], encoding="utf-8").read()

    f = Findings()
    check(plan, f)
    if source_text:
        check_source(plan, source_text, f)

    if as_json:
        print(json.dumps({"ok": not f.has_error, "findings": f.items},
                         ensure_ascii=False, indent=2))
    else:
        if not f.items:
            print("✅ 通过：未发现问题")
        for x in f.items:
            icon = {"ERROR": "❌", "WARN": "⚠️ ", "INFO": "ℹ️ "}[x["level"]]
            print(f"{icon} [{x['level']}] {x['message']}")
        n_err = sum(1 for x in f.items if x["level"] == ERROR)
        n_warn = sum(1 for x in f.items if x["level"] == WARN)
        print(f"—— {n_err} ERROR / {n_warn} WARN")
    sys.exit(1 if f.has_error else 0)


if __name__ == "__main__":
    main()
