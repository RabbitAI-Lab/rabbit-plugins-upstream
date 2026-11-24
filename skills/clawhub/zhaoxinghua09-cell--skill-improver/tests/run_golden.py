#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-improver 自检：逐条跑 tests/golden.json。

设计原则：每个用例自建临时包，互不污染；失败要说清是哪一条、哪一步。
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(PKG, "scripts"))
import improve as I  # noqa: E402

SAMPLE = """---
name: sample-skill
display_name: Sample Skill
description: "Use when testing the improver. 一个用于测试的小包。"
version: 0.1.0
license: MIT
author: Tester
category: general
---

# Sample

正文示例：

```bash
python scripts/tool.py --draft out.md --source doc.md
```
"""


def make_pkg(tmp):
    root = os.path.join(tmp, "sample")
    os.makedirs(root, exist_ok=True)
    io.open(os.path.join(root, "SKILL.md"), "w", encoding="utf-8",
            newline="\n").write(SAMPLE)
    return root


def check(case, root):
    kind = case.get("kind")
    if kind == "cli":
        # 传一个没有 SKILL.md 的目录，验证「不是技能包就拒绝」
        target = os.path.dirname(root)
        p = subprocess.run([sys.executable, os.path.join(PKG, "scripts", "improve.py"),
                            target], capture_output=True, text=True, encoding="utf-8")
        if case["expect"] == "exit_nonzero" and p.returncode != 0:
            return True, "退出码 %d（预期非 0）" % p.returncode
        return False, "退出码 %d" % p.returncode

    fn = case["fn"]
    if fn == "license":
        if case.get("pre") == "write_license":
            io.open(os.path.join(root, "LICENSE"), "w", encoding="utf-8", newline="\n").write("x\n")
            r = I.fix_license(root, {})
            return (r is None), ("已存在则不覆盖" if r is None else "被覆盖了")
        I.fix_license(root, {"author": "Tester"})
        p = os.path.join(root, "LICENSE")
        ok = os.path.exists(p)
        if case["expect"] == "lf_only":
            raw = io.open(p, "rb").read()
            return (b"\r\n" not in raw), ("LF only" if b"\r\n" not in raw else "含 CRLF")
        return ok, ("文件已生成" if ok else "未生成")

    if fn == "tags":
        fm, body = I.fm_of(root)
        I.fix_tags(root, fm, body)
        fm2, _ = I.fm_of(root)
        n = len([t for t in fm2.get("tags", "").split(",") if t.strip()])
        return (n >= 3), ("tags=%d" % n)

    if fn == "triggers":
        fm, body = I.fm_of(root)
        I.fix_triggers(root, fm, body)
        txt = I.rd(os.path.join(root, "SKILL.md"))
        ok = "## Triggers" in txt
        return ok, ("已追加" if ok else "未追加")

    if fn == "links":
        fm, body = I.fm_of(root)
        if case.get("pre") == "write_related":
            txt = I.rd(os.path.join(root, "SKILL.md")) + "\n本技能属于同系列技能。\n"
            I.wr(os.path.join(root, "SKILL.md"), txt)
            r = I.fix_links(root, fm, body, ["a", "b"])
            return (r is None), ("已有标识则不动" if r is None else "重复追加了")
        I.fix_links(root, fm, body, ["a", "b"])
        txt = I.rd(os.path.join(root, "SKILL.md"))
        ok = "同系列" in txt
        return ok, ("已追加" if ok else "未追加")

    if fn == "doc_drift":
        acts = [{"key": "block:declared_command_missing",
                 "issue": "SKILL.md:18 声明了未实现的参数 --draft"}]
        I.fix_doc_drift(root, acts)
        txt = I.rd(os.path.join(root, "SKILL.md"))
        ok = "--draft" not in txt
        return ok, ("已移除参数名" if ok else "参数名仍存在")

    return False, "未知用例"


def main():
    suite = json.load(io.open(os.path.join(HERE, "golden.json"), encoding="utf-8"))
    passed = failed = 0
    fails = []
    for c in suite["cases"]:
        tmp = tempfile.mkdtemp()
        try:
            root = make_pkg(tmp)
            ok, why = check(c, root)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        if ok:
            passed += 1
            print("  PASS  %s  %s  (%s)" % (c["id"], c["name"], why))
        else:
            failed += 1
            fails.append(c["id"])
            print("  FAIL  %s  %s  (%s)" % (c["id"], c["name"], why))
    print("\n---- %d/%d PASS ----" % (passed, passed + failed))
    if fails:
        print("失败：%s" % ", ".join(fails))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
