"""P17 — invoke the integration gate (P15) after squash-merge, before
declaring APPROVED.

``--integration-gate-manifest`` opts a run into the gate (unset — the
default — skips it entirely, so ordinary single-project loop usage is
unaffected). When set, the loop calls ``run_integration_gate`` from the
payload builder, which ``finish_pipeline`` invokes strictly after
``finalize_callback`` has already performed the squash-merge (R1).

AC1 — test_loop_invokes_integration_gate: all manifest repos green -> the
gate runs, passes, and the loop still APPROVEs with the result recorded in
final.json.
AC2 — test_loop_rejects_on_gate_failure: one manifest repo fails its
test_cmd -> the loop exits EXIT_INFRA (not a plain REJECT/blocking code),
with the failing gate recorded in final.json.

These are end-to-end subprocess tests: they run the real v4 orchestrator
against a throwaway git repo with the bash suite's mock DEV/REVIEW commands,
exercising the wiring exactly as a real run would.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

_SKILL_ROOT = Path(__file__).resolve().parents[1]
_LOOP = _SKILL_ROOT / "scripts" / "adversarial_loop_v4.py"
_MOCKS = _SKILL_ROOT / "tests" / "mocks"

# No ac-directive block, so the F1 contract gate settles APPROVE vacuously
# (P8) and cannot interfere with what this test is isolating.
_SPEC = """\
# add a function

## Acceptance criteria

- AC1: implement answer()
"""


def _env():
    return {k: v for k, v in os.environ.items()
            if k in ("PATH", "HOME", "LANG", "LC_ALL")}


def _write_manifest(tmp_path: Path, entries: list) -> Path:
    lines = []
    for entry in entries:
        lines.append(f"- name: {entry['name']}")
        lines.append(f"  path: {entry['name']}")
        lines.append(f"  test_cmd: {entry['test_cmd']}")
    manifest = tmp_path / "manifest.yaml"
    manifest.write_text("\n".join(lines) + "\n")
    return manifest


def _make_workspace(tmp_path: Path, statuses: dict) -> Path:
    """Build a workspace dir with one subdir per {name: test_cmd} entry."""
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    for name in statuses:
        (workspace / name).mkdir()
    return workspace


def _run_loop(tmp_path: Path, manifest: Path, workspace: Path) -> tuple[int, Path]:
    workdir = tmp_path / "repo"
    workdir.mkdir()
    env = {
        "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t.co",
        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t.co",
    }
    subprocess.run(["git", "init", "-q"], cwd=workdir, check=True)
    subprocess.run(["git", "config", "user.email", "a@b.c"], cwd=workdir, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=workdir, check=True)
    subprocess.run(
        ["git", "commit", "-q", "--allow-empty", "-m", "init"],
        cwd=workdir, check=True, env={**_env(), **env},
    )

    spec = tmp_path / "spec.md"
    spec.write_text(_SPEC)

    proc = subprocess.run(
        [sys.executable, str(_LOOP),
         "--spec", str(spec), "--workdir", str(workdir),
         "--feature", "igtest", "--no-merge", "--max-loops", "1",
         "--dev-cmd", str(_MOCKS / "mock_dev.sh"),
         "--review-cmd", str(_MOCKS / "mock_review.sh"),
         "--integration-gate-manifest", str(manifest),
         "--integration-gate-workspace", str(workspace)],
        capture_output=True, text=True,
    )
    out_dir = workdir / ".adversarial-loop" / "igtest"
    assert out_dir.exists(), f"no artifacts dir\n{proc.stdout}\n{proc.stderr}"
    return proc.returncode, out_dir


def _final(out_dir: Path) -> dict:
    return json.loads((out_dir / "final.json").read_text())


# AC1: a clean gate does not block APPROVE, and its result is recorded.
def test_loop_invokes_integration_gate(tmp_path):
    entries = [
        {"name": "repo-a", "test_cmd": "exit 0"},
        {"name": "repo-b", "test_cmd": "exit 0"},
    ]
    workspace = _make_workspace(tmp_path, {e["name"]: e["test_cmd"] for e in entries})
    manifest = _write_manifest(tmp_path, entries)

    code, out_dir = _run_loop(tmp_path, manifest, workspace)

    assert code == 0, f"expected APPROVE (exit 0), got {code}"
    final = _final(out_dir)
    assert final["verdict"] in ("APPROVED", "ARBITRATED"), final
    gate = final["integration_gate"]
    assert gate["gate_passed"] is True, gate
    assert {r["name"] for r in gate["per_repo"]} == {"repo-a", "repo-b"}


# AC2: one repo's test_cmd fails -> the loop exits EXIT_INFRA, never the
# plain REJECT code (3) a review/verify verdict would use.
def test_loop_rejects_on_gate_failure(tmp_path):
    entries = [
        {"name": "repo-a", "test_cmd": "exit 0"},
        {"name": "repo-b", "test_cmd": "exit 1"},
    ]
    workspace = _make_workspace(tmp_path, {e["name"]: e["test_cmd"] for e in entries})
    manifest = _write_manifest(tmp_path, entries)

    code, out_dir = _run_loop(tmp_path, manifest, workspace)

    assert code == 1, f"expected EXIT_INFRA (1), got {code}"  # EXIT_INFRA
    final = _final(out_dir)
    assert final["status"] == "infrastructure_error", final
    gate = final["integration_gate"]
    assert gate["gate_passed"] is False, gate
    statuses = {r["name"]: r["status"] for r in gate["per_repo"]}
    assert statuses["repo-a"] == "pass"
    assert statuses["repo-b"] == "fail"


# Unset --integration-gate-manifest (the default) must not change behavior:
# no gate runs, no integration_gate field appears, and existing loop usage
# against a single project is unaffected.
def test_loop_skips_gate_by_default(tmp_path):
    workdir = tmp_path / "repo"
    workdir.mkdir()
    env = {
        "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t.co",
        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t.co",
    }
    subprocess.run(["git", "init", "-q"], cwd=workdir, check=True)
    subprocess.run(["git", "config", "user.email", "a@b.c"], cwd=workdir, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=workdir, check=True)
    subprocess.run(
        ["git", "commit", "-q", "--allow-empty", "-m", "init"],
        cwd=workdir, check=True, env={**_env(), **env},
    )
    spec = tmp_path / "spec.md"
    spec.write_text(_SPEC)

    proc = subprocess.run(
        [sys.executable, str(_LOOP),
         "--spec", str(spec), "--workdir", str(workdir),
         "--feature", "igtest-default", "--no-merge", "--max-loops", "1",
         "--dev-cmd", str(_MOCKS / "mock_dev.sh"),
         "--review-cmd", str(_MOCKS / "mock_review.sh")],
        capture_output=True, text=True,
    )
    out_dir = workdir / ".adversarial-loop" / "igtest-default"

    assert proc.returncode == 0, f"{proc.stdout}\n{proc.stderr}"
    final = _final(out_dir)
    assert "integration_gate" not in final, final
