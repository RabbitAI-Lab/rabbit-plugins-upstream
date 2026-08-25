#!/usr/bin/env python3
"""taizi-coding: lightweight convention checker for Python source files.

Mirror of the `coding` skill's checker, supporting the same preference-memory
approach (loads ~/coding/memory.md if present). No network, no file writes.

Usage:
    python3 style_lint.py path/to/file.py
    python3 style_lint.py --check-memory        # validate ~/coding/memory.md itself

Checks: trailing whitespace, tab/space indent preference, long lines, trailing
newline, bare except, mutable default args.
"""
import argparse
import os
import re
import sys

VALID_CATEGORIES = {"stack", "style", "structure", "never"}
MEMORY = os.path.expanduser("~/coding/memory.md")
DEFAULTS = {"indent": "spaces", "max_line": 100}


def load_prefs():
    prefs = dict(DEFAULTS)
    if not os.path.exists(MEMORY):
        return prefs
    try:
        with open(MEMORY, encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                low = line.lower()
                if low.startswith("indent:") and "tab" in low:
                    prefs["indent"] = "tabs"
                if low.startswith("line") and "length" in low:
                    m = re.search(r"\d+", low)
                    if m:
                        prefs["max_line"] = int(m.group())
    except OSError as e:
        print(f"[style_lint] WARNING cannot read {MEMORY}: {e}", file=sys.stderr)
    return prefs


def lint_file(path, prefs):
    issues = []
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except OSError as e:
        return [f"cannot read file: {e}"]
    for i, line in enumerate(lines, 1):
        if line.endswith(" \n"):
            issues.append((i, "trailing whitespace"))
        if prefs["indent"] == "spaces" and line.startswith("\t"):
            issues.append((i, "tab used but spaces preferred"))
        if len(line.rstrip("\n")) > prefs["max_line"]:
            issues.append((i, f"line > {prefs['max_line']} chars"))
    text = "".join(lines)
    if re.search(r"except\s*:", text):
        issues.append((0, "bare 'except:' found"))
    if re.search(r"def \w+\([^)]*=\s*\[\s*\]", text):
        issues.append((0, "mutable default argument (list) found"))
    if lines and not lines[-1].endswith("\n"):
        issues.append((len(lines), "no trailing newline at EOF"))
    return issues


def check_memory():
    if not os.path.exists(MEMORY):
        print(f"[check-memory] no memory file at {MEMORY}")
        return 0
    problems = []
    with open(MEMORY, encoding="utf-8") as f:
        for i, raw in enumerate(f, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if len(line.split()) > 5:
                problems.append((i, f"entry has {len(line.split())} words (>5): {line!r}"))
    if problems:
        print("[check-memory] issues:")
        for i, msg in problems:
            print(f"  line {i}: {msg}")
        return 1
    print("[check-memory] OK: all entries <=5 words")
    return 0


def main():
    p = argparse.ArgumentParser(description="taizi-coding style_lint")
    p.add_argument("path", nargs="?", help="python file to lint")
    p.add_argument("--check-memory", action="store_true")
    args = p.parse_args()
    if args.check_memory:
        return check_memory()
    if not args.path:
        p.error("provide a file path or --check-memory")
    prefs = load_prefs()
    issues = lint_file(args.path, prefs)
    if not issues:
        print(f"[style_lint] {args.path}: OK")
        return 0
    print(f"[style_lint] {args.path}: {len(issues)} issue(s)")
    for ln, msg in issues:
        print(f"  {'file' if not ln else 'line '+str(ln)}: {msg}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
