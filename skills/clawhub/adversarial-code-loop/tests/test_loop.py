"""Probe-based regression tests for the concurrent FIX+VERIFY gate (LO1).

The concurrent branch bypasses ``gates.post_fix_gate`` -- the only place
``--test-cmd``/``--build-cmd`` runs once a fix round is needed -- so it must be
refused whenever a verification command is configured. These tests prove the
sequential gate actually executes and that a failing probe forces REJECT.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

_SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(_SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILL_ROOT))

from scripts import adversarial_loop as loop

# Two file-disjoint findings: this is exactly the shape that would otherwise
# trigger ``use_concurrent`` and skip the post-fix gate.
_FILE_DISJOINT_FINDINGS = [
    {"id": "A1", "file": "one.py", "summary": "fix one"},
    {"id": "A2", "file": "two.py", "summary": "fix two"},
]


def _args(tmp_path, *, build_cmd=None, test_cmd=None, max_loops=1):
    return SimpleNamespace(
        spec=str(tmp_path / "spec.md"),
        build_cmd=build_cmd,
        test_cmd=test_cmd,
        timeout=20,
        max_loops=max_loops,
        no_arbiter=True,
        no_merge=True,
    )


def _state(findings):
    return {
        "completed": [
            "git_setup", "pre_build_gate", "build", "post_build_gate", "review",
        ],
        "parent_branch": "main",
        "branch": "loop/test",
        "branch_point": "base",
        "findings": list(findings),
        "loop": 0,
    }


def _stub_sequential_phases(monkeypatch, *, verify_verdict="APPROVE"):
    """Mock every phase except the real verification gate."""
    monkeypatch.setattr(loop.gitops, "checkout", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "get_diff", lambda *_a: "diff")
    monkeypatch.setattr(
        loop.phase_fix, "run_fix",
        lambda *_a, **_k: {"exit_code": 0, "commit_sha": "abc"},
    )

    def _verify(findings, *_a, **_k):
        return {
            "exit_code": 0,
            "verdict": verify_verdict,
            "results": [
                {"id": f["id"], "status": "resolved"} for f in findings
            ],
        }

    monkeypatch.setattr(loop.phase_verify, "run_verify", _verify)
    # Leave loop.gates.post_fix_gate REAL so the probe actually executes.
    monkeypatch.setattr(loop, "_finish", lambda *_a, **_k: loop.EXIT_APPROVED)


def test_concurrent_disabled_when_test_cmd_set(tmp_path, monkeypatch):
    """AC1: a configured --test-cmd forces the sequential gate to run."""
    spec = tmp_path / "spec.md"
    spec.write_text("# Requirements\n\nREQ-1: the test gate must run.\n")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "02_review.json").write_text(json.dumps({
        "verdict": "REQUEST_CHANGES",
        "findings": _FILE_DISJOINT_FINDINGS,
    }))

    sentinel = tmp_path / "probe.sentinel"
    probe_cmd = f"touch {sentinel}"
    _stub_sequential_phases(monkeypatch)

    args = _args(tmp_path, test_cmd=probe_cmd)
    state = _state(_FILE_DISJOINT_FINDINGS)

    result = loop._pipeline(
        args, "dev", "review", "", str(tmp_path), "test", out_dir, state
    )

    # The sequential path ran and approved via the real verify stub.
    assert result == loop.EXIT_APPROVED
    # The probe actually executed (sentinel written by the real gate).
    assert sentinel.exists(), "post-fix gate probe never ran"
    # The gate result is persisted where the sequential path writes it.
    gate_path = out_dir / "03_post_fix_gate_1.json"
    assert gate_path.exists(), "sequential post-fix gate artifact missing"
    gate = json.loads(gate_path.read_text())
    assert gate["command"] == probe_cmd
    assert gate["ok"] is True and gate["exit_code"] == 0
    # The disable reason is recorded in state, not just stdout.
    assert any(
        "concurrent FIX+VERIFY disabled" in note
        for note in state.get("notes", [])
    ), state.get("notes")


def test_concurrent_still_used_without_test_cmd(tmp_path, monkeypatch):
    """AC2: with no verification command, the concurrent path still runs."""
    spec = tmp_path / "spec.md"
    spec.write_text("# Requirements\n\nREQ-1: keep concurrent path available.\n")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "02_review.json").write_text(json.dumps({
        "verdict": "REQUEST_CHANGES",
        "findings": _FILE_DISJOINT_FINDINGS,
    }))

    calls = {"concurrent": 0}

    def _stub_round(*_a, **_k):
        calls["concurrent"] += 1
        fix = {
            "exit_code": 0, "groups": 2, "group_errors": [],
            "concurrent": True,
        }
        verify = {
            "exit_code": 0, "verdict": "APPROVE",
            "results": [
                {"id": f["id"], "status": "resolved"}
                for f in _FILE_DISJOINT_FINDINGS
            ],
            "concurrent": True,
        }
        return fix, verify

    monkeypatch.setattr(loop.gitops, "checkout", lambda *_a: None)
    monkeypatch.setattr(loop, "_run_concurrent_fix_verify_round", _stub_round)
    monkeypatch.setattr(loop, "_finish", lambda *_a, **_k: loop.EXIT_APPROVED)

    args = _args(tmp_path)  # no build_cmd, no test_cmd
    state = _state(_FILE_DISJOINT_FINDINGS)

    result = loop._pipeline(
        args, "dev", "review", "", str(tmp_path), "test", out_dir, state
    )

    assert result == loop.EXIT_APPROVED
    assert calls["concurrent"] == 1, "concurrent path was not taken"
    # No disable note when nothing forced the sequential gate.
    assert not any(
        "concurrent FIX+VERIFY disabled" in note
        for note in state.get("notes", [])
    )


def test_failing_probe_forces_reject(tmp_path, monkeypatch):
    """AC3: a non-zero probe exit must prevent approval."""
    spec = tmp_path / "spec.md"
    spec.write_text("# Requirements\n\nREQ-1: a failing gate rejects.\n")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "02_review.json").write_text(json.dumps({
        "verdict": "REQUEST_CHANGES",
        "findings": _FILE_DISJOINT_FINDINGS,
    }))

    _stub_sequential_phases(monkeypatch)

    args = _args(tmp_path, test_cmd="exit 1")
    state = _state(_FILE_DISJOINT_FINDINGS)

    captured = {}

    def _capture_finish(*args_, **kwargs):
        captured["verdict"] = args_[5] if len(args_) > 5 else kwargs.get("verdict")
        return loop.EXIT_REJECTED

    monkeypatch.setattr(loop, "_finish", _capture_finish)

    result = loop._pipeline(
        args, "dev", "review", "", str(tmp_path), "test", out_dir, state
    )

    assert result == loop.EXIT_REJECTED
    assert captured.get("verdict") == "REJECT"
    gate = json.loads((out_dir / "03_post_fix_gate_1.json").read_text())
    assert gate["ok"] is False and gate["exit_code"] == 1


def test_cherry_pick_timeout_becomes_infra_not_traceback(tmp_path, monkeypatch):
    """AC1 (LO2): a git hang during the post-pool cherry-pick must surface as
    EXIT_INFRA with a recorded reason, never as a raw traceback out of main(),
    AND must abort the in-progress cherry-pick so the repo is not left
    mid-merge (A1).

    The concurrent round runs for real (only gitops / phase calls are mocked)
    so the cherry-pick reconciler, the caller-level R2 wrapper, and the
    mid-merge abort are all exercised. A subprocess.TimeoutExpired is neither
    a GitError nor a NoProviderAvailable, so without the reconciler fix it
    would escape main() uncaught; without the abort it would leave
    CHERRY_PICK_HEAD set so the later restore fails.
    """
    spec = tmp_path / "spec.md"
    spec.write_text("# Requirements\n\nREQ-1: cherry-pick infra must be clean.\n")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "02_review.json").write_text(json.dumps({
        "verdict": "REQUEST_CHANGES",
        "findings": _FILE_DISJOINT_FINDINGS,
    }))

    # Mirror the repo state a timed-out cherry-pick leaves behind: git has
    # written CHERRY_PICK_HEAD / staged conflicts before the subprocess died.
    cherry_pick = {"active": False, "aborted": []}

    def _timed_out_cherry_pick(workdir, commit_ref):
        cherry_pick["active"] = True
        raise subprocess.TimeoutExpired(cmd="git", timeout=5)

    def _abort(workdir, _state):
        # A real `git cherry-pick --abort` only clears state when a
        # cherry-pick is in progress; mirror that so the assertion proves the
        # loop invoked the abort on a mid-merge repo, not as a stray no-op.
        if cherry_pick["active"]:
            cherry_pick["aborted"].append(str(workdir))
            cherry_pick["active"] = False

    # Drive the real concurrent round: only git plumbing and the model phases
    # are stubbed. cherry_pick is the failure point under test.
    monkeypatch.setattr(loop.gitops, "checkout", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "create_worktree", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "get_diff", lambda *_a: "diff")
    monkeypatch.setattr(loop.gitops, "remove_worktree", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "delete_branch", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "cherry_pick", _timed_out_cherry_pick)
    monkeypatch.setattr(loop, "_abort_in_progress_cherry_pick", _abort)
    monkeypatch.setattr(
        loop.phase_fix, "run_fix",
        lambda *_a, **_k: {"exit_code": 0, "commit_sha": "abc"},
    )

    def _verify(findings, *_a, **_k):
        return {
            "exit_code": 0,
            "verdict": "APPROVE",
            "results": [
                {"id": f["id"], "status": "resolved"} for f in findings
            ],
        }

    monkeypatch.setattr(loop.phase_verify, "run_verify", _verify)

    args = _args(tmp_path)  # no build_cmd / test_cmd -> concurrent path
    state = _state(_FILE_DISJOINT_FINDINGS)

    # Must return, not raise. A raw TimeoutExpired out of _pipeline would also
    # escape main() (it is not GitError / NoProviderAvailable / KeyboardInterrupt).
    result = loop._pipeline(
        args, "dev", "review", "", str(tmp_path), "test", out_dir, state
    )

    assert result == loop.EXIT_INFRA
    # The reason is recorded for operators / final.json, not lost.
    assert "timed out" in state.get("error", "").lower(), state.get("error")
    assert "fix_1" in state["error"], state["error"]
    # A1: the in-progress cherry-pick was aborted before the infra error
    # propagated, so the repo is not left mid-merge for the restore to trip on.
    assert cherry_pick["aborted"], (
        "mid-merge cherry-pick was not aborted before re-raise"
    )
    assert not cherry_pick["active"], "repo left mid-merge after infra failure"


def test_worker_infra_failure_routes_to_exit_infra(tmp_path, monkeypatch):
    """R2 AC1: a subprocess/OS failure inside a concurrent worker (here,
    ``create_worktree`` raising ``TimeoutExpired``) is infrastructure, not a
    review dispute. Before this fix, ``_process_group``'s blanket
    ``except Exception`` folded it into a per-group ``{"error": ...}`` that
    aggregation turned into a "disputed" finding, settling the round as
    REJECT with no infra evidence. It must now propagate to EXIT_INFRA with
    no raw traceback out of ``_pipeline``.
    """
    spec = tmp_path / "spec.md"
    spec.write_text("# Requirements\n\nREQ-1: worker infra failures are EXIT_INFRA.\n")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "02_review.json").write_text(json.dumps({
        "verdict": "REQUEST_CHANGES",
        "findings": _FILE_DISJOINT_FINDINGS,
    }))

    def _raise_timeout(*_a, **_k):
        raise subprocess.TimeoutExpired(cmd="git", timeout=5)

    monkeypatch.setattr(loop.gitops, "checkout", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "create_worktree", _raise_timeout)
    monkeypatch.setattr(loop.gitops, "remove_worktree", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "delete_branch", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "prune_worktrees", lambda *_a: None)
    monkeypatch.setattr(loop, "_abort_in_progress_cherry_pick", lambda *_a: None)

    args = _args(tmp_path)  # no build_cmd / test_cmd -> concurrent path
    state = _state(_FILE_DISJOINT_FINDINGS)

    # Must return EXIT_INFRA, not raise and not settle as REJECT/disputed.
    result = loop._pipeline(
        args, "dev", "review", "", str(tmp_path), "test", out_dir, state
    )

    assert result == loop.EXIT_INFRA
    assert "fix_1" in state.get("error", ""), state.get("error")
    assert state.get("verdict") != "REJECT", state.get("verdict")


def test_worker_git_error_routes_to_exit_infra(tmp_path, monkeypatch):
    """A2: ``create_worktree`` / ``get_diff`` raise ``gitops.GitError`` (not
    ``TimeoutExpired``) for an ordinary non-zero git exit -- e.g. disk full,
    a bad ref, a corrupt object. Before this fix the worker's blanket
    ``except Exception`` folded that into a per-group ``{"error": ...}`` too,
    which aggregation turned into a "disputed" finding and settled the round
    as REJECT with no infra evidence, exactly like the TimeoutExpired case
    covered by ``test_worker_infra_failure_routes_to_exit_infra`` above. It
    must now propagate to EXIT_INFRA the same way.
    """
    spec = tmp_path / "spec.md"
    spec.write_text("# Requirements\n\nREQ-1: worker GitError is EXIT_INFRA.\n")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "02_review.json").write_text(json.dumps({
        "verdict": "REQUEST_CHANGES",
        "findings": _FILE_DISJOINT_FINDINGS,
    }))

    def _raise_git_error(*_a, **_k):
        raise loop.gitops.GitError("git worktree add failed: disk full")

    monkeypatch.setattr(loop.gitops, "checkout", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "create_worktree", _raise_git_error)
    monkeypatch.setattr(loop.gitops, "remove_worktree", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "delete_branch", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "prune_worktrees", lambda *_a: None)
    monkeypatch.setattr(loop, "_abort_in_progress_cherry_pick", lambda *_a: None)

    args = _args(tmp_path)  # no build_cmd / test_cmd -> concurrent path
    state = _state(_FILE_DISJOINT_FINDINGS)

    # Must return EXIT_INFRA, not raise and not settle as REJECT/disputed.
    result = loop._pipeline(
        args, "dev", "review", "", str(tmp_path), "test", out_dir, state
    )

    assert result == loop.EXIT_INFRA
    assert "fix_1" in state.get("error", ""), state.get("error")
    assert state.get("verdict") != "REJECT", state.get("verdict")


def test_worker_review_failure_still_disputed(tmp_path, monkeypatch):
    """R2 AC2: a genuine (non-infra) exception inside a worker -- e.g. the
    review/verify phase itself blowing up -- must still be folded into a
    disputed per-finding result exactly as before, not promoted to
    EXIT_INFRA.
    """
    spec = tmp_path / "spec.md"
    spec.write_text("# Requirements\n\nREQ-1: genuine failures stay disputed.\n")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    (out_dir / "02_review.json").write_text(json.dumps({
        "verdict": "REQUEST_CHANGES",
        "findings": _FILE_DISJOINT_FINDINGS,
    }))

    monkeypatch.setattr(loop.gitops, "checkout", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "create_worktree", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "get_diff", lambda *_a: "diff")
    monkeypatch.setattr(loop.gitops, "remove_worktree", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "delete_branch", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "cherry_pick", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "prune_worktrees", lambda *_a: None)
    monkeypatch.setattr(loop, "_abort_in_progress_cherry_pick", lambda *_a: None)

    def _explode(*_a, **_k):
        raise RuntimeError("provider returned malformed payload")

    monkeypatch.setattr(loop.phase_fix, "run_fix", _explode)

    captured = {}

    def _capture_finish(*args_, **kwargs):
        captured["verdict"] = args_[5] if len(args_) > 5 else kwargs.get("verdict")
        return loop.EXIT_REJECTED

    monkeypatch.setattr(loop, "_finish", _capture_finish)

    args = _args(tmp_path, max_loops=1)
    state = _state(_FILE_DISJOINT_FINDINGS)

    result = loop._pipeline(
        args, "dev", "review", "", str(tmp_path), "test", out_dir, state
    )

    # Genuine review-failure exceptions keep behaving as before: REJECT, not
    # EXIT_INFRA, with the findings marked disputed rather than a crash.
    assert result == loop.EXIT_REJECTED
    assert captured.get("verdict") == "REJECT"
    verify = json.loads((out_dir / "04_verdict_1.json").read_text())
    assert verify["verdict"] == "REJECT"
    assert all(r["status"] == "disputed" for r in verify["results"])
    assert any("malformed payload" in r.get("evidence", "") for r in verify["results"])


def test_abort_cherry_pick_failure_warns(tmp_path, monkeypatch):
    """R3 AC1: a real ``git cherry-pick --abort`` failure must not be
    swallowed by a bare ``except ...: pass``. It must append a warning to
    ``state["warnings"]``, mirroring the worktree-cleanup pattern, so a repo
    left mid-merge is visible to operators instead of silently vanishing.
    """
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / ".git" / "CHERRY_PICK_HEAD").write_text("deadbeef\n")

    real_run = subprocess.run

    def _fake_run(cmd, *a, **k):
        # Only the abort itself is faked; the A1 `rev-parse --git-path`
        # probe must hit the real git repo to resolve CHERRY_PICK_HEAD.
        if cmd[:2] == ["git", "cherry-pick"]:
            return SimpleNamespace(
                returncode=1, stdout=b"", stderr=b"could not abort cherry-pick",
            )
        return real_run(cmd, *a, **k)

    monkeypatch.setattr(loop.subprocess, "run", _fake_run)

    state = {}
    loop._abort_in_progress_cherry_pick(str(tmp_path), state)

    warnings = state.get("warnings", [])
    assert warnings, "abort failure was swallowed silently"
    assert any("abort" in w.lower() for w in warnings), warnings


def test_abort_cherry_pick_noop_when_nothing_in_progress(tmp_path, monkeypatch):
    """No CHERRY_PICK_HEAD means nothing to abort -- the common case on every
    round -- and must not spuriously warn.
    """
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)

    real_run = subprocess.run

    def _fail_if_called(cmd, *a, **k):
        if cmd[:2] == ["git", "cherry-pick"]:
            raise AssertionError("git cherry-pick --abort should not run")
        return real_run(cmd, *a, **k)

    monkeypatch.setattr(loop.subprocess, "run", _fail_if_called)

    state = {}
    loop._abort_in_progress_cherry_pick(str(tmp_path), state)

    assert state.get("warnings", []) == []


def test_abort_cherry_pick_resolves_nested_workdir(tmp_path, monkeypatch):
    """A1: when *workdir* is a subdirectory of the repo (or a linked
    worktree), ``<workdir>/.git/CHERRY_PICK_HEAD`` never exists even during
    a real cherry-pick -- ``.git`` lives at the repo root, not in the
    subdirectory. The check must resolve the path via
    ``git rev-parse --git-path`` so an in-progress cherry-pick is still
    detected and aborted from a nested cwd.
    """
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / ".git" / "CHERRY_PICK_HEAD").write_text("deadbeef\n")
    subdir = tmp_path / "sub"
    subdir.mkdir()

    real_run = subprocess.run
    abort_calls = []

    def _fake_run(cmd, *a, **k):
        if cmd[:2] == ["git", "cherry-pick"]:
            abort_calls.append(cmd)
            return SimpleNamespace(returncode=0, stdout=b"", stderr=b"")
        return real_run(cmd, *a, **k)

    monkeypatch.setattr(loop.subprocess, "run", _fake_run)

    state = {}
    loop._abort_in_progress_cherry_pick(str(subdir), state)

    assert abort_calls, "cherry-pick --abort was not invoked from a nested workdir"
    assert state.get("warnings", []) == []


def test_worktree_cleanup_failure_recorded_in_state_warnings(tmp_path, monkeypatch):
    """AC1 (LO3 part B): a failed remove_worktree in the concurrent cleanup
    finally must be recorded in state["warnings"] (it was silently swallowed
    by a bare `except Exception: pass`), and the warning must carry the
    worktree path so operators can find the dangling metadata.
    """
    spec = tmp_path / "spec.md"
    spec.write_text("# Requirements\n\nREQ-1: cleanup failure is recorded.\n")
    out_dir = tmp_path / "out"
    out_dir.mkdir()

    # Drive the real concurrent round; only git plumbing + model phases are
    # stubbed. remove_worktree is the failure point under test and raises an
    # exception whose message carries the worktree path (as a real GitError
    # would, since _git formats `git ... <path> ... failed`).
    removed = []

    def _raise_remove(workdir, wt_path):
        removed.append(wt_path)
        raise RuntimeError(f"remove_worktree failed for {wt_path}")

    monkeypatch.setattr(loop.gitops, "checkout", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "create_worktree", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "get_diff", lambda *_a: "diff")
    monkeypatch.setattr(loop.gitops, "remove_worktree", _raise_remove)
    monkeypatch.setattr(loop.gitops, "delete_branch", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "cherry_pick", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "prune_worktrees", lambda *_a: None)
    monkeypatch.setattr(loop, "_abort_in_progress_cherry_pick", lambda *_a: None)
    monkeypatch.setattr(
        loop.phase_fix, "run_fix",
        lambda *_a, **_k: {"exit_code": 0, "commit_sha": "abc"},
    )
    monkeypatch.setattr(
        loop.phase_verify, "run_verify",
        lambda findings, *_a, **_k: {
            "exit_code": 0, "verdict": "APPROVE",
            "results": [{"id": f["id"], "status": "resolved"} for f in findings],
        },
    )

    state = _state(_FILE_DISJOINT_FINDINGS)
    args = SimpleNamespace(max_loops=1, _force_providers={})

    fix, verify = loop._run_concurrent_fix_verify_round(
        _FILE_DISJOINT_FINDINGS, "dev", "review", str(tmp_path), "test", 1,
        20, {}, None, "base", 2, str(out_dir), state, args,
    )

    # The round still completes (cleanup failure is non-fatal) and the
    # worktree path appears in the recorded warnings, not lost to a bare pass.
    assert removed, "remove_worktree was never invoked during cleanup"
    warnings = state.get("warnings", [])
    assert warnings, "cleanup exception was swallowed silently"
    assert any(removed[0] in w for w in warnings), (removed[0], warnings)


def test_cleanup_retries_branch_delete_after_prune(tmp_path, monkeypatch):
    """R4/A3 AC1: a failed ``remove_worktree`` -- realistically, one where
    ``git worktree remove --force`` itself fails and so leaves the
    worktree's directory in place, its normal failure mode -- leaves a
    stale ``.git/worktrees/<id>`` entry that still makes git treat the
    fix-round branch as checked out. A ``git worktree prune`` run while that
    directory still exists cannot clear the entry, so an immediate
    prune-then-retry-delete_branch fails too (A3): the branch would be
    orphaned, poisoning a later ``--resume`` that reuses this exact branch
    name. Only once ``wt_base`` itself is torn down (via ``shutil.rmtree``)
    does a further prune finally drop the metadata, so ``delete_branch``
    must be retried again after that -- which is what this test guards.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    subprocess.run(
        ["git", "-C", str(repo), "config", "user.email", "loop@adversarial.local"],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(repo), "config", "user.name", "adversarial-loop"],
        check=True,
    )
    (repo / "file.txt").write_text("base\n")
    subprocess.run(["git", "-C", str(repo), "add", "file.txt"], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-q", "-m", "base"], check=True)

    out_dir = tmp_path / "out"
    out_dir.mkdir()

    def _flaky_remove(_workdir, path):
        # A real `git worktree remove --force` failure leaves the directory
        # in place -- it does not tear the tree down first. That means the
        # in-loop `prune_worktrees` + retry `delete_branch` cannot succeed
        # either (the metadata is still live because the directory still
        # exists); only the final rmtree(wt_base) + prune, later in the
        # cleanup, actually clears it.
        raise RuntimeError(f"simulated remove_worktree failure for {path}")

    monkeypatch.setattr(loop.gitops, "checkout", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "cherry_pick", lambda *_a: None)
    monkeypatch.setattr(loop.gitops, "remove_worktree", _flaky_remove)
    monkeypatch.setattr(
        loop.phase_fix, "run_fix",
        lambda *_a, **_k: {"exit_code": 0, "commit_sha": "abc"},
    )
    monkeypatch.setattr(
        loop.phase_verify, "run_verify",
        lambda findings, *_a, **_k: {
            "exit_code": 0, "verdict": "APPROVE",
            "results": [{"id": f["id"], "status": "resolved"} for f in findings],
        },
    )

    state = _state(_FILE_DISJOINT_FINDINGS)
    args = SimpleNamespace(max_loops=1, _force_providers={})

    loop._run_concurrent_fix_verify_round(
        _FILE_DISJOINT_FINDINGS, "dev", "review", str(repo), "test", 1,
        20, {}, None, "HEAD", 2, str(out_dir), state, args,
    )

    branches = subprocess.run(
        ["git", "-C", str(repo), "branch", "--list"],
        capture_output=True, text=True, check=True,
    ).stdout
    assert "fix-1/g0" not in branches and "fix-1/g1" not in branches, branches


def test_resume_prunes_stale_worktrees(tmp_path):
    """AC2 (LO3 part B): _cleanup_loop_worktrees (the --resume pre-restore
    hook) must prune dangling .git/worktrees/<id> metadata whose working
    directory no longer exists, so `git worktree list` no longer shows it.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    subprocess.run(
        ["git", "-C", str(repo), "config", "user.email", "loop@adversarial.local"],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(repo), "config", "user.name", "adversarial-loop"],
        check=True,
    )
    (repo / "file.txt").write_text("base\n")
    subprocess.run(["git", "-C", str(repo), "add", "file.txt"], check=True)
    subprocess.run(
        ["git", "-C", str(repo), "commit", "-q", "-m", "base"], check=True
    )

    wt_dir = tmp_path / "wt-stale"
    subprocess.run(
        ["git", "-C", str(repo), "worktree", "add", str(wt_dir), "-b", "wtbranch"],
        check=True,
    )
    # Simulate a prior interrupted run: the worktree directory is gone but the
    # .git/worktrees metadata is still registered -> stale.
    shutil.rmtree(str(wt_dir))

    def _list():
        out = subprocess.run(
            ["git", "-C", str(repo), "worktree", "list"],
            capture_output=True, text=True, check=True,
        ).stdout
        return out

    assert str(wt_dir) in _list(), "fixture setup: stale entry not registered"

    loop._cleanup_loop_worktrees(
        {"out_dir": str(tmp_path / "out"), "workdir": str(repo)}
    )

    listing = _list()
    assert str(wt_dir) not in listing, (
        f"stale worktree still listed after resume cleanup: {listing!r}"
    )


def test_write_final_artifact_strips_markers_on_any_infra_error(tmp_path):
    """AC1 (final-verdict-structured): marker stripping keys off the
    ``infrastructure`` boolean alone, NOT the ``'git finalize failed:'`` error
    prefix. The shared helper sets ``infrastructure=True`` on EVERY
    infra-classified exit, but only sets ``error`` to that prefix on a git
    finalize failure -- so a future-reworded (or prefix-less) infra error
    must still strip the internal ``infrastructure`` key from the public
    final.json, exactly as the finalize-failure path does, while the
    persisted ``status`` still reads ``infrastructure_error`` (R1) rather
    than drifting to ``clean`` once the marker that drove that
    classification is popped before re-derivation.
    """
    # Mirror the normalized infra payload finish_pipeline hands the writer:
    # both internal markers set, but an error that does NOT carry the prefix.
    payload = {
        "infrastructure": True,
        "status": "infrastructure_error",
        "error": "repository is locked, retry later",  # NOT the prefix
    }

    loop._write_final_artifact(str(tmp_path), "APPROVED", payload)

    final = json.loads((tmp_path / "final.json").read_text())
    # The internal marker key is stripped from the public contract.
    assert "infrastructure" not in final, final
    # R1: the infra classification is NOT discarded -- status must not read
    # "clean" just because the raw marker was popped before re-derivation.
    assert final.get("status") == "infrastructure_error", final
    # The error itself is preserved -- only the markers were stripped.
    assert final["error"] == "repository is locked, retry later", final


def test_final_json_infra_failure_not_clean(tmp_path, monkeypatch):
    """R1 AC1: force a merge-failure exit through the real finish_pipeline
    path (git finalize failure -> infrastructure=True) and confirm the
    persisted final.json has status != "clean" and the error is present.
    """
    out_dir = tmp_path / "out"
    out_dir.mkdir()

    monkeypatch.setattr(loop.gitops, "get_current_branch", lambda *_a: "loop/test")
    monkeypatch.setattr(
        loop.gitops, "squash_merge",
        lambda *_a, **_k: (_ for _ in ()).throw(
            loop.gitops.GitError("squash merge conflict: simulated")
        ),
    )

    args = SimpleNamespace(no_merge=False, ci=False)
    state = {
        "branch": "loop/test", "parent_branch": "main", "findings": [],
    }

    code = loop._finish(
        args, str(tmp_path), "test", out_dir, state, "APPROVED",
        loops=1, conditions=[], extra={"arbitrated": False},
    )

    assert code == loop.EXIT_INFRA
    final = json.loads((out_dir / "final.json").read_text())
    assert final.get("status") != "clean", final
    assert final.get("error"), final
