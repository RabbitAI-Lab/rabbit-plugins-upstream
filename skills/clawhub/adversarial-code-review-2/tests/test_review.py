"""Cross-review round-2 label reflects the perspective that actually ran.

Exercises the delegated-mode code path end to end (no LLM) and asserts that the
round-2 cross-review input describes the delegated synthesis rather than falsely
claiming an "ARCHITECT REVIEW" that never ran (finding CR6).
"""
import json

import pytest

import adversarial_review as review


def _source():
    return {
        "code_text": "x" * 200,
        "context_text": "x" * 200,
        "context_kind": "input",
        "diff_text": "",
        "project_dir": None,
    }


def test_delegated_mode_cross2_label_says_delegated_not_architect(
    tmp_path, monkeypatch,
):
    payload = {"verdict": "APPROVE", "findings": []}
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)

    # Run the delegated path: perspectives return only the "delegated" key,
    # which is what makes round 2 a cross-review of the delegated synthesis.
    monkeypatch.setattr(
        review, "_run_delegated_perspectives",
        lambda code, args, out, project, complexity: (
            {"delegated": text}, {"delegated": payload},
        ),
    )

    captured = {}

    def fake_run_role(role, cmd, stdin_text, args, out, name, proj):
        captured[name] = stdin_text
        return text

    monkeypatch.setattr(review, "_run_role", fake_run_role)

    out = tmp_path / "out"
    args = review.parse_args([
        "--file", "x.py", "--out", str(out),
        "--review-cmd", "MOCK",
    ])
    review._source_gate(_source(), args)
    review.run_adversarial_review(_source(), args)

    cross2_input = captured["04_cross_2"]
    assert "DELEGATED REVIEW" in cross2_input
    assert "ARCHITECT REVIEW" not in cross2_input
    assert "Architect's findings" not in cross2_input


def test_direct_mode_cross2_label_still_says_architect(tmp_path, monkeypatch):
    """AC2: non-delegated cross-review keeps the ARCHITECT REVIEW label."""
    payload = {"verdict": "APPROVE", "findings": []}
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)

    monkeypatch.setattr(
        review, "_run_delegated_perspectives",
        lambda code, args, out, project, complexity: (
            {"architect": text, "inspector": text},
            {"architect": payload, "inspector": payload},
        ),
    )

    captured = {}

    def fake_run_role(role, cmd, stdin_text, args, out, name, proj):
        captured[name] = stdin_text
        return text

    monkeypatch.setattr(review, "_run_role", fake_run_role)

    out = tmp_path / "out"
    args = review.parse_args([
        "--file", "x.py", "--out", str(out),
        "--review-cmd", "MOCK",
    ])
    review._source_gate(_source(), args)
    review.run_adversarial_review(_source(), args)

    cross2_input = captured["04_cross_2"]
    assert "=== ARCHITECT REVIEW TO CROSS-REVIEW ===" in cross2_input
    assert "Cross-review the Architect's findings" in cross2_input
