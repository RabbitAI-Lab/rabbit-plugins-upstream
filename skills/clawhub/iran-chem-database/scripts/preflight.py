#!/usr/bin/env python3
"""Preflight environment check (added v2.9).

Reports the environment readiness for a crawl before starting it:

  * required binary: httrack (primary mirror);
  * fallback binaries: curl, wget (optional — the skill degrades gracefully);
  * python version (>= 3.11 required);
  * optional python packages (soft — the skill works without the heavy ones);
  * config.yaml loads.

Exit 0 when the minimal contract is met (python + config); missing binaries
are reported with install hints. This mirrors the same idea as the
persian-pdf-studyguide-forge preflight.
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

OPTIONAL_MODULES = {
    "sqlalchemy": "PostgreSQL persistence",
    "bs4": "HTML parsing",
    "fitz": "PDF parsing (PyMuPDF)",
    "PIL": "image handling",
    "celery": "task queue",
    "yaml": "config parsing (required)",
    "rdkit": "structure validation (optional)",
}


def main() -> int:
    report = {
        "python": f"{sys.version_info.major}.{sys.version_info.minor}",
        "binaries": {},
        "modules": {},
        "config_ok": False,
    }

    for b in ("httrack", "curl", "wget", "python3"):
        report["binaries"][b] = shutil.which(b)

    for m, _ in OPTIONAL_MODULES.items():
        report["modules"][m] = importlib.util.find_spec(m) is not None

    try:
        from src.config import load_config
        load_config(str(ROOT / "config.yaml"))
        report["config_ok"] = True
    except Exception as exc:  # noqa: BLE001
        report["config_ok"] = f"error: {type(exc).__name__}"

    report["ready_minimal"] = bool(report["binaries"]["python3"]) and report["config_ok"] is True
    report["httrack_present"] = bool(report["binaries"]["httrack"])
    report["install_hints"] = {
        "debian": "sudo apt install httrack curl wget",
        "python": "pip install -r requirements.txt",
    }
    print(json.dumps(report, indent=2))
    return 0 if report["ready_minimal"] else 1


if __name__ == "__main__":
    sys.exit(main())
