#!/usr/bin/env python3
"""Adversarial Plan — git-native orchestrator.

PLAN -> CHALLENGE -> (REVISE -> VERIFY)^N, on a dedicated ``plan/<feature>/<N>``
branch. One model (plan-writer) writes ``plan.md`` from a ``spec.md`` (and
optional review findings), another (plan-challenger) challenges it; the writer
revises, the challenger verifies. On approval the branch is squash-merged into
the parent; otherwise a ``[REJECTED]`` marker commit is recorded.

Phase logic lives in scripts/phases/*; the shared engine (gitops, providers,
jsonio) lives in the adversarial-common sibling skill. This file only wires
phases together and maps verdicts to exit codes (same layout as
adversarial-spec's adversarial_spec.py, which mirrors adversarial-code-loop).

Optional modes (P17):
  --deep-research   run bounded external research after preflight
  --delegated       delegate high-complexity specs to worker decomposition
  --html            render an HTML report after final.json
  --ci              CI-friendly output (no banners, plain stderr, stable codes)
  --fail-on         set failure conditions (findings, severity, verdict, …)

Exit codes:
  0 APPROVED — plan squash-merged into the parent branch (or left on its
               branch with --no-merge)
  1 infrastructure failure (phase crash, git error, interrupt)
  2 usage error (bad flags, missing/empty spec, unparseable findings)
  3 REJECT   — findings unresolved after max-loops

In --ci mode, the shared lifecycle maps the persisted final verdict to stable
CI exit codes.

The machine-readable contract is <out>/<feature>/final.json; the produced
``plan.md`` is a human/agent-readable implementation plan — adversarial-code-loop
does not currently consume it automatically, see
references/run-plan-steps-without-plan-mode.md for the manual hand-off.
"""
import argparse
import dataclasses
import html as _html
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
# skill root (for `scripts.phases.*`) and the adversarial-common sibling skill
# (for `adversarial_common.*`) must both be importable.
sys.path.insert(0, str(_SCRIPTS_DIR.parent))
sys.path.insert(0, str(_SCRIPTS_DIR.parent.parent / "adversarial-common"))

from adversarial_common import (
    FinishPolicy,
    GitSetupPolicy,
    NoProviderAvailable,
    ProviderConfigError,
    QuotaResolver,
    RestorePolicy,
    RetrospectivePolicy,
    banner,
    ci_exit_from_final,
    collect_provider_history,
    costs,
    ensure_finding_ids,
    finish_pipeline,
    gates,
    gitops,
    jsonio,
    load_provider_config,
    phase_failure,
    positive_int,
    record_phase,
    restore_git,
    run_contract_gate,
    run_phase_cmd,
    setup_git,
    unresolved_findings,
    write_json,
)
from adversarial_common.providers import resolve_role_cmd
from adversarial_common.runner import (
    CI_EXIT_INFRASTRUCTURE,
    ci_mode, ci_print,
    run_delegated, run_research,
)
from scripts.phases import (extract_frontmatter, phase_challenge, phase_plan,
                            phase_revise, phase_verify)

EXIT_APPROVED = 0
EXIT_INFRA = 1
EXIT_USAGE = 2
EXIT_REJECTED = 3

DEFAULT_DEV_CMD = "pi --provider zai --model glm-5.2"
DEFAULT_REVIEW_CMD = "pi --provider deepseek --model deepseek-v4-pro"
DEFAULT_RESEARCH_CMD = "pi --provider deepseek --model deepseek-v4-pro"

# Complexity delegation threshold (R5 "high" tier).
_DELEGATE_COMPLEXITY = "high"
_FORCE_PROVIDER_ROLES = frozenset({"challenger", "verify", "writer"})

def _provider_call_args(args, role, explicit_cmd):
    """Return provider controls shared by every invocation of *role*."""
    return {
        "explicit_cmd": explicit_cmd,
        "force": bool(getattr(args, "force", False)),
        "force_provider": getattr(args, "_force_providers", {}).get(role),
    }


_GIT_SETUP_POLICY = GitSetupPolicy(
    prefix="plan",
    gitignore_entry=".adversarial-plan/",
)
_RESTORE_POLICY = RestorePolicy(reporter=ci_print)
_RETROSPECTIVE_POLICY = RetrospectivePolicy(
    reporter=ci_print,
    infrastructure_exit=EXIT_INFRA,
)


# --- HTML report renderer (--html) ---------------------------------------------

_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Adversarial Plan — {feature}</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ font-family: system-ui, sans-serif; max-width: 960px; margin: 2rem auto;
       padding: 0 1rem; line-height: 1.5; }}
h1 {{ border-bottom: 2px solid #ccc; padding-bottom: .3rem; }}
.verdict {{ font-weight: bold; font-size: 1.2rem; }}
.verdict.approved {{ color: #2a7d2a; }}
.verdict.rejected {{ color: #c0392b; }}
table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }}
th, td {{ border: 1px solid #aaa; padding: .4rem .6rem; text-align: left; }}
th {{ background: #f0f0f0; }}
details {{ margin: .5rem 0; }}
summary {{ cursor: pointer; font-weight: 600; }}
pre {{ background: #f5f5f5; padding: .5rem; overflow-x: auto; font-size: .85rem; }}
code {{ font-size: .9em; }}
</style>
</head>
<body>
<h1>Adversarial Plan — {feature}</h1>
{body}
<p><small>Generated {timestamp}</small></p>
</body>
</html>
"""


def _render_html(out_dir, feature):
    """Read final.json from *out_dir* and write report.html alongside it."""
    final_path = Path(out_dir) / "final.json"
    if not final_path.is_file():
        return
    try:
        final = json.loads(final_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return

    body_parts = [_html_status(final)]
    body_parts.append(_html_complexity(final))
    body_parts.append(_html_costs(final))
    body_parts.append(_html_artifact_links(out_dir))
    body_parts.append(_html_plan_preview(out_dir))

    html = _HTML_TEMPLATE.format(
        feature=_html.escape(feature),
        body="\n".join(body_parts),
        timestamp=_html.escape(datetime.now(timezone.utc).isoformat()),
    )
    (Path(out_dir) / "report.html").write_text(html, encoding="utf-8")


def _html_status(final):
    verdict = final.get("verdict", "UNKNOWN")
    css = "approved" if verdict == "APPROVED" else "rejected"
    lines = [
        f'<p class="verdict {css}">Verdict: {_html.escape(verdict)}</p>',
        "<table>",
        f"<tr><th>Verdict</th><td>{_html.escape(verdict)}</td></tr>",
        f"<tr><th>Loops</th><td>{final.get('loops', 0)}</td></tr>",
        f"<tr><th>Reason</th><td>{_html.escape(str(final.get('reason', '')))}</td></tr>",
        f"<tr><th>Branch</th><td><code>{_html.escape(final.get('branch', ''))}</code></td></tr>",
        f"<tr><th>Merged</th><td>{final.get('merged', False)}</td></tr>",
        f"<tr><th>Artifacts</th><td><code>{_html.escape(final.get('artifacts_dir', ''))}</code></td></tr>",
        "</table>",
    ]
    return "\n".join(lines)


def _html_complexity(final):
    cx = final.get("complexity")
    if not isinstance(cx, dict):
        return ""
    lines = [
        "<h2>Complexity</h2>",
        "<table>",
        f"<tr><th>Score</th><td>{cx.get('score', '')}</td></tr>",
        f"<tr><th>Level</th><td>{_html.escape(str(cx.get('level', '')))}</td></tr>",
        f"<tr><th>Recommended Agents</th><td>{cx.get('recommended_agents', '')}</td></tr>",
        "</table>",
    ]
    return "\n".join(lines)


def _html_costs(final):
    costs_data = final.get("costs")
    if not isinstance(costs_data, dict):
        return ""
    total = costs_data.get("total", {})
    lines = [
        "<h2>Cost Summary</h2>",
        "<table>",
        "<tr><th>Prompt Tokens</th><th>Completion Tokens</th><th>Est. Cost (USD)</th></tr>",
        f"<tr><td>{total.get('prompt_tokens', 0)}</td>"
        f"<td>{total.get('completion_tokens', 0)}</td>"
        f"<td>${total.get('est_cost_usd', 0):.6f}</td></tr>",
        "</table>",
    ]
    models = costs_data.get("models", {})
    if models:
        lines.append("<h3>By Model</h3>")
        lines.append("<table><tr><th>Model</th><th>Prompt</th><th>Completion</th><th>Cost</th></tr>")
        for model, usage in sorted(models.items()):
            lines.append(
                f"<tr><td><code>{_html.escape(model)}</code></td>"
                f"<td>{usage.get('prompt_tokens', 0)}</td>"
                f"<td>{usage.get('completion_tokens', 0)}</td>"
                f"<td>${usage.get('est_cost_usd', 0):.6f}</td></tr>"
            )
        lines.append("</table>")
    return "\n".join(lines)


def _html_artifact_links(out_dir):
    artifacts = sorted(Path(out_dir).glob("*.json"))
    if not artifacts:
        return ""
    lines = ["<h2>Artifacts</h2>", "<ul>"]
    for path in artifacts:
        if path.name == "final.json":
            continue
        lines.append(f"<li><code>{_html.escape(path.name)}</code></li>")
    lines.append("</ul>")
    return "\n".join(lines)


def _html_plan_preview(out_dir):
    plan_path = Path(out_dir).parent.parent  # out_dir/feature -> workdir
    plan_md = plan_path / "plan.md"
    if not plan_md.is_file():
        return ""
    try:
        text = plan_md.read_text(encoding="utf-8")
    except OSError:
        return ""
    # Truncate to roughly 8 KB for the preview
    preview = text[:8192]
    truncated = len(text) > 8192
    lines = [
        "<h2>Plan Preview</h2>",
        "<details open>",
        "<summary>plan.md</summary>",
        f"<pre>{_html.escape(preview)}</pre>",
    ]
    if truncated:
        lines.append("<p><em>(truncated)</em></p>")
    lines.append("</details>")
    return "\n".join(lines)


# --- PHASE 0: plan-specific lifecycle policy ----------------------------------


def _stage_inputs(workdir, spec_text, findings_text):
    """Materialise the inputs on the plan branch so the plan-writer (and the
    plan.md consumers) always find `spec.md` / `findings.json` in the workdir.

    Written unconditionally: a pre-existing dirty copy may have been stashed
    by PHASE 0, and an external --spec/--findings must land in the workdir.
    The plan-phase `commit_all` records them on the branch.
    """
    (Path(workdir) / "spec.md").write_text(spec_text, encoding="utf-8")
    if findings_text is not None:
        (Path(workdir) / "findings.json").write_text(findings_text,
                                                     encoding="utf-8")


def _plan_finish_payload(context):
    """Build the plan-only provider audit field for final.json."""
    return {
        "provider_history": context["state"].get("provider_history", []),
    }


def _write_plan_final(out_dir, verdict, payload):
    """Retain adversarial-plan's pre-P24 final.json field contract."""
    plan_payload = dict(payload)
    plan_payload.pop("conditions", None)
    plan_payload.setdefault("error", "")
    return write_json(
        out_dir, "final.json", {"verdict": verdict, **plan_payload},
    )


def _render_optional_html(context):
    if not context["args"].html:
        return
    try:
        _render_html(context["out_dir"], context["feature"])
    except Exception as exc:
        ci_print(f"! HTML report generation failed: {exc}")


def _plan_ci_exit(context):
    payload = context["final_payload"]
    if payload.get("infrastructure"):
        legacy_code = EXIT_INFRA
    elif context["verdict"] == "APPROVED":
        legacy_code = EXIT_APPROVED
    else:
        legacy_code = EXIT_REJECTED
    return ci_exit_from_final(
        context["out_dir"],
        legacy_code,
        fail_on_selector=context["args"].fail_on,
    )


_FINISH_POLICY = FinishPolicy(
    pipeline_name="Adversarial Plan",
    approval_label="plan",
    loop_label="Revise/verify loops",
    exit_by_verdict={"APPROVED": EXIT_APPROVED},
    rejected_exit=EXIT_REJECTED,
    infrastructure_exit=EXIT_INFRA,
    payload_builder=_plan_finish_payload,
    final_writer=_write_plan_final,
    post_write=_render_optional_html,
    ci_exit_mapper=_plan_ci_exit,
    reporter=ci_print,
)


def _no_provider_finish_payload(context):
    """Plan-only provider audit field, plus a fixed CI exit code recorded on
    final.json itself.

    finish_pipeline calls the payload builder after git finalization, so
    ``context["finalize_error"]`` already reflects whether finalization (not
    just provider exhaustion) failed. Recording the resulting code under
    ``ci.exit_code`` means a later remap of the persisted final.json (e.g.
    via ``ci_exit_from_final`` outside this process) reproduces the same
    code regardless of ``--fail-on``, instead of re-deriving it from the
    empty findings list on a finding-style REJECT verdict.
    """
    payload = _plan_finish_payload(context)
    exit_code = EXIT_INFRA if context.get("finalize_error") else EXIT_REJECTED
    payload["ci"] = {"exit_code": exit_code}
    return payload


def _no_provider_ci_exit(context):
    """NoProviderAvailable is an infrastructure failure: it must exit
    non-zero even under --ci --fail-on, which would otherwise filter an
    empty findings list down to a clean (0) exit.

    Reads the code back from ``final_payload["ci"]["exit_code"]`` (set by
    _no_provider_finish_payload) rather than hardcoding EXIT_REJECTED, so a
    git-finalization failure surfaced alongside provider exhaustion is
    reported as an infrastructure failure (EXIT_INFRA) instead of being
    masked as a plain rejection.
    """
    payload = context["final_payload"]
    ci_meta = payload.get("ci")
    if isinstance(ci_meta, dict) and isinstance(ci_meta.get("exit_code"), int):
        return ci_meta["exit_code"]
    return EXIT_INFRA if payload.get("infrastructure") else EXIT_REJECTED


# Same as _FINISH_POLICY except in --ci mode, where the no-provider outcome
# must always fail regardless of --fail-on (see _no_provider_ci_exit), and
# the payload records that fixed exit code on final.json itself (see
# _no_provider_finish_payload).
_NO_PROVIDER_FINISH_POLICY = dataclasses.replace(
    _FINISH_POLICY,
    payload_builder=_no_provider_finish_payload,
    ci_exit_mapper=_no_provider_ci_exit,
)


# --- deep research (R10) -------------------------------------------------------

def _build_research_queries(spec_text, feature):
    """Derive research queries from the spec's frontmatter and content."""
    queries = []
    fm_text = extract_frontmatter(spec_text)
    if fm_text:
        data, _ = jsonio.parse_frontmatter(fm_text)
        if isinstance(data, dict):
            # Use frontmatter keywords/summary
            name = data.get("name", "").strip()
            if name:
                queries.append(f"current best practices for implementing: {name}")
            summary = data.get("summary", data.get("description", "")).strip()
            if summary:
                queries.append(summary)

    # Fallback: first substantive heading as query
    if not queries:
        for line in spec_text.splitlines():
            stripped = line.strip().lstrip("#").strip()
            if stripped and stripped != "---" and len(stripped) > 10:
                queries.append(stripped)
                break
    if not queries:
        queries.append(f"implementation plan for: {feature}")
    return queries


def _run_deep_research(args, spec_text, dev_cmd, workdir, feature, out_dir, ledger):
    """Run bounded external research and merge findings into the pipeline."""
    research_cmd = (os.environ.get("ADVERSARIAL_RESEARCH_CMD", "")
                    or args.research_cmd
                    or dev_cmd)
    queries = _build_research_queries(spec_text, feature)
    ci_print(f"  Research: {len(queries)} query(s) via {research_cmd[:60]}")

    result = run_research(
        queries,
        provider_cmd=research_cmd,
        enabled=True,
        max_queries=args.research_max_queries,
        max_results=args.research_max_results,
        timeout=args.research_timeout,
        cwd=workdir,
        ledger=ledger,
    )
    write_json(out_dir, "00_research.json", result)
    if result is None:
        ci_print("  Research disabled (no provider configured)")
        return None

    status = result.get("status", "skipped")
    count = result.get("result_count", 0)
    ci_print(f"  Research: {status}, {count} finding(s)")
    if result.get("warnings"):
        for w in result["warnings"]:
            ci_print(f"    ! {w.get('message', str(w))}")
    return result


# --- delegated execution (R11) -------------------------------------------------

def _delegated_payload_text(payload):
    """Serialize a delegated stage payload without recursive result tuples."""
    if isinstance(payload, str):
        return payload

    def json_safe(value):
        if isinstance(value, dict):
            return {
                str(key): json_safe(item) for key, item in value.items()
                if key != "result"
            }
        if isinstance(value, (list, tuple)):
            return [json_safe(item) for item in value]
        if value is None or isinstance(value, (str, int, float, bool)):
            return value
        return str(value)

    return json.dumps(json_safe(payload), ensure_ascii=False, sort_keys=True)


def _delegated_phase_call(args, dev_cmd, workdir, ledger, phase):
    """Build a delegated call factory that resolves the writer at run time."""
    resolver = getattr(args, "_provider_resolver", None)
    # ``main`` normalizes the explicit override into dev_cmd.  In registry
    # mode an empty value must remain ``None`` so run_phase_cmd consults the
    # resolver; in legacy mode the selected/default command is supplied below
    # through the backward-compatible ``cmd`` argument.
    explicit_cmd = (dev_cmd or None) if resolver is not None else None
    provider_args = _provider_call_args(args, "writer", explicit_cmd)

    def call(payload):
        def invoke():
            command_args = {}
            if resolver is None:
                command_args["cmd"] = dev_cmd
            return run_phase_cmd(
                phase_name=phase,
                role="writer",
                workdir=workdir,
                resolver=resolver,
                stdin_text=_delegated_payload_text(payload),
                timeout=args.timeout,
                ledger=ledger,
                persona="plan-writer",
                max_retries=args.retries,
                **provider_args,
                **command_args,
            )

        return invoke

    return call


def _delegated_provider_history(result):
    """Collect provider decisions retained in delegated call records."""
    calls = []
    for key in ("decomposition", "fallback"):
        record = result.get(key)
        if isinstance(record, dict) and record.get("result") is not None:
            calls.append(record["result"])
    for record in result.get("workers", []):
        if isinstance(record, dict) and record.get("result") is not None:
            calls.append(record["result"])
    synthesis = result.get("synthesis")
    if isinstance(synthesis, dict) and synthesis.get("result") is not None:
        calls.append(synthesis["result"])
    return collect_provider_history(calls)

def _run_delegated_pipeline(args, spec_text, dev_cmd, workdir, feature,
                            out_dir, complexity, ledger):
    """Delegate a high-complexity spec to worker decomposition + synthesis.

    Uses runner.run_delegated which:
      1. Calls a decomposition model to split the spec into subtasks.
      2. Fans out workers (capped by complexity recommendation).
      3. Synthesizes surviving worker outputs into plan.md.
    """
    ci_print(f"  Delegating: complexity={complexity.get('level')} "
             f"(score={complexity.get('score')})")

    # Factories defer command selection until each stage starts. This keeps
    # delegated execution on the same quota-aware path as ordinary phases,
    # while an explicit --dev-cmd remains a writer-role bypass.
    decomposition_call = _delegated_phase_call(
        args, dev_cmd, workdir, ledger, "decomposition"
    )
    worker_call = _delegated_phase_call(
        args, dev_cmd, workdir, ledger, "worker"
    )
    synthesis_call = _delegated_phase_call(
        args, dev_cmd, workdir, ledger, "synthesis"
    )
    fallback_call = _delegated_phase_call(
        args, dev_cmd, workdir, ledger, "plan"
    )

    result = run_delegated(
        spec_text,
        decomposition_call=decomposition_call,
        worker_call=worker_call,
        synthesis_call=synthesis_call,
        fallback_call=fallback_call,
        concurrency=args.delegated_concurrency,
        max_concurrency=6,
        complexity=complexity,
    )
    result["provider_history"] = _delegated_provider_history(result)
    write_json(out_dir, "00_delegated.json", result)
    status = result.get("status", "unknown")
    ci_print(f"  Delegated: {status}, mode={result.get('mode', 'direct')}")
    if result.get("reason"):
        ci_print(f"    Reason: {result['reason']}")
    return result


# --- contract gate (F1) ---------------------------------------------------------

def _run_contract_gate(workdir):
    """Run the F1 ac-directive contract gate over spec.md in *workdir*.

    Returns ``(contract, blocked)`` where ``contract`` is the gate result
    dict (``settle``/``ac_status``/``failures``/``directives``) and
    ``blocked`` is True when its ``settle`` is not ``APPROVE``.
    """
    spec_path = Path(workdir) / "spec.md"
    contract = run_contract_gate(spec_path, workdir)
    blocked = contract["settle"] != "APPROVE"
    return contract, blocked


def _contract_fail_reason(contract):
    """Rejection reason naming only the ACs that actually failed.

    A2: filtered to failing ACs so a passing AC is never reported as failed.
    """
    failed = sorted(
        ac for ac, status in contract.get("ac_status", {}).items()
        if status != "pass"
    )
    acs = ",".join(failed) or "contract"
    return f"contract gate failed for: {acs}"


def _contract_extra(contract):
    """The per-AC contract block written into final.json (P5, observability)."""
    return {
        "settle": contract["settle"],
        "ac_status": contract["ac_status"],
        "failures": contract["failures"],
    }


# --- pipeline -------------------------------------------------------------------

def _pipeline(args, dev_cmd, review_cmd, workdir, feature, out_dir,
              spec_text, findings, findings_text, state, ci=True):
    """Run the full workflow. Returns the process exit code."""
    # --- pre-flight: context check (R3) ---
    ctx = gates.check_context("spec", spec_text)
    if not ctx["ok"]:
        ci_print(f"X Spec context check failed: {ctx['reason']}")
        return EXIT_USAGE

    # --- cost ledger + complexity (R4) ---
    ledger = costs.CostLedger()
    complexity = gates.estimate_complexity(spec_text)
    state.setdefault("provider_history", [])

    # --- deep research (R10) ---
    research_result = None
    if args.deep_research:
        ci_print("  [deep-research enabled]")
        research_result = _run_deep_research(
            args, spec_text, dev_cmd, workdir, feature, out_dir, ledger)
        # Merge research findings into the findings list
        if research_result and research_result.get("findings"):
            research_findings = research_result["findings"]
            if findings is None:
                findings = []
            findings = list(findings) + list(research_findings)
            ci_print(f"  Merged {len(research_findings)} research findings")

    # PHASE 0 — GIT SETUP (must run before delegated so state is populated)
    setup = setup_git(workdir, feature, state, policy=_GIT_SETUP_POLICY)
    state.update(setup)
    if setup["exit_code"] != 0:
        ci_print(f"X git setup failed: {setup.get('error', 'unknown error')}")
        return EXIT_INFRA
    state["feature"] = feature
    banner(
        f"PLAN BRANCH  {setup['branch']}  (from {setup['parent_branch']})",
        ci=ci,
    )
    jsonio.save_artifact(out_dir, "00_spec.txt", spec_text)
    if findings_text is not None:
        jsonio.save_artifact(out_dir, "00_findings.json", findings_text)
    _stage_inputs(workdir, spec_text, findings_text)

    # --- delegated execution (R11) ---
    delegated_result = None
    if args.delegated:
        ci_print("  [delegated mode enabled]")
        delegated_result = _run_delegated_pipeline(
            args, spec_text, dev_cmd, workdir, feature, out_dir,
            complexity, ledger)
        record_phase(state, "delegated", delegated_result, ledger)
        # If delegated succeeded, skip the normal pipeline and finalize
        if delegated_result.get("status") in ("synthesized", "complete"):
            merged = delegated_result.get("delegated", False)
            if merged and delegated_result.get("result"):
                # Worker output may contain plan.md — validate and commit
                plan_path = Path(workdir) / "plan.md"
                if plan_path.is_file():
                    try:
                        gitops.commit_all(workdir,
                                          f"plan: {feature} — delegated synthesis")
                    except gitops.GitError as exc:
                        ci_print(f"! Delegated git commit failed: {exc}")

            # A1: apply the F1 contract gate before approving a delegated
            # run, so a failing ac-directive blocks APPROVE here too.
            contract, contract_blocked = _run_contract_gate(workdir)
            if contract_blocked:
                verdict = "REJECT"
                reason = _contract_fail_reason(contract)
            else:
                verdict = "APPROVED"
                reason = ""
            cost_summary = ledger.summary()
            extra = {
                "costs": cost_summary,
                "complexity": complexity,
                "contract": _contract_extra(contract),
                "delegated": delegated_result,
            }
            if research_result is not None:
                extra["research"] = research_result
            return finish_pipeline(
                args, workdir, feature, out_dir, state, verdict,
                reason=reason, loops=delegated_result.get("tasks_dispatched", 0),
                extra=extra, policy=_FINISH_POLICY,
            )
        # Fallback: delegated fell through to direct — proceed with normal pipeline
        ci_print("  Delegation fell back to direct pipeline")

    # --- tag user-provided findings (R8) ---
    if findings is not None:
        for finding in findings:
            if isinstance(finding, dict):
                finding.setdefault("origin", "user")

    # PHASE 1 — PLAN
    banner("PLAN  (PLAN-WRITER)", ci=ci)
    plan = phase_plan.run_plan(spec_text, findings, dev_cmd, workdir,
                               args.timeout, feature,
                               getattr(args, "_provider_resolver", None),
                               **_provider_call_args(args, "writer", args.dev_cmd),
                               ledger=ledger, show_costs=args.show_costs,
                               max_retries=args.retries,
                               max_input_chars=args.max_input_chars,
                               max_output_chars=args.max_output_chars)
    write_json(out_dir, "01_plan.json", plan)
    record_phase(state, "plan", plan, ledger)
    if plan["exit_code"] != 0:
        if plan.get("exit_code") == EXIT_USAGE:
            ci_print(f"X plan validation failed: {plan.get('error', 'invalid plan')}")
            return EXIT_USAGE
        return phase_failure(
            "plan", plan, state, out_dir, policy=_RETROSPECTIVE_POLICY,
        )
    ci_print(f"  OK commit {plan.get('commit_sha', '')[:12]}")

    # PHASE 2 — CHALLENGE
    banner("CHALLENGE  (PLAN-CHALLENGER)", ci=ci)
    challenge = phase_challenge.run_challenge(
        review_cmd, workdir, args.timeout,
        getattr(args, "_provider_resolver", None),
        branch_point=state["branch_point"],
        **_provider_call_args(args, "challenger", args.review_cmd),
        ledger=ledger, show_costs=args.show_costs,
        max_retries=args.retries,
        max_input_chars=args.max_input_chars,
        max_output_chars=args.max_output_chars)
    write_json(out_dir, "02_challenge.json", challenge)
    record_phase(state, "challenge", challenge, ledger)
    if challenge["exit_code"] != 0:
        return phase_failure(
            "challenge", challenge, state, out_dir,
            policy=_RETROSPECTIVE_POLICY,
        )
    # R5: normalize epistemic labels on challenge findings
    jsonio.normalize_findings(challenge)
    challenge_findings = ensure_finding_ids(challenge.get("findings", []))
    verdict = challenge.get("verdict", "APPROVE")
    ci_print(f"  OK {len(challenge_findings)} findings — verdict {verdict}")

    # PHASES 3/4 — REVISE / VERIFY loop. An empty findings list only approves
    # when the challenger's verdict is also APPROVE.
    approved = not challenge_findings and verdict == "APPROVE"
    loops_run = 0
    for n in range(1, args.max_loops + 1):
        if approved:
            break
        loops_run = n

        banner(f"REVISE  (round {n}/{args.max_loops})", ci=ci)
        revise = phase_revise.run_revise(challenge_findings, dev_cmd, workdir,
                                         args.timeout, feature, n,
                                         getattr(args, "_provider_resolver", None),
                                         **_provider_call_args(
                                             args, "writer", args.dev_cmd),
                                         ledger=ledger, show_costs=args.show_costs,
                                         max_retries=args.retries,
                                         max_input_chars=args.max_input_chars,
                                         max_output_chars=args.max_output_chars)
        write_json(out_dir, f"03_revise_{n}.json", revise)
        record_phase(state, f"revise_{n}", revise, ledger)
        if revise["exit_code"] != 0:
            return phase_failure(
                f"revise_{n}", revise, state, out_dir,
                policy=_RETROSPECTIVE_POLICY,
            )

        banner(f"VERIFY  (round {n}/{args.max_loops})", ci=ci)
        verify = phase_verify.run_verify(
            challenge_findings, review_cmd, workdir, args.timeout,
            getattr(args, "_provider_resolver", None),
            branch_point=state["branch_point"],
            **_provider_call_args(args, "verify", args.review_cmd),
            ledger=ledger, show_costs=args.show_costs,
            max_retries=args.retries,
            max_input_chars=args.max_input_chars,
            max_output_chars=args.max_output_chars)
        write_json(out_dir, f"04_verify_{n}.json", verify)
        record_phase(state, f"verify_{n}", verify, ledger)
        if verify["exit_code"] != 0:
            return phase_failure(
                f"verify_{n}", verify, state, out_dir,
                policy=_RETROSPECTIVE_POLICY,
            )
        # R5: normalize epistemic labels on verify results
        jsonio.normalize_findings({"findings": verify.get("results", [])})

        results = verify.get("results", [])
        remaining = unresolved_findings(challenge_findings, results)
        ci_print(f"  Verdict {verify.get('verdict')} — "
                 f"{len(challenge_findings) - len(remaining)}"
                 f"/{len(challenge_findings)} settled")
        if verify.get("verdict") == "APPROVE" and results and not remaining:
            approved = True
            break
        # Narrow to the still-open findings for the next round; if the verifier
        # rejected overall while marking everything settled (contradiction),
        # keep the current list so the next round sees real content.
        if remaining:
            challenge_findings = remaining

    # R1: F1 contract gate — a failing ac-directive blocks APPROVE. Invoked
    # after CHALLENGE/VERIFY settle the findings, before the final verdict;
    # a spec with no directives settles APPROVE vacuously (no-op here).
    contract, contract_blocked = _run_contract_gate(workdir)
    if contract_blocked:
        approved = False

    # R4: record costs + complexity in final.json
    cost_summary = ledger.summary()
    if approved:
        verdict = "APPROVED"
        reason = ""
    else:
        verdict = "REJECT"
        if contract_blocked:
            reason = _contract_fail_reason(contract)
        else:
            reason = f"findings unresolved after {args.max_loops} loops"
    extra = {
        "costs": cost_summary,
        "complexity": complexity,
        # contract gate per-AC results (P5), derived for observability
        "contract": _contract_extra(contract),
    }
    if research_result is not None:
        extra["research"] = research_result
    if delegated_result is not None:
        extra["delegated"] = delegated_result
    return finish_pipeline(
        args, workdir, feature, out_dir, state, verdict,
        reason=reason, loops=loops_run, extra=extra, policy=_FINISH_POLICY,
    )


# --- CLI --------------------------------------------------------------------------

def _force_provider_value(value):
    """argparse type for repeatable ``ROLE:ALIAS`` provider overrides."""
    role, separator, alias = value.partition(":")
    role = role.strip().lower()
    alias = alias.strip()
    if not separator or role not in _FORCE_PROVIDER_ROLES or not alias:
        allowed = ", ".join(sorted(_FORCE_PROVIDER_ROLES))
        raise argparse.ArgumentTypeError(
            f"expected <role>:<alias> with role in: {allowed}"
        )
    return role, alias


def _force_provider_map(values):
    """Validate repeatable overrides and return one alias per role."""
    result = {}
    for role, alias in values:
        if role in result:
            raise ValueError(f"--force-provider specified more than once for {role}")
        result[role] = alias
    return result


def build_parser():
    p = argparse.ArgumentParser(
        description="Adversarial Plan "
                    "(PLAN -> CHALLENGE -> (REVISE -> VERIFY)^N, git-native)")
    p.add_argument("--spec", default=None,
                   help="spec.md to plan (default: <workdir>/spec.md)")
    p.add_argument("--findings", default=None,
                   help="Optional findings.json from a review")
    p.add_argument("--dev-cmd", default=None,
                   help=f"plan-writer command (default: $APLAN_DEV_CMD or "
                        f"'{DEFAULT_DEV_CMD}')")
    p.add_argument("--review-cmd", default=None,
                   help=f"plan-challenger command (default: $APLAN_REVIEW_CMD "
                        f"or '{DEFAULT_REVIEW_CMD}')")
    p.add_argument(
        "--provider-config", default=None, metavar="PATH",
        help="provider registry YAML (env: ADVERSARIAL_PROVIDER_CONFIG)",
    )
    p.add_argument(
        "--force", action="store_true",
        help="skip quota checks and select each role's primary provider",
    )
    p.add_argument(
        "--force-provider", action="append", default=[],
        type=_force_provider_value, metavar="ROLE:ALIAS",
        help="force an alias for one role; repeat for multiple roles",
    )
    p.add_argument("--workdir", default=".", help="Target directory (default: .)")
    p.add_argument("--max-loops", type=positive_int, default=2)
    p.add_argument("--feature", default=None,
                   help="Branch/artifact name (default: spec filename)")
    p.add_argument("--timeout", type=positive_int, default=600,
                   help="Per-subprocess timeout (s)")
    p.add_argument("--out", default=".adversarial-plan", help="Artifacts directory")
    p.add_argument("--no-merge", action="store_true",
                   help="On approval, leave the plan branch unmerged")
    p.add_argument("--show-costs", action="store_true",
                   help="Print per-phase cost breakdown to stderr")
    p.add_argument("--retries", type=positive_int, default=3,
                   help="Max CLI retries per phase call (default: 3)")
    p.add_argument("--max-input-chars", type=positive_int, default=None,
                   help="Cap prompt input chars per phase call")
    p.add_argument("--max-output-chars", type=positive_int, default=None,
                   help="Cap provider output chars per phase call")

    # P17: Optional modes
    p.add_argument("--html", action="store_true",
                   help="Render an HTML report after final.json (R9)")
    p.add_argument("--ci", action="store_true",
                   help="CI-friendly output: no banners, plain stderr, stable exit codes (R10)")
    p.add_argument("--fail-on", default=None,
                   help="Failure conditions (e.g. 'findings,severity:blocker') (R10)")
    p.add_argument("--deep-research", action="store_true",
                   help="Run bounded external research after preflight (R11)")
    p.add_argument("--research-cmd", default=None,
                   help="Research provider command (default: dev-cmd or $ADVERSARIAL_RESEARCH_CMD)")
    p.add_argument("--research-max-queries", type=positive_int, default=5,
                   help="Max research queries (default: 5)")
    p.add_argument("--research-max-results", type=positive_int, default=5,
                   help="Max research results (default: 5)")
    p.add_argument("--research-timeout", type=positive_int, default=60,
                   help="Per-query research timeout in seconds (default: 60)")
    p.add_argument("--delegated", action="store_true",
                   help="Delegate high-complexity specs to worker decomposition (R12)")
    p.add_argument("--delegated-concurrency", type=positive_int, default=None,
                   help="Max concurrent delegated workers (default: complexity recommendation)")
    return p


def _derive_feature(args, spec_text):
    """Feature name: --feature > spec filename stem > frontmatter name >
    first heading line.

    A stem of exactly ``spec`` (the conventional filename) carries no
    information, so the frontmatter/heading fallbacks are used instead.
    """
    raw = args.feature or ""
    if not raw and args.spec:
        stem = Path(args.spec).stem
        if stem.lower() != "spec":
            raw = stem
    if not raw:
        fm = extract_frontmatter(spec_text) or ""
        for line in fm.splitlines():
            key, sep, value = line.partition(":")
            if sep and key.strip() == "name":
                raw = value.strip().strip("\"'")
                break
    if not raw:
        for line in spec_text.splitlines():
            stripped = line.strip().lstrip("#").strip()
            if stripped and stripped != "---":
                raw = stripped
                break
    return gitops.sanitize_feature_name(raw)


def _load_findings(path):
    """Read + parse review findings. Returns ``(findings, raw_text, error)``.

    Accepts either a bare JSON array of findings or an object with a
    ``findings`` array (the adversarial-review final.json shape).
    """
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return None, None, f"could not read findings {path}: {exc}"
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, None, f"findings {path} is not valid JSON: {exc}"
    if isinstance(payload, dict):
        payload = payload.get("findings")
    if not isinstance(payload, list):
        return None, None, (f"findings {path} must be a JSON array or an "
                            f"object with a 'findings' array")
    return payload, raw, None


def main(argv=None):
    args = build_parser().parse_args(argv)

    try:
        args._force_providers = _force_provider_map(args.force_provider)
        args._provider_config = load_provider_config(args.provider_config)
        if args._provider_config is None:
            args._provider_resolver = None
        else:
            if not args._provider_config.quota_cmd:
                raise ProviderConfigError(
                    "PROVIDER_CONFIG_QUOTA_CMD_REQUIRED",
                    "quota_cmd is required when adversarial-plan uses a provider registry",
                )
            args._provider_resolver = QuotaResolver(
                args._provider_config, args._provider_config.quota_cmd
            )
    except (ProviderConfigError, TypeError, ValueError) as exc:
        ci_print(f"X invalid provider configuration: {exc}", enabled=True)
        return EXIT_USAGE

    workdir = str(Path(args.workdir).resolve())
    if not os.path.isdir(workdir):
        ci_print(f"X Workdir not found: {args.workdir}", enabled=args.ci)
        return EXIT_USAGE

    spec_path = Path(args.spec) if args.spec else Path(workdir) / "spec.md"
    try:
        spec_text = spec_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        ci_print(f"X Could not read spec {spec_path}: {exc}", enabled=args.ci)
        return EXIT_USAGE
    if not spec_text.strip():
        ci_print(f"X Empty spec: {spec_path}", enabled=args.ci)
        return EXIT_USAGE

    findings, findings_text = None, None
    if args.findings:
        findings, findings_text, err = _load_findings(args.findings)
        if err:
            ci_print(f"X {err}", enabled=args.ci)
            return EXIT_USAGE

    ok, info = gitops.ensure_git_available()
    if not ok:
        ci_print(f"X {info}", enabled=args.ci)
        return EXIT_INFRA

    if args._provider_config is None:
        dev_cmd = resolve_role_cmd("dev", args.dev_cmd, "APLAN_DEV_CMD",
                                   DEFAULT_DEV_CMD)
        review_cmd = resolve_role_cmd(
            "review", args.review_cmd, "APLAN_REVIEW_CMD", DEFAULT_REVIEW_CMD
        )
    else:
        # Registry commands are selected immediately before each phase. Only
        # explicit legacy flags are retained here as per-role bypasses.
        dev_cmd = (args.dev_cmd or "").strip()
        review_cmd = (args.review_cmd or "").strip()

    feature = _derive_feature(args, spec_text)
    if not feature:
        ci_print("X Could not derive a feature name; pass --feature", enabled=args.ci)
        return EXIT_USAGE

    out_base = Path(args.out)
    if not out_base.is_absolute():
        out_base = Path(workdir) / out_base
    out_dir = out_base / feature
    out_dir.mkdir(parents=True, exist_ok=True)

    provider_mode = "registry" if args._provider_resolver is not None else "legacy"
    ci_print(f"\n{'#' * 60}\n  ADVERSARIAL PLAN\n"
             f"  Feature: {feature}\n  Max loops: {args.max_loops}\n"
             f"  Findings input: {'yes' if findings is not None else 'no'}\n"
             f"  Provider mode: {provider_mode}\n{'#' * 60}",
             enabled=not args.ci)

    state = {}
    code = EXIT_INFRA
    try:
        with ci_mode(enabled=args.ci):
            code = _pipeline(args, dev_cmd, review_cmd, workdir, feature,
                             out_dir, spec_text, findings, findings_text, state,
                             ci=args.ci)
    except KeyboardInterrupt:
        ci_print("\nX Interrupted — restoring workdir (plan branch kept)", enabled=args.ci)
        code = CI_EXIT_INFRASTRUCTURE if args.ci else EXIT_INFRA
    except NoProviderAvailable as exc:
        ci_print(f"X no provider available for role '{exc.role}'", enabled=True)
        aliases = set(exc.snapshots) | set(exc.reasons)
        for alias in sorted(aliases):
            snapshot = json.dumps(
                exc.snapshots.get(alias, {}), sort_keys=True, default=str
            )
            ci_print(
                f"  {alias}: {exc.reasons.get(alias, 'ineligible')}; "
                f"snapshot={snapshot}", enabled=True,
            )
        decision = getattr(exc, "provider_decision", None)
        if isinstance(decision, dict):
            state.setdefault("provider_history", []).append(dict(decision))
        # Route through the shared finish_pipeline so --html / --fail-on and
        # final.md formatting stay consistent with the approve/reject path.
        snapshots = json.loads(json.dumps(exc.snapshots, default=str))
        reasons = dict(exc.reasons)
        code = finish_pipeline(
            args, workdir, feature, out_dir, state,
            verdict="REJECT", reason="no provider available", loops=0,
            extra={"provider_snapshots": snapshots, "provider_reasons": reasons},
            policy=_NO_PROVIDER_FINISH_POLICY,
        )
    except gitops.GitError as exc:
        ci_print(f"\nX git error: {exc}", enabled=args.ci)
        code = CI_EXIT_INFRASTRUCTURE if args.ci else EXIT_INFRA
    finally:
        restore_git(workdir, state, out_dir, policy=_RESTORE_POLICY)

    # In non-CI mode, fold CI exit codes back to historic 0/1/2/3
    if not args.ci and code >= 10:
        code = EXIT_INFRA

    return code


if __name__ == "__main__":
    sys.exit(main())
