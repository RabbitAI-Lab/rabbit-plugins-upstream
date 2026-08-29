#!/usr/bin/env python3
"""coding: lightweight convention checker for Python source files.

This is a read-only linter. It checks the file the user provides as an
argument against built-in safe defaults and any overrides passed on the
command line. It does not read, write, or keep any state or reference file.

Usage:
    python3 style_lint.py path/to/file.py
    python3 style_lint.py path/to/file.py --max-line 88
    python3 style_lint.py path/to/file.py --indent tabs
"""
import argparse
import re
import sys

DEFAULTS = {"indent": "spaces", "max_line": 100}


def lint_file(path, prefs):
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except OSError as e:
        return [f"cannot read file: {e}"]
    issues = []
    for i, line in enumerate(lines, 1):
        stripped = line.rstrip("\n")
        if stripped != stripped.rstrip() and line.endswith(" \n"):
            issues.append((i, "trailing whitespace"))
        if prefs["indent"] == "spaces" and line.startswith("\t"):
            issues.append((i, "tab used but spaces preferred"))
        if len(stripped) > prefs["max_line"]:
            issues.append((i, f"line > {prefs['max_line']} chars"))
    text = "".join(lines)
    if re.search(r"except\s*:", text):
        issues.append((0, "bare 'except:' found"))
    if re.search(r"def \w+\([^)]*=\s*\[\s*\]", text):
        issues.append((0, "mutable default argument (list) found"))
    if lines and not lines[-1].endswith("\n"):
        issues.append((len(lines), "no trailing newline at EOF"))
    return issues


def main():
    p = argparse.ArgumentParser(description="coding style_lint (convention checker)")
    p.add_argument("path", nargs="?", help="python file to lint")
    p.add_argument("--max-line", type=int, help="override max line length")
    p.add_argument("--indent", choices=["spaces", "tabs"], help="indent style to enforce")
    p.add_argument("--quiet", action="keep_true", help="only print issues")
    args = p.parse_args()

    if not args.path:
        p.error("provide a file path")

    prefs = dict(DEFAULTS)
    if args.max_line:
        prefs["max_line"] = args.max_line
    if args.indent:
        prefs["indent"] = args.indent

    if not args.quiet:
        print(f"[style_lint] prefs: indent={prefs['indent']} max_line={prefs['max_line']}")
    issues = lint_file(args.path, prefs)
    if not issues:
        print(f"[style_lint] {args.path}: OK")
        return 0
    print(f"[style_lint] {args.path}: {len(issues)} issue(s)")
    for ln, msg in issues:
        where = f"line {ln}" if ln else "file"
        print(f"  {where}: {msg}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
