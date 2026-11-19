#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""summarize-pro 正文瘦身：把长段移到 references，正文留指针。

原则：内容不删，只搬家；每搬一段，正文留一行指向。
"""
import io
import os
import re

SRC = r"D:\Doubao\_skillhub_v200\summarize-pro\SKILL.md"
REF = r"D:\Doubao\_skillhub_v200\summarize-pro\references"

# 1-indexed 闭区间，从下往上处理，避免行号漂移
MOVES = [
    (395, 407, "chain.md", "链式路由：摘要产出后交给谁", "## 输出之后交给谁\n\n正文已搬到 `references/chain.md`：那里按「下一步动作」列了 4 条衔接路径与交接要点。\n"),
    (375, 378, "render.md", "确定性渲染与子命令", "## 确定性渲染\n\n三个子命令与确定性渲染要点见 `references/render.md`。\n"),
    (351, 361, "faq.md", "FAQ 与多语种如实说明", "## FAQ 与多语种\n\n常见问题与多语种支持的真实边界见 `references/faq.md`。\n"),
    (310, 336, "strength.md", "决策与承诺的强度分级", "## 决策与承诺的强度分级\n\n五级强度（陈述/推断/建议/承诺/指令）的判定口径见 `references/strength.md`，含每条的反例。\n"),
    (201, 229, "routing.md", "意图路由与搜索关键词", "## 意图路由\n\n按意图而不是关键词路由，完整路由表与关键词见 `references/routing.md`。\n"),
    (87, 116, "en-overview.md", "Overview (English)", "## Overview (English)\n\nSee `references/en-overview.md` for the English overview, boundaries and routing summary.\n"),
]


def rd(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def wr(p, t):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


lines = rd(SRC).split("\n")
os.makedirs(REF, exist_ok=True)

for start, end, fn, title, pointer in MOVES:
    seg = lines[start - 1:end]
    rp = os.path.join(REF, fn)
    head = "# %s\n\n" % title
    if os.path.exists(rp):
        wr(rp, rd(rp).rstrip("\n") + "\n\n" + "\n".join(seg).strip() + "\n")
    else:
        wr(rp, head + "\n".join(seg).strip() + "\n")
    lines[start - 1:end] = pointer.split("\n")

# 折叠连续空行
out = []
prev_blank = False
for l in lines:
    if l.strip() == "":
        if prev_blank:
            continue
        prev_blank = True
        out.append("")
    else:
        prev_blank = False
        out.append(l.rstrip())

wr(SRC, "\n".join(out).rstrip("\n") + "\n")
print("正文行数:", len(open(SRC, encoding="utf-8").read().split("\n")))
print("references:", sorted(os.listdir(REF)))
