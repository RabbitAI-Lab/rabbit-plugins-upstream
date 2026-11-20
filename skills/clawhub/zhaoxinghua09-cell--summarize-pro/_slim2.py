#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第二轮瘦身：再移两段，并把误建的 render.md 合并进 render-and-cli.md。"""
import io
import os

SRC = r"D:\Doubao\_skillhub_v200\summarize-pro\SKILL.md"
REF = r"D:\Doubao\_skillhub_v200\summarize-pro\references"

MOVES = [
    (160, 172, "tools.md", "三条命令上手（复制即用）",
     "## 三条命令上手\n\nscan / apply 两个子命令与最小可用示例见 `references/tools.md`。\n"),
    (126, 138, "commands.md", "怎么让我按你要的格式来（自然语言指令）",
     "## 怎么让我按你要的格式来\n\n常用自然语言指令与对应格式族见 `references/commands.md`。\n"),
    (139, 159, "tools.md", "可选本地工具链（v0 依赖、不联网）",
     "## 可选本地工具链\n\n零依赖工具链的安装与参数见 `references/tools.md`。\n"),
]


def rd(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def wr(p, t):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


lines = rd(SRC).split("\n")

for start, end, fn, title, pointer in MOVES:
    seg = lines[start - 1:end]
    rp = os.path.join(REF, fn)
    head = "# %s\n\n" % title
    if os.path.exists(rp):
        wr(rp, rd(rp).rstrip("\n") + "\n\n" + "\n".join(seg).strip() + "\n")
    else:
        wr(rp, head + "\n".join(seg).strip() + "\n")
    lines[start - 1:end] = pointer.split("\n")

# 合并重复的 render.md → render-and-cli.md，然后删除
rp = os.path.join(REF, "render.md")
target = os.path.join(REF, "render-and-cli.md")
if os.path.exists(rp):
    body = rd(rp)
    if os.path.exists(target):
        wr(target, rd(target).rstrip("\n") + "\n\n" + body.split("\n", 1)[1].lstrip("\n"))
    os.remove(rp)

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
txt = rd(SRC)
print("正文行数:", len(txt.split("\n")))
print("references:", sorted(os.listdir(REF)))
print("正文提到 references/ 次数:", txt.count("references/"))
