#!/usr/bin/env python3
"""轻量静态审查清单：密钥/超长函数/裸except/TODO 等模式预检（不替代语义审查）。"""
import argparse, json, os, re, sys


KEY_RE = re.compile(r"(?i)(api[_-]?key|secret|token|password|passwd)\s*[:=]\s*['\"][^'\"]{6,}")
TODO_RE = re.compile(r"(?i)\b(TODO|FIXME|XXX|HACK)\b")
EXCEPT_RE = re.compile(r"except\s*:")
LONG_FN = 60  # 函数行数阈值


def check(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        src = f.read()
    lines = src.splitlines()
    issues = []
    # 密钥硬编码
    for i, ln in enumerate(lines, 1):
        if KEY_RE.search(ln):
            issues.append({"sev": "blocker", "line": i, "kind": "hardcoded_secret",
                           "msg": "疑似硬编码密钥/令牌（请改用环境变量）"})
        if TODO_RE.search(ln):
            issues.append({"sev": "minor", "line": i, "kind": "todo",
                           "msg": "TODO/FIXME 待办标记"})
        if EXCEPT_RE.search(ln):
            issues.append({"sev": "major", "line": i, "kind": "bare_except",
                           "msg": "裸 except（应捕获具体异常）"})
    # 超长函数（按 def 行数粗算）
    fn_start = None
    for i, ln in enumerate(lines, 1):
        if re.match(r"\s*def\s+\w+\s*\(", ln):
            if fn_start and (i - fn_start) > LONG_FN:
                issues.append({"sev": "minor", "line": fn_start, "kind": "long_fn",
                               "msg": f"函数过长（约 {i-fn_start} 行）"})
            fn_start = i
    if fn_start and (len(lines) - fn_start) > LONG_FN:
        issues.append({"sev": "minor", "line": fn_start, "kind": "long_fn",
                       "msg": f"函数过长（约 {len(lines)-fn_start} 行）"})
    return {"path": path, "lines": len(lines), "issues": issues,
            "blocker": sum(1 for x in issues if x["sev"] == "blocker"),
            "major": sum(1 for x in issues if x["sev"] == "major")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    r = check(args.path)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(f"文件：{r['path']}（{r['lines']} 行）")
        print(f"Blocker={r['blocker']} Major={r['major']} 总问题={len(r['issues'])}")
        for x in r["issues"]:
            print(f"  [{x['sev']}] L{x['line']} {x['kind']}: {x['msg']}")


if __name__ == "__main__":
    main()
