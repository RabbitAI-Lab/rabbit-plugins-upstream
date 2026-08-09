"""Integration tests for P11 optional code-review modes."""

import json
from types import SimpleNamespace

import pytest

import adversarial_review as review


def _finding(severity="minor", **extra):
    value = {
        "id": "F1",
        "severity": severity,
        "file": "x.py",
        "line": 1,
        "summary": "unsafe <script>alert(1)</script>",
        "evidence": "value < expected & unchecked",
        "confidence": "high",
        "basis": "code",
    }
    value.update(extra)
    return value


def test_html_is_rendered_after_final_and_escapes_model_content(tmp_path):
    args = SimpleNamespace(
        out=str(tmp_path),
        html=True,
        ci=False,
    )

    final_path = review._write_final(
        args,
        "REQUEST_CHANGES",
        status="complete",
        finding_details=[_finding()],
        findings={"minor": 1},
        costs={"total": {"est_cost_usd": 0}},
    )

    payload = json.loads(final_path.read_text())
    report_path = tmp_path / "report.html"
    assert payload["html_report"] == str(report_path)
    output = report_path.read_text()
    assert "<script>alert(1)</script>" not in output
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in output
    assert "value &lt; expected &amp; unchecked" in output


@pytest.mark.parametrize(
    ("verdict", "findings", "selector", "extra", "expected"),
    [
        ("APPROVE", [], None, {}, 0),
        ("REQUEST_CHANGES", [_finding("major")], None, {}, 2),
        ("APPROVE", [_finding("minor")], None, {}, 3),
        ("REQUEST_CHANGES", [_finding("major")], "none", {}, 0),
        ("ERROR", [], None, {"infrastructure": True}, 1),
        ("CONTEXT_BLOCKED", [], None, {"context_blocked": True}, 5),
    ],
)
def test_ci_exit_codes_follow_shared_policy(
    tmp_path, verdict, findings, selector, extra, expected,
):
    out = tmp_path / f"case-{expected}-{selector or 'default'}-{verdict}"
    args = SimpleNamespace(
        out=str(out),
        html=False,
        ci=True,
        fail_on=selector,
    )
    review._write_final(
        args,
        verdict,
        finding_details=findings,
        **extra,
    )

    assert review.pipeline_base.ci_exit_from_final(
        args.out,
        review.EXIT_OK,
        fail_on_selector=args.fail_on,
    ) == expected


def test_ci_main_keeps_stdout_silent_and_strips_ansi(tmp_path, monkeypatch, capsys):
    source = {
        "code_text": "x" * 40,
        "context_text": "x" * 40,
        "context_kind": "input",
        "diff_text": "",
        "project_dir": None,
    }
    monkeypatch.setattr(review, "build_file_source", lambda path: source)

    def fake_review(_source, args, context=None):
        print("\x1b[32mhuman progress\x1b[0m")
        review._write_final(
            args,
            "APPROVE",
            status="complete",
            finding_details=[],
        )
        return review.EXIT_OK

    monkeypatch.setattr(review, "_review_source", fake_review)

    code = review.main([
        "--file", "x.py", "--ci", "--out", str(tmp_path / "out"),
    ])

    captured = capsys.readouterr()
    assert code == 0
    assert captured.out == ""
    assert "human progress" in captured.err
    assert "\x1b[" not in captured.err


@pytest.mark.parametrize("ci", [False, True])
def test_main_preserves_nothing_to_review_without_error_artifact(
    tmp_path, monkeypatch, ci,
):
    monkeypatch.setattr(
        review,
        "build_file_source",
        lambda path: (_ for _ in ()).throw(review.ReviewError("empty diff")),
    )
    out = tmp_path / ("ci" if ci else "legacy")
    argv = ["--file", "x.py", "--out", str(out)]
    if ci:
        argv.append("--ci")

    code = review.main(argv)

    assert code == review.EXIT_NOTHING
    assert not (out / "final.json").exists()


def test_ci_main_preserves_diff_git_nothing_to_review(tmp_path, monkeypatch):
    monkeypatch.setattr(
        review, "run_diff_git", lambda args: review.EXIT_NOTHING,
    )

    code = review.main([
        "--diff-git", "--ci", "--out", str(tmp_path),
    ])

    assert code == review.EXIT_NOTHING
    assert not (tmp_path / "final.json").exists()


def test_main_prints_traceback_and_writes_artifact_for_unexpected_error(
    tmp_path, monkeypatch, capsys,
):
    monkeypatch.setattr(
        review,
        "build_file_source",
        lambda path: (_ for _ in ()).throw(TypeError("unexpected bug")),
    )

    code = review.main(["--file", "x.py", "--out", str(tmp_path)])

    assert code == review.EXIT_INFRA
    captured = capsys.readouterr()
    assert "Traceback (most recent call last)" in captured.err
    assert "TypeError: unexpected bug" in captured.err
    final = json.loads((tmp_path / "final.json").read_text())
    assert final["infrastructure"] is True


def test_severity_counts_deduplicates_ids_but_counts_idless_findings():
    findings = [
        {"id": "R1", "severity": "major"},
        {"id": "R1", "severity": "major"},
        {"severity": "minor"},
        {"severity": "minor"},
    ]

    assert review._severity_counts(json.dumps({"findings": findings})) == {
        "major": 1,
        "minor": 2,
    }


@pytest.mark.parametrize("enabled", [False, True])
def test_research_enabled_and_disabled(
    tmp_path, monkeypatch, enabled,
):
    args_list = [
        "--file", "x.py",
        "--out", str(tmp_path / ("enabled" if enabled else "disabled")),
    ]
    if enabled:
        args_list.append("--deep-research")
    args = review.parse_args(args_list)
    args.review_cmd = args.a_cmd = args.b_cmd = args.synth_cmd = "provider"
    source = {
        "code_text": "x" * 40,
        "context_text": "x" * 40,
        "context_kind": "input",
        "diff_text": "",
        "project_dir": None,
    }
    reviewer = {"verdict": "APPROVE", "findings": []}
    calls = []

    def fake_research(*positional, **kwargs):
        calls.append((positional, kwargs))
        return {
            "enabled": True,
            "status": "complete",
            "findings": [{
                "id": "R1",
                "severity": "minor",
                "evidence": "upstream documentation",
            }],
            "calls": [],
            "warnings": [],
        }

    def fake_perspectives(code, run_args, out, project, complexity):
        run_args._review_payloads = {
            "architect": reviewer,
            "inspector": reviewer,
        }
        text = json.dumps(reviewer)
        return {"architect": text, "inspector": text}, run_args._review_payloads

    monkeypatch.setattr(review.runner, "run_research", fake_research)
    monkeypatch.setattr(review, "_run_delegated_perspectives", fake_perspectives)
    monkeypatch.setattr(
        review,
        "_run_role",
        lambda role, cmd, stdin_text, run_args, out, name, project: "synthesis",
    )

    review.run_adversarial_review(source, args)

    final_path = (
        tmp_path / ("enabled" if enabled else "disabled") / "final.json"
    )
    final = json.loads(final_path.read_text())
    if enabled:
        assert len(calls) == 1
        assert final["research"]["result_count"] == 1
        evidence = next(
            finding for finding in final["finding_details"]
            if finding.get("id") == "R1"
        )
        assert evidence["basis"] == "external"
        assert evidence["origin"] == "research"
        assert evidence["confidence"] == "low"
    else:
        assert calls == []
        assert "research" not in final


def test_delegation_below_high_never_starts_delegated_runner(monkeypatch, tmp_path):
    args = SimpleNamespace(delegated=True, _warnings=[])
    sentinel = ({"architect": "direct"}, {"architect": {}})
    monkeypatch.setattr(
        review,
        "_run_initial_perspectives",
        lambda *values: sentinel,
    )
    monkeypatch.setattr(
        review.runner,
        "run_delegated",
        lambda *args, **kwargs: pytest.fail("delegated runner must not start"),
    )
    complexity = {"level": "medium", "recommended_agents": 4}

    result = review._run_delegated_perspectives(
        "code", args, tmp_path, None, complexity,
    )

    assert result == sentinel
    assert args._delegated["delegated"] is False
    assert "below required level 'high'" in args._delegated["reason"]


@pytest.mark.parametrize(
    ("role", "phase"),
    [
        ("orchestrator", "delegated_decomposition"),
        ("inspector", "delegated_worker"),
        ("inspector", "delegated_synthesis"),
    ],
)
def test_delegated_stage_calls_keep_project_working_directory(
    role, phase, tmp_path,
):
    project = tmp_path / "project"
    project.mkdir()
    args = review.parse_args(["--file", "x.py", "--delegated"])
    args._ledger = review.CostLedger()

    call = review._delegated_stage_call(
        role, "provider", "input", args, str(project), phase,
    )

    assert call["cwd"] == str(project.resolve())


def test_high_complexity_delegation_preserves_worker_origin(
    monkeypatch, tmp_path,
):
    args = review.parse_args(["--file", "x.py", "--delegated"])
    args.orchestrator_cmd = args.worker_cmd = args.synth_cmd = "provider"
    args._ledger = review.CostLedger()
    args._calls = []
    args._artifacts = {}
    args._warnings = []
    args._review_payloads = {}
    payload = {
        "verdict": "REQUEST_CHANGES",
        "findings": [_finding("major", origin=None)],
    }

    monkeypatch.setattr(review.runner, "run_delegated", lambda *args, **kwargs: {
        "delegated": True,
        "status": "synthesized",
        "reason": "synthesized surviving workers after partial failure",
        "partial": True,
        "decomposition": None,
        "workers": [],
        "synthesis": {
            "payload": payload,
            "stdout": json.dumps(payload),
        },
    })

    texts, payloads = review._run_delegated_perspectives(
        "large code",
        args,
        tmp_path,
        None,
        {"level": "high", "recommended_agents": 6},
    )

    assert "delegated" in texts
    assert payloads["delegated"]["findings"][0]["origin"] == "worker"
    assert any(
        warning["code"] == "delegated_partial_failure"
        for warning in args._warnings
    )
