#!/usr/bin/env python3
"""Package self-test for release readiness (added v2.9).

Run BEFORE publishing a new version to ClawHub. Verifies the skill folder is
complete and self-consistent:

    python3 tools/package_selftest.py [path]

Exits 0 only when every check passes. Mirrors the practice used by
persian-pdf-studyguide-forge so releases never ship broken.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REQUIRED = [
    "SKILL.md", "README.md", "CHANGELOG.md", "LICENSE", "config.yaml",
    "requirements.txt", "Dockerfile", "docker-compose.yml", "install.sh",
    "scripts/self_test.py", "scripts/preflight.py",
    "src/crawler/httrack_engine.py",
    "src/crawler/woo_rest_engine.py",
    "src/crawler/free_access_engine.py",
    "src/crawler/http_fetch_engine.py",
    "src/parser/product_extractor.py",
    "src/discovery/seed_list.py",
    "src/tasks/crawl_tasks.py",
    "docs/architecture.md",
    "tests/test_free_access_engine.py",
    "tests/test_http_fetch_engine.py",
]


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures: list = []

    missing = [f for f in REQUIRED if not (root / f).is_file()]
    if missing:
        failures.append("missing files: " + ", ".join(missing))

    skill = (root / "SKILL.md").read_text("utf-8")
    for token in ("name: iran-chem-database", "version:", "categories:", "topics:", "requires:"):
        if token not in skill:
            failures.append(f"SKILL.md frontmatter missing: {token}")

    # version string present but not a placeholder
    import re
    m = re.search(r"^version:\s*([0-9.]+)\s*$", skill, re.M)
    if not m:
        failures.append("SKILL.md version not found")
    else:
        print(f"version: {m.group(1)}")

    # run the full self-test (compiles + imports + offline pytest)
    r = subprocess.run([sys.executable, str(root / "scripts" / "self_test.py")],
                       capture_output=True, text=True, timeout=400)
    print(r.stdout)
    if r.returncode != 0:
        failures.append(f"scripts/self_test.py failed (exit {r.returncode})")

    if failures:
        print("FAIL:\n- " + "\n- ".join(failures))
        return 1
    print("package selftest: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
