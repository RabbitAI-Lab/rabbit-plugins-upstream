#!/usr/bin/env python3
"""Adversarial Code Review — multi-perspective review of a diff or codebase.

Runs two independent reviewers (Architect, Inspector), two cross-review passes
(cross-1: A reviews B's findings, cross-2: B reviews A's findings), and a final
synthesis, then writes per-phase artifacts and a machine-readable ``final.json``.

The shared engine (providers, runner, jsonio, gitops) and the personas live in
the sibling ``adversarial-common`` skill; this file only wires the review flow.

Sources (mutually exclusive):
  --diff FILE        review a unified-diff file
  --dir DIR          review every file under a directory
  --file FILE        review a single file
  --project-dir DIR  review an existing project directory (reviewer explores it)
  --diff-git         review ``<base>..HEAD`` inside an isolated git worktree

--diff-git options:
  --base BRANCH      base ref (default: --base > $ACR_BASE > main > master)
  --feature NAME     feature slug for the worktree path (default: current branch)
  --allow-fallback   if worktree creation fails, fall back to --project-dir on the
                     current working directory with a prominent stderr warning
                     (default: exit 2 instead of silently falling back)

Exit codes:
  0  review complete
  1  pipeline / infrastructure failure (CLI crash, git error)
  2  review setup failure (missing base, worktree failure)
  5  primary context blocked before provider use

The machine-readable contract is ``<out>/final.json``.
"""
import argparse
import json
import os
import subprocess
import sys
import traceback
import re
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
# skill root (for `scripts.*`) and the adversarial-common sibling skill (for
# `adversarial_common.*`) must both be importable.
sys.path.insert(0, str(_SCRIPTS_DIR.parent))
sys.path.insert(0, str(_SCRIPTS_DIR.parent.parent / "adversarial-common"))

from adversarial_common import (  # noqa: E402
    CostLedger,
    ProviderConfigError,
    QuotaResolver,
    estimate_complexity,
    gitops,
    jsonio,
    pipeline_base,
    persona_path,
    providers,
    run_contract_gate,
    runner,
)
from adversarial_common import report as html_report  # noqa: E402

EXIT_OK = 0
EXIT_INFRA = 1
EXIT_NOTHING = 2
EXIT_CONTEXT_BLOCKED = runner.CI_EXIT_CONTEXT_BLOCKED

# ponytail: one review command drives all five LLM passes. Override per-run with
# --review-cmd or persistently with $ACR_REVIEW_CMD. No model is named here — the
# CLI's own default is the right model.
DEFAULT_REVIEW_CMD = providers.default_wrapper_cmd()

# Directories never fed to the reviewer as "code".
_SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules", ".pytest_cache",
              ".adversarial-review", ".adversarial-loop"}

_VALID_VERDICTS = {"APPROVE", "REQUEST_CHANGES", "REJECT"}
_REQUIRED_FINDING_KEYS = {"id", "severity", "file", "line", "summary", "evidence"}

_ROLE_LABELS = {
    "architect": "01_architect",
    "inspector": "02_inspector",
}
_PHASE_LABELS = {
    "01_architect": "architect",
    "02_inspector": "inspector",
    "03_cross_1": "cross_review_1",
    "04_cross_2": "cross_review_2",
    "05_synthesis": "synthesis",
}
_FORCE_PROVIDER_ROLES = frozenset({"review", "arbiter"})
_THRESHOLD_ENV = {
    "min_chars": (
        "ACR_MIN_CONTEXT_CHARS", "ACR_CONTEXT_MIN_CHARS", "ACR_MIN_CHARS",
        "ADVERSARIAL_MIN_CHARS",
    ),
    "min_tokens": (
        "ACR_MIN_CONTEXT_TOKENS", "ACR_CONTEXT_MIN_TOKENS", "ACR_MIN_TOKENS",
        "ADVERSARIAL_MIN_TOKENS",
    ),
    "min_source_lines": (
        "ACR_MIN_SOURCE_LINES", "ADVERSARIAL_MIN_SOURCE_LINES",
    ),
}


def _json_safe(value):
    """Return bounded runner metadata in a JSON-serializable shape.

    Delegated records retain tuple-like ``result`` objects for internal stage
    chaining. ``final.json`` already carries their stdout/stderr/return code,
    so omitting that duplicate field avoids non-serializable metadata.
    """
    if isinstance(value, dict):
        return {
            str(key): _json_safe(item)
            for key, item in value.items()
            if key != "result"
        }
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _write_final(args, verdict, **extra):
    """Write final.json, then render the optional report from that artifact."""
    if getattr(args, "html", False):
        extra.setdefault("html_report", str(Path(args.out) / "report.html"))
    if getattr(args, "ci", False):
        policy = runner.parse_fail_on(args.fail_on)
        exit_code = runner.ci_exit_code(
            verdict,
            findings=extra.get("finding_details", []),
            fail_on_selector=args.fail_on,
            infrastructure=bool(extra.get("infrastructure")),
            context_blocked=bool(extra.get("context_blocked")),
        )
        extra.setdefault("ci", {
            "enabled": True,
            "fail_on": sorted(policy),
            "exit_code": exit_code,
        })

    final_path = jsonio.write_final_json(args.out, verdict, **extra)
    if getattr(args, "html", False):
        html_report.render_html_report(final_path)
    return final_path


def _write_setup_error(args, error):
    """Persist a complete operational failure without changing legacy exits."""
    return _write_final(
        args,
        "ERROR",
        status="failed",
        infrastructure=True,
        error=str(error),
        finding_details=[],
        warnings=[],
        calls=[],
        failures=[],
        costs=CostLedger().summary(),
        artifacts={},
    )


class ReviewError(Exception):
    """Recoverable review-setup error (empty diff, missing base, etc.).

    Maps to exit code 2 (nothing to review / cannot proceed).
    """


class PhaseFailure(Exception):
    """A provider phase failed after its execution evidence was recorded."""

    def __init__(self, label: str, code: int, stderr: str) -> None:
        detail = str(stderr or "").strip()
        message = f"{label} failed with exit code {code}"
        if detail:
            message += f": {detail[:500]}"
        super().__init__(message)
        self.label = label
        self.code = code
        self.stderr = stderr


# ---------------------------------------------------------------------------
# --diff-git helpers
# ---------------------------------------------------------------------------

def _ref_exists(workdir, ref):
    """True if *ref* resolves to a commit (local branch, tag, SHA, or remote)."""
    proc = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"],
        capture_output=True, text=True, cwd=workdir,
    )
    return proc.returncode == 0


def resolve_base(workdir, flag_value):
    """Pick the base ref: --base > $ACR_BASE > main > master (first existing).

    De-duplicates so a flag equal to the env value is only tried once.
    """
    candidates = []
    if flag_value:
        candidates.append(flag_value)
    env_base = os.environ.get("ACR_BASE")
    if env_base:
        candidates.append(env_base)
    candidates += ["main", "master"]
    tried = []
    for cand in candidates:
        if cand in tried:
            continue
        tried.append(cand)
        if _ref_exists(workdir, cand):
            return cand
    raise ReviewError(f"no base branch found; tried: {', '.join(tried)}")


def next_worktree_path(feature, root="/tmp"):
    """First free ``<root>/review-<feature>-<N>`` path (git worktree add needs it).

    *root* defaults to ``/tmp`` but is parameterized so the logic is testable
    without touching the real ``/tmp``.
    """
    prefix = f"review-{feature}-"
    n = 1
    while True:
        path = Path(root) / f"{prefix}{n}"
        if not path.exists():
            return path
        n += 1


def _worktree_add(workdir, path, commit):
    subprocess.run(
        ["git", "worktree", "add", str(path), commit],
        check=True, capture_output=True, text=True, cwd=workdir,
    )


def _worktree_remove(workdir, path):
    # --force: the applied patch leaves the worktree dirty; never fail cleanup.
    subprocess.run(
        ["git", "worktree", "remove", "--force", str(path)],
        check=False, capture_output=True, text=True, cwd=workdir,
    )


def _apply_diff(worktree, diff_text):
    """Apply a unified diff into the worktree working tree (reproduces HEAD)."""
    proc = subprocess.run(
        ["git", "apply"],
        input=diff_text, capture_output=True, text=True, cwd=str(worktree),
    )
    if proc.returncode != 0:
        raise ReviewError(
            f"git apply failed in worktree {worktree}: {proc.stderr.strip()}")


# ---------------------------------------------------------------------------
# source gathering (shared by every mode)
# ---------------------------------------------------------------------------

def changed_files_from_diff(diff_text):
    """Parse the changed target paths out of a unified diff.

    Uses the ``+++ b/<path>`` lines so renames point at the new name and pure
    deletions (``+++ /dev/null``) are skipped.
    """
    files = []
    for line in diff_text.splitlines():
        if not line.startswith("+++ "):
            continue
        path = line[4:]
        if path.startswith("b/"):
            path = path[2:]
        if not path or path == "/dev/null" or path in files:
            continue
        files.append(path)
    return files


def _list_tree(root, limit=200):
    """Relative paths of reviewable files under *root* (skips noise dirs).

    Walks lazily and prunes _SKIP_DIRS in place (os.walk dirs[:]) so we never
    descend into .git/objects or node_modules — a sorted(rglob('*')) would
    materialize the whole tree (incl. loose git objects, which can number in
    the millions) before the limit cut could take effect.
    """
    out = []
    for dirpath, dirs, files in os.walk(root):
        # Prune in place: os.walk then skips these subtrees entirely.
        dirs[:] = [d for d in dirs if d not in _SKIP_DIRS]
        for name in files:
            out.append(os.path.relpath(os.path.join(dirpath, name), root))
            if len(out) >= limit:
                return sorted(out)
    return sorted(out)


def _read_file(path):
    try:
        return Path(path).read_text(errors="replace")
    except OSError as exc:
        # Don't silently drop a file from review input: surface the failure so
        # a permission issue or broken symlink isn't mistaken for an empty file.
        print(f"! WARNING: could not read {path}: {exc}", file=sys.stderr)
        return ""


def build_project_source(project_dir, diff_text="", branch_point=""):
    """Build review input for a project dir: diff first, then changed-file bodies.

    For ``--diff-git`` the diff is prepended so reviewers see exactly what
    changed, and the changed files are always present in the listing/contents.
    """
    project_dir = Path(project_dir)
    project_root = project_dir.resolve()
    has_diff = bool(diff_text.strip())
    parts = []
    if branch_point:
        parts.append(
            "=== REVIEW SCOPE ===\n"
            f"Branch-point SHA: {branch_point}\n"
            f"Cumulative diff: git diff {branch_point}..HEAD\n"
        )
    if has_diff:
        parts.append("=== DIFF (what changed) ===\n" + diff_text.strip() + "\n")
    files = changed_files_from_diff(diff_text) or _list_tree(project_dir)
    parts.append("=== Files under review ===\n" + "\n".join(files) + "\n")
    bodies = []
    for rel in files:
        rel_path = Path(rel)
        if rel_path.is_absolute():
            continue
        try:
            # ponytail: accepted TOCTOU — resolve/is_file then a separate read
            # is a narrow race, low-severity for this single-user local CLI.
            candidate = (project_root / rel_path).resolve()
            if candidate == project_root or project_root not in candidate.parents:
                print(f"! WARNING: skipping {rel}: resolves outside {project_dir}", file=sys.stderr)
                continue
            is_file = candidate.is_file()
        except (OSError, RuntimeError, ValueError) as exc:
            print(f"! WARNING: skipping {rel}: {exc}", file=sys.stderr)
            continue
        text = _read_file(candidate) if is_file else ""
        if text:
            bodies.append(f"--- {rel} ---\n{text}")
    if bodies:
        parts.append("=== File contents ===\n" + "\n\n".join(bodies))
    return {
        "code_text": "\n".join(parts),
        "project_dir": str(project_dir),
        "diff_text": diff_text,
        "context_kind": "diff" if has_diff else "input",
        # Gate a literal diff when one exists. Otherwise gate only actual file
        # contents, not the generated headings/listing around them.
        "context_text": diff_text if has_diff else "\n\n".join(bodies),
    }


def build_diff_source(path):
    diff_text = _read_file(path)
    files = changed_files_from_diff(diff_text)
    code = "=== DIFF ===\n" + diff_text.strip()
    if files:
        code += "\n=== Changed files ===\n" + "\n".join(files)
    return {
        "code_text": code,
        "project_dir": None,
        "diff_text": diff_text,
        "context_kind": "diff",
        "context_text": diff_text,
    }


def build_dir_source(path):
    root = Path(path)
    project_root = root.resolve()
    files = _list_tree(root)
    bodies = []
    for rel in files:
        try:
            # ponytail: accepted TOCTOU — resolve/is_file then a separate read
            # is a narrow race, low-severity for this single-user local CLI.
            candidate = (project_root / rel).resolve()
            if candidate == project_root or project_root not in candidate.parents:
                print(f"! WARNING: skipping {rel}: resolves outside {root}", file=sys.stderr)
                continue
            if not candidate.is_file():
                continue
        except (OSError, RuntimeError, ValueError) as exc:
            print(f"! WARNING: skipping {rel}: {exc}", file=sys.stderr)
            continue
        text = _read_file(candidate)
        bodies.append(f"--- {rel} ---\n{text}")
    text = "\n\n".join(bodies)
    return {
        "code_text": text,
        "project_dir": str(root),
        "diff_text": "",
        "context_kind": "input",
        "context_text": text,
    }


def build_file_source(path):
    text = _read_file(path)
    return {
        "code_text": f"--- {path} ---\n{text}",
        "project_dir": None,
        "diff_text": "",
        "context_kind": "input",
        "context_text": text,
    }


# ---------------------------------------------------------------------------
# review pipeline
# ---------------------------------------------------------------------------

def _findings_obj(text, warnings=None):
    """Best-effort parse of a reviewer's JSON output to a dict (or None)."""
    obj = jsonio.parse_json_output(text, warnings=warnings)
    return obj if isinstance(obj, dict) else None


def _valid_line(line):
    """Accept int, non-empty string, or None (models emit null for
    project-wide findings that don't map to a line)."""
    return (line is None or isinstance(line, int)
            or (isinstance(line, str) and line.strip()))


def _validate(payload):
    """Validate an Architect or Inspector response against the review schema."""
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
        if not _REQUIRED_FINDING_KEYS.issubset(finding):
            return False
        if not _valid_line(finding["line"]):
            return False
    return True


def _role_execution_args(role, cmd, stdin_text, args, project, phase):
    """Build the common runner arguments for one provider phase."""
    effective_cmd = (
        providers.enhance_cmd_for_project(cmd, project)
        if cmd and project else cmd
    )
    persona_cmd = effective_cmd
    if not persona_cmd:
        config = getattr(args, "_provider_config", None)
        provider_role = _provider_role(role)
        chain = config.roles.get(provider_role, ()) if config is not None else ()
        if chain:
            persona_cmd = chain[0].command
    try:
        role_persona = providers.persona_for_role(role, persona_cmd or "")
        persona_file = persona_path(role_persona)
    except FileNotFoundError:
        persona_file = None
    return {
        "explicit_cmd": effective_cmd,
        "stdin_text": stdin_text,
        "timeout": args.timeout,
        "persona_file": persona_file,
        "ledger": args._ledger,
        "phase": phase,
        "persona": role,
        "max_retries": args.max_retries,
        "max_input_chars": args.max_input_chars,
        "max_output_chars": args.max_output_chars,
        "truncate_input": args.truncate_input,
        "cwd": str(Path(project or os.getcwd()).resolve()),
    }


def _provider_role(role):
    """Map review personas to the two provider-registry roles."""
    return "arbiter" if role == "synthesis" else "review"


def _delegated_registry_cmd(role, flag_cmd, env_var, fallback_cmd, chain):
    """Resolve one delegated command or report an actionable config error."""
    cmd = (
        flag_cmd
        or os.environ.get(env_var)
        or fallback_cmd
        or (chain[0].command if chain else "")
    ).strip()
    if cmd:
        return cmd
    raise ProviderConfigError(
        "PROVIDER_CONFIG_DELEGATED_COMMAND_REQUIRED",
        f"No command configured for delegated role '{role}' "
        f"(pass --{role}-cmd, set ${env_var}, or configure roles.{role})",
    )


def _execute_role_phase(role, cmd, stdin_text, args, project, phase):
    """Resolve and execute one phase through the provider-aware runner."""
    execution = _role_execution_args(
        role, cmd, stdin_text, args, project, phase,
    )
    explicit_cmd = execution.pop("explicit_cmd")
    resolver = getattr(args, "_provider_resolver", None)
    workdir = str(Path(project or os.getcwd()).resolve())
    if resolver is None and explicit_cmd is None:
        # Direct unit callers may skip main() command resolution. Preserve a
        # useful legacy fallback without consulting a provider registry.
        explicit_cmd = DEFAULT_REVIEW_CMD
    forced = getattr(args, "_force_providers", {})
    return runner.run_phase_cmd(
        phase,
        _provider_role(role),
        workdir,
        resolver,
        explicit_cmd=explicit_cmd,
        force=bool(getattr(args, "force", False)),
        force_provider=forced.get(_provider_role(role)),
        **execution,
    )


def _record_call(args, label, role, phase, result):
    """Persist bounded execution metadata without retaining a tuple object."""
    metadata = getattr(result, "metadata", {})
    if not isinstance(metadata, dict):
        metadata = {}
    call = {
        "label": label,
        "phase": phase,
        "persona": role,
        "ok": len(result) >= 3 and result[2] == 0,
        "returncode": result[2] if len(result) >= 3 else -1,
        "attempts": list(metadata.get("attempts", [])),
        "cap_events": list(metadata.get("cap_events", [])),
    }
    if len(result) >= 2 and result[1]:
        call["stderr"] = str(result[1])[:2000]
    if metadata.get("usage") is not None:
        call["usage"] = metadata["usage"]
    if isinstance(metadata.get("provider_decision"), dict):
        call["provider_decision"] = dict(metadata["provider_decision"])
    args._calls.append(call)
    return call


def _consume_role_result(role, result, args, out_dir, name, phase):
    """Save and validate one completed role result, returning text + payload."""
    stdout = result[0] if len(result) >= 1 else ""
    stderr = result[1] if len(result) >= 2 else "malformed runner result"
    rc = result[2] if len(result) >= 3 else -1
    path = jsonio.save_artifact(out_dir, f"{name}.txt", stdout or "")
    args._artifacts[name] = str(path)
    call = _record_call(args, name, role, phase, result)
    if rc != 0:
        return stdout or "", None, PhaseFailure(f"{role} ({name})", rc, stderr)

    parse_warnings = []
    payload = _findings_obj(stdout, warnings=parse_warnings)
    args._warnings.extend(
        warning for warning in parse_warnings if warning not in args._warnings
    )
    if role in {"architect", "inspector"} and not _validate(payload):
        error = (
            "invalid reviewer JSON: expected findings with id, severity, file, "
            "line, summary, and evidence, plus a valid verdict"
        )
        call["ok"] = False
        call["error"] = error
        return stdout or "", payload, PhaseFailure(
            f"{role} ({name})",
            EXIT_INFRA,
            error,
        )
    return stdout or "", payload, None


def _run_role(role, cmd, stdin_text, args, out_dir, name, project):
    """Run one ordered provider phase through the shared phase runner."""
    phase = _PHASE_LABELS.get(name, name)
    result = _execute_role_phase(
        role, cmd, stdin_text, args, project, phase,
    )
    stdout, _payload, failure = _consume_role_result(
        role, result, args, out_dir, name, phase,
    )
    if failure:
        raise failure
    return stdout


def _selected_perspectives(args, complexity):
    """Select both independent reviewers required by the review protocol."""
    return ["architect", "inspector"]


def _run_initial_perspectives(code, args, out, project, complexity):
    """Dispatch Architect/Inspector through one shared resolver in parallel."""
    roles = _selected_perspectives(args, complexity)
    commands = {"architect": args.a_cmd, "inspector": args.b_cmd}
    requested = args.concurrency or complexity["recommended_agents"]
    concurrency_cap = min(args.max_agents, args.max_concurrency)
    worker_count = min(requested, concurrency_cap, len(roles))
    calls = [
        (
            role,
            lambda role=role: _execute_role_phase(
                role, commands[role], code, args, project, role,
            ),
        )
        for role in roles
    ]
    results = runner.run_parallel(
        calls,
        concurrency=requested,
        max_concurrency=concurrency_cap,
    )
    args._parallel = {
        "perspectives": roles,
        "requested_concurrency": requested,
        "max_concurrency": concurrency_cap,
        "effective_concurrency": worker_count,
    }

    texts = {}
    payloads = {}
    failures = []
    for role, record in zip(roles, results):
        raw_result = record.get("result", ("", record.get("stderr", ""), -1))
        text, payload, failure = _consume_role_result(
            role, raw_result, args, out, _ROLE_LABELS[role], role,
        )
        texts[role] = text
        if payload is not None:
            payloads[role] = payload
        if failure:
            failures.append(failure)
    args._review_payloads = payloads
    if failures:
        # Every sibling result and artifact has been retained before failing.
        raise failures[0]
    return texts, payloads


def _delegated_stage_call(role, cmd, stdin_text, args, project, phase):
    """Build a delegated-stage call with the same caps and cost ledger."""
    execution = _role_execution_args(
        role, cmd, stdin_text, args, project, phase,
    )
    execution["cmd"] = execution.pop("explicit_cmd")
    return execution


def _capture_delegated_record(args, out, record, name, role, phase):
    """Persist one delegated call without turning a worker failure fatal."""
    if not isinstance(record, dict):
        return
    result = record.get("result")
    if not isinstance(result, (list, tuple)) or len(result) < 3:
        return
    path = jsonio.save_artifact(out, f"{name}.txt", result[0] or "")
    args._artifacts[name] = str(path)
    _record_call(args, name, role, phase, result)


def _run_delegated_perspectives(code, args, out, project, complexity):
    """Use R12 only for high inputs; otherwise retain the direct protocol."""
    if not args.delegated:
        return _run_initial_perspectives(code, args, out, project, complexity)
    if complexity.get("level") != "high":
        reason = (
            "delegated execution skipped: complexity level "
            f"{complexity.get('level')!r} is below required level 'high'"
        )
        args._delegated = {
            "delegated": False,
            "mode": "direct",
            "status": "fallback",
            "reason": reason,
            "log": [reason],
            "complexity": complexity,
        }
        args._warnings.append({
            "code": "delegation_fallback",
            "message": reason,
        })
        print(f"! {reason}; continuing with direct review", file=sys.stderr)
        return _run_initial_perspectives(code, args, out, project, complexity)

    decomposition_prompt = "\n\n".join([
        "Decompose this code review into independent file groups or concerns.",
        (
            "Return JSON only: {\"tasks\":[{\"id\":\"stable-id\","
            "\"scope\":\"files/concern\",\"instructions\":\"what to inspect\"}]}."
        ),
        f"Create at most {min(args.max_agents, args.max_concurrency)} tasks.",
        "=== CODE REVIEW INPUT ===",
        code,
    ])

    def worker_call(task):
        return _delegated_stage_call(
            "inspector",
            args.worker_cmd,
            "\n\n".join([
                "Review only the delegated scope below, but use the complete input",
                "to verify interactions. Return the standard reviewer JSON object",
                "with verdict and findings; every finding must include id, severity,",
                "file, line, summary, evidence, confidence, and basis.",
                "=== DELEGATED TASK ===",
                json.dumps(_json_safe(task), ensure_ascii=False, sort_keys=True),
                "=== COMPLETE REVIEW INPUT ===",
                code,
            ]),
            args,
            project,
            "delegated_worker",
        )

    def synthesis_call(survivors):
        return _delegated_stage_call(
            "inspector",
            args.synth_cmd,
            "\n\n".join([
                "Merge the surviving delegated reviews into one reviewer result.",
                "Return JSON only with verdict and findings using the standard",
                "review schema. Preserve origin=worker on worker-sourced findings.",
                "=== SURVIVING WORKER RECORDS ===",
                json.dumps(_json_safe(survivors), ensure_ascii=False, sort_keys=True),
            ]),
            args,
            project,
            "delegated_synthesis",
        )

    delegated = runner.run_delegated(
        code,
        _delegated_stage_call(
            "orchestrator",
            args.orchestrator_cmd,
            decomposition_prompt,
            args,
            project,
            "delegated_decomposition",
        ),
        worker_call,
        synthesis_call,
        concurrency=args.concurrency,
        max_concurrency=min(args.max_agents, args.max_concurrency),
        complexity=complexity,
    )

    _capture_delegated_record(
        args, out, delegated.get("decomposition"), "00_decomposition",
        "orchestrator", "delegated_decomposition",
    )
    for index, worker in enumerate(delegated.get("workers", []), start=1):
        _capture_delegated_record(
            args, out, worker, f"01_worker_{index:02d}",
            "worker", "delegated_worker",
        )
    _capture_delegated_record(
        args, out, delegated.get("synthesis"), "02_worker_synthesis",
        "synthesis", "delegated_synthesis",
    )

    synthesis = delegated.get("synthesis")
    payload = synthesis.get("payload") if isinstance(synthesis, dict) else None
    if payload is None and isinstance(synthesis, dict):
        payload = _findings_obj(synthesis.get("stdout", ""), warnings=args._warnings)
    if isinstance(payload, dict) and isinstance(payload.get("findings"), list):
        for finding in payload["findings"]:
            if isinstance(finding, dict):
                finding["origin"] = "worker"
    args._delegated = _json_safe(delegated)
    delegated_synthesized = (
        delegated.get("delegated")
        and delegated.get("status") == "synthesized"
    )
    if delegated_synthesized and _validate(payload):
        text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        args._review_payloads = {"delegated": payload}
        if delegated.get("partial"):
            args._warnings.append({
                "code": "delegated_partial_failure",
                "message": "delegated synthesis used the surviving worker results",
            })
        return {"delegated": text}, {"delegated": payload}

    reason = delegated.get("reason", "delegated synthesis was not usable")
    warning = {
        "code": "delegation_fallback",
        "message": str(reason),
    }
    args._warnings.append(warning)
    print(f"! {warning['message']}; continuing with direct review", file=sys.stderr)
    return _run_initial_perspectives(code, args, out, project, complexity)


def _derive_verdict(*review_texts):
    """APPROVE when all selected reviews approve; REJECT if any rejects.

    Each text is first probed for a JSON object with a ``verdict`` key
    (the standard reviewer output).  When no JSON verdict is found the
    function falls back to a **Markdown** ``Verdict: <value>`` line so
    that the synthesis report (which is prose, not JSON) can also
    determine the final verdict.
    """
    verdicts = []
    for text in review_texts:
        obj = _findings_obj(text)
        if isinstance(obj, dict) and obj.get("verdict"):
            verdicts.append(obj["verdict"])
        else:
            m = re.search(
                r"(?:^|\n)##\s*Verdict:\s*(APPROVE|REQUEST_CHANGES|REJECT)\b",
                text, re.MULTILINE,
            )
            if m:
                verdicts.append(m.group(1))
    if "REJECT" in verdicts:
        return "REJECT"
    if verdicts and all(v == "APPROVE" for v in verdicts):
        return "APPROVE"
    return "REQUEST_CHANGES"


def _validate_spec(args):
    """Fail fast on an unreadable --spec before any provider phase runs.

    A missing spec otherwise surfaces only from :func:`_contract_gate`, after
    all five provider phases have already executed; that late
    FileNotFoundError would then be misreported as infrastructure exit 1 and
    overwrite their cost metadata with a zero-call setup artifact. Surface it
    up front as a review-setup error (exit 2) instead.
    """
    spec_path = getattr(args, "spec", None)
    if not spec_path:
        return
    if not Path(spec_path).is_file():
        raise ReviewError(f"--spec file not found: {spec_path}")


def _contract_gate(args, project):
    """Run the shared P5 contract gate (canonical settle gate, P7c).

    Delegates to :func:`adversarial_common.run_contract_gate` — the single
    cross-pipeline entry point the spec/plan/review/loop pipelines all share
    (R2) — so the same *spec_path* + *repo_root* settle identically and gate
    semantics can never diverge between pipelines. Returns its canonical
    ``{settle, ac_status, failures, directives}`` result for final.json, or
    None when no spec was requested (the gate is a no-op). The caller settles
    the verdict by reading ``gate["settle"]``.
    """
    spec_path = getattr(args, "spec", None)
    if not spec_path:
        return None
    repo_root = project or os.getcwd()
    return run_contract_gate(spec_path, repo_root)


def _severity_counts(*texts):
    counts = {}
    seen = set()
    for text in texts:
        for finding in (_findings_obj(text) or {}).get("findings", []) or []:
            fid = finding.get("id")
            if fid is not None:
                if fid in seen:
                    continue
                seen.add(fid)
            sev = finding.get("severity", "unknown")
            counts[sev] = counts.get(sev, 0) + 1
    return counts


def _runtime_metadata(args):
    calls = list(args._calls)
    attempts = []
    cap_events = []
    for call in calls:
        attempts.extend({
            "call": call["label"],
            "phase": call["phase"],
            "persona": call["persona"],
            **attempt,
        } for attempt in call.get("attempts", []))
        cap_events.extend({
            "call": call["label"],
            "phase": call["phase"],
            "persona": call["persona"],
            **event,
        } for event in call.get("cap_events", []))
    public_calls = [
        {key: value for key, value in call.items()
         if key not in {"attempts", "cap_events"}}
        for call in calls
    ]
    metadata = {
        "context": args._context,
        "thresholds": args._context.get("thresholds", {}),
        "complexity": args._complexity,
        "execution": {
            "max_retries": args.max_retries,
            "max_input_chars": args.max_input_chars,
            "max_output_chars": args.max_output_chars,
            "truncate_input": args.truncate_input,
            "show_costs": args.show_costs,
            "concurrency": args.concurrency,
            "max_concurrency": args.max_concurrency,
            "max_agents": args.max_agents,
        },
        "parallel": getattr(args, "_parallel", {}),
        "attempts": attempts,
        "cap_events": cap_events,
        "calls": public_calls,
        "failures": [call for call in public_calls if not call["ok"]],
        "costs": args._ledger.summary(),
        "artifacts": dict(args._artifacts),
    }
    provider_history = [
        dict(call["provider_decision"])
        for call in calls
        if isinstance(call.get("provider_decision"), dict)
    ]
    if provider_history:
        metadata["provider_history"] = provider_history
    if hasattr(args, "_research"):
        metadata["research"] = args._research
    if hasattr(args, "_delegated"):
        metadata["delegated"] = args._delegated
    return metadata


def _all_review_findings(payloads):
    findings = []
    for payload in payloads.values():
        value = payload.get("findings", [])
        if isinstance(value, list):
            findings.extend(value)
    return findings


def _external_findings(items):
    """Defensively label provider evidence even when a test/provider is loose."""
    findings = []
    for item in items:
        finding = dict(item) if isinstance(item, dict) else {"evidence": _json_safe(item)}
        finding["basis"] = "external"
        if finding.get("confidence") not in jsonio.VALID_CONFIDENCE:
            finding["confidence"] = "low"
        finding.setdefault("origin", "research")
        findings.append(finding)
    return findings


def _all_warnings(args, payloads):
    warnings = list(args._warnings)
    for payload in payloads.values():
        value = payload.get("warnings", [])
        if not isinstance(value, list):
            continue
        for warning in value:
            if not isinstance(warning, dict):
                continue
            if warning not in warnings:
                warnings.append(warning)
    return warnings


def _write_phase_error(args, failure):
    payloads = getattr(args, "_review_payloads", {})
    findings = _all_review_findings(payloads)
    _write_final(
        args,
        "ERROR",
        status="failed",
        infrastructure=True,
        error=str(failure),
        finding_details=findings,
        epistemic_labels=jsonio.epistemic_distribution(findings),
        epistemic_distribution=jsonio.epistemic_distribution(findings),
        warnings=_all_warnings(args, payloads),
        **_runtime_metadata(args),
    )


def run_adversarial_review(source, args):
    """Run adaptive parallel perspectives, ordered debate, and synthesis."""
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    project = source.get("project_dir")
    code = source.get("code_text", "")
    # main() resolves these fallbacks in _resolve_commands(), but direct callers
    # may provide only the already-resolved primary reviewer commands.
    if not getattr(args, "cross_a_cmd", None):
        args.cross_a_cmd = args.a_cmd
    if not getattr(args, "cross_b_cmd", None):
        args.cross_b_cmd = args.b_cmd
    args._ledger = CostLedger()
    args._calls = []
    args._artifacts = {}
    args._warnings = []
    args._review_payloads = {}
    _validate_spec(args)
    if not hasattr(args, "_context"):
        args._context = {"ok": True, "reason": "not_run", "thresholds": {}}
    if not hasattr(args, "_complexity"):
        args._complexity = estimate_complexity(
            source.get("context_text", code), max_agents=args.max_agents,
        )
    research_findings = []
    review_input = code
    if args.deep_research:
        research_query = "\n\n".join([
            "Validate claims in this code review input against current upstream",
            "standards and authoritative documentation. Return bounded JSON evidence",
            "with findings/results/items and include source identifiers when known.",
            "=== REVIEW INPUT ===",
            code,
        ])
        try:
            research = runner.run_research(
                research_query,
                provider_cmd=args.research_cmd,
                enabled=True,
                max_results=args.max_research_results,
                timeout=args.research_timeout,
                max_input_chars=min(
                    args.max_input_chars,
                    runner.DEFAULT_RESEARCH_MAX_INPUT_CHARS,
                ),
                max_output_chars=min(
                    args.max_output_chars,
                    runner.DEFAULT_RESEARCH_MAX_OUTPUT_CHARS,
                ),
                ledger=args._ledger,
                cwd=project,
                stderr=sys.stderr,
            )
        except Exception as exc:
            reason = f"research integration error: {type(exc).__name__}: {exc}"
            print(f"Research skipped: {reason}", file=sys.stderr)
            research = {
                "enabled": True,
                "status": "skipped",
                "non_fatal": True,
                "reason": reason,
                "findings": [],
                "calls": [],
                "warnings": [],
            }
        if isinstance(research, dict):
            value = research.get("findings", [])
            if isinstance(value, list):
                research_findings = _external_findings(value)
                research["findings"] = research_findings
                research["result_count"] = len(research_findings)
            warnings = research.get("warnings", [])
            if isinstance(warnings, list):
                args._warnings.extend(
                    warning for warning in warnings
                    if isinstance(warning, dict) and warning not in args._warnings
                )
        args._research = _json_safe(research)
        if research_findings:
            review_input = "\n\n".join([
                code,
                "=== EXTERNAL RESEARCH EVIDENCE ===",
                json.dumps(
                    research_findings,
                    ensure_ascii=False,
                    sort_keys=True,
                ),
                "Use this evidence only when it is relevant and independently",
                "consistent with the reviewed code.",
            ])

    try:
        review_texts, payloads = _run_delegated_perspectives(
            review_input, args, out, project, args._complexity,
        )
        normalized_texts = {
            role: json.dumps(payload, ensure_ascii=False, sort_keys=True)
            for role, payload in payloads.items()
        }
        # Cross-review 1: A reviews B's findings (Architect reviews Inspector)
        cross1_target = normalized_texts.get(
            "inspector",
            normalized_texts.get(
                "architect", normalized_texts.get("delegated", "{}"),
            ),
        )
        cross1 = _run_role("cross_review", args.cross_a_cmd, cross1_target,
                           args, out, "03_cross_1", project)
        # Cross-review 2: B reviews A's findings (Inspector reviews Architect)
        cross2_target = normalized_texts.get(
            "architect",
            normalized_texts.get(
                "inspector", normalized_texts.get("delegated", "{}"),
            ),
        )
        # CR6: in delegated mode normalized_texts has only the "delegated" key
        # (no architect pass ran), so round 2 must not claim "ARCHITECT REVIEW".
        cross2_delegated = "architect" not in normalized_texts
        cross2_subject = "DELEGATED REVIEW" if cross2_delegated else "ARCHITECT REVIEW"
        cross2_target_desc = (
            "delegated synthesis findings" if cross2_delegated else "Architect's findings"
        )
        cross2_input = "\n\n".join([
            f"=== {cross2_subject} TO CROSS-REVIEW ===\n" + cross2_target,
            "=== CROSS-REVIEW ROUND 1 (A reviews B) OUTPUT ===\n" + cross1,
            "=== ROUND 2 INSTRUCTIONS ===\n"
            f"Cross-review the {cross2_target_desc}. Find missed challenges, "
            "validate or challenge each one. Do not repeat round 1's work.",
        ])
        cross2 = _run_role("cross_review", args.cross_b_cmd, cross2_input,
                           args, out, "04_cross_2", project)

        normalized_findings = _all_review_findings(payloads)
        normalized_findings.extend(research_findings)
        distribution = jsonio.epistemic_distribution(normalized_findings)
        synth_sections = [
            "=== NORMALIZED ARCHITECT REVIEW ===\n",
            normalized_texts.get("architect", "Not selected by adaptive review."),
            "=== NORMALIZED INSPECTOR REVIEW ===\n",
            normalized_texts.get("inspector", "Not selected by adaptive review."),
        ]
        if "delegated" in normalized_texts:
            synth_sections.extend([
                "=== DELEGATED WORKER SYNTHESIS ===\n",
                normalized_texts["delegated"],
            ])
        if research_findings:
            synth_sections.extend([
                "=== EXTERNAL RESEARCH EVIDENCE ===\n",
                json.dumps(research_findings, ensure_ascii=False, sort_keys=True),
            ])
        synth_sections.extend([
            "=== CROSS-REVIEW ROUND 1 ===\n", cross1,
            "=== CROSS-REVIEW ROUND 2 ===\n", cross2,
            "=== EPISTEMIC DISTRIBUTION ===\n",
            json.dumps(distribution, ensure_ascii=False, sort_keys=True),
            "Down-weight findings supported only by low-confidence inference "
            "and surface this distribution in the synthesis.",
        ])
        synth_input = "\n\n".join(synth_sections)
        synthesis = _run_role("synthesis", args.synth_cmd, synth_input, args, out,
                              "05_synthesis", project)

        ordered_reviews = [
            review_texts[role]
            for role in ("architect", "inspector", "delegated")
            if role in review_texts
        ]
        # Synthesis is the final arbiter — its verdict takes priority over
        # the individual reviewers so cross-review can override initial outputs.
        verdict = _derive_verdict(synthesis, *ordered_reviews)
        gate = _contract_gate(args, project)
        if gate is not None and gate["settle"] != "APPROVE" and verdict == "APPROVE":
            verdict = "REQUEST_CHANGES"
        count_inputs = list(ordered_reviews)
        if research_findings:
            count_inputs.append(json.dumps({"findings": research_findings}))
        counts = _severity_counts(*count_inputs)
        synthesis_report = (
            synthesis.rstrip()
            + "\n\n## Epistemic label distribution\n\n"
            + json.dumps(distribution, indent=2, ensure_ascii=False, sort_keys=True)
            + "\n"
        )
        report_path = jsonio.save_artifact(out, "review.md", synthesis_report)
        args._artifacts["review"] = str(report_path)
        _write_final(
            args, verdict,
            status="complete",
            summary="\n".join((synthesis or "").splitlines()[:6]),
            findings=counts,
            finding_details=normalized_findings,
            epistemic_labels=distribution,
            epistemic_distribution=distribution,
            warnings=_all_warnings(args, payloads),
            report=str(report_path),
            source_diff=bool(source.get("diff_text", "").strip()),
            **{
                **_runtime_metadata(args),
                **({"contract": gate} if gate is not None else {}),
            },
        )
    except PhaseFailure as failure:
        _write_phase_error(args, failure)
        if args.show_costs:
            args._ledger.print_summary(file=sys.stderr)
        runner.fail_phase(failure.label, failure.code, failure.stderr)

    if args.show_costs:
        args._ledger.print_summary(file=sys.stderr)
    print(f"✓ review complete: verdict={verdict} findings={counts} "
          f"-> {out}/final.json")
    return verdict


# ---------------------------------------------------------------------------
# --diff-git orchestration
# ---------------------------------------------------------------------------

def _review_execution_settings(args):
    """Return the review-specific execution fields kept in blocked reports."""
    return {
        "max_retries": args.max_retries,
        "max_input_chars": args.max_input_chars,
        "max_output_chars": args.max_output_chars,
        "truncate_input": args.truncate_input,
        "show_costs": args.show_costs,
        "concurrency": args.concurrency,
        "max_concurrency": args.max_concurrency,
        "max_agents": args.max_agents,
    }


def _source_gate(source, args):
    """Configure the shared preflight for a non-mutating review source."""
    primary = source.get("context_text", source.get("code_text", ""))
    kind = source.get("context_kind", "diff" if source.get("diff_text") else "input")

    def write_blocked(_out_dir, verdict, payload):
        # ``warnings`` is part of the common blocked shape but was not present
        # in review's established schema. Keep this adapter schema-neutral.
        review_payload = dict(payload)
        review_payload.pop("warnings", None)
        return _write_final(args, verdict, **review_payload)

    policy = pipeline_base.PreflightPolicy(
        context_kind=kind,
        threshold_env=_THRESHOLD_ENV,
        threshold_error_type=ReviewError,
        enforce_input_cap=False,
        execution_settings=_review_execution_settings,
        blocked_writer=write_blocked,
        blocked_extra={"failures": [], "artifacts": {}},
    )
    return pipeline_base.preflight(args, primary, args.out, policy=policy)


def _resolve_commands(args):
    """Load one registry/resolver or resolve the complete legacy command set."""
    config = providers.load_provider_config(args.provider_config)
    args._provider_config = config
    args._force_providers = _force_provider_map(args.force_provider)

    if config is None:
        args._provider_resolver = None
        args.review_cmd = providers.resolve_role_cmd(
            "review", args.review_cmd, "ACR_REVIEW_CMD",
            default=DEFAULT_REVIEW_CMD,
        )
        args.a_cmd = providers.resolve_role_cmd(
            "review", args.a_cmd, "ACR_A_CMD", default=args.review_cmd,
        )
        args.b_cmd = providers.resolve_role_cmd(
            "review", args.b_cmd, "ACR_B_CMD", default=args.review_cmd,
        )
        args.synth_cmd = providers.resolve_role_cmd(
            "review", args.synth_cmd, "ACR_SYNTH_CMD",
            default=args.review_cmd,
        )
        args.cross_a_cmd = providers.resolve_role_cmd(
            "review", args.cross_a_cmd, "ACR_CROSS_A_CMD",
            default=args.a_cmd,
        )
        args.cross_b_cmd = providers.resolve_role_cmd(
            "review", args.cross_b_cmd, "ACR_CROSS_B_CMD",
            default=args.b_cmd,
        )
    else:
        if not config.quota_cmd:
            raise ProviderConfigError(
                "PROVIDER_CONFIG_QUOTA_CMD_REQUIRED",
                "quota_cmd is required when code review uses a provider registry",
            )
        # This single resolver is injected into both parallel calls and every
        # later ordered phase. Its synchronized TTL cache therefore permits
        # only one quota-checker invocation for a fresh snapshot.
        args._provider_resolver = QuotaResolver(config, config.quota_cmd)
        review_override = (
            args.review_cmd or os.environ.get("ACR_REVIEW_CMD") or ""
        ).strip() or None
        args.review_cmd = review_override
        args.a_cmd = (
            args.a_cmd or os.environ.get("ACR_A_CMD") or review_override or ""
        ).strip() or None
        args.b_cmd = (
            args.b_cmd or os.environ.get("ACR_B_CMD") or review_override or ""
        ).strip() or None
        args.synth_cmd = (
            args.synth_cmd
            or os.environ.get("ACR_SYNTH_CMD")
            or review_override
            or ""
        ).strip() or None
        args.cross_a_cmd = (
            args.cross_a_cmd
            or os.environ.get("ACR_CROSS_A_CMD")
            or args.a_cmd
            or ""
        ).strip() or None
        args.cross_b_cmd = (
            args.cross_b_cmd
            or os.environ.get("ACR_CROSS_B_CMD")
            or args.b_cmd
            or ""
        ).strip() or None

    if args.deep_research and args.research_cmd is None:
        args.research_cmd = os.environ.get("ACR_RESEARCH_CMD")
    if args.delegated:
        if config is None:
            args.orchestrator_cmd = providers.resolve_role_cmd(
                "orchestrator",
                args.orchestrator_cmd,
                "ACR_ORCHESTRATOR_CMD",
                default=args.a_cmd,
            )
            args.worker_cmd = providers.resolve_role_cmd(
                "worker",
                args.worker_cmd,
                "ACR_WORKER_CMD",
                default=args.b_cmd,
            )
        else:
            # Delegation is an optional sub-pipeline with its own legacy flags.
            # Avoid reloading the registry; use explicit overrides or the
            # already-loaded role primary as its existing command fallback.
            orchestrator_chain = config.roles.get("orchestrator", ())
            worker_chain = config.roles.get("worker", ())
            args.orchestrator_cmd = _delegated_registry_cmd(
                "orchestrator",
                args.orchestrator_cmd,
                "ACR_ORCHESTRATOR_CMD",
                args.a_cmd,
                orchestrator_chain,
            )
            args.worker_cmd = _delegated_registry_cmd(
                "worker",
                args.worker_cmd,
                "ACR_WORKER_CMD",
                args.b_cmd,
                worker_chain,
            )


def _review_source(source, args, context=None):
    context = _source_gate(source, args).context if context is None else context
    if not context["ok"]:
        return EXIT_CONTEXT_BLOCKED
    _resolve_commands(args)
    run_adversarial_review(source, args)
    return EXIT_OK

def run_diff_git(args):

    """Review ``<base>..HEAD`` in an isolated worktree; full try/finally cleanup."""
    workdir = os.getcwd()
    root = gitops.detect_enclosing_repo(workdir)
    if not root:
        print("X --diff-git must run inside a git repository", file=sys.stderr)
        return EXIT_NOTHING

    try:
        base = resolve_base(root, args.base)
    except ReviewError as exc:
        print(f"X {exc}", file=sys.stderr)
        return EXIT_NOTHING

    original_branch = None
    try:
        original_branch = gitops.get_current_branch(root)
    except gitops.GitError:
        pass  # detached HEAD: nothing to restore to
    state = {"stash_id": ""}
    worktree = None
    try:
        state["stash_id"] = gitops.stash_dirty(root)
        merge_base = gitops.record_branch_point(root, base)
        diff_text = gitops.get_diff(root, merge_base, "HEAD")
        # A literal diff is the primary input. Gate it before worktree creation
        # and, critically, before command resolution or any provider process.
        gate = _source_gate({
            "code_text": diff_text,
            "context_text": diff_text,
            "context_kind": "diff",
            "diff_text": diff_text,
        }, args)
        if not gate.ok:
            return EXIT_CONTEXT_BLOCKED
        context = gate.context

        feature = gitops.sanitize_feature_name(args.feature or original_branch or "review")
        worktree = next_worktree_path(feature)

        try:
            _worktree_add(root, worktree, merge_base)
        except subprocess.CalledProcessError as exc:
            msg = (exc.stderr or "").strip() or f"exit {exc.returncode}"
            if args.allow_fallback:
                print(f"! WARNING: git worktree add failed ({msg}). "
                      f"--allow-fallback set: reviewing the current workdir "
                      f"'{root}' as --project-dir instead of the isolated "
                      f"worktree.", file=sys.stderr)
                source = build_project_source(root, diff_text, branch_point=merge_base)
                return _review_source(source, args, context=context)
            print(f"X --diff-git worktree creation failed: {msg}\n"
                  f"  (pass --allow-fallback to review the live workdir instead)",
                  file=sys.stderr)
            return EXIT_NOTHING

        _apply_diff(worktree, diff_text)
        source = build_project_source(worktree, diff_text, branch_point=merge_base)
        return _review_source(source, args, context=context)
    finally:
        try:
            if worktree is not None:
                _worktree_remove(root, worktree)
            # `git worktree add` never moves the main workdir's HEAD, but stay
            # defensive if a future caller checks the base out here.
            if original_branch:
                try:
                    if gitops.get_current_branch(root) != original_branch:
                        gitops.checkout(root, original_branch)
                except gitops.GitError:
                    pass
        finally:
            stash_id = state["stash_id"]
            if stash_id:
                try:
                    gitops.unstash(root, stash_id)
                    state["stash_id"] = ""
                except gitops.GitError as exc:
                    print(f"! WARNING: could not restore stash {stash_id}: {exc}",
                          file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _fail_on_arg(value):
    try:
        runner.parse_fail_on(value)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    return value


def _force_provider_value(value):
    """Argparse type for repeatable ``ROLE:ALIAS`` provider overrides."""
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
            raise ValueError(
                f"--force-provider specified more than once for {role}"
            )
        result[role] = alias
    return result


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="adversarial_review.py",
        description="Adversarial multi-perspective code review.",
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--diff", metavar="FILE",
                     help="review a unified-diff file")
    src.add_argument("--dir", metavar="DIR",
                     help="review every file under a directory")
    src.add_argument("--file", metavar="FILE",
                     help="review a single file")
    src.add_argument("--project-dir", metavar="DIR",
                     help="review an existing project directory in place")
    src.add_argument("--diff-git", action="store_true",
                     help="review <base>..HEAD in an isolated git worktree")

    p.add_argument("--base", default=None,
                   help="base ref for --diff-git (default: $ACR_BASE, main, master)")
    p.add_argument("--feature", default=None,
                   help="feature slug for the worktree name (default: current branch)")
    p.add_argument("--allow-fallback", action="store_true",
                   help="on --diff-git worktree failure, review the live workdir")

    p.add_argument("--out", default=".adversarial-review",
                   help="output directory for artifacts (default: .adversarial-review)")
    p.add_argument("--review-cmd", default=None,
                   help="reviewer CLI (default: $ACR_REVIEW_CMD, then the claude wrapper)")
    p.add_argument("--a-cmd", default=None,
                   help="Architect review command (default: --review-cmd)")
    p.add_argument("--b-cmd", default=None,
                   help="Inspector review command (default: --review-cmd)")
    p.add_argument("--synth-cmd", default=None,
                   help="Synthesis command (default: --review-cmd)")
    p.add_argument("--cross-a-cmd", default=None,
                   help="Cross-review A — A reviews B's findings (default: --a-cmd)")
    p.add_argument("--cross-b-cmd", default=None,
                   help="Cross-review B — B reviews A's findings (default: --b-cmd)")
    p.add_argument(
        "--provider-config",
        default=None,
        metavar="PATH",
        help="provider registry YAML (env: ADVERSARIAL_PROVIDER_CONFIG)",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="skip quota checks and select each role's primary provider",
    )
    p.add_argument(
        "--force-provider",
        action="append",
        default=[],
        type=_force_provider_value,
        metavar="ROLE:ALIAS",
        help="force an alias for review or arbiter; may be repeated",
    )
    p.add_argument("--timeout", type=int, default=600,
                   help="per-phase timeout in seconds (default: 600)")
    p.add_argument("--html", action="store_true",
                   help="render a self-contained report.html after final.json")
    p.add_argument("--ci", action="store_true",
                   help="enable deterministic CI stdout and exit-code policy")
    p.add_argument("--fail-on", type=_fail_on_arg, default=None,
                   help="comma-separated CI selectors (default: findings)")
    p.add_argument("--deep-research", action="store_true",
                   help="run bounded external research before reviewers")
    p.add_argument("--research-cmd", default=None,
                   help="research provider command (env: ACR_RESEARCH_CMD)")
    p.add_argument("--max-research-results", "--research-max-results",
                   dest="max_research_results", type=pipeline_base.non_negative_int,
                   default=runner.DEFAULT_RESEARCH_MAX_RESULTS,
                   help="maximum external evidence items (default: 5)")
    p.add_argument("--research-timeout", type=pipeline_base.positive_int,
                   default=runner.DEFAULT_RESEARCH_TIMEOUT,
                   help="research provider timeout in seconds (default: 60)")
    p.add_argument("--delegated", action="store_true",
                   help="delegate high-complexity reviews to bounded workers")
    p.add_argument("--orchestrator-cmd", default=None,
                   help="delegation decomposition command (default: --a-cmd)")
    p.add_argument("--worker-cmd", default=None,
                   help="delegated worker command (default: --b-cmd)")

    p.add_argument("--min-chars", "--min-context-chars", "--context-min-chars",
                   dest="min_chars",
                   type=pipeline_base.non_negative_int, default=None,
                   help="minimum primary-input characters (env: ACR_MIN_CONTEXT_CHARS)")
    p.add_argument("--min-tokens", "--min-context-tokens", "--context-min-tokens",
                   dest="min_tokens",
                   type=pipeline_base.non_negative_int, default=None,
                   help="minimum estimated input tokens (env: ACR_MIN_CONTEXT_TOKENS)")
    p.add_argument("--min-source-lines", type=pipeline_base.non_negative_int, default=None,
                   help="minimum changed source lines for diffs (env: ACR_MIN_SOURCE_LINES)")
    p.add_argument("--max-retries", type=pipeline_base.non_negative_int, default=3,
                   help="transient retries per provider phase (default: 3)")
    p.add_argument("--max-input-chars", type=pipeline_base.non_negative_int,
                   default=runner.DEFAULT_MAX_INPUT_CHARS,
                   help="hard input cap per provider phase")
    p.add_argument("--max-output-chars", type=pipeline_base.non_negative_int,
                   default=runner.DEFAULT_MAX_OUTPUT_CHARS,
                   help="hard output cap per provider phase")
    p.add_argument("--truncate-input", action="store_true",
                   help="head-truncate oversized provider input instead of rejecting it")
    p.add_argument("--show-costs", action="store_true",
                   help="print the final per-model cost breakdown to stderr")
    p.add_argument("--concurrency", type=pipeline_base.positive_int, default=None,
                   help="parallel perspective workers (default: complexity recommendation)")
    p.add_argument("--max-concurrency", type=pipeline_base.positive_int, default=6,
                   help="hard parallel worker cap (default: 6)")
    p.add_argument("--max-agents", type=pipeline_base.positive_int, default=6,
                   help="complexity recommendation cap (default: 6)")
    p.add_argument("--spec", metavar="FILE", default=None,
                   help="path to a spec.md; its ac-directive blocks run as a "
                        "gate before the verdict settles — a failing directive "
                        "blocks an APPROVE (downgrades to REQUEST_CHANGES)")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    legacy_code = EXIT_INFRA
    setup_error = None
    with runner.ci_mode(args.ci):
        try:
            if args.diff_git:
                legacy_code = run_diff_git(args)
            else:
                if args.diff:
                    source = build_diff_source(args.diff)
                elif args.dir:
                    source = build_dir_source(args.dir)
                elif args.file:
                    source = build_file_source(args.file)
                else:  # source group is required; --project-dir is the remainder
                    source = build_project_source(args.project_dir)
                legacy_code = _review_source(source, args)
        except ReviewError as exc:
            setup_error = str(exc)
            print(f"X {exc}", file=sys.stderr)
            legacy_code = EXIT_NOTHING
        except gitops.GitError as exc:
            setup_error = f"git operation failed: {exc}"
            print(f"X {setup_error}", file=sys.stderr)
            legacy_code = EXIT_INFRA
        except Exception as exc:
            traceback.print_exc()
            setup_error = f"review pipeline failed: {type(exc).__name__}: {exc}"
            legacy_code = EXIT_INFRA

        if legacy_code == EXIT_INFRA:
            _write_setup_error(
                args,
                setup_error or "review setup failed before provider execution",
            )
        if legacy_code == EXIT_NOTHING:
            return EXIT_NOTHING
        if not args.ci:
            return legacy_code
        return pipeline_base.ci_exit_from_final(
            args.out,
            legacy_code,
            fail_on_selector=args.fail_on,
            error_writer=lambda exc: _write_setup_error(
                args, f"final artifact unavailable: {exc}",
            ),
        )


if __name__ == "__main__":
    sys.exit(main())
