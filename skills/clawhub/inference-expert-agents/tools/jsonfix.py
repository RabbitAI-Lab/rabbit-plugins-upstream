#!/usr/bin/env python3
"""jsonfix.py — best-effort JSON repair for model outputs (v2.2.0).

Small models emit near-JSON: markdown fences, trailing commas, Python
literals, truncated tails. This tool applies a documented sequence of
small repairs, re-parsing after each, and reports exactly what it did.
If nothing parses it fails cleanly ({"error":...} + exit 2) — never a guess
presented as data.

  python3 jsonfix.py --text '...' | --text-file F | stdin
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import clean_errors


def _try(s):
    try:
        return True, json.loads(s)
    except ValueError:
        return False, None


def _strip_fences(s):
    # Only strip fences that precede the JSON body (never ``` inside strings).
    first = min([p for p in (s.find("{"), s.find("[")) if p >= 0], default=len(s))
    m = re.search(r"```(?:json)?[^\S\n]*\n?(.*)```", s, re.S | re.I)
    if m and m.start() < first:
        return m.group(1)
    m2 = re.search(r"```(?:json)?[^\n]*\n?", s, re.I)  # unclosed fence (truncated output)
    if m2 and m2.start() < first:
        return s[m2.end():]
    return s


def _segments(s):
    """Split into (start, end, in_string) spans via a string-aware scan."""
    spans = []
    start, instr, esc = 0, False, False
    for i, ch in enumerate(s):
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                spans.append((start, i + 1, True))
                start, instr = i + 1, False
        elif ch == '"':
            if i > start:
                spans.append((start, i, False))
            start, instr = i, True
    if start < len(s):
        spans.append((start, len(s), instr))
    return spans


def _outside(s, fn):
    return "".join(s[a:b] if instr else fn(s[a:b]) for a, b, instr in _segments(s))


def _fix_commas(s):
    return _outside(s, lambda x: re.sub(r",(\s*[}\]])", r"\1", x))


def _fix_literals(s):
    def f(x):
        x = re.sub(r"\bNone\b", "null", x)
        x = re.sub(r"\bFalse\b", "false", x)
        return re.sub(r"\bTrue\b", "true", x)
    return _outside(s, f)


def _trim(s):
    i = min([p for p in (s.find("{"), s.find("[")) if p >= 0], default=-1)
    j = max(s.rfind("}"), s.rfind("]"))
    return s[i:j + 1] if 0 <= i <= j else s


def _close(s):
    """Append missing closers with a string-aware stack scan (cap 20)."""
    stack, instr, esc = [], False, False
    pairs = {"{": "}", "[": "]"}
    for ch in s:
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                instr = False
        elif ch == '"':
            instr = True
        elif ch in pairs:
            stack.append(ch)
        elif ch in "}]":
            if stack and pairs[stack[-1]] == ch:
                stack.pop()
    if instr:
        s += '"'
    while stack and len(s) < 200000:
        s += pairs[stack.pop()]
    return s


def repair(raw):
    tried = []
    s = raw
    ok, data = _try(s)
    if ok:
        return True, data, ["already-valid"]
    for name, fn in (
        ("fence-strip", _strip_fences),
        ("prose-trim", _trim),
        ("trailing-commas", _fix_commas),
        ("python-literals", _fix_literals),
        ("close-brackets", _close),
    ):
        s2 = fn(s)
        tried.append(name)
        ok, data = _try(s2)
        if ok:
            return True, data, tried
        s = s2
    return False, None, tried


@clean_errors
def main(argv=None):
    ap = argparse.ArgumentParser(prog="jsonfix.py")
    ap.add_argument("--text")
    ap.add_argument("--text-file")
    a = ap.parse_args(argv)
    if a.text_file:
        raw = open(a.text_file, encoding="utf-8", errors="replace").read()
    elif a.text is not None:
        raw = a.text
    else:
        raw = sys.stdin.read()
    if not raw.strip():
        print(json.dumps({"error": "empty input"}))
        return 2
    ok, data, tried = repair(raw)
    if ok:
        print(json.dumps({"fixed": True, "repairs": tried, "data": data}, indent=2))
        return 0
    print(json.dumps({"error": "unrepairable JSON after: " + ", ".join(tried)}))
    return 2


if __name__ == "__main__":
    sys.exit(main())
