#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""9 条自检：每条在临时目录里自建最小树，跑完即删，互不污染。"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PKG, "scripts"))
import anchor  # noqa: E402


def wr(p, t):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def mk(root, rel, lines=40):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
    wr(p, "\n".join("line %d" % i for i in range(1, lines + 1)) + "\n")
    return p


def status_of(root, text):
    f = anchor.scan(text, root)
    return f[0][1] if f else "NO_ANCHOR"


def check(fn, root):
    if fn == "ok_anchor":
        mk(root, "a.py", 40)
        s = status_of(root, "见 a.py:12")
        return s == "OK", s
    if fn == "missing_file":
        s = status_of(root, "见 nope.md:5")
        return s == "FILE_MISSING", s
    if fn == "line_oor":
        mk(root, "b.md", 10)
        s = status_of(root, "见 b.md:99")
        return s == "LINE_OOR", s
    if fn == "backslash_path":
        mk(root, "sub/c.py", 10)
        s = status_of(root, "见 sub\\c.py:3")
        return s == "OK", s
    if fn == "col_suffix":
        mk(root, "d.py", 30)
        s = status_of(root, "见 d.py:12:5")
        return s == "OK", s
    if fn == "no_anchor":
        s = status_of(root, "这段话没有任何锚点。")
        return s == "NO_ANCHOR", s
    if fn == "check_exit":
        mk(root, "e.py", 20)
        rep = os.path.join(root, "rep.md")
        wr(rep, "好锚点 e.py:5\n坏锚点 gone.md:3\n")
        p = subprocess.run([sys.executable, os.path.join(PKG, "scripts", "anchor.py"),
                            "check", rep, "--root", root],
                           capture_output=True, text=True, encoding="utf-8")
        return p.returncode == 1, "退出码 %d" % p.returncode
    if fn == "bad_root":
        rep = os.path.join(root, "rep.md")
        wr(rep, "x.py:1\n")
        p = subprocess.run([sys.executable, os.path.join(PKG, "scripts", "anchor.py"),
                            "check", rep, "--root", os.path.join(root, "nope")],
                           capture_output=True, text=True, encoding="utf-8")
        return p.returncode == 2, "退出码 %d" % p.returncode
    if fn == "lf_only":
        f = os.path.join(PKG, "tests", "golden.json")
        with io.open(f, "rb") as fh:
            b = fh.read()
        return (b"\r\n" not in b), "LF only"
    return False, "未知用例"


def main():
    with io.open(os.path.join(PKG, "tests", "golden.json"), encoding="utf-8") as f:
        cases = json.load(f)["cases"]
    fails = []
    for c in cases:
        root = tempfile.mkdtemp()
        try:
            ok, detail = check(c["fn"], root)
        except Exception as e:  # noqa: BLE001
            ok, detail = False, "异常：" + str(e)
        finally:
            shutil.rmtree(root, ignore_errors=True)
        print("%s  %s  %s  (%s)" % ("PASS" if ok else "FAIL", c["id"], c["desc"], detail))
        if not ok:
            fails.append(c["id"])
    print("\n---- %d/%d PASS ----" % (len(cases) - len(fails), len(cases)))
    if fails:
        print("失败：" + ", ".join(fails))
        sys.exit(1)


if __name__ == "__main__":
    main()
