#!/usr/bin/env python3
"""Search the bundled Datawhale source-link catalog without network access."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def tokens(query: str) -> list[str]:
    values = [query.strip().lower()]
    values += re.findall(r"[a-z][a-z0-9_.+-]*|[\u4e00-\u9fff]{2,}", query.lower())
    return list(dict.fromkeys(value for value in values if value))


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: search_sources.py "<question or keywords>"', file=sys.stderr)
        return 2

    catalog = Path(__file__).resolve().parents[1] / "references" / "source-catalog.md"
    needles = tokens(" ".join(sys.argv[1:]))
    results: list[tuple[int, str]] = []

    for line in catalog.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- ["):
            continue
        lower = line.lower()
        score = sum(8 if needle == needles[0] and needle in lower else lower.count(needle) for needle in needles)
        if score:
            results.append((score, line[2:]))

    for _, line in sorted(results, reverse=True)[:12]:
        print(line)
    if not results:
        print("No exact catalog match. Try a broader Chinese or English concept name.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
