#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""demo：造一棵最小树 + 一份含三类锚点的报告，跑 check，看判定。

不依赖评测器，纯文件断言，拿来就能跑。
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def wr(p, t):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def main():
    root = tempfile.mkdtemp(prefix="anchor-demo-")
    try:
        os.makedirs(os.path.join(root, "src"), exist_ok=True)
        wr(os.path.join(root, "src", "app.py"), "\n".join("line %d" % i for i in range(1, 31)) + "\n")
        wr(os.path.join(root, "SKILL.md"), "\n".join("line %d" % i for i in range(1, 21)) + "\n")

        report = os.path.join(root, "review.md")
        wr(report, (
            "# 一份有三个锚点的报告\n\n"
            "1. 参数在 `src/app.py:14` 声明了却没有实现。\n"
            "2. 版本号写在 `docs/CHANGELOG.md:8`，但根目录下没有这个文件。\n"
            "3. 主文件第 `SKILL.md:412` 行有相关说明（改版后行号过期了）。\n"
        ))

        print("临时树：", root)
        print("报告：", report)
        print("\n执行 check：")
        p = subprocess.run([sys.executable, os.path.join(PKG, "scripts", "anchor.py"),
                            "check", report, "--root", root],
                           capture_output=True, text=True, encoding="utf-8")
        for l in (p.stdout + p.stderr).strip().split("\n"):
            print("  " + l)
        print("\n退出码：", p.returncode, "（1 表示有锚点解析不了）")
        print("\n一句话：报告写得再漂亮，锚点打不开就不算证据。")
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    main()
