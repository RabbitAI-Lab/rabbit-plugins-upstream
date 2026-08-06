"""P7b — F1 contract gate wired into the plan pipeline (AC1, AC2, AC3)."""
import json
import re
import subprocess
import textwrap
from pathlib import Path

from conftest import VALID_PLAN, VALID_SPEC
from scripts import adversarial_plan as orch

# A reviewer that unconditionally approves — so the only thing that can block
# APPROVE is the contract gate.
APPROVE_REVIEWER = textwrap.dedent("""\
    import json, sys
    sys.stdin.read()
    print(json.dumps({"findings": [], "verdict": "APPROVE", "summary": "clean"}))
""")

WRITER_SCRIPT = textwrap.dedent("""\
    import pathlib, sys
    sys.stdin.read()
    pathlib.Path("plan.md").write_text('''{plan}''')
    print("plan.md written")
""")

# The passing spec: VALID_SPEC with an AC1 directive that greps for a token
# present in the plan the writer commits -> gate settles APPROVE. Proves the
# gate is wired and not spuriously rejecting.
_PASSING_BODY = VALID_SPEC.replace(
    '- AC1 (R1): running `demo` exits 0 and prints "ok".\n',
    '- AC1 (R1): running `demo` exits 0 and prints "ok".\n'
    '  ```ac-directive\n'
    '  ac: AC1\n'
    '  kind: grep\n'
    '  command: grep "Implementation Plan"\n'
    '  ```\n',
)

# The failing spec: same shape, but the directive greps for an anchored token
# absent from every tracked file. The pattern is anchored (^...$) so it cannot
# match its own command line, which gets staged/committed as spec.md — without
# the anchors grep would match that line and spuriously pass.
_FAILING_BODY = VALID_SPEC.replace(
    '- AC1 (R1): running `demo` exits 0 and prints "ok".\n',
    '- AC1 (R1): running `demo` exits 0 and prints "ok".\n'
    '  ```ac-directive\n'
    '  ac: AC1\n'
    '  kind: grep\n'
    '  command: grep "^zzz_absent_contract_token_zzz$"\n'
    '  ```\n',
)


def _run_pipeline(tmp_path, spec_text):
    workdir = tmp_path / "project"
    workdir.mkdir()
    writer = tmp_path / "writer.py"
    writer.write_text(WRITER_SCRIPT.format(plan=VALID_PLAN))
    reviewer = tmp_path / "reviewer.py"
    reviewer.write_text(APPROVE_REVIEWER)
    spec = tmp_path / "demo-feature.md"
    spec.write_text(spec_text)
    argv = [
        "--spec", str(spec),
        "--workdir", str(workdir),
        "--dev-cmd", f"python3 {writer}",
        "--review-cmd", f"python3 {reviewer}",
        "--max-loops", "1",
        "--timeout", "60",
    ]
    return workdir, orch.main(argv)


def test_failing_ac_blocks_approve(tmp_path):
    # AC1: the reviewer approves, but a failing ac-directive blocks APPROVE.
    workdir, code = _run_pipeline(tmp_path, _FAILING_BODY)
    assert code == orch.EXIT_REJECTED
    final = json.loads(
        (workdir / ".adversarial-plan" / "demo-feature" / "final.json")
        .read_text())
    assert final["verdict"] == "REJECT"
    # contract gate per-AC results land in final.json
    assert final["contract"]["settle"] == "REJECT"
    assert final["contract"]["ac_status"] == {"AC1": "fail"}
    assert final["contract"]["failures"][0]["ac"] == "AC1"


def test_passing_directive_still_approves(tmp_path):
    # Sanity: a directive that passes must not spuriously block APPROVE —
    # proves the gate is actually wired (not just hard-rejecting).
    workdir, code = _run_pipeline(tmp_path, _PASSING_BODY)
    assert code == orch.EXIT_APPROVED
    final = json.loads(
        (workdir / ".adversarial-plan" / "demo-feature" / "final.json")
        .read_text())
    assert final["verdict"] == "APPROVED"
    assert final["contract"]["settle"] == "APPROVE"
    assert final["contract"]["ac_status"] == {"AC1": "pass"}


def test_contract_fail_reason_names_only_failing_acs():
    # A2: a passing AC must not be labelled as failed in the reject reason.
    contract = {"ac_status": {"AC1": "pass", "AC2": "fail"}}
    assert orch._contract_fail_reason(contract) == "contract gate failed for: AC2"


def test_contract_fail_reason_fallback_when_no_ac_status():
    # No per-AC map (e.g. a parse-only failure) -> generic label, not a crash.
    assert orch._contract_fail_reason({}) == "contract gate failed for: contract"


def test_delegated_success_blocked_by_contract_gate(tmp_path, monkeypatch):
    # A1: a synthesized delegated run must still pass the F1 contract gate.
    # A failing ac-directive downgrades the verdict to REJECT, and both the
    # contract results and the delegated record land in final.json.
    workdir = tmp_path / "project"
    workdir.mkdir()
    spec = tmp_path / "demo-feature.md"
    spec.write_text(_FAILING_BODY)

    def fake_delegated(args, spec_text, dev_cmd, workdir, feature, out_dir,
                       complexity, ledger):
        # Worker produced a plan but ignored the AC -> gate must catch it.
        Path(workdir, "plan.md").write_text(VALID_PLAN)
        return {"status": "synthesized", "delegated": True,
                "result": "plan.md", "tasks_dispatched": 1}

    monkeypatch.setattr(orch, "_run_delegated_pipeline", fake_delegated)

    code = orch.main([
        "--spec", str(spec),
        "--workdir", str(workdir),
        "--dev-cmd", "true",
        "--review-cmd", "true",
        "--max-loops", "1",
        "--timeout", "60",
        "--delegated",
    ])
    assert code == orch.EXIT_REJECTED
    final = json.loads(
        (workdir / ".adversarial-plan" / "demo-feature" / "final.json")
        .read_text())
    assert final["verdict"] == "REJECT"
    assert final["reason"] == "contract gate failed for: AC1"
    assert final["contract"]["settle"] == "REJECT"
    assert final["contract"]["ac_status"] == {"AC1": "fail"}
    assert final["delegated"]["status"] == "synthesized"


def test_imports_contract_gate_from_adversarial_common():
    # AC2: the plan imports the contract gate from adversarial_common. The
    # import is a multi-line ``from adversarial_common import (...)`` block,
    # so check run_contract_gate is a name inside that block.
    source = Path(orch.__file__).read_text(encoding="utf-8")
    block = re.search(
        r"from\s+adversarial_common\s+import\s*\(([^)]*)\)",
        source, re.DOTALL,
    )
    assert block is not None, "missing `from adversarial_common import (...)`"
    assert re.search(r"\brun_contract_gate\b", block.group(1)), (
        "plan must import run_contract_gate from adversarial_common"
    )
