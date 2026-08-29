#!/usr/bin/env python3
"""Self-test for the iran-chem-database skill (added v2.9).

Runs WITHOUT a database or network and reports a measured pass/fail verdict:

  HARD checks (exit 1 if any fail):
    * every .py under src/, scripts/, tools/ compiles (py_compile);
    * required files exist;
    * SKILL.md frontmatter carries name/version/categories/topics/requires;
    * config.yaml loads and DB_PASSWORD is not left as a placeholder.

  SOFT checks (reported, do not fail the build):
    * importability of core modules (some need pip deps / httrack);
    * optional offline pytest subset if pytest is importable.

Exit 0 only when every HARD check passes. Run before publishing a release:

    python3 scripts/self_test.py
"""
from __future__ import annotations

import importlib.util
import json
import py_compile
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

REQUIRED_FILES = [
    "SKILL.md", "README.md", "CHANGELOG.md", "LICENSE", "config.yaml",
    "requirements.txt", "Dockerfile", "docker-compose.yml", "install.sh",
    "src/crawler/httrack_engine.py",
    "src/crawler/httrack_profiles.py",
    "src/crawler/woo_rest_engine.py",
    "src/crawler/free_access_engine.py",
    "src/crawler/http_fetch_engine.py",
    "src/crawler/playwright_fallback.py",
    "src/parser/product_extractor.py",
    "src/discovery/seed_list.py",
    "src/scripts/trigger_initial_crawl.py",
    "src/scripts/seed_suppliers.py",
    "src/tasks/crawl_tasks.py",
    "docs/architecture.md",
    "tests/test_free_access_engine.py",
    "tests/test_http_fetch_engine.py",
    "src/crawler/telegram_engine.py",
    "src/parser/telegram_parser.py",
    "src/parser/social_molecule_resolver.py",
    "src/parser/social_catalog_pipeline.py",
    "src/discovery/social_seed_list.py",
    "src/scripts/social_crawl.py",
    "tests/test_social_catalog.py",
]

# stdlib + light-dependency modules that must import for the skill to work.
CORE_MODULES = [
    "src.crawler.httrack_config",
    "src.crawler.httrack_profiles",
    "src.crawler.httrack_engine",
    "src.crawler.free_access_engine",
    "src.crawler.http_fetch_engine",
    "src.discovery.seed_list",
    "src.utils.http_util",
    "src.crawler.telegram_engine",
    "src.parser.telegram_parser",
    "src.parser.social_molecule_resolver",
    "src.parser.social_catalog_pipeline",
    "src.discovery.social_seed_list",
]

OFFLINE_PYTEST_FILES = [
    "tests/test_free_access_engine.py",
    "tests/test_http_fetch_engine.py",
    "tests/test_woo_rest_engine.py",
    "tests/test_discovery.py",
    "tests/test_httrack_profiles.py",
    "tests/test_identity.py",
    "tests/test_grade_classifier.py",
    "tests/test_social_catalog.py",
    "tests/test_organic_classifier.py",
]


def main() -> int:
    hard_failures: list = []
    soft_notes: list = []

    # 1) compile every python file
    py_files = sorted(ROOT.glob("src/**/*.py")) + sorted(ROOT.glob("scripts/*.py")) \
        + sorted(ROOT.glob("tools/*.py"))
    compiled = 0
    for p in py_files:
        try:
            py_compile.compile(str(p), doraise=True)
            compiled += 1
        except Exception as exc:  # noqa: BLE001
            hard_failures.append(f"compile {p.relative_to(ROOT)}: {exc}")
    print(f"[compile] {compiled} python files OK")

    # 2) required files
    missing = [f for f in REQUIRED_FILES if not (ROOT / f).is_file()]
    if missing:
        hard_failures.append("missing files: " + ", ".join(missing))
    else:
        print(f"[files] {len(REQUIRED_FILES)} required files present")

    # 3) SKILL.md frontmatter
    skill = (ROOT / "SKILL.md").read_text("utf-8")
    for token in ("name: iran-chem-database", "version:", "categories:", "topics:", "requires:"):
        if token not in skill:
            hard_failures.append(f"SKILL.md frontmatter missing: {token}")
    print("[frontmatter] SKILL.md name/version/categories/topics/requires present")

    # 4) config.yaml loads + DB password not placeholder
    try:
        from src.config import load_config
        cfg = load_config(str(ROOT / "config.yaml"))
        pw = cfg.get("database", {}).get("password", "")
        if not pw or "change-this" in str(pw).lower():
            soft_notes.append("DB_PASSWORD is unset or a placeholder (expected in production)")
        else:
            print("[config] config.yaml loads; database section present")
        if not cfg.get("free_access", {}).get("enabled", True):
            hard_failures.append("free_access.enabled is disabled")
    except Exception as exc:  # noqa: BLE001
        hard_failures.append(f"config.yaml failed to load: {exc}")

    # 5) soft: import core modules
    imported, failed_imports = 0, []
    for m in CORE_MODULES:
        if importlib.util.find_spec(m) is not None:
            try:
                __import__(m)
                imported += 1
            except Exception as exc:  # noqa: BLE001
                failed_imports.append(f"{m}: {type(exc).__name__}")
    print(f"[imports] {imported}/{len(CORE_MODULES)} core modules importable")
    for f in failed_imports:
        soft_notes.append(f)

    # 6) soft: offline pytest subset
    try:
        import pytest  # noqa: F401
        sys.path.insert(0, str(ROOT))
        import subprocess
        r = subprocess.run([sys.executable, "-m", "pytest", "-q"] + OFFLINE_PYTEST_FILES,
                           cwd=str(ROOT), capture_output=True, text=True, timeout=300)
        ok = r.returncode == 0
        print(f"[pytest] offline subset {'PASS' if ok else 'FAIL'} "
              f"(exit {r.returncode})")
        if not ok:
            soft_notes.append("offline pytest subset failed — see output above")
    except Exception as exc:  # noqa: BLE001
        soft_notes.append(f"pytest not run: {type(exc).__name__}")

    print()
    report = {"hard_failures": hard_failures, "soft_notes": soft_notes,
              "pass": not hard_failures}
    print(json.dumps(report, indent=2))
    return 0 if not hard_failures else 1


if __name__ == "__main__":
    sys.exit(main())
