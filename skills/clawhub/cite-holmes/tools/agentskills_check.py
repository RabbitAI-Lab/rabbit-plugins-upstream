#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""agentskills.io 规范自检（v1.7 F3）：SKILL.md frontmatter 兼容矩阵。

校验规则（跨注册表通用）：
  1. frontmatter 存在且可解析（--- 围栏）
  2. name 存在、kebab-case、与目录名一致（可选 --dir 校验）
  3. description 存在且 ≤1024 字符（超长会被静默丢弃——ZCode 实测铁律）
  4. 必备键齐全（name/description）；license 建议存在
  5. 未知顶层键仅提示（各平台兼容度不同，不算错误）
用法：python3 agentskills_check.py <SKILL.md 路径> [--dir <技能目录名>]
"""
import argparse
import re
import sys


def frontmatter(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else ""


def parse_keys(fm: str) -> dict:
    out = {}
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):", line)
        if m:
            out[m.group(1)] = line
    return out


def scalar_value(fm: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+?)$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("skill_md")
    ap.add_argument("--dir", help="技能目录名（校验 name 一致性）")
    args = ap.parse_args()
    text = open(args.skill_md, encoding="utf-8").read()
    fm = frontmatter(text)
    fails, notes = [], []

    if not fm:
        print("FAIL: frontmatter 缺失或格式错误")
        return 1
    keys = parse_keys(fm)

    name = scalar_value(fm, "name")
    if not name:
        fails.append("name 缺失")
    elif not re.match(r"^[a-z0-9][a-z0-9-]*$", name):
        fails.append(f"name 非 kebab-case: {name}")
    if args.dir and name and name != args.dir:
        fails.append(f"name ({name}) 与目录名 ({args.dir}) 不一致")

    desc = scalar_value(fm, "description")
    if not desc and "description:" not in fm:
        fails.append("description 缺失")
    else:
        # 折叠标量（>-）取正文块长度
        m = re.search(r"description:\s*>-?\n((?:[ \t]+.*\n?)+)", fm)
        dlen = len(m.group(1)) if m else len(desc)
        if dlen > 1024:
            fails.append(f"description 超长（{dlen} > 1024，会被静默丢弃）")
        else:
            notes.append(f"description {dlen} 字符（≤1024 安全）")

    for k in ("name", "description"):
        if k not in keys:
            fails.append(f"必备键缺失: {k}")
    if "license" not in keys:
        notes.append("建议补 license 键（部分注册表展示用）")

    known = {"name", "license", "description", "when_to_use", "metadata",
             "version", "author", "homepage", "documentation", "icon"}
    unknown = [k for k in keys if k not in known]
    if unknown:
        notes.append("非通用键（各平台兼容度不同，仅提示）: " + ", ".join(unknown))

    for n in notes:
        print("NOTE:", n)
    for f in fails:
        print("FAIL:", f)
    print("AGENTSPEAK_CHECK:", "PASS" if not fails else "FAIL")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
