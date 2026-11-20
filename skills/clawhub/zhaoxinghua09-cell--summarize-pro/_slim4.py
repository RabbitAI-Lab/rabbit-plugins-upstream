#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通用段移动：按标题把整段搬进已有 references 文件，正文留一行指针。"""
import io
import os
import re

SRC = r"D:\Doubao\_skillhub_v200\summarize-pro\SKILL.md"
REF = r"D:\Doubao\_skillhub_v200\summarize-pro\references"

TARGETS = [
    (r"^##\s*边界与异常", "boundaries.md", "## 边界与异常", "边界条件与降级路径见 `references/boundaries.md`。"),
    (r"^##\s*输入\s*→\s*输出", "examples.md", "## 输入 → 输出 示例", "输入到输出的完整示例见 `references/examples.md`。"),
]


def rd(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def wr(p, t):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


for pat, fn, head, pointer in TARGETS:
    lines = rd(SRC).split("\n")
    start = None
    for i, l in enumerate(lines):
        if re.match(pat, l):
            start = i
            break
    if start is None:
        print("未找到:", pat)
        continue
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^##\s", lines[j]) or re.match(r"^#\s", lines[j]):
            end = j
            break
    seg = "\n".join(lines[start:end]).strip()
    rp = os.path.join(REF, fn)
    body = rd(rp).rstrip("\n") + "\n\n" + seg + "\n" if os.path.exists(rp) else seg + "\n"
    wr(rp, body)
    lines[start:end] = [head, "", pointer]
    out, prev = [], False
    for l in lines:
        if l.strip() == "":
            if prev:
                continue
            prev = True
            out.append("")
        else:
            prev = False
            out.append(l.rstrip())
    wr(SRC, "\n".join(out).rstrip("\n") + "\n")
    print("已移动:", pat, "->", fn)

print("原始行数:", len(rd(SRC).split("\n")))
print("非空行数:", len([l for l in rd(SRC).split("\n") if l.strip()]))
