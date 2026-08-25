#!/usr/bin/env python3
"""Validate a skill's SKILL.md against writing-skills requirements.

Stdlib only (no PyYAML). Checks:
  - Valid frontmatter with name + description
  - name matches the directory name
  - description starts with "Use when" and is <= 160 chars
  - no secrets/tokens (sk-..., ghp_..., gho_..., github_pat...)
  - body length 60-140 lines (warning only)

Usage:
  python3 validate_skill.py skills/<name>/SKILL.md
  python3 validate_skill.py skills/<name>      # appends /SKILL.md
"""
import os
import re
import sys

SECRET_RE = re.compile(
    r'sk-[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}'
)
TRIGGER_RE = re.compile(r'^Use when', re.IGNORECASE)


def load_frontmatter(text):
    if not text.startswith('---'):
        return None, "file does not start with '---' frontmatter"
    end = text.find('\n---', 3)
    if end == -1:
        return None, "unterminated frontmatter"
    block = text[3:end].strip('\n')
    fm = {}
    for line in block.splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, None


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else ''
    if not path:
        print("Usage: validate_skill.py <path-to-SKILL.md-or-dir>", file=sys.stderr)
        sys.exit(2)
    if os.path.isdir(path):
        path = os.path.join(path, 'SKILL.md')
    if not os.path.isfile(path):
        print(f"{path} not found", file=sys.stderr)
        sys.exit(2)

    with open(path, encoding='utf-8') as f:
        text = f.read()

    errors = []
    warnings = []

    fm, err = load_frontmatter(text)
    if err:
        errors.append(err)
    else:
        name = fm.get('name')
        desc = fm.get('description', '')
        if not name:
            errors.append("missing 'name' in frontmatter")
        else:
            dirmatch = os.path.basename(os.path.dirname(os.path.abspath(path)))
            if name != dirmatch:
                errors.append(f"name '{name}' != directory name '{dirmatch}'")
        if not desc:
            errors.append("missing 'description' in frontmatter")
        else:
            if not TRIGGER_RE.match(desc):
                warnings.append("description should start with 'Use when...'")
            if len(desc) > 160:
                warnings.append(f"description is {len(desc)} chars (>160)")

    if SECRET_RE.search(text):
        errors.append("possible secret/token embedded in skill — must not ship")

    # crude line count of the body (excluding frontmatter)
    body = text
    if fm is not None:
        end = text.find('\n---', 3)
        if end != -1:
            body = text[end + 4:]
    body_lines = len([l for l in body.splitlines() if l.strip()])
    if body_lines < 60:
        warnings.append(f"body is {body_lines} lines (<60) — possible under-detailing")
    elif body_lines > 140:
        warnings.append(f"body is {body_lines} lines (>140) — possible bloat")

    print(f"Validating: {path}")
    for w in warnings:
        print(f"  [warn] {w}")
    for e in errors:
        print(f"  [FAIL] {e}")

    if errors:
        print("RESULT: INVALID")
        sys.exit(1)
    print("RESULT: VALID" + (" (with warnings)" if warnings else ""))
    sys.exit(0)


if __name__ == "__main__":
    main()
