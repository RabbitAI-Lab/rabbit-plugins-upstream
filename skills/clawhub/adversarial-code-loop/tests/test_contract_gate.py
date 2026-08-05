"""P8 — the F1 AC-directive contract gate is wired into the code-loop pipeline.

pitfall #37: a loop could APPROVE without satisfying its textual acceptance
criteria. The fix is a single chokepoint before every APPROVE settle that
re-runs the shared ``adversarial_common.gates.run_contract_gate`` over the
spec's ``ac-directive`` blocks on the final repo state and blocks APPROVE when
any directive fails.

AC1 — a failing directive blocks APPROVE (loop ends REJECT).
AC2 — the loop imports/invokes the contract gate from adversarial_common.

These are end-to-end subprocess tests: they run the real orchestrator against a
throwaway git repo with the same mock DEV/REVIEW commands the bash suite uses,
so they exercise the wiring exactly as a real run would, no monkeypatching.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

_SKILL_ROOT = Path(__file__).resolve().parents[1]
_LOOP = _SKILL_ROOT / "scripts" / "adversarial_loop_v4.py"
_MOCKS = _SKILL_ROOT / "tests" / "mocks"

# A spec whose ac-directive the mock DEV output cannot satisfy: mock_dev.sh
# writes ``def answer(): return 42`` (no "bar"), so ``grep bar`` is absent.
_FAILING_SPEC = """\
# add a function

## Acceptance criteria

- AC1: source must contain bar
  ```ac-directive
  ac: AC1
  kind: grep
  command: grep bar
  ```
"""

# Same shape, but a directive the mock output DOES satisfy (grep answer).
_PASSING_SPEC = _FAILING_SPEC.replace("grep bar", "grep answer")

# Finding A2 regression: a directive whose grep token appears NEITHER in the
# spec's own prose NOR in the mock builder's output. The only way the gate
# can APPROVE such a directive is to never parse it at all — i.e. read a
# mutated, directive-free spec instead of the pre-BUILD snapshot.
_MUTATE_SPEC = """\
# add a function

## Acceptance criteria

- AC1: implementation must register the handler
  ```ac-directive
  ac: AC1
  kind: grep
  command: grep ZNIL_TOKEN_42
  ```
"""


def _run_loop(tmp_path: Path, spec_body: str) -> tuple[int, Path]:
    """Run the v4 loop against a fresh git repo; return (exit_code, out_dir).

    Uses ``--no-merge --max-loops 1`` and the bash suite's mock DEV/REVIEW
    commands, so the model layer is deterministic and needs no network.
    """
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
    spec.write_text(spec_body)

    proc = subprocess.run(
        [sys.executable, str(_LOOP),
         "--spec", str(spec), "--workdir", str(workdir),
         "--feature", "cgtest", "--no-merge", "--max-loops", "1",
         "--dev-cmd", str(_MOCKS / "mock_dev.sh"),
         "--review-cmd", str(_MOCKS / "mock_review.sh")],
        capture_output=True, text=True,
    )
    out_dir = workdir / ".adversarial-loop" / "cgtest"
    return proc.returncode, out_dir


def _env():
    return {k: v for k, v in os.environ.items()
            if k in ("PATH", "HOME", "LANG", "LC_ALL")}


def _final(out_dir: Path) -> dict:
    return json.loads((out_dir / "final.json").read_text())


# AC1: a failing AC directive blocks APPROVE — the loop ends REJECT.
def test_failing_ac_blocks_approve(tmp_path):
    code, out_dir = _run_loop(tmp_path, _FAILING_SPEC)

    assert code == 3, f"expected REJECT (exit 3), got {code}"  # EXIT_REJECTED

    final = _final(out_dir)
    assert final["verdict"] == "REJECT", final
    # The directive is the named reason APPROVE was blocked (pitfall #37).
    assert "CONTRACT_GATE_FAILED" in (final.get("reason") or ""), final

    gate = json.loads((out_dir / "02_contract_gate.json").read_text())
    assert gate["settle"] == "REJECT", gate
    assert gate["ac_status"]["AC1"] == "fail", gate
    assert any(f["ac"] == "AC1" for f in gate["failures"]), gate

    # R4/AC5: the contract result must reach final.json as ac_checks[] —
    # every directive carries its id/status/diagnostic (not just gates[] raw).
    checks = final.get("ac_checks") or []
    assert any(c.get("id") == "AC1:grep" and c.get("status") == "fail"
               for c in checks), final


# Finding A2 (trusted-spec model): the final contract gate must re-read the
# snapshot taken before BUILD (00_spec.txt), never args.spec. A spec that
# lives under workdir can be rewritten by BUILDER/FIXER to strip its
# directives, which would let run_contract_gate APPROVE vacuously. Here the
# mock DEV rewrites spec.md on disk to drop the ac-directive; the loop must
# still REJECT because the snapshot still carries the (failing) directive.
def test_contract_gate_uses_snapshot_not_mutated_spec(tmp_path):
    workdir = tmp_path / "repo"
    workdir.mkdir()
    env = {
        "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t.co",
        "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t.co",
    }
    subprocess.run(["git", "init", "-q"], cwd=workdir, check=True)
    subprocess.run(["git", "config", "user.email", "a@b.c"], cwd=workdir, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=workdir, check=True)

    # The spec LIVES INSIDE workdir (tracked + clean, so stash_dirty -u does
    # not remove it before BUILD) — exactly the shape the trusted-spec model
    # protects against: args.spec points at a file the builder can rewrite.
    spec = workdir / "spec.md"
    spec.write_text(_MUTATE_SPEC)
    subprocess.run(["git", "add", "spec.md"], cwd=workdir, check=True)
    subprocess.run(
        ["git", "commit", "-q", "-m", "init"], cwd=workdir, check=True,
        env={**_env(), **env},
    )

    proc = subprocess.run(
        [sys.executable, str(_LOOP),
         "--spec", str(spec), "--workdir", str(workdir),
         "--feature", "snapshot", "--no-merge", "--max-loops", "1",
         "--dev-cmd", str(_MOCKS / "mock_dev_mutate_spec.sh"),
         "--review-cmd", str(_MOCKS / "mock_review.sh")],
        capture_output=True, text=True,
    )
    out_dir = workdir / ".adversarial-loop" / "snapshot"

    # The snapshot still carries the (failing) directive, so the gate finds
    # it, runs grep ZNIL_TOKEN_42, it fails, and the loop REJECTs. A gate that
    # re-read the mutated args.spec would parse zero directives (directives ==
    # []) and APPROVE vacuously — the bug this test pins down.
    assert proc.returncode == 3, (
        f"expected REJECT (exit 3), got {proc.returncode}\n"
        f"{proc.stdout}\n{proc.stderr}")
    final = _final(out_dir)
    assert final["verdict"] == "REJECT", final
    assert "CONTRACT_GATE_FAILED" in (final.get("reason") or ""), final

    gate = json.loads((out_dir / "02_contract_gate.json").read_text())
    assert gate["settle"] == "REJECT", gate
    assert gate["ac_status"]["AC1"] == "fail", gate
    assert any(d["id"] == "AC1:grep" for d in gate["directives"]), gate

    # The artifact snapshot still carries the original directive block.
    assert "ac-directive" in (out_dir / "00_spec.txt").read_text()


# A passing directive must NOT be a false positive: the loop still APPROVEs.
# Without this, "blocks APPROVE" is meaningless (it could block everything).
def test_passing_ac_allows_approve(tmp_path):
    code, out_dir = _run_loop(tmp_path, _PASSING_SPEC)

    assert code == 0, f"expected APPROVE (exit 0), got {code}"

    final = _final(out_dir)
    assert final["verdict"] in ("APPROVED", "ARBITRATED"), final

    gate = json.loads((out_dir / "02_contract_gate.json").read_text())
    assert gate["settle"] == "APPROVE", gate
    assert gate["ac_status"]["AC1"] == "pass", gate


# AC2: the loop imports the contract gate from adversarial_common (R1).
def test_loop_imports_contract_gate_from_adversarial_common():
    source = (_SKILL_ROOT / "scripts" / "adversarial_loop_v4.py").read_text()

    # The import reaches into adversarial_common for the shared gate (P5)…
    assert "from adversarial_common" in source, "no adversarial_common import"
    # …and names the contract gate specifically.
    assert "run_contract_gate" in source, "contract gate not referenced"
    # …and it is actually invoked before the APPROVE settle.
    assert "run_contract_gate(" in source, "contract gate never called"
