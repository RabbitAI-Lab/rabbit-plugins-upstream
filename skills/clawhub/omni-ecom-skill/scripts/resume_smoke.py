#!/usr/bin/env python3
"""Smoke-test safe continuation states without fabricating member evidence."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = ROOT / "scripts" / "team_bootstrap_guard.py"
RESUME = ROOT / "scripts" / "collaboration_resume_guard.py"
AGENTS = ("data-analyst", "platform-ops", "content-live-growth", "ad-profit-optimizer")


def run(command: list[str], expected: int | None = None) -> tuple[int, dict]:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", env={**__import__("os").environ, "PYTHONUTF8": "1"})
    payload = json.loads(result.stdout or "{}")
    if expected is not None and result.returncode != expected:
        raise AssertionError(f"unexpected exit {result.returncode}: {result.stdout}{result.stderr}")
    return result.returncode, payload


def write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="omni-ecom-resume-") as temp:
        run_dir = Path(temp) / "run-r159"
        run_dir.mkdir(parents=True)
        _, missing = run([sys.executable, str(RESUME), "--run-dir", str(run_dir), "--run-id", "run-r159", "--team-version", "1.5.10"], expected=2)
        assert missing["reason"] == "team_bootstrap_missing"

        run([sys.executable, str(BOOTSTRAP), "record", "--run-dir", str(run_dir), "--run-id", "run-r159", "--team-version", "1.5.10", "--team-name", "omni-ecom-resume-smoke", "--host-mode", "interactive"])
        returns_dir = run_dir / "agent_returns" / "run-r159"
        write(returns_dir / "data-analyst-a1.return.json", {"run_id": "run-r159", "agent_id": "data-analyst", "attempt_id": "data-analyst-a1", "return_status": "completed"})
        _, waiting = run([sys.executable, str(RESUME), "--run-dir", str(run_dir), "--run-id", "run-r159", "--team-version", "1.5.10"], expected=2)
        assert waiting["phase"] == "member_returns_pending"

        for agent_id in AGENTS:
            attempt = f"{agent_id}-a1"
            write(returns_dir / f"{attempt}.return.json", {"run_id": "run-r159", "agent_id": agent_id, "attempt_id": attempt, "return_status": "completed"})
            write(run_dir / "sealed-handoffs" / f"handoff-{attempt}.sealed.json", {"run_id": "run-r159", "agent_id": agent_id})
        _, report_ready = run([sys.executable, str(RESUME), "--run-dir", str(run_dir), "--run-id", "run-r159", "--team-version", "1.5.10"])
        assert report_ready["phase"] == "report_pending"

        write(run_dir / "report" / "report.json", {"status": "awaiting_delivery_review"})
        (run_dir / "report" / "report.pdf").write_bytes(b"pdf")
        write(run_dir / "report" / "pdf-delivery.json", {"status": "pdf_render_verified"})
        write(run_dir / "review-manifest.json", {"status": "review_manifest_prepared"})
        _, review = run([sys.executable, str(RESUME), "--run-dir", str(run_dir), "--run-id", "run-r159", "--team-version", "1.5.10"])
        assert review["phase"] == "review_pending"

        write(run_dir / "completion-receipt.json", {"status": "formal_delivery_complete"})
        _, complete = run([sys.executable, str(RESUME), "--run-dir", str(run_dir), "--run-id", "run-r159", "--team-version", "1.5.10"])
        assert complete["phase"] == "complete"

    print(json.dumps({"status": "PASS", "checks": 5, "phases": ["team_bootstrap_missing", "member_returns_pending", "report_pending", "review_pending", "complete"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
