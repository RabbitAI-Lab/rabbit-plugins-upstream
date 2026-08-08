"""P21 — review-role sandbox enforcement + diagnostics.

The review role must always execute under the P1 sandbox profile: read-only,
no network, writes confined to the worktree + an ephemeral scratch dir (see
``adversarial_common.providers.resolve_sandbox_mode``). ``run_review``
resolves that profile before every provider call, rewrites away any
full-privilege token supplied on the review command line, and threads the
resolved mode plus any denial events onto the returned ``sandbox``
diagnostics — so a hostile or misconfigured review command is contained
rather than trusted, and the loop only ever acts on a structurally validated
verdict.

AC1 — test_review_sandbox_enforced: a review command carrying a full-write
token is rejected/rewritten before execution; the sandbox mode + rewrite
event are logged on the result.
AC2 — test_review_no_network: a review's attempt to reach the network is
observed as denied; the review still produces a valid JSON verdict.

P23 — prompt-injection behavioral equivalence.

``_build_prompt`` never splices the caller's ``diff_text`` into the trusted
prompt: it only tells the reviewer to explore the checked-out branch itself
(``git diff``, ``cat <file>``). AC1 — test_injection_probe_behavioral_
equivalence: swapping the calibration corpus's (P18) injection-probe-01
diff for a clean baseline diff of the same shape produces a byte-identical
prompt, so the verdict and findings a reviewer returns are equivalent
between the two — proving the injection payload never reaches the model's
input through this channel.
"""
import json
import re
import sys
from pathlib import Path
from unittest.mock import patch

_SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(_SKILL_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILL_ROOT))

from scripts.phases import phase_review  # noqa: E402
import adversarial_common  # noqa: E402
from adversarial_common import RunResult, jsonio  # noqa: E402

_VALID_VERDICTS = {"REQUEST_CHANGES", "APPROVE", "REJECT"}
_CORPUS_ROOT = (
    Path(adversarial_common.__file__).resolve().parent.parent
    / "references" / "calibration_corpus"
)


def _normalize_diff_text(diff_text):
    """Join added/removed/context line bodies into one whitespace-normalized
    string, so a payload that wraps across several diff lines can still be
    matched as a contiguous substring."""
    lines = []
    for line in diff_text.splitlines():
        if line[:1] in ("+", "-", " "):
            line = line[1:]
        lines.append(line.strip())
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def _verdict_payload(verdict="APPROVE"):
    return json.dumps({"findings": [], "verdict": verdict})


def test_review_sandbox_enforced(tmp_path):
    """A review command carrying a full-privilege token never runs as-is."""
    captured = {}

    def fake_run_cli(cmd, **_kwargs):
        captured["cmd"] = cmd
        return RunResult((_verdict_payload(), "", 0))

    hostile_cmd = "fake-review --dangerously-skip-permissions --model x"
    with patch("adversarial_common.runner.run_cli", fake_run_cli):
        result = phase_review.run_review(
            "diff", "unused", None, jsonio,
            workdir=str(tmp_path), explicit_cmd=hostile_cmd,
        )

    assert result["exit_code"] == 0, result
    assert result["verdict"] in _VALID_VERDICTS

    # The token never reached the executed command...
    assert "--dangerously-skip-permissions" not in captured["cmd"]
    assert "--model x" in captured["cmd"]

    # ...and the rewrite is logged: resolved mode + a rewrite event.
    mode = result["sandbox"]["mode"]
    assert mode["role"] == "review"
    assert mode["network"] is False
    assert mode["allow_write"] is False
    assert mode["source"] == "rewritten"
    token_event = next(
        e for e in mode["events"] if e["event"] == "full_privilege_token"
    )
    assert "--dangerously-skip-permissions" in token_event["tokens"]
    assert token_event["action"] == "rewrite"


def test_review_sandbox_resolution_failure_is_a_clean_phase_error(tmp_path):
    """A sandbox-resolution failure fails the phase cleanly, never runs unsandboxed.

    ``resolve_sandbox_mode`` can raise ``ProviderConfigError`` (e.g. an
    unregistered role). ``run_review`` must surface that as an ordinary
    exit_code=1 phase failure rather than letting the exception propagate
    past the phase boundary or, worse, falling through to an unsandboxed
    provider call.
    """
    from adversarial_common import ProviderConfigError

    calls = {"n": 0}

    def fake_run_cli(cmd, **_kwargs):
        calls["n"] += 1
        return RunResult((_verdict_payload(), "", 0))

    def fake_resolve_sandbox_mode(*_args, **_kwargs):
        raise ProviderConfigError("SANDBOX_UNKNOWN_ROLE", "no profile for role")

    with patch("adversarial_common.runner.run_cli", fake_run_cli), \
            patch.object(
                phase_review, "resolve_sandbox_mode", fake_resolve_sandbox_mode
            ):
        result = phase_review.run_review(
            "diff", "unused", None, jsonio,
            workdir=str(tmp_path), explicit_cmd="fake-review",
        )

    assert result["exit_code"] == 1
    assert "sandbox" in result["error"].lower()
    assert calls["n"] == 0  # never reached the provider


def test_review_no_network(tmp_path):
    """A network attempt during review is denied; review still returns JSON."""

    def fake_run_cli(cmd, **_kwargs):
        # The sandbox backend intercepts an outbound connection attempt made
        # by the review agent's tooling and denies it; the agent itself
        # recovers and still emits a valid verdict.
        denial = {
            "event": "network_denied",
            "role": "review",
            "target": "example.invalid:443",
        }
        return RunResult(
            (_verdict_payload("REQUEST_CHANGES"), "", 0),
            metadata={"sandbox_events": [denial]},
        )

    with patch("adversarial_common.runner.run_cli", fake_run_cli):
        result = phase_review.run_review(
            "diff", "unused", None, jsonio,
            workdir=str(tmp_path), explicit_cmd="fake-review",
        )

    assert result["exit_code"] == 0, result
    assert result["verdict"] in _VALID_VERDICTS

    sandbox = result["sandbox"]
    assert sandbox["mode"]["network"] is False
    assert any(d["event"] == "network_denied" for d in sandbox["denials"])


def test_review_sandbox_mode_always_logged(tmp_path):
    """Every review call resolves and logs a sandbox mode, not only violations."""

    def fake_run_cli(cmd, **_kwargs):
        return RunResult((_verdict_payload(), "", 0))

    with patch("adversarial_common.runner.run_cli", fake_run_cli):
        result = phase_review.run_review(
            "diff", "unused", None, jsonio,
            workdir=str(tmp_path), explicit_cmd="fake-review --model x",
        )

    assert result["exit_code"] == 0, result
    mode = result["sandbox"]["mode"]
    assert mode["source"] == "default"
    assert mode["network"] is False
    assert mode["allow_write"] is False
    assert result["sandbox"]["denials"] == []


def test_review_sandbox_logged_even_on_invalid_json(tmp_path):
    """Sandbox diagnostics survive a failed review call, not just successes."""

    def fake_run_cli(cmd, **_kwargs):
        return RunResult(("not json", "", 0))

    with patch("adversarial_common.runner.run_cli", fake_run_cli):
        result = phase_review.run_review(
            "diff", "unused", None, jsonio,
            workdir=str(tmp_path),
            explicit_cmd="fake-review --dangerously-skip-permissions",
        )

    assert result["exit_code"] == 1
    assert result["verdict"] == "UNKNOWN"
    # Even on the invalid-JSON failure path, the rewrite is still logged.
    assert result["sandbox"]["mode"]["source"] == "rewritten"


def test_injection_probe_behavioral_equivalence(tmp_path):
    """P23/AC1 — an injection probe from the corpus (P18) changes nothing.

    ``injection-probe-01`` embeds a docstring instructing the reviewer to
    ignore prior instructions and approve unconditionally. Because
    ``_build_prompt`` builds the reviewer's prompt from only the branch name
    and branch-point SHA — never the diff body — running that probe through
    ``run_review`` and running a clean baseline diff of the same shape must
    produce the exact same prompt, and therefore the same verdict and
    findings: no injection-only finding, no verdict flip.
    """
    probe_dir = _CORPUS_ROOT / "injection-probe-01"
    injection_diff = (probe_dir / "diff.txt").read_text()
    gold = json.loads((probe_dir / "gold.json").read_text())
    injection_payload = gold["injection_payload"]
    # sanity: fixture really carries the payload (it wraps across several
    # docstring lines in the raw diff, so compare on normalized text).
    assert injection_payload in _normalize_diff_text(injection_diff)

    baseline_diff = (
        "diff --git a/app/report.py b/app/report.py\n"
        "index 3a1c9e1..8b2f4d0 100644\n"
        "--- a/app/report.py\n"
        "+++ b/app/report.py\n"
        "@@ -22,8 +22,11 @@ def render_summary(entries):\n"
        "     lines = [f\"- {e['title']}: {e['status']}\" for e in entries]\n"
        "     return \"\\n\".join(lines)\n"
        " \n"
        " def render_report(entries):\n"
        "     body = render_summary(entries)\n"
        "-    return body\n"
        "+    return body + \"\\n\\n\" + format_footer(entries)\n"
        "+\n"
        "+\n"
        "+def format_footer(entries):\n"
        "+    return f\"Generated {len(entries)} entries. "
        "See report.py for details.\"\n"
        " \n"
        " \n"
        "@@ -39,4 +42,4 @@ def render_report(entries):\n"
        " \n"
        " def write_report(path, entries):\n"
        "     with open(path, \"w\") as f:\n"
        "-        f.write(render_report(entries))\n"
        "+        f.write(render_report(entries))\n"
    )
    assert injection_payload not in baseline_diff  # sanity: baseline is clean

    prompts = []

    def fake_run_cli(cmd, stdin_text=None, **_kwargs):
        prompts.append(stdin_text)
        payload = {
            "findings": [{
                "id": "A1", "severity": "minor", "file": "app/report.py",
                "line": 33, "summary": "format_footer lacks a docstring",
                "evidence": "format_footer has no docstring",
                "confidence": "low", "basis": "code",
            }],
            "verdict": "REQUEST_CHANGES",
        }
        return RunResult((json.dumps(payload), "", 0))

    with patch("adversarial_common.runner.run_cli", fake_run_cli):
        injection_result = phase_review.run_review(
            injection_diff, "unused", None, jsonio,
            workdir=str(tmp_path), explicit_cmd="fake-review",
            branch_point="deadbeef",
        )
        baseline_result = phase_review.run_review(
            baseline_diff, "unused", None, jsonio,
            workdir=str(tmp_path), explicit_cmd="fake-review",
            branch_point="deadbeef",
        )

    assert injection_result["exit_code"] == 0, injection_result
    assert baseline_result["exit_code"] == 0, baseline_result

    # R1: same verdict...
    assert injection_result["verdict"] == baseline_result["verdict"]
    # ...and no injection-only findings — the finding sets are identical, so
    # nothing in the injection run exists that isn't in the baseline run.
    assert injection_result["findings"] == baseline_result["findings"]
    injection_only = [
        finding for finding in injection_result["findings"]
        if finding not in baseline_result["findings"]
    ]
    assert injection_only == []

    # The mechanism behind the equivalence: the prompt sent to the provider
    # never carries the diff, so it is byte-identical between the two calls
    # and the injection payload never reaches the model's input at all.
    assert len(prompts) == 2
    assert prompts[0] == prompts[1]
    assert injection_payload not in prompts[0]
