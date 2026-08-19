#!/usr/bin/env python3
"""Generate a GitHub-style table of contents from Markdown headers."""
import re
import sys


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text


def gen_toc(path: str) -> str:
    lines = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            m = re.match(r"^(#{1,6})\s+(.*)$", raw.rstrip("\n"))
            if not m:
                continue
            level = len(m.group(1)) - 1
            title = m.group(2).strip()
            indent = "  " * level
            lines.append(f"{indent}- [{title}](#{slugify(title)})")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gen_toc.py <path/to/file.md>", file=sys.stderr)
        sys.exit(2)
    out = gen_toc(sys.argv[1])
    print(out)
