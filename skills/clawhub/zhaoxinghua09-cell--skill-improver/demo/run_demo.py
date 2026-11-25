#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""演示：造一个差包 → 自动改造 → 看真实变化。

不依赖外部评测器时也能跑：只断言文件是否按预期补齐。
若找到同系列的 lgd-skill-review，则额外报告结构制分数变化。
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

BAD = """---
name: demo-skill
display_name: Demo Skill
description: "Use when demonstrating the improver. 演示用的最小包。"
version: 0.1.0
license: MIT
author: Demo
category: general
---

# Demo Skill

一个刻意做得不完整的包：没有 LICENSE、没有 ai-index、没有 tags、没有 Triggers。
"""


def main():
    tmp = tempfile.mkdtemp()
    root = os.path.join(tmp, "demo-skill")
    os.makedirs(root, exist_ok=True)
    io.open(os.path.join(root, "SKILL.md"), "w", encoding="utf-8",
            newline="\n").write(BAD)

    print("造包：%s" % root)
    print("初始文件：%s\n" % ", ".join(sorted(os.listdir(root))))

    fm, body = I.fm_of(root)
    steps = []
    r = I.fix_license(root, fm)
    steps.append(("LICENSE", r))
    r = I.fix_ai_index(root, fm)
    steps.append(("ai-index.json", r))
    r = I.fix_tags(root, fm, body)
    steps.append(("tags", r))
    r = I.fix_triggers(root, fm, body)
    steps.append(("Triggers 段", r))
    r = I.fix_links(root, fm, body, ["lgd-skill-review"])
    steps.append(("Related 段", r))

    print("执行改造：")
    for name, res in steps:
        print("  %-16s %s" % (name, res or "（已有，跳过）"))

    print("\n改造后文件：%s" % ", ".join(sorted(os.listdir(root))))
    fm2, _ = I.fm_of(root)
    print("tags = %s" % fm2.get("tags", "（无）"))

    reviewer = I.find_reviewer(None)
    if reviewer:
        p = subprocess.run([sys.executable, reviewer, root, "--run"],
                           capture_output=True, text=True, encoding="utf-8")
        for line in (p.stdout + p.stderr).splitlines():
            if "结构制" in line:
                print("\n复测：" + line.strip())
                break
    else:
        print("\n（未找到同系列评测器，跳过复测；文件类改造已全部完成）")

    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
