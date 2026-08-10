"""Regression tests for interrupt cleanup and shared branch resolution."""

import json
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

_SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(_SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILL_ROOT))

from scripts import adversarial_loop as loop
from scripts.phases import phase_review, phase_verify
from adversarial_common import RunResult, gitops


def _allow_main_to_reach_pipeline(monkeypatch):
    monkeypatch.setattr(loop, "load_provider_config", lambda _path: None)
    monkeypatch.setattr(loop.gitops, "ensure_git_available", lambda: (True, ""))
    monkeypatch.setattr(loop, "resolve_role_cmd", lambda *_args: "mock-provider")
    monkeypatch.setattr(loop, "_restore", lambda *_args: None)

    def preflight(args, spec_text, _out_dir):
        args._context = {"ok": True, "thresholds": {}}
        args._complexity = {}
        args._preflight_cap_events = []
        return spec_text, True

    monkeypatch.setattr(loop, "_preflight", preflight)


def test_keyboard_interrupt_cleans_active_provider_once_and_state_resumes(
        tmp_path, monkeypatch, capsys):
    spec = tmp_path / "interrupt.md"
    spec.write_text("A detailed interrupt cleanup specification.", encoding="utf-8")
    out_base = tmp_path / "artifacts"
    active_provider = SimpleNamespace(active=True, cleanup_calls=0)
    pipeline_calls = []

    _allow_main_to_reach_pipeline(monkeypatch)

    def terminate_active_provider():
        assert active_provider.active is True
        active_provider.cleanup_calls += 1
        active_provider.active = False

    def pipeline(_args, _dev, _review, _arbiter, _workdir, _feature,
                 _out_dir, state):
        pipeline_calls.append(dict(state))
        if len(pipeline_calls) == 1:
            state.update({
                "branch": "loop/interrupt/1",
                "parent_branch": "main",
                "completed": ["git_setup"],
            })
            raise KeyboardInterrupt
        assert state["phase"] == "interrupted"
        assert state["branch"] == "loop/interrupt/1"
        assert state["completed"] == ["git_setup"]
        return loop.EXIT_APPROVED

    monkeypatch.setattr(
        loop.runner, "terminate_active_processes", terminate_active_provider
    )
    monkeypatch.setattr(loop, "_pipeline", pipeline)

    argv = [
        "--spec", str(spec),
        "--workdir", str(tmp_path),
        "--out", str(out_base),
        "--feature", "interrupt",
    ]
    assert loop.main(argv) == loop.EXIT_INFRA
    interrupt_output = capsys.readouterr().out

    state_path = out_base / "interrupt" / "state.json"
    interrupted_state = json.loads(state_path.read_text(encoding="utf-8"))
    assert active_provider.cleanup_calls == 1
    assert active_provider.active is False
    assert interrupted_state["phase"] == "interrupted"
    assert interrupted_state["branch"] == "loop/interrupt/1"
    assert "done" not in interrupted_state["completed"]
    assert "--resume" in interrupt_output

    assert loop.main([*argv, "--resume"]) == loop.EXIT_APPROVED
    assert len(pipeline_calls) == 2
    assert active_provider.cleanup_calls == 1


def _successful_phase_output(phase):
    if phase == "review":
        return {"findings": [], "verdict": "APPROVE"}
    return {
        "results": [],
        "epistemic_distribution": {
            "confidence": {"high": 0, "medium": 0, "low": 0},
            "basis": {
                "spec": 0, "code": 0, "inference": 0, "external": 0,
            },
        },
        "verdict": "APPROVE",
    }


def _run_phase_and_capture_prompt(module, monkeypatch, workdir):
    prompts = []

    def run_phase_cmd(**kwargs):
        prompts.append(kwargs["stdin_text"])
        payload = _successful_phase_output(kwargs["phase_name"])
        return RunResult((json.dumps(payload), "", 0))

    monkeypatch.setattr(module, "run_phase_cmd", run_phase_cmd)
    if module is phase_review:
        result = module.run_review(
            "diff", "", object(), loop.jsonio, workdir=workdir,
        )
    else:
        result = module.run_verify(
            [], "diff", "", object(), loop.jsonio, workdir=workdir,
        )
    assert result["exit_code"] == 0
    return prompts[0]


@pytest.mark.parametrize("module", [phase_review, phase_verify])
def test_phase_uses_shared_current_branch(module, tmp_path, monkeypatch):
    calls = []

    def get_current_branch(workdir):
        calls.append(workdir)
        return "feature/shared-lookup"

    monkeypatch.setattr(module.gitops, "get_current_branch", get_current_branch)

    prompt = _run_phase_and_capture_prompt(module, monkeypatch, str(tmp_path))

    assert calls == [str(tmp_path)]
    assert "`feature/shared-lookup`" in prompt


@pytest.mark.parametrize("module", [phase_review, phase_verify])
@pytest.mark.parametrize(
    "error",
    [gitops.GitError("detached HEAD"), FileNotFoundError("git not found")],
)
def test_phase_falls_back_for_branch_lookup_failure(
        module, error, tmp_path, monkeypatch):
    def fail_branch_lookup(_workdir):
        raise error

    monkeypatch.setattr(module.gitops, "get_current_branch", fail_branch_lookup)

    prompt = _run_phase_and_capture_prompt(module, monkeypatch, str(tmp_path))

    assert "`(unknown)`" in prompt


def test_branch_lookup_falls_back_on_simulated_timeout(monkeypatch):
    # ponytail: mock only the I/O boundary (subprocess.run) so the REAL
    # get_current_branch runs, proving its TimeoutExpired -> GitError conversion
    # — which is what makes the phase files' `except (GitError, OSError)` sufficient.
    def raise_timeout(*_args, **_kwargs):
        raise subprocess.TimeoutExpired(
            cmd=["git", "symbolic-ref", "--short", "HEAD"], timeout=5,
        )

    monkeypatch.setattr(gitops.subprocess, "run", raise_timeout)

    with pytest.raises(gitops.GitError):
        gitops.get_current_branch(".")
