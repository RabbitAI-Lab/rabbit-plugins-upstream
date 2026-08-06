"""P15 — integration_gate.py manifest-driven runner.

``run_integration_gate`` reads a repos manifest (P14's ``{name, path,
test_cmd, timeout}`` shape), runs each repo's ``test_cmd`` as a subprocess
bounded by a per-repo timeout, and aggregates a single ``gate_passed``
verdict. A timeout must kill the whole process group (no orphan children)
and long output must be truncated with a visible marker.

AC1 — all repos pass -> gate_passed=True.
AC2 — one repo fails -> gate_passed=False.
AC3 — one repo times out -> status=fail, timed_out=True, gate_passed=False.

P16 — a failing gate is an infrastructure failure, not a code-quality
rejection, and its result projects onto final.json's ``integration_gate``
field.

test_gate_failure_exits_infra — gate fails: exit code is EXIT_INFRA (not
EXIT_REJECTED).
test_final_json_integration_gate_field — after a gate run, final.json has
``integration_gate`` with per_repo entries and gate_passed.
"""
import json
import sys
from pathlib import Path

_SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(_SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILL_ROOT))

from scripts.phases.integration_gate import (
    integration_gate_exit_code,
    run_integration_gate,
)
from adversarial_common import jsonio, runner


def _write_manifest(tmp_path: Path, entries: list) -> Path:
    lines = []
    for entry in entries:
        lines.append(f"- name: {entry['name']}")
        lines.append(f"  path: {entry['name']}")
        lines.append(f"  test_cmd: {entry['test_cmd']}")
        if "timeout" in entry:
            lines.append(f"  timeout: {entry['timeout']}")
    manifest = tmp_path / "manifest.yaml"
    manifest.write_text("\n".join(lines) + "\n")
    return manifest


def _make_repos(tmp_path: Path, count: int) -> list:
    names = [f"repo{i}" for i in range(count)]
    for name in names:
        (tmp_path / name).mkdir()
    return names


# AC1: mock 5 repos with passing test commands, gate_passed=true.
def test_gate_all_repos_pass(tmp_path):
    names = _make_repos(tmp_path, 5)
    entries = [{"name": n, "test_cmd": "exit 0"} for n in names]
    manifest = _write_manifest(tmp_path, entries)

    result = run_integration_gate(str(tmp_path), manifest_path=str(manifest))

    assert result["gate_passed"] is True
    assert len(result["per_repo"]) == 5
    for repo_result in result["per_repo"]:
        assert repo_result["status"] == "pass"
        assert repo_result["output_truncated"] is False
        assert repo_result["timed_out"] is False


# AC2: one repo fails, gate_passed=false.
def test_gate_single_repo_fails(tmp_path):
    names = _make_repos(tmp_path, 5)
    entries = [
        {"name": n, "test_cmd": "exit 1" if n == "repo2" else "exit 0"}
        for n in names
    ]
    manifest = _write_manifest(tmp_path, entries)

    result = run_integration_gate(str(tmp_path), manifest_path=str(manifest))

    assert result["gate_passed"] is False
    statuses = {r["name"]: r["status"] for r in result["per_repo"]}
    assert statuses["repo2"] == "fail"
    assert statuses["repo0"] == "pass"
    assert statuses["repo1"] == "pass"


# AC3: a repo exceeds its timeout -> status=fail, timed_out=true,
# gate_passed=false. The process group must actually be killed, not just
# abandoned (R2): a grandchild forked inside the same group must die too.
def test_gate_repo_timeout(tmp_path):
    _make_repos(tmp_path, 1)
    child_pid_file = tmp_path / "repo0" / "child.pid"
    test_cmd = (
        "python3 -c \""
        "import os,time;"
        "pid=os.fork();"
        "open('child.pid','w').write(str(pid)) if pid else None;"
        "time.sleep(10)"
        "\""
    )
    entries = [{"name": "repo0", "test_cmd": test_cmd, "timeout": 1}]
    manifest = _write_manifest(tmp_path, entries)

    start = __import__("time").monotonic()
    result = run_integration_gate(str(tmp_path), manifest_path=str(manifest))
    elapsed = __import__("time").monotonic() - start

    assert elapsed < 8, f"gate did not return promptly after timeout: {elapsed}s"
    assert result["gate_passed"] is False
    repo_result = result["per_repo"][0]
    assert repo_result["status"] == "fail"
    assert repo_result["timed_out"] is True

    # The forked grandchild was in the same process group as the killed
    # parent, so it must not still be alive well past the 1s timeout.
    if child_pid_file.exists():
        child_pid = int(child_pid_file.read_text().strip())
        import os as _os
        import time as _time
        _time.sleep(0.2)
        try:
            _os.kill(child_pid, 0)
            alive = True
        except ProcessLookupError:
            alive = False
        except PermissionError:
            alive = True
        assert not alive, "timed-out repo left an orphaned grandchild process"


# Long output is bounded and carries a visible truncation marker (R2).
def test_gate_output_truncated_marker(tmp_path):
    _make_repos(tmp_path, 1)
    entries = [{"name": "repo0", "test_cmd": "yes x | head -c 200000; exit 1"}]
    manifest = _write_manifest(tmp_path, entries)

    result = run_integration_gate(str(tmp_path), manifest_path=str(manifest))

    repo_result = result["per_repo"][0]
    assert repo_result["output_truncated"] is True
    assert "truncated" in repo_result["output"]


# R1/AC1 (P16): a failed gate is infrastructure, never REJECT/blocking.
def test_gate_failure_exits_infra(tmp_path):
    names = _make_repos(tmp_path, 2)
    entries = [
        {"name": n, "test_cmd": "exit 1" if n == "repo0" else "exit 0"}
        for n in names
    ]
    manifest = _write_manifest(tmp_path, entries)

    result = run_integration_gate(str(tmp_path), manifest_path=str(manifest))

    assert result["gate_passed"] is False
    assert integration_gate_exit_code(result) == runner.CI_EXIT_INFRASTRUCTURE
    assert integration_gate_exit_code(result) != runner.CI_EXIT_BLOCKING

    # A passing gate must not be misclassified as infrastructure either.
    passing = run_integration_gate(
        str(tmp_path),
        manifest_path=str(_write_manifest(
            tmp_path, [{"name": n, "test_cmd": "exit 0"} for n in names],
        )),
    )
    assert integration_gate_exit_code(passing) == runner.CI_EXIT_CLEAN


# R1/AC2 (P16): final.json carries integration_gate with per_repo/gate_passed.
def test_final_json_integration_gate_field(tmp_path):
    names = _make_repos(tmp_path, 2)
    entries = [{"name": n, "test_cmd": "exit 0"} for n in names]
    manifest = _write_manifest(tmp_path, entries)

    result = run_integration_gate(str(tmp_path), manifest_path=str(manifest))
    payload = runner.ensure_final_payload(
        verdict="APPROVED", integration_gate=result,
    )

    out_dir = tmp_path / "out"
    jsonio.write_final_json(
        str(out_dir), payload["verdict"],
        **{k: v for k, v in payload.items() if k != "verdict"},
    )
    final = json.loads((out_dir / "final.json").read_text())

    gate = final["integration_gate"]
    assert gate["gate_passed"] is True
    assert isinstance(gate["per_repo"], list)
    assert len(gate["per_repo"]) == 2
    assert isinstance(gate["gate_duration_s"], (int, float))

    # A failing gate flips the derived status to infrastructure_error, not
    # a plain rejection, mirroring the exit-code contract from R1/AC1.
    failing_entries = [
        {"name": n, "test_cmd": "exit 1" if n == "repo0" else "exit 0"}
        for n in names
    ]
    failing_result = run_integration_gate(
        str(tmp_path), manifest_path=str(_write_manifest(tmp_path, failing_entries)),
    )
    failing_payload = runner.ensure_final_payload(
        verdict="APPROVED", integration_gate=failing_result,
    )
    assert failing_payload["integration_gate"]["gate_passed"] is False
    assert failing_payload["status"] == "infrastructure_error"
