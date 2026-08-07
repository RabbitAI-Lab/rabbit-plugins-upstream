"""Checks command overrides and provider-registry review wiring.

No LLM is invoked — `main()` resolution is exercised with the review run
stubbed out, and role routing is exercised with phase runners recorded.
"""
import ast
import json
import shlex
import sys
import threading
from pathlib import Path

import pytest

import adversarial_review as review


_SKILL_ROOT = Path(__file__).resolve().parents[1]
_ROLE_ENV_VARS = (
    "ACR_REVIEW_CMD",
    "ACR_A_CMD",
    "ACR_B_CMD",
    "ACR_SYNTH_CMD",
    "ACR_ORCHESTRATOR_CMD",
    "ACR_WORKER_CMD",
)


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for var in _ROLE_ENV_VARS:
        monkeypatch.delenv(var, raising=False)


@pytest.fixture
def get_review_final(tmp_path):
    """Return a file path with sufficient content for a review to pass gating."""
    p = tmp_path / "reviewable.py"
    p.write_text("x" * 200)
    return p


def _fenced_blocks(path):
    """Return Markdown fenced blocks without depending on source line numbers."""
    parts = path.read_text().split("```")
    assert len(parts) % 2 == 1, f"unclosed Markdown fence in {path}"
    return parts[1::2]


def test_orchestrator_uses_shared_lifecycle_without_git_finalization():
    """P26 keeps review policy shared while isolated worktrees stay local."""
    tree = ast.parse(
        (_SKILL_ROOT / "scripts" / "adversarial_review.py").read_text()
    )
    local_definitions = {
        node.name for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    removed_duplicates = {
        "_threshold_overrides",
        "_preflight_source",
        "_ci_exit",
        "_positive_arg",
        "_non_negative_arg",
    }
    assert local_definitions.isdisjoint(removed_duplicates)

    shared_attributes = {
        node.attr for node in ast.walk(tree)
        if isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "pipeline_base"
    }
    assert {
        "preflight",
        "ci_exit_from_final",
        "positive_int",
        "non_negative_int",
    }.issubset(shared_attributes)
    assert shared_attributes.isdisjoint({
        "setup_git", "restore_git", "finish_pipeline",
    })


# --- documentation invariants ----------------------------------------------

def test_skill_exit_table_documents_context_blocked_constant():
    skill = (_SKILL_ROOT / "SKILL.md").read_text()

    assert review.EXIT_CONTEXT_BLOCKED == review.runner.CI_EXIT_CONTEXT_BLOCKED
    assert f"| `{review.EXIT_CONTEXT_BLOCKED}` |" in skill
    assert "EXIT_CONTEXT_BLOCKED" in skill


def test_recovery_doc_does_not_instruct_an_unsupported_resume_flag():
    resume_flag = "--" + "resume"
    recovery = (
        _SKILL_ROOT / "references" / "manual-recovery-procedure.md"
    ).read_text()

    assert resume_flag not in recovery
    with pytest.raises(SystemExit) as exc_info:
        review.parse_args(["--file", "x.py", resume_flag])
    assert exc_info.value.code == 2


def test_documentation_preserves_symmetric_cross_review_contract():
    docs = {
        path.relative_to(_SKILL_ROOT).as_posix(): " ".join(
            path.read_text().split()
        )
        for path in _SKILL_ROOT.rglob("*.md")
    }
    all_docs = "\n".join(docs.values())

    # Both default command routing and review targets must remain mutual.
    assert "A reviews B" in docs["SKILL.md"]
    assert "B reviews A" in docs["SKILL.md"]
    assert "Architect command reviews the Inspector's findings" in docs[
        "references/cross-review-flags.md"
    ]
    assert "Inspector command reviews the Architect's findings" in docs[
        "references/cross-review-flags.md"
    ]
    assert "CROSS A→B" in docs["references/monitoring-background-reviews.md"]
    assert "CROSS B→A" in docs["references/monitoring-background-reviews.md"]

    # Guard against the superseded self-review model and its artifact names.
    for obsolete in (
        "each model validates its own work",
        "03_cross_a_on_b.json",
        "04_cross_a_on_b_round2.json",
        "CROSS A→B round 2",
        "Second pass, often faster",
    ):
        assert obsolete not in all_docs

    monitoring = docs["references/monitoring-background-reviews.md"]
    assert "03_cross_1.txt" in monitoring
    assert "04_cross_2.txt" in monitoring


@pytest.mark.parametrize("doc_name", ["SKILL.md", "README.md"])
def test_fenced_documentation_commands_do_not_use_rejected_yolo_flag(doc_name):
    yolo_flag = "--" + "yolo"

    assert all(
        yolo_flag not in block
        for block in _fenced_blocks(_SKILL_ROOT / doc_name)
    )


# --- parse_args surface -----------------------------------------------------

def test_parse_args_accepts_role_flags():
    args = review.parse_args([
        "--diff", "x.diff",
        "--a-cmd", "CMDA", "--b-cmd", "CMDB", "--synth-cmd", "CMDS",
    ])
    assert (args.a_cmd, args.b_cmd, args.synth_cmd) == ("CMDA", "CMDB", "CMDS")


def test_parse_args_accepts_provider_registry_flags():
    args = review.parse_args([
        "--diff", "x.diff", "--provider-config", "providers.yaml",
        "--force", "--force-provider", "review:fast",
        "--force-provider", "arbiter:careful",
    ])

    assert args.provider_config == "providers.yaml"
    assert args.force is True
    assert args.force_provider == [
        ("review", "fast"), ("arbiter", "careful"),
    ]


def test_parse_args_role_flags_default_to_none():
    args = review.parse_args(["--diff", "x.diff"])
    assert args.a_cmd is None and args.b_cmd is None and args.synth_cmd is None


# --- main() resolution: flag > env > --review-cmd fallback -------------------

def _run_main_capturing_args(monkeypatch, tmp_path, extra_argv):
    """Run main() with the review itself stubbed; return the resolved args."""
    captured = {}

    def fake_run(source, args):
        captured["args"] = args
        return "APPROVE"

    valid_diff = (
        "diff --git a/x.py b/x.py\n--- a/x.py\n+++ b/x.py\n"
        "@@ -1 +1 @@\n-old\n+new\n"
    )
    monkeypatch.setattr(review, "build_diff_source", lambda p: {
        "code_text": valid_diff,
        "context_text": valid_diff,
        "context_kind": "diff",
        "diff_text": valid_diff,
        "project_dir": None,
    })
    monkeypatch.setattr(review, "run_adversarial_review", fake_run)
    diff = tmp_path / "x.diff"
    diff.write_text("--- a\n+++ b\n")
    rc = review.main(["--diff", str(diff), *extra_argv])
    assert rc == review.EXIT_OK
    return captured["args"]


def test_main_resolves_a_cmd_override_and_defaults_rest(monkeypatch, tmp_path):
    args = _run_main_capturing_args(
        monkeypatch, tmp_path, ["--review-cmd", "DEFR", "--a-cmd", "CMDA"])
    assert args.review_cmd == "DEFR"
    assert args.a_cmd == "CMDA"
    assert args.b_cmd == "DEFR"
    assert args.synth_cmd == "DEFR"


def test_main_unset_flags_all_fall_back_to_review_cmd(monkeypatch, tmp_path):
    args = _run_main_capturing_args(monkeypatch, tmp_path, ["--review-cmd", "DEFR"])
    assert (args.a_cmd, args.b_cmd, args.synth_cmd) == ("DEFR", "DEFR", "DEFR")


def test_main_env_vars_override_review_cmd_default(monkeypatch, tmp_path):
    monkeypatch.setenv("ACR_B_CMD", "ENVB")
    monkeypatch.setenv("ACR_SYNTH_CMD", "ENVS")
    args = _run_main_capturing_args(monkeypatch, tmp_path, ["--review-cmd", "DEFR"])
    assert args.a_cmd == "DEFR"
    assert args.b_cmd == "ENVB"
    assert args.synth_cmd == "ENVS"


def test_main_flag_beats_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv("ACR_A_CMD", "ENVA")
    args = _run_main_capturing_args(
        monkeypatch, tmp_path, ["--review-cmd", "DEFR", "--a-cmd", "CMDA"])
    assert args.a_cmd == "CMDA"


# --- run_adversarial_review routes each role to its resolved command ---------

def test_roles_receive_their_resolved_commands(monkeypatch, tmp_path):
    calls = []
    response = json.dumps({"verdict": "APPROVE", "findings": []})
    hidden_default = "HIDDEN_DEFAULT_WRAPPER"

    def fake_parallel(parallel_calls, concurrency, max_concurrency):
        results = []
        for role, invoke in parallel_calls:
            result = invoke()
            results.append({
                "label": role,
                "ok": True,
                "stdout": response,
                "stderr": "",
                "returncode": 0,
                "result": result,
            })
        return results

    def fake_run_phase(
        phase_name, provider_role, workdir, resolver, *, explicit_cmd=None,
        **kwargs,
    ):
        calls.append((kwargs["persona"], provider_role, explicit_cmd))
        return response, "", 0

    monkeypatch.setattr(review.runner, "run_parallel", fake_parallel)
    monkeypatch.setattr(review.runner, "run_phase_cmd", fake_run_phase)
    monkeypatch.setattr(review, "DEFAULT_REVIEW_CMD", hidden_default)

    args = review.parse_args(["--diff", "x.diff", "--out", str(tmp_path / "out")])
    args.review_cmd = "DEFR"
    args.a_cmd = "CMDA"
    args.b_cmd = "CMDB"
    args.synth_cmd = "CMDS"
    source = {"project_dir": str(tmp_path), "code_text": "code", "diff_text": ""}

    verdict = review.run_adversarial_review(source, args)

    assert verdict == "APPROVE"
    assert calls == [
        ("architect", "review", "CMDA"),
        ("inspector", "review", "CMDB"),
        ("cross_review", "review", "CMDA"),
        ("cross_review", "review", "CMDB"),
        ("synthesis", "arbiter", "CMDS"),
    ]
    assert all(command != hidden_default for _, _, command in calls)


def test_provider_config_is_loaded_once_and_builds_one_resolver(
    monkeypatch, tmp_path,
):
    loaded_paths = []
    constructed = []

    class Config:
        quota_cmd = "quota-check"
        roles = {"review": (), "arbiter": ()}

    config = Config()
    resolver = object()

    def fake_load(path):
        loaded_paths.append(path)
        return config

    def fake_resolver(received_config, checker):
        constructed.append((received_config, checker))
        return resolver

    monkeypatch.setattr(review.providers, "load_provider_config", fake_load)
    monkeypatch.setattr(review, "QuotaResolver", fake_resolver)

    args = _run_main_capturing_args(
        monkeypatch, tmp_path,
        ["--provider-config", "providers.yaml"],
    )

    assert loaded_paths == ["providers.yaml"]
    assert constructed == [(config, "quota-check")]
    assert args._provider_resolver is resolver
    assert args.a_cmd is None and args.b_cmd is None and args.synth_cmd is None


@pytest.mark.parametrize(
    ("extra_argv", "missing_role"),
    [
        ([], "orchestrator"),
        (["--orchestrator-cmd", "orchestrate"], "worker"),
    ],
)
def test_delegated_registry_requires_each_delegated_command(
    monkeypatch, extra_argv, missing_role,
):
    class Config:
        quota_cmd = "quota-check"
        roles = {"review": (), "arbiter": ()}

    monkeypatch.setattr(
        review.providers, "load_provider_config", lambda path: Config(),
    )
    monkeypatch.setattr(review, "QuotaResolver", lambda config, checker: object())
    args = review.parse_args([
        "--file", "x.py", "--provider-config", "providers.yaml",
        "--delegated", *extra_argv,
    ])

    with pytest.raises(review.ProviderConfigError) as exc_info:
        review._resolve_commands(args)

    assert exc_info.value.code == "PROVIDER_CONFIG_DELEGATED_COMMAND_REQUIRED"
    assert f"delegated role '{missing_role}'" in exc_info.value.detail


def test_a_cmd_bypasses_architect_only(monkeypatch, tmp_path):
    response = json.dumps({"verdict": "APPROVE", "findings": []})
    resolved_roles = []
    executed_commands = []

    class Resolver:
        def resolve(self, role, **kwargs):
            resolved_roles.append(role)
            return review.runner.quota.ProviderDecision(
                alias=f"{role}-provider",
                command=f"echo {role}",
                quota_state="OK",
                fallback=False,
                reason="test selection",
                raw_snapshot={},
                forced=False,
                error=None,
            )

    def fake_run_cli(cmd, **kwargs):
        executed_commands.append(cmd)
        return review.runner.RunResult((response, "", 0))

    monkeypatch.setattr(review.runner, "run_cli", fake_run_cli)
    args = review.parse_args(["--diff", "x.diff", "--a-cmd", "echo architect"])
    args._ledger = review.CostLedger()
    args._provider_resolver = Resolver()
    args._provider_config = None
    args._force_providers = {}

    review._execute_role_phase(
        "architect", args.a_cmd, "input", args, str(tmp_path), "architect",
    )
    review._execute_role_phase(
        "inspector", None, "input", args, str(tmp_path), "inspector",
    )
    review._execute_role_phase(
        "cross_review", None, "input", args, str(tmp_path), "cross_review",
    )
    review._execute_role_phase(
        "synthesis", None, "input", args, str(tmp_path), "synthesis",
    )

    assert resolved_roles == ["review", "review", "arbiter"]
    assert executed_commands == [
        "echo architect", "echo review", "echo review", "echo arbiter",
    ]


def test_parallel_perspectives_share_resolver_cache(monkeypatch, tmp_path):
    response = json.dumps({"verdict": "APPROVE", "findings": []})

    class CachedResolver:
        def __init__(self):
            self.lock = threading.Lock()
            self.snapshot = None
            self.checker_calls = 0

        def resolve(self, role, **kwargs):
            with self.lock:
                if self.snapshot is None:
                    self.checker_calls += 1
                    self.snapshot = {"review-provider": {"used_pct": 10}}
            return review.runner.quota.ProviderDecision(
                alias="review-provider",
                command="echo review",
                quota_state="OK",
                fallback=False,
                reason="cached test selection",
                raw_snapshot=self.snapshot,
                forced=False,
                error=None,
            )

    monkeypatch.setattr(
        review.runner,
        "run_cli",
        lambda cmd, **kwargs: review.runner.RunResult((response, "", 0)),
    )
    resolver = CachedResolver()
    args = review.parse_args([
        "--diff", "x.diff", "--out", str(tmp_path / "out"),
        "--concurrency", "2",
    ])
    args.a_cmd = None
    args.b_cmd = None
    args._provider_resolver = resolver
    args._provider_config = None
    args._force_providers = {}
    args._ledger = review.CostLedger()
    args._calls = []
    args._artifacts = {}
    args._warnings = []

    review._run_initial_perspectives(
        "input", args, tmp_path / "out", str(tmp_path),
        {"recommended_agents": 2},
    )

    assert resolver.checker_calls == 1


def test_preflight_blocks_before_command_resolution_or_provider(tmp_path, monkeypatch):
    provider_calls = []

    def provider_started(*args, **kwargs):
        provider_calls.append((args, kwargs))
        raise AssertionError("provider must not start for blocked context")

    monkeypatch.setattr(review.runner, "run_cli", provider_started)
    monkeypatch.setattr(review.providers, "resolve_role_cmd", provider_started)
    diff = tmp_path / "empty.diff"
    diff.write_text("   \n")
    out = tmp_path / "out"

    code = review.main(["--diff", str(diff), "--out", str(out)])

    assert code == review.EXIT_CONTEXT_BLOCKED
    assert provider_calls == []
    final = json.loads((out / "final.json").read_text())
    assert final["status"] == "blocked"
    assert final["reason"] == "empty_input"
    assert final["thresholds"]["min_source_lines"] == 1
    assert final["calls"] == [] and final["costs"]["records"] == []


def test_threshold_env_is_audited_and_cli_flag_wins(tmp_path, monkeypatch):
    source = {
        "code_text": "x" * 20,
        "context_text": "x" * 20,
        "context_kind": "input",
        "diff_text": "",
        "project_dir": None,
    }
    monkeypatch.setattr(review, "build_file_source", lambda path: source)
    monkeypatch.setenv("ACR_MIN_CONTEXT_CHARS", "30")
    out = tmp_path / "blocked"

    blocked = review.main(["--file", "x.py", "--out", str(out)])

    assert blocked == review.EXIT_CONTEXT_BLOCKED
    final = json.loads((out / "final.json").read_text())
    assert final["reason"] == "below_min_chars"
    assert final["thresholds"]["min_chars"] == 30

    captured = {}
    monkeypatch.setattr(
        review, "run_adversarial_review",
        lambda _source, args: captured.setdefault("thresholds", args._context["thresholds"]),
    )
    passed = review.main([
        "--file", "x.py", "--min-chars", "10", "--min-tokens", "0",
        "--review-cmd", "provider", "--out", str(tmp_path / "passed"),
    ])
    assert passed == review.EXIT_OK
    assert captured["thresholds"]["min_chars"] == 10


@pytest.mark.parametrize("value", ["invalid", "-1"])
def test_shared_threshold_errors_remain_review_errors(
    tmp_path, monkeypatch, value,
):
    monkeypatch.setenv("ACR_MIN_CONTEXT_CHARS", value)
    args = review.parse_args([
        "--file", "x.py", "--out", str(tmp_path),
    ])
    source = {
        "code_text": "x" * 40,
        "context_text": "x" * 40,
        "context_kind": "input",
        "diff_text": "",
    }

    with pytest.raises(
        review.ReviewError,
        match=r"\$ACR_MIN_CONTEXT_CHARS must be a non-negative integer",
    ):
        review._source_gate(source, args)


@pytest.mark.parametrize(
    "flag,value",
    [
        ("--max-retries", "-1"),
        ("--max-agents", "0"),
        ("--research-timeout", "not-an-integer"),
    ],
)
def test_cli_uses_shared_integer_validators(flag, value):
    with pytest.raises(SystemExit) as exc_info:
        review.parse_args(["--file", "x.py", flag, value])

    assert exc_info.value.code == 2


def test_caps_costs_and_default_reviewers_survive_trivial_complexity(tmp_path, capsys):
    finding = {
        "id": "A1", "severity": "major", "file": "x.py", "line": 1,
        "summary": "unsafe edge", "evidence": "the branch is unchecked",
    }
    response = json.dumps({"verdict": "REQUEST_CHANGES", "findings": [finding]})
    command = shlex.join([sys.executable, "-c", f"print({response!r})"])
    source_file = tmp_path / "x.py"
    source_file.write_text("x" * 800)
    out = tmp_path / "out"

    code = review.main([
        "--file", str(source_file), "--out", str(out),
        "--review-cmd", command,
        "--max-input-chars", "3000", "--truncate-input", "--show-costs",
    ])

    assert code == review.EXIT_OK
    final = json.loads((out / "final.json").read_text())
    assert final["complexity"]["level"] == "trivial"
    assert final["complexity"]["recommended_agents"] == 1
    assert final["parallel"]["perspectives"] == ["architect", "inspector"]
    assert {call["persona"] for call in final["calls"][:2]} == {
        "architect", "inspector",
    }
    assert final["cap_events"] and all(
        event["kind"] == "input" for event in final["cap_events"]
    )
    assert final["costs"]["records"]
    assert {record["persona"] for record in final["costs"]["records"]} >= {
        "architect", "inspector", "cross_review", "synthesis",
    }
    assert all(record["estimated"] is True for record in final["costs"]["records"])
    assert final["finding_details"][0]["confidence"] == "low"
    assert final["finding_details"][0]["basis"] == "inference"
    assert final["epistemic_labels"]["combined"] == {"low/inference": 2}
    assert any(warning["code"] == "epistemic_label_defaulted"
               for warning in final["warnings"])
    assert "Estimated model costs:" in capsys.readouterr().err


def test_all_warnings_ignores_non_list_reviewer_values():
    args = type("Args", (), {"_warnings": [{"code": "runner_warning"}]})()
    payloads = {
        "architect": {"warnings": None},
        "inspector": {"warnings": {"code": "not_a_list"}},
        "other": {"warnings": [None, "bad", {"code": "reviewer_warning"}]},
    }

    assert review._all_warnings(args, payloads) == [
        {"code": "runner_warning"},
        {"code": "reviewer_warning"},
    ]


def test_shared_preflight_context_shape_matches_r1_contract():
    """R1: shared preflight returns the review context and attaches metadata."""
    source = {
        "code_text": "x" * 200,
        "context_text": "x" * 50,
        "context_kind": "brief",
        "diff_text": "",
    }
    args = review.parse_args(["--file", "tmp.py"])
    result = review._source_gate(source, args)
    context = result.context

    assert isinstance(result, review.pipeline_base.PreflightResult)
    assert result.ok is True
    assert context["ok"] is True
    assert "thresholds" in context
    thresholds = context["thresholds"]
    for key in ("min_chars", "min_tokens", "required_sections", "min_source_lines"):
        assert key in thresholds, f"thresholds missing {key!r}"
    assert args._context is context
    assert "level" in args._complexity


def test_shared_preflight_keeps_review_source_cap_policy_disabled(tmp_path):
    source = {
        "code_text": "x" * 200,
        "context_text": "x" * 200,
        "context_kind": "input",
        "diff_text": "",
    }
    args = review.parse_args([
        "--file", "tmp.py",
        "--out", str(tmp_path),
        "--max-input-chars", "10",
    ])

    result = review._source_gate(source, args)

    assert result.ok is True
    assert result.effective_text == source["context_text"]
    assert result.cap_events == []


def test_shared_preflight_context_below_threshold_rejects_and_flags(tmp_path):
    """R1: below-threshold context gate writes final.json before any provider."""
    source = {
        "code_text": "x",
        "context_text": "x",
        "context_kind": "input",
        "diff_text": "",
    }
    out = tmp_path / "out"
    args = review.parse_args(["--file", "tmp.py", "--out", str(out)])
    result = review._source_gate(source, args)
    context = result.context

    assert result.ok is False
    assert context["ok"] is False
    assert "min_chars" in context["reason"] or "below_min" in context["reason"]
    final = json.loads((out / "final.json").read_text())
    assert "warnings" not in final
    assert final["cap_events"] == []
    assert set(final["execution"]) == {
        "max_retries", "max_input_chars", "max_output_chars",
        "truncate_input", "show_costs", "concurrency",
        "max_concurrency", "max_agents",
    }


def test_r2_retry_and_cap_defaults_at_parse():
    """R2: retry/cap defaults are present and positive at CLI parse level."""
    args = review.parse_args(["--diff", "x.diff"])
    assert isinstance(args.max_retries, int) and args.max_retries == 3
    assert args.max_input_chars == review.runner.DEFAULT_MAX_INPUT_CHARS
    assert args.max_output_chars == review.runner.DEFAULT_MAX_OUTPUT_CHARS
    assert args.max_input_chars > 0
    assert args.max_output_chars > 0


def test_r2_cap_defaults_survive_main_entry(tmp_path, monkeypatch):
    """R2: cap defaults flow through main() and survive adaptive changes."""
    source = {
        "code_text": "x" * 40,
        "context_text": "x" * 40,
        "context_kind": "input",
        "diff_text": "",
        "project_dir": None,
    }
    captured = {}

    def fake_review(src, args, context=None):
        captured["max_retries"] = args.max_retries
        captured["max_input"] = args.max_input_chars
        captured["max_output"] = args.max_output_chars
        captured["truncate"] = args.truncate_input
        assert isinstance(args.max_retries, int) and args.max_retries >= 0
        assert args.max_input_chars >= 0
        assert args.max_output_chars >= 0
        return review.EXIT_OK

    monkeypatch.setattr(review, "build_file_source", lambda path: source)
    monkeypatch.setattr(review, "_review_source", fake_review)

    code = review.main(["--file", "x.py", "--out", str(tmp_path)])
    assert code == review.EXIT_OK
    assert captured["max_retries"] == 3
    assert captured["max_input"] == review.runner.DEFAULT_MAX_INPUT_CHARS
    assert captured["max_output"] == review.runner.DEFAULT_MAX_OUTPUT_CHARS
    assert captured["truncate"] is False


def test_r4_epistemic_labels_in_final_json_on_approve(tmp_path, monkeypatch):
    """R4: epistemic labels survive code-review pipeline; final.json carries them."""
    finding = {
        "id": "E1", "severity": "minor", "file": "x.py", "line": 1,
        "summary": "testing", "evidence": "code",
        "confidence": "medium", "basis": "code",
    }
    response = json.dumps({"verdict": "APPROVE", "findings": [finding]})
    command = shlex.join([sys.executable, "-c", f"print({response!r})"])
    source_file = tmp_path / "x.py"
    source_file.write_text("x" * 40)
    out = tmp_path / "out"

    code = review.main([
        "--file", str(source_file), "--out", str(out),
        "--review-cmd", command,
    ])

    assert code == review.EXIT_OK
    final = json.loads((out / "final.json").read_text())
    assert final["status"] == "complete"
    assert "epistemic_labels" in final
    labels = final["epistemic_labels"]
    for axis in ("confidence", "basis", "combined"):
        assert axis in labels, f"epistemic_labels missing {axis!r}"
    assert labels["combined"]["medium/code"] >= 1


def test_r5_final_json_required_shape_on_every_exit_path(tmp_path, monkeypatch):
    """R5: final.json always has verdict, status, costs, complexity fields."""
    base_fields = {"verdict", "status"}

    # Path 1: context blocked
    out_blocked = tmp_path / "blocked"
    source = {"code_text": "x", "context_text": "x", "context_kind": "input", "diff_text": ""}
    args_blocked = review.parse_args(["--file", "tmp.py", "--out", str(out_blocked)])
    review._source_gate(source, args_blocked)
    blocked = json.loads((Path(args_blocked.out) / "final.json").read_text())
    assert base_fields.issubset(blocked)
    assert blocked["status"] == "blocked"
    assert "costs" in blocked
    assert "complexity" in blocked

    # Path 2: error / infra
    out_err = tmp_path / "err"
    code = review.main(["--diff", str(tmp_path / "nonexistent.diff"), "--out", str(out_err)])
    assert code == review.EXIT_CONTEXT_BLOCKED
    # EXIT_CONTEXT_BLOCKED = 5: empty diff blocked by preflight.
    # An ACR-blocked exit writes final.json with status=blocked.

    # Path 3: success (already tested, but verify shape here)
    finding = {"id": "S1", "severity": "minor", "file": "x.py", "line": 1,
               "summary": "ok", "evidence": "code"}
    response = json.dumps({"verdict": "APPROVE", "findings": [finding]})
    command = shlex.join([sys.executable, "-c", f"print({response!r})"])
    sf = tmp_path / "sf.py"
    sf.write_text("x" * 40)
    out_ok = tmp_path / "ok"

    code = review.main([
        "--file", str(sf), "--out", str(out_ok),
        "--review-cmd", command,
    ])
    assert code == review.EXIT_OK
    final_ok = json.loads((out_ok / "final.json").read_text())
    assert base_fields.issubset(final_ok)
    assert final_ok["status"] == "complete"
    assert "costs" in final_ok
    assert final_ok["costs"]["total"]["est_cost_usd"] == 0.0
    assert "complexity" in final_ok


def test_r7_ci_exit_policy_in_final_json(get_review_final, tmp_path):
    """R7: CI mode elevates exit codes and embeds policy in final.json."""
    out = tmp_path / "ci_out"
    code = review.main([
        "--file", str(get_review_final),
        "--out", str(out),
        "--ci",
        "--fail-on", "findings",
        "--review-cmd", "echo '{\"verdict\":\"REQUEST_CHANGES\",\"findings\":[{\"id\":\"C1\",\"severity\":\"major\",\"file\":\"x.py\",\"line\":1,\"summary\":\"bug\",\"evidence\":\"code\"}]}'",
    ])
    assert code == review.runner.CI_EXIT_BLOCKING
    final = json.loads((out / "final.json").read_text())
    assert final["ci"]["enabled"] is True
    assert final["ci"]["exit_code"] == review.runner.CI_EXIT_BLOCKING
    assert "findings" in final["ci"]["fail_on"]


def test_persona_commands_survive_complexity_defaults(tmp_path, monkeypatch):
    """Explicit --a-cmd/--b-cmd/--synth-cmd survive complexity-adaptive defaults."""
    captured_cmds = {}
    source = {
        "code_text": "x" * 30000,
        "context_text": "x" * 30000,
        "context_kind": "input",
        "diff_text": "",
        "project_dir": None,
    }

    def fake_parallel(calls, concurrency, max_concurrency):
        response_json = json.dumps({"verdict": "APPROVE", "findings": []})
        results = []
        for role, invoke in calls:
            result = invoke()
            results.append({
                "label": role, "ok": True, "stdout": response_json,
                "stderr": "", "returncode": 0, "result": result,
            })
        return results

    def fake_run_phase(
        phase_name, provider_role, workdir, resolver, *, explicit_cmd=None,
        **kwargs,
    ):
        captured_cmds[kwargs["persona"]] = explicit_cmd
        return json.dumps({"verdict": "APPROVE", "findings": []}), "", 0

    monkeypatch.setattr(review.runner, "run_parallel", fake_parallel)
    monkeypatch.setattr(review.runner, "run_phase_cmd", fake_run_phase)
    captured_run_role = {}
    monkeypatch.setattr(
        review, "_run_role",
        lambda role, cmd, stdin_text, args, out, name, proj: captured_run_role.setdefault(
            role, []).append(cmd)
        or json.dumps({"verdict": "APPROVE", "findings": []}),
    )

    out = tmp_path / "out"
    args = review.parse_args([
        "--file", "x.py", "--out", str(out),
        "--a-cmd", "EXPLICIT_A",
        "--b-cmd", "EXPLICIT_B",
        "--synth-cmd", "EXPLICIT_S",
        "--review-cmd", "FALLBACK_DEFAULT",
    ])
    review._source_gate(source, args)
    review._resolve_commands(args)
    review.run_adversarial_review(source, args)

    assert captured_cmds.get("architect") == "EXPLICIT_A"
    assert captured_cmds.get("inspector") == "EXPLICIT_B"
    # synthesis must receive the explicit --synth-cmd
    assert captured_run_role.get("synthesis") == ["EXPLICIT_S"]


def test_parallel_partial_failures_write_final_json(tmp_path, monkeypatch):
    """R9: parallel partial failures produce final.json with error metadata."""
    source = {
        "code_text": "x" * 30000,
        "context_text": "x" * 30000,
        "context_kind": "input",
        "diff_text": "",
        "project_dir": None,
    }

    architect_response = json.dumps({"verdict": "APPROVE", "findings": []})

    def fake_parallel(calls, concurrency, max_concurrency):
        results = []
        for role, call_args in calls:
            if role == "architect":
                results.append({
                    "label": role, "ok": True,
                    "stdout": architect_response, "stderr": "", "returncode": 0,
                    "result": (architect_response, "", 0),
                })
            else:
                results.append({
                    "label": role, "ok": False,
                    "stdout": "", "stderr": "inspector crash", "returncode": 1,
                    "result": ("", "inspector crash", 1),
                })
        return results

    monkeypatch.setattr(review.runner, "run_parallel", fake_parallel)

    out = tmp_path / "out"
    args = review.parse_args([
        "--file", "x.py", "--out", str(out),
        "--review-cmd", "MOCK",
    ])
    review._source_gate(source, args)
    review._resolve_commands(args)

    with pytest.raises(SystemExit):
        review.run_adversarial_review(source, args)

    final = json.loads((out / "final.json").read_text())
    assert final["verdict"] == "ERROR"
    assert final["status"] == "failed"
    assert final["infrastructure"] is True
    assert any(call["ok"] is False and call["label"] == "02_inspector" 
               for call in final["calls"])


def test_output_cap_records_parse_warning_and_failed_call(tmp_path):
    response = json.dumps({"verdict": "APPROVE", "findings": []}) + "x" * 500
    command = shlex.join([sys.executable, "-c", f"print({response!r})"])
    source_file = tmp_path / "x.py"
    source_file.write_text("x" * 40)
    out = tmp_path / "out"

    with pytest.raises(SystemExit) as exc:
        review.main([
            "--file", str(source_file), "--out", str(out),
            "--review-cmd", command, "--max-output-chars", "80",
        ])

    assert exc.value.code == review.EXIT_INFRA
    final = json.loads((out / "final.json").read_text())
    assert final["status"] == "failed"
    assert final["cap_events"][0]["kind"] == "output"
    assert final["failures"][0]["label"] == "01_architect"
    assert "invalid reviewer JSON" in final["failures"][0]["error"]
    assert any(warning["code"] == "truncated_json_output"
               for warning in final["warnings"])


def test_valid_line_accepts_none_for_global_findings():
    from scripts import adversarial_review as ar
    assert ar._valid_line(None)          # project-wide finding (no line)
    assert ar._valid_line(42)            # integer line
    assert ar._valid_line("(global)")    # free-form marker
    assert not ar._valid_line("")        # empty string still rejected
    assert not ar._valid_line("   ")     # whitespace-only still rejected
    assert not ar._valid_line(3.14)      # non-int number rejected
