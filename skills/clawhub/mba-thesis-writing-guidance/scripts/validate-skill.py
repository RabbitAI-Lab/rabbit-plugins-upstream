#!/usr/bin/env python3
"""Check this repo can be installed with: npx skills add <owner/repo>"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
skill = ROOT / "SKILL.md"
errors = []

if not skill.is_file():
    errors.append("missing SKILL.md at repository root (npx skills add looks here first)")
else:
    text = skill.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        errors.append("SKILL.md must start with YAML frontmatter between --- markers")
    else:
        fm = m.group(1)
        name = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
        desc = re.search(r"^description:\s*", fm, re.M)
        if not name:
            errors.append("frontmatter missing name")
        elif name.group(1) != "mba-thesis-writing-guidance":
            errors.append(f"name must be mba-thesis-writing-guidance, got {name.group(1)}")
        else:
            n = name.group(1)
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", n):
                errors.append("name must be 1–64 chars: lowercase letters, numbers, hyphens")
        if not desc:
            errors.append("frontmatter missing description")

for rel in ("references", "workflows", "templates", "checklists", "examples", "assets"):
    if not (ROOT / rel).exists():
        errors.append(f"missing {rel}/ (npx skills add copies the whole skill folder)")

if errors:
    print("skill validation failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print("ok: root SKILL.md is valid; npx skills add <owner/repo> can discover this skill")
