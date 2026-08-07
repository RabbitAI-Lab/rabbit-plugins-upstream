"""P7c — the contract gate blocks APPROVE when an ac-directive fails.

Exercises the F1 contract gate end to end (no LLM): an APPROVE verdict is
downgraded to REQUEST_CHANGES when a directive fails (AC1), and the shared
contract gate is imported from adversarial_common (AC2).
"""
import json
import subprocess
from pathlib import Path

import pytest

import adversarial_review as review


def _source(project_dir):
    return {
        "code_text": "x" * 200,
        "context_text": "x" * 200,
        "context_kind": "input",
        "diff_text": "",
        "project_dir": project_dir,
    }


def _approve_everything(monkeypatch):
    """Make every perspective and cross-review return APPROVE with no findings."""
    payload = {"verdict": "APPROVE", "findings": []}
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    monkeypatch.setattr(
        review, "_run_delegated_perspectives",
        lambda code, args, out, project, complexity: (
            {"architect": text, "inspector": text},
            {"architect": payload, "inspector": payload},
        ),
    )
    monkeypatch.setattr(
        review, "_run_role",
        lambda role, cmd, stdin_text, args, out, name, proj: text,
    )
    return text


def _spec(path, body):
    path.write_text(
        "# Spec\n\n## Acceptance criteria\n\n"
        "- AC1: gateway directive\n"
        "  ```ac-directive\n"
        + body +
        "  ```\n"
    )


def test_failing_ac_blocks_approve(tmp_path, monkeypatch):
    """AC1: a failing ac-directive downgrades an APPROVE to REQUEST_CHANGES."""
    _approve_everything(monkeypatch)
    _spec(tmp_path / "spec.md",
          "  ac: AC1\n  kind: grep\n"
          "  command: grep THIS_TOKEN_IS_ABSENT_EVERYWHERE_ZZZ\n")

    out = tmp_path / "out"
    args = review.parse_args([
        "--file", "x.py", "--out", str(out),
        "--review-cmd", "MOCK", "--spec", str(tmp_path / "spec.md"),
    ])
    review._source_gate(_source(str(tmp_path)), args)
    review.run_adversarial_review(_source(str(tmp_path)), args)

    final = json.loads((out / "final.json").read_text())
    assert final["verdict"] != "APPROVE", final
    assert final["contract"]["settle"] == "REJECT"
    assert final["contract"]["failures"], final["contract"]


def test_passing_ac_keeps_approve(tmp_path, monkeypatch):
    """A passing gate leaves APPROVE intact (regression guard)."""
    _approve_everything(monkeypatch)

    # grep runs over git-tracked files, so set up a real repo with the marker.
    marker = tmp_path / "marker.txt"
    marker.write_text("GATEWAY_TOKEN_PRESENT\n")
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "marker.txt"], cwd=tmp_path, check=True)
    _spec(tmp_path / "spec.md",
          "  ac: AC1\n  kind: grep\n"
          "  command: grep GATEWAY_TOKEN_PRESENT\n")

    out = tmp_path / "out"
    args = review.parse_args([
        "--file", "x.py", "--out", str(out),
        "--review-cmd", "MOCK", "--spec", str(tmp_path / "spec.md"),
    ])
    review._source_gate(_source(str(tmp_path)), args)
    review.run_adversarial_review(_source(str(tmp_path)), args)

    final = json.loads((out / "final.json").read_text())
    assert final["verdict"] == "APPROVE", final
    assert final["contract"]["settle"] == "APPROVE"


def test_no_spec_leaves_verdict_and_schema_untouched(tmp_path, monkeypatch):
    """Without --spec the gate is a no-op and adds nothing to final.json."""
    _approve_everything(monkeypatch)
    out = tmp_path / "out"
    args = review.parse_args([
        "--file", "x.py", "--out", str(out), "--review-cmd", "MOCK",
    ])
    review._source_gate(_source(str(tmp_path)), args)
    review.run_adversarial_review(_source(str(tmp_path)), args)

    final = json.loads((out / "final.json").read_text())
    assert final["verdict"] == "APPROVE"
    assert "contract" not in final


def test_missing_spec_fails_before_providers(tmp_path, monkeypatch):
    """A2: an unreadable --spec fails before any provider phase runs.

    The spec path is validated up front as a review-setup error rather than
    after the five provider calls, so main reports exit 2 (not infra exit 1)
    and does not overwrite provider cost metadata with a zero-call artifact.
    """
    ran = {"perspectives": False}

    def _spy(*_args, **_kw):
        ran["perspectives"] = True
        return {}, {}

    monkeypatch.setattr(review, "_run_delegated_perspectives", _spy)

    out = tmp_path / "out"
    args = review.parse_args([
        "--file", "x.py", "--out", str(out), "--review-cmd", "MOCK",
        "--spec", str(tmp_path / "does_not_exist.md"),
    ])
    review._source_gate(_source(str(tmp_path)), args)
    with pytest.raises(review.ReviewError):
        review.run_adversarial_review(_source(str(tmp_path)), args)
    assert ran["perspectives"] is False


def test_contract_gate_imported_from_adversarial_common():
    """AC2: the review script imports the shared contract gate (R1)."""
    src = Path(review.__file__).read_text()
    assert "from adversarial_common import" in src
    assert "run_contract_gate" in src
