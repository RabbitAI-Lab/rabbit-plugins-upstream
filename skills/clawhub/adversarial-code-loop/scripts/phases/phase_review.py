"""
REVIEW phase: run REVIEW model with project access to the loop branch.

The reviewer checks the code on disk (checked out at loop branch HEAD).
They can read files directly and run ``git diff <branch-point>..HEAD`` to see
the cumulative change. Output is validated JSON findings.

``run_review(diff_text, review_cmd, providers, jsonio, workdir) -> dict``
"""
from collections.abc import Mapping
from typing import Any

from adversarial_common import (
    NoProviderAvailable,
    ProviderConfigError,
    gitops,
    resolve_sandbox_mode,
    run_phase_cmd,
)
from scripts.phases.runtime import (
    merge_provider_history,
    merge_runtime,
    merge_warnings,
    raise_no_provider_available,
)

__all__ = ["run_review"]

_VALID_VERDICTS = {"REQUEST_CHANGES", "APPROVE", "REJECT"}
_REQUIRED_FINDING_KEYS = {"id", "severity", "file", "line", "summary", "evidence"}


def _valid_line(line: Any) -> bool:
    return isinstance(line, int) or (isinstance(line, str) and line.isdigit())


def _validate(payload: Any) -> bool:
    """Lightweight v4 schema check. No jsonschema dependency."""
    if not isinstance(payload, dict):
        return False
    if payload.get("verdict") not in _VALID_VERDICTS:
        return False
    findings = payload.get("findings")
    if not isinstance(findings, list):
        return False
    for finding in findings:
        if not isinstance(finding, dict):
            return False
        if not _REQUIRED_FINDING_KEYS.issubset(finding.keys()):
            return False
        if not _valid_line(finding.get("line")):
            return False
    return True


def _candidate_command(
    review_cmd: str, resolver: Any, explicit_cmd: str | None
) -> str | None:
    """Return the literal command that will run unmediated by a resolver.

    Mirrors the ``cmd`` selection ``_attempt`` hands to ``run_phase_cmd``: an
    explicit command always wins; otherwise the legacy ``review_cmd`` is used
    only when no resolver is in play. A registry resolver picks its own
    command internally (from vetted config, not a raw string) and is out of
    reach here, so it yields no candidate to inspect.
    """
    if explicit_cmd is not None:
        return explicit_cmd
    if resolver is None:
        return review_cmd
    return None


def _build_prompt(diff_text: str, workdir: str, branch_point: str = "") -> str:
    """Build a prompt that tells the reviewer to explore the code on disk.

    The reviewer is in `workdir` (checked out at loop branch HEAD). They can:
    - Read any file from disk
    - Run ``git diff <branch-point>..HEAD`` to see the cumulative change
    """
    try:
        branch = gitops.get_current_branch(workdir or ".")
    except (gitops.GitError, OSError):
        branch = "(unknown)"

    diff_base = branch_point or "<branch-point>"
    return (
        f"You are reviewing code in a git branch. The working directory is "
        f"checked out at `{branch}` (the latest commit to review).\n\n"
        f"The branch-point SHA for this review is `{diff_base}`.\n"
        f"To see the cumulative change since that branch point, run:\n"
        f"  git diff {diff_base}..HEAD   — line-by-line diff\n\n"
        f"To see the full context of a file, read it from disk or use:\n"
        f"  cat <filepath>\n\n"
        f"Review the cumulative changes since `{diff_base}`. Each finding must "
        f"reference a real file and line visible in that diff. Do NOT report "
        f"pre-existing issues outside this branch's change.\n\n"
        f"Output ONLY valid JSON:\n"
        f'{{"findings": [{{"id": "A1", "severity": "blocker|major|minor|nit", '
        f'"file": "path", "line": 42, "summary": "...", '
        f'"evidence": "...", "confidence": "high|medium|low", '
        f'"basis": "spec|code|inference|external"}}], '
        f'"verdict": "REQUEST_CHANGES|APPROVE|REJECT"}}'
    )


def run_review(
    diff_text: str,
    review_cmd: str,
    resolver: Any,
    jsonio: Any,
    workdir: str = "",
    timeout: int = 600,
    branch_point: str = "",
    explicit_cmd: str | None = None,
    force: bool = False,
    force_provider: str | None = None,
    execution: Mapping[str, Any] | None = None,
    ledger: Any = None,
) -> dict:
    """
    Run REVIEW model with project access to the loop branch.

    The reviewer reads files directly from disk and runs git diff to see
    what changed since the branch point. Output JSON is validated against the
    v4 schema. Retries once on invalid JSON.

    Returns ``{"phase": "review", "findings": [...], "verdict": "...",
               "exit_code": 0, "infra": False,
               "sandbox": {"mode": {...}, "denials": [...]}}``.

    A verdict that fails structural validation (:func:`_validate`) — missing
    ``verdict``/``findings``, malformed findings, or JSON that never parses,
    even after the one retry — is an infrastructure failure, not a review
    decision: the dict comes back with ``exit_code: 1`` and ``infra: True``,
    which the loop must route to ``EXIT_INFRA`` rather than ever treating as
    APPROVE/REQUEST_CHANGES/REJECT.

    Before any provider call, the review role's command is resolved against
    the P1 sandbox profile (read-only, no network, writes confined to the
    worktree + an ephemeral scratch dir — see
    ``adversarial_common.providers.resolve_sandbox_mode``). A literal
    command carrying a full-privilege token (``--yolo``,
    ``--dangerously-skip-permissions``, ``--sandbox danger-full-access``, ...)
    is rewritten to drop it; the resolved mode and any rewrite are recorded
    on ``sandbox["mode"]`` regardless of outcome. Denial events the provider
    layer itself surfaces during execution (e.g. a blocked network attempt),
    if present in provider result metadata under ``sandbox_events``, are
    collected onto ``sandbox["denials"]``. The verdict is structurally
    validated (:func:`_validate`) before it is ever returned to the loop.
    """
    sandbox_diagnostics: dict[str, Any] = {}
    try:
        sandbox_mode = resolve_sandbox_mode(
            "review",
            command=_candidate_command(review_cmd, resolver, explicit_cmd),
            workdir=workdir,
            diagnostics=sandbox_diagnostics,
        )
    except ProviderConfigError as exc:
        return {
            "phase": "review", "exit_code": 1, "infra": True,
            "error": f"sandbox resolution failed: {exc}",
        }

    if sandbox_mode.source == "rewritten":
        safe_command = sandbox_mode.safe_command or ""
        if explicit_cmd is not None:
            explicit_cmd = safe_command
        elif resolver is None:
            review_cmd = safe_command

    def _sandbox_report(denials: list) -> dict:
        return {
            "mode": sandbox_mode.to_dict(),
            "denials": [dict(event) for event in denials],
        }

    prompt = _build_prompt(diff_text, workdir, branch_point)
    runtime_calls = []
    provider_results = []
    parse_warnings = []
    sandbox_denials: list = []

    def _attempt(prompt_text):
        execution_args = dict(execution or {})
        if execution is not None or ledger is not None:
            execution_args["phase"] = "review"
        if ledger is not None:
            execution_args["ledger"] = ledger
        command_args = {}
        if resolver is None and explicit_cmd is None:
            command_args["cmd"] = review_cmd
        provider_result = run_phase_cmd(
            phase_name="review",
            role="review",
            workdir=workdir,
            resolver=resolver,
            explicit_cmd=explicit_cmd,
            force=force,
            force_provider=force_provider,
            stdin_text=prompt_text,
            timeout=timeout,
            persona="critic",
            **command_args,
            **execution_args,
        )
        raise_no_provider_available(provider_result, "review")
        provider_results.append(provider_result)
        stdout, stderr, code = provider_result[:3]
        metadata = getattr(provider_result, "metadata", {})
        metadata_dict = dict(metadata) if isinstance(metadata, Mapping) else {}
        runtime_calls.append(metadata_dict)
        sandbox_denials.extend(
            event for event in metadata_dict.get("sandbox_events", [])
            if isinstance(event, Mapping)
        )
        if code != 0:
            return None, f"REVIEW exited {code}: {(stderr or '')[:200]}", stdout
        payload = jsonio.parse_json_output(stdout, warnings=parse_warnings)
        return payload, None, stdout

    try:
        payload, err, stdout = _attempt(prompt)
        if err:
            return {
                "phase": "review", "exit_code": 1, "infra": True, "error": err,
                "execution": merge_runtime(runtime_calls),
                "provider_history": merge_provider_history(provider_results),
                "sandbox": _sandbox_report(sandbox_denials),
            }
        if not _validate(payload):
            payload, err, stdout = _attempt(
                prompt + (
                    "\n\nIMPORTANT: Your response was not valid JSON. "
                    "Respond with ONLY valid JSON matching the schema."
                )
            )
            if err:
                return {
                    "phase": "review", "exit_code": 1, "infra": True,
                    "error": err,
                    "execution": merge_runtime(runtime_calls),
                    "provider_history": merge_provider_history(provider_results),
                    "sandbox": _sandbox_report(sandbox_denials),
                }
            if not _validate(payload):
                # Structurally invalid verdict after the retry: an
                # infrastructure failure, never a review decision. The loop
                # must route this to EXIT_INFRA and must not act on
                # "findings"/"verdict" below as if they were real output.
                return {
                    "phase": "review", "exit_code": 1, "infra": True,
                    "findings": [], "verdict": "UNKNOWN",
                    "error": "invalid JSON after retry", "stdout": stdout,
                    "warnings": parse_warnings,
                    "execution": merge_runtime(runtime_calls),
                    "provider_history": merge_provider_history(provider_results),
                    "sandbox": _sandbox_report(sandbox_denials),
                }
        return {
            "phase": "review", "exit_code": 0, "infra": False,
            "findings": payload["findings"], "verdict": payload["verdict"],
            "warnings": merge_warnings(payload, parse_warnings),
            "epistemic_labels": jsonio.epistemic_distribution(payload["findings"]),
            "stdout": stdout,
            "execution": merge_runtime(runtime_calls),
            "provider_history": merge_provider_history(provider_results),
            "sandbox": _sandbox_report(sandbox_denials),
        }
    except NoProviderAvailable:
        raise
    except Exception as exc:
        return {
            "phase": "review", "exit_code": 1, "infra": True, "error": str(exc),
            "sandbox": _sandbox_report(sandbox_denials),
        }
