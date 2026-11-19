#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第三轮：按标题定位「同系列技能（LGD 生态）」整段移到 references/ecosystem.md。"""
import io
import os
import re

SRC = r"D:\Doubao\_skillhub_v200\summarize-pro\SKILL.md"
REF = r"D:\Doubao\_skillhub_v200\summarize-pro\references"


def rd(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def wr(p, t):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


lines = rd(SRC).split("\n")
start = None
for i, l in enumerate(lines):
    if re.match(r"^##\s*同系列技能", l):
        start = i
        break
if start is None:
    raise SystemExit("未找到目标段")

end = len(lines)
for j in range(start + 1, len(lines)):
    if re.match(r"^##\s", lines[j]) or re.match(r"^#\s", lines[j]):
        end = j
        break

seg = "\n".join(lines[start:end]).strip()
target = os.path.join(REF, "ecosystem.md")
wr(target, rd(target).rstrip("\n") + "\n\n" + seg + "\n")
lines[start:end] = ["## 同系列技能（LGD 生态）", "",
                    "同系列包清单与互链关系见 `references/ecosystem.md`。"]

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
print("正文行数:", len(rd(SRC).split("\n")))
