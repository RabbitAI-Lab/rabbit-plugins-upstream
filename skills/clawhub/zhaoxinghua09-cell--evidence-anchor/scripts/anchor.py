#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""evidence-anchor: 把报告里的 `文件:行号` 锚点逐个回真实文件里点一遍。

只判定两件事实：文件在不在、行号越不越界。
不判定锚点所在那一行"说得对不对"——那需要读上下文，机器判定只会制造假证据。
"""
import argparse
import io
import os
import re
import sys

# 锚点：文件名.扩展名:行号（允许可选的 :列号）
ANCHOR = re.compile(r"([A-Za-z0-9_.\-/\\]+\.(?:py|md|json|html|txt|ya?ml|toml|ini|cfg)):(\d+)(?::(\d+))?")


def read_text(path):
    with io.open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def line_count(path):
    return len(read_text(path).split("\n"))


def scan(text, root):
    """返回 [(anchor, status, detail, lineno_in_report)]"""
    findings = []
    lines = text.split("\n")
    for i, l in enumerate(lines, 1):
        for m in ANCHOR.finditer(l):
            raw = m.group(0)
            rel = m.group(1).replace("\\", "/")
            ln = int(m.group(2))
            full = os.path.normpath(os.path.join(root, rel))
            if not os.path.isfile(full):
                findings.append((raw, "FILE_MISSING", "根目录下没有 " + rel, i))
                continue
            total = line_count(full)
            if ln < 1 or ln > total:
                findings.append((raw, "LINE_OOR", "文件只有 %d 行" % total, i))
            else:
                findings.append((raw, "OK", "文件 %d 行" % total, i))
    return findings


def collect(args):
    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        sys.stderr.write("根目录不存在：%s\n" % root)
        return None, root
    all_findings = []
    for rp in args.reports:
        if not os.path.isfile(rp):
            sys.stderr.write("报告不存在：%s\n" % rp)
            return None, root
        for f in scan(read_text(rp), root):
            all_findings.append((os.path.basename(rp),) + f)
    return all_findings, root


def fmt(name, raw, status, detail, ln):
    return "%-12s %-40s %s（报告第 %d 行）" % (status, raw, detail, ln)


def main():
    ap = argparse.ArgumentParser(
        prog="anchor.py",
        description="校验报告里的文件:行号锚点。tools: check（汇总）、list（逐条）")
    sub = ap.add_subparsers(dest="cmd")
    p_check = sub.add_parser("check", help="汇总判定，有问题时退出码 1")
    p_list = sub.add_parser("list", help="逐条列出，不汇总")
    for p in (p_check, p_list):
        p.add_argument("reports", nargs="+", help="要校验的报告文件")
        p.add_argument("--root", default=".", help="锚点相对路径的基准目录")

    argv = sys.argv[1:]
    if not argv or argv[0] not in ("check", "list"):
        argv = ["check"] + argv
    a = ap.parse_args(argv)

    findings, root = collect(a)
    if findings is None:
        sys.exit(2)

    if not findings:
        print("未发现任何 `文件:行号` 锚点（纯叙述文档可忽略）")
        if a.cmd == "list":
            return
        print("结论：无锚点可验")
        return

    bad = [f for f in findings if f[2] != "OK"]
    for name, raw, status, detail, ln in findings:
        print(fmt(name, raw, status, detail, ln))

    if a.cmd == "list":
        return

    print("\n锚点 %d 个：OK %d / 不合格 %d" % (len(findings), len(findings) - len(bad), len(bad)))
    if bad:
        print("结论不合格：有 %d 个锚点解析不了，不能当作证据。" % len(bad))
        sys.exit(1)
    print("结论可核：所有锚点都能在 %s 下打开同一行。" % root)


if __name__ == "__main__":
    main()
