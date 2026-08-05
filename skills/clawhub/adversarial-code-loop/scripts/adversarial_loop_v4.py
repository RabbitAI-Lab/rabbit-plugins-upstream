#!/usr/bin/env python3
"""Adversarial Code Loop v4 — git-native orchestrator.

BUILD -> REVIEW -> (FIX -> VERIFY)^N -> ARBITER, on a dedicated loop branch.

Phase logic lives in scripts/phases/*; the shared engine (providers, jsonio,
gitops) lives in the adversarial-common sibling skill. This file only wires
phases together, persists state.json for --resume, and maps verdicts to exit
codes. The legacy predecessor entry point was removed before release.

Exit codes:
  0 APPROVED    — squash-merged into the parent branch
  1 infrastructure failure (phase crash, git error, interrupt)
  2 usage error (bad flags, missing spec)
  3 REJECT      — findings unresolved after max-loops, or a gate failed
  4 ARBITRATED  — approved by the arbiter; conditions recorded in final.json
  5 context blocked before any provider or git mutation

The machine-readable contract is <out>/<feature>/final.json.
"""
import argparse
import concurrent.futures
import json
import os
import shutil
import subprocess
import sys
import threading
from functools import partial
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
# skill root (for `scripts.phases.*`) and the adversarial-common sibling skill
# (for `adversarial_common.*`) must both be importable.
sys.path.insert(0, str(_SCRIPTS_DIR.parent))
sys.path.insert(0, str(_SCRIPTS_DIR.parent.parent / "adversarial-common"))

from adversarial_common import (
    CostLedger,
    NoProviderAvailable,
    ProviderConfigError,
    QuotaResolver,
    gates,
    gitops,
    jsonio,
    load_provider_config,
    runner,
)
import adversarial_common.pipeline_base as pipeline_base
from adversarial_common.providers import resolve_role_cmd
from adversarial_common.gates import run_contract_gate  # F1 AC-directive contract gate (P5)
from scripts.phases import (
    integration_gate,
    phase_arbiter,
    phase_build,
    phase_fix,
    phase_git,
    phase_review,
    phase_verify,
)

EXIT_APPROVED = 0
EXIT_INFRA = 1
EXIT_USAGE = 2
EXIT_REJECTED = 3
EXIT_ARBITRATED = 4
EXIT_CONTEXT_BLOCKED = runner.CI_EXIT_CONTEXT_BLOCKED

# DEV must write files into the worktree; REVIEW must not.
DEFAULT_DEV_CMD = "codex exec --skip-git-repo-check --sandbox workspace-write"
DEFAULT_REVIEW_CMD = "pi --provider zai --model glm-5.2"

_EXIT_BY_VERDICT = {"APPROVED": EXIT_APPROVED, "ARBITRATED": EXIT_ARBITRATED}

_THRESHOLD_ENV = {
    "min_chars": (
        "ACL_MIN_CONTEXT_CHARS", "ACL_CONTEXT_MIN_CHARS",
        "ADVERSARIAL_MIN_CHARS",
    ),
    "min_tokens": (
        "ACL_MIN_CONTEXT_TOKENS", "ACL_CONTEXT_MIN_TOKENS",
        "ADVERSARIAL_MIN_TOKENS",
    ),
}
_GATE_FINDING_ID = "GATE-VERIFICATION"
_FORCE_PROVIDER_ROLES = frozenset({"dev", "review", "verify", "arbiter"})


def _read_json(path):
    """Load JSON from *path*; None on any read/parse failure (defensive)."""
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _mark(state, out_dir, phase, loop=None, findings=None):
    """Record *phase* as completed and flush state.json for --resume."""
    state["phase"] = phase
    if loop is not None:
        state["loop"] = loop
    if findings is not None:
        state["findings"] = findings
    completed = state.setdefault("completed", [])
    if phase not in completed:
        completed.append(phase)
    _write_json(out_dir, "state.json", state)


def _execution_settings(args):
    """Return runner settings shared by every model phase."""
    return {
        "max_retries": getattr(args, "max_retries", 3),
        "max_input_chars": getattr(
            args, "max_input_chars", runner.DEFAULT_MAX_INPUT_CHARS
        ),
        "max_output_chars": getattr(
            args, "max_output_chars", runner.DEFAULT_MAX_OUTPUT_CHARS
        ),
        "truncate_input": getattr(args, "truncate_input", False),
    }


def _execution_record(args):
    """Return serializable effective execution controls for artifacts."""
    return {
        **_execution_settings(args),
        "show_costs": getattr(args, "show_costs", False),
        "max_agents": getattr(args, "max_agents", 6),
    }


def _restore_ledger(state):
    """Rebuild recorded usage on resume so costs are neither lost nor duplicated."""
    ledger = CostLedger()
    costs = state.get("costs", {})
    records = costs.get("records", []) if isinstance(costs, dict) else []
    for record in records:
        if not isinstance(record, dict):
            continue
        try:
            record_args = {
                "phase": str(record.get("phase", "")),
                "persona": str(record.get("persona", "")),
            }
            if record.get("estimated", False):
                record_args.update({
                    "prompt_text": _estimated_token_text(
                        record.get("prompt_tokens", 0)
                    ),
                    "completion_text": _estimated_token_text(
                        record.get("completion_tokens", 0)
                    ),
                })
            else:
                record_args["usage"] = {
                    "prompt_tokens": record.get("prompt_tokens", 0),
                    "completion_tokens": record.get("completion_tokens", 0),
                }
            ledger.record(record.get("model"), **record_args)
        except (TypeError, ValueError):
            continue
    return ledger


def _estimated_token_text(token_count):
    """Return minimal text whose char/4 estimate equals *token_count*."""
    if (
        isinstance(token_count, bool)
        or not isinstance(token_count, int)
        or token_count < 0
    ):
        raise ValueError("estimated token count must be a non-negative integer")
    return "" if token_count == 0 else " " * (token_count * 4 - 3)


def _provider_call_args(args, role, explicit_cmd):
    """Return the registry controls shared by every invocation of *role*."""
    forced = getattr(args, "_force_providers", {})
    return {
        "explicit_cmd": explicit_cmd,
        "force": bool(getattr(args, "force", False)),
        "force_provider": forced.get(role),
    }


def _provider_history_from_group_results(group_results, phase):
    """Flatten concurrent phase decisions in stable group order."""
    history = []
    for index in sorted(group_results):
        result = group_results[index].get(phase) or {}
        for decision in result.get("provider_history", []):
            if isinstance(decision, dict):
                history.append(dict(decision))
    return history


def _normalize_findings(findings, state=None):
    """Normalize R8 labels without dropping or replacing finding identity."""
    payload = {"findings": findings}
    warnings = []
    jsonio.normalize_findings(payload, warnings=warnings)
    if state is not None:
        for warning in warnings:
            if warning not in state.setdefault("warnings", []):
                state["warnings"].append(warning)
    return findings


def _gate_finding(gate, stage, loop_n=0):
    """Convert objective verification evidence into one stable FIX finding."""
    return {
        "id": _GATE_FINDING_ID,
        "severity": "blocker",
        "file": "(verification gate)",
        "line": 1,
        "summary": f"{stage.replace('_', ' ').title()} verification failed",
        "evidence": (
            f"Command: {gate.get('command', '')}\n"
            f"Exit: {gate.get('exit_code')}\n"
            f"Log: {gate.get('log', '')}"
        ),
        "confidence": "high",
        "basis": "code",
        "origin": "verification_gate",
        "gate_stage": stage,
        "fix_round": loop_n,
        "gate": gate,
    }


def _replace_gate_finding(findings, gate_finding):
    return [
        finding for finding in findings
        if finding.get("id") != _GATE_FINDING_ID
    ] + [gate_finding]


def _without_gate_findings(findings):
    """Discard synthetic gate evidence after objective verification passes."""
    return [finding for finding in findings if not finding.get("gate")]


# --- partition & concurrent batches (R7) -------------------------------------

def _partition_findings_by_file(findings):
    """Partition *findings* into file-disjoint groups.

    Two findings that share a filename land in the same group; findings
    that touch disjoint files are placed in independent groups that can
    be fixed concurrently without conflicts.
    """
    # Union-find: two findings are linked if they share a file.
    parent = list(range(len(findings)))

    def _find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def _union(a, b):
        ra, rb = _find(a), _find(b)
        if ra != rb:
            parent[ra] = rb

    file_to_indices = {}
    for i, f in enumerate(findings):
        name = (f.get("file") or "").strip()
        indices = file_to_indices.setdefault(name, [])
        if indices:
            _union(indices[0], i)
        indices.append(i)

    root_groups = {}
    for i, f in enumerate(findings):
        root_groups.setdefault(_find(i), []).append(f)

    return list(root_groups.values())


def _abort_in_progress_cherry_pick(workdir, state):
    """Abort a cherry-pick left mid-merge in *workdir* (no-op if none).

    ``gitops.cherry_pick`` aborts on non-zero exit but not on a
    ``TimeoutExpired``: git may have written ``CHERRY_PICK_HEAD`` and staged
    conflicts before the subprocess timed out. If that state survives, the
    restore checkout/stash-pop fails and the loop branch is left mid-merge
    with the saved stash un-popped (A1).

    A missing ``CHERRY_PICK_HEAD`` means there is nothing to abort -- the
    overwhelmingly common case on every round -- and is silently skipped.
    A real abort failure (R3) is no longer swallowed: it is recorded in
    ``state["warnings"]``, mirroring the worktree-cleanup pattern below,
    so a repo left mid-merge is visible to operators instead of vanishing.

    A1: ``<workdir>/.git/CHERRY_PICK_HEAD`` only holds when *workdir* is a
    repository's top-level checkout with an on-disk ``.git`` directory. When
    *workdir* is a subdirectory of the repo, or a linked worktree (where
    ``.git`` is a file pointing elsewhere), that path never exists even
    mid-cherry-pick, so this used to no-op right past an active abort. Ask
    git for the resolved path instead via ``rev-parse --git-path``.
    """
    try:
        path_result = subprocess.run(
            ["git", "rev-parse", "--git-path", "CHERRY_PICK_HEAD"],
            cwd=str(workdir), capture_output=True, timeout=30, text=True,
        )
    except (subprocess.SubprocessError, OSError) as exc:
        state.setdefault("warnings", []).append(
            f"cherry-pick abort failed: {exc}"
        )
        return
    if path_result.returncode != 0:
        return
    cherry_pick_head = Path(workdir) / path_result.stdout.strip()
    if not cherry_pick_head.exists():
        return
    try:
        result = subprocess.run(
            ["git", "cherry-pick", "--abort"],
            cwd=str(workdir), capture_output=True, timeout=30,
        )
    except (subprocess.SubprocessError, OSError) as exc:
        state.setdefault("warnings", []).append(
            f"cherry-pick abort failed: {exc}"
        )
        return
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or b"").decode(
            "utf-8", "replace"
        ).strip()
        state.setdefault("warnings", []).append(
            f"cherry-pick abort failed: {detail or f'exit {result.returncode}'}"
        )


def _run_concurrent_fix_verify_round(
    findings, dev_cmd, review_cmd, workdir, feature, loop_n,
    timeout, execution, ledger,
    branch_point, max_workers, out_dir, state, args,
):
    """Run one FIX-to-VERIFY round concurrently in isolated worktrees.

    Findings are partitioned into file-disjoint groups. Each group runs
    its own FIX then VERIFY in a dedicated worktree. Successful worktree
    commits are cherry-picked back into the main worktree in order. All
    worktrees are cleaned up on any exit path.
    """
    groups = _partition_findings_by_file(findings)
    workers = min(len(groups), max_workers)

    wt_base = Path(out_dir) / "worktrees"
    # Clean up any stale worktrees from a prior interrupted run.
    if wt_base.exists():
        shutil.rmtree(str(wt_base), ignore_errors=True)
    wt_base.mkdir(parents=True, exist_ok=True)

    lock = threading.Lock()
    group_results = {}     # group_index -> result dict
    worktree_infos = []    # [(wt_path, branch_name)]

    def _process_group(idx, group):
        wt_path = wt_base / f"wt-{idx}"
        branch = f"loop/{feature}/fix-{loop_n}/g{idx}"

        try:
            gitops.create_worktree(workdir, str(wt_path), "HEAD", branch)
            with lock:
                worktree_infos.append((str(wt_path), branch))

            fix = phase_fix.run_fix(
                group, dev_cmd, str(wt_path), timeout,
                feature, loop_n, getattr(args, "_provider_resolver", None),
                **_provider_call_args(args, "dev", getattr(args, "dev_cmd", None)),
                execution=execution, ledger=ledger,
            )
            # Record per-group fix artifact
            _write_json(out_dir, f"03_fix_{loop_n}_g{idx}.json", fix)

            if fix.get("exit_code") != 0:
                return idx, {"fix": fix, "verify": None,
                             "group_size": len(group),
                             "error": fix.get("error", "FIX failed")}

            wt_diff = gitops.get_diff(str(wt_path), branch_point)
            verify = phase_verify.run_verify(
                group, wt_diff, review_cmd,
                getattr(args, "_provider_resolver", None), jsonio,
                timeout=timeout, workdir=str(wt_path),
                branch_point=branch_point,
                **_provider_call_args(
                    args, "verify", getattr(args, "review_cmd", None)
                ),
                execution=execution, ledger=ledger,
            )
            _write_json(out_dir, f"04_verdict_{loop_n}_g{idx}.json", verify)

            return idx, {"fix": fix, "verify": verify,
                         "group_size": len(group), "branch": branch}
        except NoProviderAvailable:
            raise
        except (subprocess.SubprocessError, OSError, gitops.GitError):
            # R2/A2: a git hang, timeout, missing binary, or a plain non-zero
            # git exit (create_worktree, get_diff above all raise GitError
            # for that) is an infrastructure failure here, not a review
            # dispute -- this is setup, not the merge step below where a
            # GitError is genuine dispute evidence. Re-raise (rather than
            # folding it into a per-group {"error": ...}) so it reaches
            # _pipeline's generic-exception handler and routes to
            # EXIT_INFRA instead of being buried as a "disputed" finding
            # that would settle the round as REJECT.
            raise
        except Exception as exc:
            return idx, {"error": str(exc), "group_size": len(group)}

    _banner(
        f"FIX+VERIFY (round {loop_n}/{args.max_loops}) "
        f"— {workers} worker(s), {len(groups)} group(s)"
    )

    try:
        # Run all groups concurrently (capped at max_workers).
        provider_error = None
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
            futs = {pool.submit(_process_group, i, g): i for i, g in enumerate(groups)}
            for fut in concurrent.futures.as_completed(futs):
                try:
                    idx, result = fut.result()
                except NoProviderAvailable as exc:
                    if provider_error is None:
                        provider_error = exc
                    continue
                with lock:
                    group_results[idx] = result

        # Cherry-pick successful worktree commits back in order.
        for idx in sorted(group_results):
            result = group_results[idx]
            branch = result.get("branch")
            if not branch or result.get("error"):
                continue
            try:
                gitops.checkout(workdir, state["branch"])
                gitops.cherry_pick(workdir, branch)
            except (gitops.GitError, subprocess.SubprocessError, OSError) as exc:
                # A real merge conflict (GitError) is actionable evidence:
                # mark the group disputed and keep reconciling (AC2).
                # A subprocess/OS failure (git hung or binary missing) is
                # infrastructure, not a code dispute: re-raise so the caller
                # maps it to EXIT_INFRA instead of a raw traceback (AC1).
                if isinstance(exc, gitops.GitError):
                    result["merge_error"] = str(exc)
                else:
                    raise

        if provider_error is not None:
            raise provider_error
    finally:
        # ponytail: cleanup on any exit path (success, failure, interrupt).
        # Keep this outside the try body so an aggregate block is one shot.
        # A1: a timed-out cherry-pick can leave CHERRY_PICK_HEAD set in the
        # main workdir (gitops aborts only on non-zero exit, not on
        # TimeoutExpired); clear it before _restore's checkout/stash-pop runs.
        _abort_in_progress_cherry_pick(workdir, state)
        pending_branch_deletes = []
        for wt_path, branch in worktree_infos:
            remove_failed = False
            try:
                gitops.remove_worktree(workdir, str(wt_path))
            except Exception as exc:
                remove_failed = True
                state.setdefault("warnings", []).append(
                    f"worktree cleanup: {exc}"
                )
            try:
                gitops.delete_branch(workdir, branch)
            except Exception as exc:
                if not remove_failed:
                    state.setdefault("warnings", []).append(
                        f"worktree cleanup: {exc}"
                    )
                    continue
                # R4: remove_worktree above failed, so git may still treat
                # *branch* as checked out in the now-broken worktree entry.
                # Prune the stale .git/worktrees/<id> metadata and retry the
                # delete once -- otherwise the branch survives cleanup and
                # poisons a later --resume that reuses this exact name.
                try:
                    gitops.prune_worktrees(workdir)
                except Exception as prune_exc:
                    state.setdefault("warnings", []).append(
                        f"worktree prune: {prune_exc}"
                    )
                try:
                    gitops.delete_branch(workdir, branch)
                except Exception as retry_exc:
                    # A3: remove_worktree above failed *and left wt_path on
                    # disk* (its normal failure mode), so the prune just run
                    # still can't drop the stale .git/worktrees/<id> entry --
                    # git keeps treating *branch* as checked out there, and
                    # this retry fails for the same reason as the first
                    # attempt. Defer one more retry until after wt_base is
                    # rmtree'd and pruned again below, once the directory is
                    # actually gone and prune can reconcile the metadata.
                    pending_branch_deletes.append((branch, retry_exc))
        try:
            shutil.rmtree(str(wt_base), ignore_errors=True)
        except Exception as exc:
            state.setdefault("warnings", []).append(
                f"worktree cleanup: {exc}"
            )
        # R2: reconcile dangling .git/worktrees/<id> metadata left by any
        # failed removal above. Runs after the cleanup loop, never mid-round.
        # A1: prune failures are cleanup-only; record them as warnings so an
        # active NoProviderAvailable/timeout/etc. survives this finally block
        # instead of being masked by a GitError from pruning.
        try:
            gitops.prune_worktrees(workdir)
        except Exception as exc:
            state.setdefault("warnings", []).append(
                f"worktree prune: {exc}"
            )
        # A3: wt_base is gone now, so the prune above can finally drop any
        # worktree metadata that survived the per-worktree retry only
        # because its directory was still on disk. Retry the branch deletes
        # deferred above now that git has no remaining reason to treat them
        # as checked out -- otherwise the branch survives cleanup and
        # poisons a later --resume that reuses this exact name.
        for branch, first_exc in pending_branch_deletes:
            try:
                gitops.delete_branch(workdir, branch)
            except Exception as exc:
                state.setdefault("warnings", []).append(
                    f"worktree cleanup: branch {branch!r} not deleted "
                    f"(first attempt: {first_exc}; final retry: {exc})"
                )

    # --- Aggregate results ---
    all_verify_results = []
    group_fix_errors = []

    for idx in sorted(group_results):
        result = group_results[idx]
        fix = result.get("fix") or {}
        if fix.get("exit_code") != 0 or result.get("error"):
            group_fix_errors.append(idx)
        verify = result.get("verify") or {}
        all_verify_results.extend(verify.get("results", []))
        # Findings in groups that failed fix or merge are marked disputed.
        if result.get("error") or result.get("merge_error"):
            reason = result.get("error") or result.get("merge_error", "unknown")
            for f in groups[idx]:
                all_verify_results.append({
                    "id": f["id"], "status": "disputed",
                    "evidence": f"FIX group failed: {reason[:200]}",
                    "confidence": "medium", "basis": "inference",
                })

    # Combined fix artifact
    fix_exit = 0 if not group_fix_errors else 1
    combined_fix = {
        "phase": "fix", "loop": loop_n, "exit_code": fix_exit,
        "groups": len(groups), "group_results": [
            group_results[i].get("fix", {}) for i in sorted(group_results)
        ],
        "group_errors": group_fix_errors,
        "concurrent": True, "workers": workers,
        "provider_history": _provider_history_from_group_results(
            group_results, "fix"
        ),
    }

    # Combined verify artifact
    all_verdict = "APPROVE" if (
        all_verify_results and
        all(
            pipeline_base.is_settled_status(r.get("status"))
            for r in all_verify_results
        )
    ) else "REJECT"
    combined_verify = {
        "phase": "verify", "exit_code": 0,
        "results": all_verify_results,
        "verdict": all_verdict,
        "groups": len(groups),
        "concurrent": True, "workers": workers,
        "provider_history": _provider_history_from_group_results(
            group_results, "verify"
        ),
    }

    return combined_fix, combined_verify


# --- shared lifecycle policy -------------------------------------------------


class _ConsoleVerdictOverride:
    """Holds the A1 console-line rewrite for the *current* finish_pipeline
    call. Reassigned unconditionally by _after_final_write on every call
    (never merely reset-then-forgotten), so a stale value from a prior
    _finish() invocation can never bleed into the next one's output."""

    value = None


_console_verdict_override = _ConsoleVerdictOverride()


def _loop_reporter(message):
    """Wrap the shared helper's stdout reporter (A1).

    finish_pipeline prints its final "\\n{verdict}" line from the raw verdict
    string it was called with -- fixed as APPROVED/ARBITRATED before a
    post-merge integration-gate failure (P17) or a finalize failure can ever
    be known, since both are only discovered inside that same call. Rewrite
    just that line to the INFRASTRUCTURE_ERROR sentinel _write_final_artifact
    already downgrades final.json to, so the console never claims an approval
    the run didn't actually reach.
    """
    override = _console_verdict_override.value
    if override and message.startswith("\n"):
        body = message[1:]
        for verdict in _EXIT_BY_VERDICT:
            if body == verdict or body.startswith(verdict + " "):
                message = "\n" + override + body[len(verdict):]
                break
    print(message)


def _write_final_artifact(out_dir, verdict, payload):
    """Keep the loop's authoritative final.json writer contract."""
    artifact = dict(payload)
    if artifact.get("infrastructure") is True:
        # Any infra-classified exit (a git finalize failure OR an infra flag
        # carried in the payload) sets the shared helper's internal
        # infrastructure marker, which it uses to select EXIT_INFRA.  Strip
        # that marker and the derived status so they never leak into the
        # public final.json contract as internal fields, but re-inject
        # infrastructure=True into the re-derivation call below (R1) so the
        # recomputed status still reads "infrastructure_error" instead of
        # drifting to "clean" once the marker that drove that classification
        # is gone.
        artifact.pop("infrastructure")
        artifact.pop("status", None)
        # A1: an infra-classified exit reached here with the run's original
        # would-be-approved verdict still attached (e.g. a post-merge P17
        # gate failure, or the squash-merge itself failing) must never
        # persist as an approval -- downgrade the verdict written to
        # final.json to the same INFRASTRUCTURE_ERROR sentinel the pre-merge
        # contract-gate-infra path already uses, so gate_passed=False (or a
        # failed merge) never coexists with verdict=APPROVED/ARBITRATED.
        if verdict in _EXIT_BY_VERDICT:
            verdict = "INFRASTRUCTURE_ERROR"
        artifact = runner.ensure_final_payload(
            payload=artifact, verdict=verdict, infrastructure=True,
        )
        artifact.pop("infrastructure", None)
        artifact.pop("verdict", None)
    return jsonio.write_final_json(out_dir, verdict, **artifact)


def _blocked_artifact_extra(_args, _result):
    """Fields historically present on a context-blocked loop run."""
    return {
        "gates": [],
        "findings": [],
        "epistemic_labels": jsonio.epistemic_distribution([]),
    }


def _loop_git_setup(context):
    """Adapt the phase-owned setup while the shared base owns its lifecycle."""
    policy = context["policy"]
    return phase_git.setup_git(
        context["workdir"], context["feature"], policy.parent_branch,
    )


def _cleanup_loop_worktrees(context):
    """Purge orphaned worktrees before branch/stash restoration."""
    out_dir = context.get("out_dir")
    workdir = context.get("workdir")
    if out_dir is not None:
        shutil.rmtree(str(Path(out_dir) / "worktrees"), ignore_errors=True)
    # R2: a prior interrupted run can leave dangling .git/worktrees/<id>
    # metadata (no matching directory) that rmtree above does not reach.
    if workdir is not None:
        gitops.prune_worktrees(workdir)


def _record_failed_state(state, out_dir, phase):
    _mark(state, out_dir, phase)


def _record_phase_failure(label, result, state, out_dir):
    """Preserve the loop's pre-migration phase-failure artifact contract."""
    error = result.get("error", "unknown error")
    state["error"] = f"{label}: {error}"
    _record_failed_state(state, out_dir, f"{label}_failed")
    print(f"X {label} failed: {error}")
    return EXIT_INFRA


def _loop_git_finalize(context):
    """Map loop verdicts to phase_git without changing marker/merge policy."""
    verdict = context["verdict"]
    git_verdict = (
        "APPROVE" if verdict in ("APPROVED", "ARBITRATED") else "REJECT"
    )
    return phase_git.finalize_git(
        context["workdir"], context["feature"],
        context["state"]["parent_branch"], git_verdict,
        str(Path(context["out_dir"]) / "final.md"),
        no_merge=context["args"].no_merge,
    )


def _maybe_run_integration_gate(context):
    """P17/R1: after squash-merge, before declaring APPROVED, verify the
    sibling adversarial-* repos named in the manifest still pass their own
    suites (P15). Opt-in via --integration-gate-manifest: unset (the
    default) skips this entirely so ordinary loop usage against a single
    project is unaffected. Only runs on a would-be-approved verdict — this
    callback fires from the payload builder, which finish_pipeline invokes
    strictly after finalize_callback has already performed the squash-merge.
    A2: if that finalize itself failed (no merge landed), there is nothing
    to integration-test, so the gate is skipped rather than launching every
    manifest test command against a merge that never happened.
    """
    args = context["args"]
    manifest_path = getattr(args, "integration_gate_manifest", None)
    if (
        not manifest_path
        or context["verdict"] not in _EXIT_BY_VERDICT
        or context.get("finalize_error")
    ):
        return None
    workspace = getattr(args, "integration_gate_workspace", None) or str(
        Path(context["workdir"]).resolve().parent
    )
    _banner("INTEGRATION GATE")
    try:
        result = integration_gate.run_integration_gate(
            workspace, manifest_path=manifest_path,
        )
    except Exception as exc:  # fail closed — never APPROVE an unrun gate
        result = {
            "per_repo": [], "gate_passed": False,
            "gate_duration_s": 0.0, "error": f"gate error: {exc}",
        }
    passed = sum(1 for r in result["per_repo"] if r["status"] == "pass")
    print(f"  gate_passed={result['gate_passed']} "
          f"({passed}/{len(result['per_repo'])} repos)")
    return result


def _loop_final_payload(context):
    """Supply loop-only evidence fields to the common final payload."""
    state = context["state"]
    args = context["args"]
    findings = _normalize_findings(list(state.get("findings", [])), state)
    distribution = state.get("epistemic_labels")
    if not isinstance(distribution, dict):
        distribution = jsonio.epistemic_distribution(findings)
    ledger = getattr(args, "_ledger", None)
    costs = ledger.summary() if ledger is not None else state.get("costs", {})
    # R4/AC5: project the F1 contract gate into ac_checks[] so every directive
    # (and every parse failure) carries its status/diagnostic in final.json.
    contract = _contract_gate_result(state)
    payload = {
        "arbitrated": bool(context["extra"].get("arbitrated", False)),
        "context": state.get("context", getattr(args, "_context", {})),
        "thresholds": state.get("thresholds", {}),
        "execution": state.get("execution", _execution_record(args)),
        "attempts": state.get("attempts", []),
        "cap_events": state.get("cap_events", []),
        "calls": state.get("calls", []),
        "costs": costs,
        "gates": state.get("gates", []),
        "complexity": state.get("complexity", {}),
        "findings": findings,
        "epistemic_labels": distribution,
        "epistemic_distribution": distribution,
        "warnings": state.get("warnings", []),
    }
    if contract is not None:
        # ensure_final_payload projects this mapping via _normalized_ac_checks.
        payload["ac_checks"] = contract
    gate_result = _maybe_run_integration_gate(context)
    if gate_result is not None:
        payload["integration_gate"] = gate_result
        if not gate_result.get("gate_passed"):
            # ensure_final_payload (P16) derives status="infrastructure_error"
            # from a failing gate on its own, but finish_pipeline's EXIT_INFRA
            # branch keys off the explicit "infrastructure" flag, not status
            # -- set it here so a gate failure actually exits EXIT_INFRA (R1),
            # not the exit_by_verdict code the (unchanged) verdict text implies.
            payload["infrastructure"] = True
    return payload


def _after_final_write(context):
    """Persist a failed finalize without marking the run terminal."""
    # ponytail: the "X git finalize failed ({verdict}): {error}" console line
    # is already emitted by the shared finish_pipeline through
    # FinishPolicy.reporter (stdout) before post_write is invoked, so R1 is
    # satisfied via the "route through the existing reporter mechanism" option
    # — re-printing here would duplicate the failure line.
    if context["finalize_error"]:
        state = context["state"]
        error = context["finalized"].get("error", "unknown error")
        state["error"] = f"git finalize: {error}"
        _write_json(context["out_dir"], "state.json", state)
    # A1: finish_pipeline prints its final "\n{verdict}" line from the raw
    # verdict string it was called with, which was fixed as APPROVED/ARBITRATED
    # before the (post-merge) integration gate or a finalize failure could
    # ever be known -- _write_final_artifact already downgrades final.json's
    # verdict for this case, but the console line is emitted by the shared
    # helper itself and has no payload hook of its own. Stash the downgrade
    # here (context["final_payload"] is the same infrastructure-flagged
    # payload _write_final_artifact just wrote) so _loop_reporter, called for
    # every remaining reporter message in this finish_pipeline invocation
    # including that final line, can rewrite it before it reaches stdout.
    final_payload = context.get("final_payload") or {}
    _console_verdict_override.value = (
        "INFRASTRUCTURE_ERROR" if final_payload.get("infrastructure") else None
    )


def _complete_loop_state(context):
    """Preserve the terminal marker ordering used by resume."""
    state = context["state"]
    verdict = context["verdict"]
    state["verdict"] = verdict
    final_payload = context.get("final_payload") or {}
    if final_payload.get("infrastructure"):
        # A post-merge integration-gate failure (P17) keeps the "APPROVED"
        # verdict text but the actual exit was EXIT_INFRA -- resume must
        # replay that, not the exit code the verdict text alone implies.
        state["exit_code"] = EXIT_INFRA
    else:
        state["exit_code"] = _EXIT_BY_VERDICT.get(verdict, EXIT_REJECTED)
    _mark(state, context["out_dir"], "done")


_LOOP_PREFLIGHT_POLICY = pipeline_base.PreflightPolicy(
    context_kind="input",
    threshold_env=_THRESHOLD_ENV,
    execution_settings=_execution_record,
    blocked_writer=_write_final_artifact,
    blocked_extra=_blocked_artifact_extra,
)
_LOOP_RESTORE_POLICY = pipeline_base.RestorePolicy(
    git_adapter=gitops,
    pre_restore=_cleanup_loop_worktrees,
    state_writer=lambda out_dir, name, payload: _write_json(
        out_dir, name, payload,
    ),
)
_LOOP_FINISH_POLICY = pipeline_base.FinishPolicy(
    pipeline_name="Adversarial Loop",
    approval_label="adversarial",
    loop_label="Fix/verify loops",
    approved_verdicts=frozenset({"APPROVED", "ARBITRATED"}),
    exit_by_verdict=_EXIT_BY_VERDICT,
    rejected_exit=EXIT_REJECTED,
    infrastructure_exit=EXIT_INFRA,
    finalize_callback=_loop_git_finalize,
    payload_builder=_loop_final_payload,
    final_writer=_write_final_artifact,
    post_write=_after_final_write,
    state_complete=_complete_loop_state,
    reporter=_loop_reporter,
)

# Compatibility aliases remain importable.  The phase-failure adapter stays
# local because the shared helper always emits a retrospective, which was not
# part of this loop's pre-migration artifact contract.
_write_json = pipeline_base.write_json
_banner = pipeline_base.banner
_ensure_ids = pipeline_base.ensure_finding_ids
_unresolved = pipeline_base.unresolved_findings
_positive_int = pipeline_base.positive_int
_non_negative_int = pipeline_base.non_negative_int
_threshold_overrides = partial(
    pipeline_base.threshold_overrides, threshold_env=_THRESHOLD_ENV,
)
_preflight = partial(pipeline_base.preflight, policy=_LOOP_PREFLIGHT_POLICY)
_record_phase = partial(
    pipeline_base.record_phase, include_epistemic=True,
)
_phase_failed = _record_phase_failure
_restore = partial(pipeline_base.restore_git, policy=_LOOP_RESTORE_POLICY)
_finish = partial(pipeline_base.finish_pipeline, policy=_LOOP_FINISH_POLICY)


# --- pipeline -----------------------------------------------------------------

def _run_contract_gate(spec_path, workdir, out_dir, state):
    """Run the shared F1 AC-directive contract gate (P5) over *spec_path*.

    ``run_contract_gate`` parses the ``ac-directive`` blocks bound to the
    spec's acceptance criteria, executes each in *workdir*, and settles
    ``APPROVE`` only when every directive (and every bound AC) passes. A spec
    with no directive blocks settles ``APPROVE`` vacuously, so non-contract
    specs are unaffected — the gate only ever *blocks* APPROVE.

    Returns the gate result (``{settle, ac_status, failures, directives}``),
    persisted as ``02_contract_gate.json``. Any unexpected error fails closed
    (``REJECT``): a directive that could not be verified must not let the run
    APPROVE (pitfall #37).
    """
    try:
        contract = run_contract_gate(spec_path, workdir)
    except Exception as exc:  # fail closed — never APPROVE an unverifiable spec
        contract = {
            "settle": "REJECT",
            "ac_status": {},
            "failures": [{"ac": "UNKNOWN", "id": None,
                          "reason": f"gate error: {exc}"}],
            "directives": [],
            "infra": True,
        }
    _write_json(out_dir, "02_contract_gate.json", contract)
    state.setdefault("gates", []).append(contract)
    return contract


def _contract_gate_result(state):
    """Return the F1 contract-gate entry recorded on state, or None.

    It is the only gate carrying a ``settle`` verdict (shell gates use
    ``ok``), so it is uniquely identifiable among state["gates"]. A resumed
    run can re-execute the gate (it is not guarded by ``completed``), so the
    last such entry wins — it reflects the final repo state."""
    contract = None
    for gate in state.get("gates", []):
        if isinstance(gate, dict) and "settle" in gate:
            contract = gate
    return contract


def _contract_gate_infra(contract):
    """True if the contract gate failed for infrastructure, not a real REJECT.

    A top-level ``infra`` marks a gate that could not run at all (caught
    exception in _run_contract_gate); individual directive outcomes carry
    ``infra`` when their containment was unavailable. Either means the spec
    was not rejected on its merits — it could not be verified — so the run
    must finalize as an infrastructure failure, not a plain REJECT (R1)."""
    if not isinstance(contract, dict):
        return False
    if contract.get("infra"):
        return True
    return any(
        isinstance(d, dict) and d.get("infra")
        for d in contract.get("directives", [])
    )


def _pipeline(args, dev_cmd, review_cmd, arbiter_cmd,
              workdir, feature, out_dir, state):
    """Run (or resume) the full v4 workflow. Returns the process exit code."""
    state.setdefault("feature", feature)
    completed = state.setdefault("completed", [])
    ledger = getattr(args, "_ledger", None) or CostLedger()
    args._ledger = ledger
    execution = _execution_settings(args)

    # A finished run must not be re-entered: on APPROVED the loop branch was
    # squash-merged and deleted, so replaying the resume checkout would fail.
    if "done" in completed:
        print(f"Run already finished ({state.get('verdict', 'unknown')}) — "
              f"nothing to resume.")
        return int(state.get("exit_code", EXIT_INFRA))

    # PHASE 0 — git setup. R1/R3 preflight has already completed in main().
    if "git_setup" in completed:
        _banner(f"RESUME  (phase={state.get('phase')}, loop={state.get('loop', 0)})")
        gitops.checkout(workdir, state["branch"])
    else:
        if gitops.detect_enclosing_repo(workdir):
            parent_branch = gitops.get_current_branch(workdir)
        else:
            parent_branch = "main"
        setup = pipeline_base.setup_git(
            workdir,
            feature,
            state,
            policy=pipeline_base.GitSetupPolicy(
                parent_branch=parent_branch,
                setup_callback=_loop_git_setup,
            ),
        )
        if setup["exit_code"] != 0:
            print(f"X git setup failed: {setup.get('error', 'unknown error')}")
            return EXIT_INFRA
        state.update({
            "parent_branch": parent_branch,
            "branch": setup["branch"],
            "branch_point": setup["branch_point"],
            "stash_id": setup["stash_id"],
            "loop": 0,
            "findings": [],
        })
        _mark(state, out_dir, "git_setup")
        _banner(f"LOOP BRANCH  {setup['branch']}  (from {parent_branch})")

    branch_point = state["branch_point"]
    spec_text = getattr(args, "_spec_text", None)
    if spec_text is None:
        spec_text = Path(args.spec).read_text(encoding="utf-8")
    jsonio.save_artifact(out_dir, "00_spec.txt", spec_text)
    build_verification_cmd = args.build_cmd
    fix_verification_cmd = args.test_cmd or args.build_cmd

    # Validate the project and configured command before the first model call.
    if "pre_build_gate" in completed:
        pre_gate = _read_json(Path(out_dir) / "00_pre_build_gate.json") or {}
    else:
        pre_gate = gates.pre_build_gate(workdir, build_verification_cmd)
        _write_json(out_dir, "00_pre_build_gate.json", pre_gate)
        state.setdefault("gates", []).append(pre_gate)
        if not pre_gate.get("ok", False):
            if pre_gate.get("infra"):
                return _phase_failed("pre_build_gate", pre_gate, state, out_dir)
            return _finish(
                args, workdir, feature, out_dir, state, "REJECT",
                reason="PRE_BUILD_GATE_FAILED",
            )
        _mark(state, out_dir, "pre_build_gate")

    if "build" not in completed:
        _banner("BUILD  (DEV)")
        result = phase_build.run_build(
            spec_text, dev_cmd, workdir, args.timeout, feature,
            getattr(args, "_provider_resolver", None),
            **_provider_call_args(args, "dev", getattr(args, "dev_cmd", None)),
            execution=execution, ledger=ledger,
        )
        _record_phase(state, "build", result, ledger)
        _write_json(out_dir, "01_build.json", result)
        if result["exit_code"] != 0:
            return _phase_failed("build", result, state, out_dir)
        _mark(state, out_dir, "build")
        print(f"  OK commit {result.get('commit_sha', '')[:12]}")

    # A post-build failure is actionable evidence, not a terminal rejection.
    post_build_failed = False
    if build_verification_cmd:
        if "post_build_gate" in completed:
            build_gate = _read_json(
                Path(out_dir) / "01_post_build_gate.json"
            ) or {}
        else:
            build_gate = gates.post_build_gate(
                workdir, build_verification_cmd, timeout=args.timeout
            )
            _write_json(out_dir, "01_post_build_gate.json", build_gate)
            state.setdefault("gates", []).append(build_gate)
            if build_gate.get("infra"):
                return _phase_failed(
                    "post_build_gate", build_gate, state, out_dir
                )
            _mark(state, out_dir, "post_build_gate")
        post_build_failed = not build_gate.get("ok", False)

    # REVIEW runs only after an objectively verified build. A failed build gate
    # becomes a normalized synthetic finding consumed by the first FIX round.
    if "review" in completed:
        review = _read_json(Path(out_dir) / "02_review.json") or {}
        findings = _ensure_ids(
            state.get("findings", review.get("findings", []))
        )
        _normalize_findings(findings, state)
        review_verdict = review.get(
            "verdict", "REQUEST_CHANGES" if findings else "APPROVE"
        )
    elif post_build_failed:
        findings = [_gate_finding(build_gate, "post_build")]
        review_verdict = "REQUEST_CHANGES"
        review = {
            "phase": "review",
            "exit_code": 0,
            "findings": findings,
            "verdict": review_verdict,
            "source": "post_build_gate",
            "warnings": [],
            "epistemic_labels": jsonio.epistemic_distribution(findings),
        }
        _write_json(out_dir, "02_review.json", review)
        _mark(state, out_dir, "review", findings=findings)
        print("  ! post-build verification failed — routing evidence to FIX")
    else:
        diff = gitops.get_diff(workdir, branch_point)
        if not diff.strip():
            return _finish(
                args, workdir, feature, out_dir, state,
                "REJECT", reason="EMPTY_DIFF",
            )
        _banner("REVIEW  (CRITIC)")
        review = phase_review.run_review(
            diff, review_cmd, getattr(args, "_provider_resolver", None), jsonio,
            workdir=workdir,
            branch_point=branch_point, execution=execution, ledger=ledger,
            timeout=args.timeout,
            **_provider_call_args(
                args, "review", getattr(args, "review_cmd", None)
            ),
        )
        _record_phase(state, "review", review, ledger)
        _write_json(out_dir, "02_review.json", review)
        if review["exit_code"] != 0:
            return _phase_failed("review", review, state, out_dir)
        findings = _ensure_ids(review["findings"])
        _normalize_findings(findings, state)
        review_verdict = review.get(
            "verdict", "REQUEST_CHANGES" if findings else "APPROVE"
        )
        _mark(state, out_dir, "review", findings=findings)
        print(f"  OK {len(findings)} findings — verdict {review_verdict}")

    approved = not findings and review_verdict == "APPROVE"
    arbitrated = False
    conditions = []
    loops_run = state.get("loop", 0)

    # A review can approve without entering FIX.  An explicitly configured
    # test gate still has to run once against that approved build.
    if approved and args.test_cmd:
        gate_name = "post_review_test_gate"
        gate_path = Path(out_dir) / "02_post_review_test_gate.json"
        if gate_name in completed:
            final_gate = _read_json(gate_path) or {}
        else:
            final_gate = gates.post_fix_gate(
                workdir, args.test_cmd, timeout=args.timeout
            )
            _write_json(out_dir, gate_path.name, final_gate)
            state.setdefault("gates", []).append(final_gate)
            if final_gate.get("infra"):
                return _phase_failed(gate_name, final_gate, state, out_dir)
            _mark(state, out_dir, gate_name)
        if not final_gate.get("ok", False):
            findings = [_gate_finding(final_gate, "post_review")]
            approved = False

    # R5 complexity cap for concurrent workers.
    complexity = state.get("complexity", {})
    max_concurrent = complexity.get(
        "recommended_agents", getattr(args, "max_agents", 6)
    )

    for n in range(1, args.max_loops + 1):
        if approved or not findings:
            break
        loops_run = n
        fix_path = Path(out_dir) / f"03_fix_{n}.json"

        # --- Determine whether to run concurrent batches ---
        # LO1: concurrent FIX+VERIFY bypasses the post-fix gate (the only path
        # that runs --test-cmd/--build-cmd once a fix is needed), so it is
        # refused whenever a verification command is configured.
        groups = _partition_findings_by_file(findings)
        partitionable = (
            len(groups) > 1
            and not any(finding.get("gate") for finding in findings)
            and not (f"fix_{n}" in completed or f"verify_{n}" in completed)
        )
        use_concurrent = partitionable and not fix_verification_cmd
        if partitionable and fix_verification_cmd:
            reason = (
                "concurrent FIX+VERIFY disabled: "
                "--test-cmd requires the sequential gate"
            )
            print(f"  ({reason})")
            state.setdefault("notes", []).append(reason)

        if use_concurrent:
            # --- Concurrent FIX+VERIFY round ---
            # R2: an unexpected failure here (e.g. a git hang or missing binary
            # surfacing as subprocess.SubprocessError / OSError during the
            # post-pool cherry-pick) must fail cleanly as EXIT_INFRA with the
            # reason recorded, never a raw traceback out of main().
            # NoProviderAvailable is still propagated for main() to handle.
            try:
                fix, verify = _run_concurrent_fix_verify_round(
                    findings, dev_cmd, review_cmd, workdir, feature, n,
                    args.timeout, execution, ledger,
                    branch_point, max_concurrent, out_dir, state, args,
                )
            except NoProviderAvailable:
                raise
            except Exception as exc:
                return _phase_failed(
                    f"fix_{n}", {"error": str(exc)}, state, out_dir,
                )
            _record_phase(state, f"fix_{n}", fix, ledger)
            _record_phase(state, f"verify_{n}", verify, ledger)
            _write_json(out_dir, fix_path.name, fix)
            _write_json(out_dir, f"04_verdict_{n}.json", verify)
            if fix["exit_code"] != 0:
                print(f"  ! {len(fix.get('group_errors', []))} group(s) failed FIX")
            _mark(state, out_dir, f"fix_{n}", loop=n)

            # Concurrent rounds always run both phases; no separate gate.
            results = verify.get("results", [])
            verdict = verify.get("verdict", "REJECT")
            remaining = _unresolved(findings, results)
            all_settled = bool(results) and not remaining
            print(f"  Verdict {verdict} — "
                  f"{len(findings) - len(remaining)}/{len(findings)} settled")

            if verdict == "APPROVE" and all_settled:
                approved = True
                _mark(state, out_dir, f"verify_{n}", loop=n, findings=findings)
                break

            if remaining:
                findings = remaining
            _normalize_findings(findings, state)
            _mark(state, out_dir, f"verify_{n}", loop=n, findings=findings)
            continue

        # --- Sequential FIX (original path) ---
        if f"fix_{n}" in completed:
            fix = _read_json(fix_path) or {}
        else:
            _banner(f"FIX  (round {n}/{args.max_loops})")
            _normalize_findings(findings, state)
            fix = phase_fix.run_fix(
                findings, dev_cmd, workdir, args.timeout, feature, n,
                getattr(args, "_provider_resolver", None),
                **_provider_call_args(
                    args, "dev", getattr(args, "dev_cmd", None)
                ),
                execution=execution, ledger=ledger,
            )
            _record_phase(state, f"fix_{n}", fix, ledger)
            _write_json(out_dir, fix_path.name, fix)
            if fix["exit_code"] != 0:
                return _phase_failed(f"fix_{n}", fix, state, out_dir)
            _mark(state, out_dir, f"fix_{n}", loop=n)

        gate_blocked = False
        gate_resolved = False
        if fix_verification_cmd:
            gate_name = f"post_fix_gate_{n}"
            gate_path = Path(out_dir) / f"03_post_fix_gate_{n}.json"
            if gate_name in completed:
                fix_gate = _read_json(gate_path) or {}
            else:
                fix_gate = gates.post_fix_gate(
                    workdir, fix_verification_cmd, timeout=args.timeout
                )
                _write_json(out_dir, gate_path.name, fix_gate)
                state.setdefault("gates", []).append(fix_gate)
                if fix_gate.get("infra"):
                    return _phase_failed(gate_name, fix_gate, state, out_dir)
                _mark(state, out_dir, gate_name, loop=n)

            # The FIX artifact is the authoritative evidence bundle for its
            # objective post-gate, including failures routed to the next round.
            fix["verification_gate"] = fix_gate
            if not fix_gate.get("ok", False):
                gate_finding = _gate_finding(fix_gate, "post_fix", n)
                fix["attached_evidence"] = [gate_finding]
                findings = _replace_gate_finding(findings, gate_finding)
                state["findings"] = findings
                _write_json(out_dir, fix_path.name, fix)
                _write_json(out_dir, "state.json", state)
                if n < args.max_loops:
                    continue
                gate_blocked = True
            else:
                gate_resolved = any(
                    finding.get("id") == _GATE_FINDING_ID
                    for finding in findings
                )
                findings = _without_gate_findings(findings)
                state["findings"] = findings
                _write_json(out_dir, fix_path.name, fix)

        if gate_resolved and not findings:
            verify = {
                "phase": "verify",
                "exit_code": 0,
                "results": [{
                    "id": _GATE_FINDING_ID,
                    "status": "resolved",
                    "note": "post-fix verification gate passed",
                }],
                "verdict": "APPROVE",
                "source": "post_fix_gate",
            }
            _write_json(out_dir, f"04_verdict_{n}.json", verify)
            approved = True
            _mark(state, out_dir, f"verify_{n}", loop=n, findings=[])
            break

        if gate_blocked:
            verify = {
                "phase": "verify", "results": [],
                "verdict": "REJECT", "exit_code": 0,
                "source": "post_fix_gate",
            }
            _write_json(out_dir, f"04_verdict_{n}.json", verify)
        elif f"verify_{n}" in completed:
            verify = _read_json(Path(out_dir) / f"04_verdict_{n}.json") or {}
        else:
            _banner(f"VERIFY  (round {n}/{args.max_loops})")
            diff = gitops.get_diff(workdir, branch_point)
            verify = phase_verify.run_verify(
                findings, diff, review_cmd,
                getattr(args, "_provider_resolver", None), jsonio,
                workdir=workdir, branch_point=branch_point,
                timeout=args.timeout,
                **_provider_call_args(
                    args, "verify", getattr(args, "review_cmd", None)
                ),
                execution=execution, ledger=ledger,
            )
            _record_phase(state, f"verify_{n}", verify, ledger)
            _write_json(out_dir, f"04_verdict_{n}.json", verify)
            if verify["exit_code"] != 0:
                return _phase_failed(f"verify_{n}", verify, state, out_dir)

        results = verify.get("results", [])
        verdict = verify.get("verdict", "REJECT")
        if verdict == "APPROVE" and not results:
            print("  ! verifier returned APPROVE with no per-finding results "
                  "— treating as inconclusive; findings stay open")
        remaining = _unresolved(findings, results)
        all_settled = bool(results) and not remaining
        print(f"  Verdict {verdict} — "
              f"{len(findings) - len(remaining)}/{len(findings)} settled")

        if verdict == "APPROVE" and all_settled:
            approved = True
            _mark(state, out_dir, f"verify_{n}", loop=n, findings=findings)
            break

        if remaining:
            findings = remaining
        _normalize_findings(findings, state)
        _mark(state, out_dir, f"verify_{n}", loop=n, findings=findings)

        if n < args.max_loops:
            continue

        if arbiter_cmd and not args.no_arbiter:
            if "arbiter" in completed:
                arb = _read_json(Path(out_dir) / "05_arbiter.json") or {}
            else:
                _banner("ARBITER  (JUDGE)")
                _normalize_findings(findings, state)
                arb = phase_arbiter.run_arbiter(
                    findings, dev_cmd, review_cmd, arbiter_cmd,
                    getattr(args, "_provider_resolver", None),
                    workdir=workdir,
                    timeout=args.timeout,
                    **_provider_call_args(
                        args, "arbiter", getattr(args, "arbiter_cmd", None)
                    ),
                    execution=execution,
                    ledger=ledger,
                )
                _record_phase(state, "arbiter", arb, ledger)
                _write_json(out_dir, "05_arbiter.json", arb)
                if arb["exit_code"] != 0:
                    return _phase_failed("arbiter", arb, state, out_dir)
                _mark(state, out_dir, "arbiter")
            if arb.get("verdict") == "APPROVE":
                approved = True
                arbitrated = True
                conditions = arb.get("conditions", [])

    state["findings"] = findings
    state["costs"] = ledger.summary()
    reason = ""
    if not approved:
        if findings:
            reason = f"findings unresolved after {args.max_loops} loops"
        else:
            reason = f"review verdict {review_verdict} with no findings"

    # pitfall #37: a failing AC directive (the F1 contract gate) blocks APPROVE
    # regardless of review/verify/arbiter verdicts — the directive is the
    # source of truth, re-checked here on the final repo state.
    contract_infra = False
    if approved:
        # pitfall #37 + trusted-spec model: re-run the contract gate over the
        # snapshot saved before BUILD (00_spec.txt), never args.spec — a spec
        # under workdir can be deleted/rewritten by BUILDER/FIXER, which would
        # let run_contract_gate APPROVE a vacuous (directive-free) spec.
        trusted_spec = str(Path(out_dir) / "00_spec.txt")
        contract = _run_contract_gate(trusted_spec, workdir, out_dir, state)
        if contract.get("settle") != "APPROVE":
            approved = False
            contract_infra = _contract_gate_infra(contract)
            reason = "CONTRACT_GATE_FAILED: " + (
                "; ".join(f"{f['ac']}: {f['reason']}"
                          for f in contract.get("failures", []))
                or "directive rejected"
            )

    if approved:
        verdict = "ARBITRATED" if arbitrated else "APPROVED"
        return _finish(
            args, workdir, feature, out_dir, state, verdict,
            loops=loops_run, conditions=conditions,
            extra={"arbitrated": arbitrated},
        )
    # An unverifiable contract (infra) is an infrastructure failure, not a
    # rejection: the spec was never actually checked, so exit 1, not 3 (R1).
    if contract_infra:
        return _finish(
            args, workdir, feature, out_dir, state, "INFRASTRUCTURE_ERROR",
            reason=reason, loops=loops_run,
            extra={"infrastructure": True},
        )
    return _finish(
        args, workdir, feature, out_dir, state, "REJECT",
        reason=reason, loops=loops_run,
    )


# --- CLI ----------------------------------------------------------------------


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
        description="Adversarial Code Loop v4 "
                    "(BUILD -> REVIEW -> (FIX -> VERIFY)^N -> ARBITER, git-native)")
    p.add_argument("--spec", required=True, help="Specification file to implement")
    p.add_argument("--workdir", default=".", help="Project directory (default: .)")
    p.add_argument("--dev-cmd", default=None,
                   help=f"BUILDER/FIXER command (default: $ACL_DEV_CMD or '{DEFAULT_DEV_CMD}')")
    p.add_argument("--review-cmd", default=None,
                   help=f"CRITIC/VERIFIER command (default: $ACL_REVIEW_CMD or '{DEFAULT_REVIEW_CMD}')")
    p.add_argument("--arbiter-cmd", default=None,
                   help="JUDGE command (optional; default: $ACL_ARBITER_CMD; unset = no arbiter)")
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
        help="force an alias for one role; repeat for multiple roles",
    )
    p.add_argument("--max-loops", type=_positive_int, default=3)
    p.add_argument("--no-arbiter", action="store_true", help="Skip the arbiter")
    p.add_argument("--timeout", type=_positive_int, default=600,
                   help="Per-subprocess timeout (s)")
    p.add_argument("--build-cmd", default=None, help="Optional build gate (shell)")
    p.add_argument("--test-cmd", default=None, help="Optional test gate (shell)")
    p.add_argument(
        "--integration-gate-manifest", default=None, metavar="PATH",
        help="Enable the cross-repo integration gate (P15/P17) before "
             "declaring APPROVED, using this repos manifest; unset (default) "
             "skips the gate entirely",
    )
    p.add_argument(
        "--integration-gate-workspace", default=None, metavar="PATH",
        help="Workspace root containing the sibling repos named in "
             "--integration-gate-manifest (default: parent of --workdir)",
    )
    p.add_argument("--no-merge", action="store_true",
                   help="On approval, leave the loop branch unmerged")
    p.add_argument("--feature", default=None,
                   help="Branch/artifact name (default: spec filename)")
    p.add_argument("--out", default=".adversarial-loop", help="Artifacts directory")
    p.add_argument("--resume", action="store_true", help="Resume from state.json")
    p.add_argument(
        "--min-chars", "--min-context-chars", dest="min_chars",
        type=_non_negative_int, default=None,
        help="minimum specification characters (env: ACL_MIN_CONTEXT_CHARS)",
    )
    p.add_argument(
        "--min-tokens", "--min-context-tokens", dest="min_tokens",
        type=_non_negative_int, default=None,
        help="minimum estimated specification tokens (env: ACL_MIN_CONTEXT_TOKENS)",
    )
    p.add_argument(
        "--max-retries", type=_non_negative_int, default=3,
        help="transient retries per provider phase (default: 3)",
    )
    p.add_argument(
        "--max-input-chars", type=_non_negative_int,
        default=runner.DEFAULT_MAX_INPUT_CHARS,
        help="hard input cap per provider phase",
    )
    p.add_argument(
        "--max-output-chars", type=_non_negative_int,
        default=runner.DEFAULT_MAX_OUTPUT_CHARS,
        help="hard output cap per provider phase",
    )
    p.add_argument(
        "--truncate-input", action="store_true",
        help="head-truncate oversized provider input instead of rejecting it",
    )
    p.add_argument(
        "--show-costs", action="store_true",
        help="print the final per-model cost breakdown to stderr",
    )
    p.add_argument(
        "--max-agents", type=_positive_int, default=6,
        help="complexity recommendation cap recorded for adaptive execution",
    )
    return p


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
                    "quota_cmd is required when the code loop uses a provider registry",
                )
            # One resolver owns the process-scoped quota cache and selection
            # history for every phase, retry, and concurrent group.
            args._provider_resolver = QuotaResolver(
                args._provider_config, args._provider_config.quota_cmd
            )
    except (ProviderConfigError, TypeError, ValueError) as exc:
        print(f"X invalid provider configuration: {exc}", file=sys.stderr)
        return EXIT_USAGE

    workdir = str(Path(args.workdir).resolve())
    if not os.path.isdir(workdir):
        print(f"X Workdir not found: {args.workdir}")
        return EXIT_USAGE

    feature = gitops.sanitize_feature_name(args.feature or Path(args.spec).stem)
    if not feature:
        print("X Could not derive a feature name; pass --feature")
        return EXIT_USAGE
    out_base = Path(args.out)
    if not out_base.is_absolute():
        out_base = Path(workdir) / out_base
    out_dir = out_base / feature
    out_dir.mkdir(parents=True, exist_ok=True)

    state = {}
    if args.resume:
        saved = _read_json(out_dir / "state.json")
        if saved and saved.get("branch"):
            state = saved
            if "done" in state.get("completed", []):
                print(
                    f"Run already finished ({state.get('verdict', 'unknown')}) "
                    "— nothing to resume."
                )
                return int(state.get("exit_code", EXIT_INFRA))
        else:
            print("! No resumable state.json found — starting fresh")

    if not os.path.isfile(args.spec):
        print(f"X Spec not found: {args.spec}")
        return EXIT_USAGE
    try:
        spec_text = Path(args.spec).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"X could not read spec {args.spec}: {exc}")
        return EXIT_USAGE

    try:
        preflight_result = _preflight(args, spec_text, out_dir)
    except (TypeError, ValueError) as exc:
        print(f"X invalid preflight configuration: {exc}", file=sys.stderr)
        return EXIT_USAGE
    # Retain the historical private-hook shape for tests/extensions that
    # monkeypatch _preflight; the shared implementation returns PreflightResult.
    if isinstance(preflight_result, tuple):
        spec_text, preflight_ok = preflight_result
    else:
        spec_text = preflight_result.effective_text
        preflight_ok = preflight_result.ok
    if not preflight_ok:
        return EXIT_CONTEXT_BLOCKED

    # R1/R3 have succeeded. Only now may git or command resolution run.
    ok, info = gitops.ensure_git_available()
    if not ok:
        print(f"X {info}")
        return EXIT_INFRA
    if args._provider_config is None:
        dev_cmd = resolve_role_cmd(
            "dev", args.dev_cmd, "ACL_DEV_CMD", DEFAULT_DEV_CMD
        )
        review_cmd = resolve_role_cmd(
            "review", args.review_cmd, "ACL_REVIEW_CMD", DEFAULT_REVIEW_CMD
        )
        arbiter_cmd = (
            args.arbiter_cmd or os.environ.get("ACL_ARBITER_CMD") or ""
        ).strip()
    else:
        # Registry commands are deliberately not resolved here: each phase
        # must consult the shared quota resolver immediately before execution.
        dev_cmd = (args.dev_cmd or "").strip()
        review_cmd = (args.review_cmd or "").strip()
        arbiter_cmd = (args.arbiter_cmd or "").strip()
        if not arbiter_cmd and args._provider_config.roles.get("arbiter"):
            # Only used as an enablement sentinel; run_phase_cmd selects the
            # actual command after quota resolution.
            arbiter_cmd = args._provider_config.roles["arbiter"][0].command

    args._spec_text = spec_text
    args._ledger = _restore_ledger(state)
    state.setdefault("context", args._context)
    state.setdefault("thresholds", args._context.get("thresholds", {}))
    state.setdefault("complexity", args._complexity)
    state.setdefault("execution", _execution_record(args))
    state.setdefault("attempts", [])
    state.setdefault("calls", [])
    state.setdefault("warnings", [])
    state.setdefault("provider_history", [])
    cap_events = state.setdefault("cap_events", [])
    if not any(
        isinstance(event, dict) and event.get("phase") == "preflight"
        for event in cap_events
    ):
        cap_events.extend(args._preflight_cap_events)
    state.setdefault("gates", [])
    state["costs"] = args._ledger.summary()

    provider_mode = "registry" if args._provider_resolver is not None else "legacy"
    print(f"\n{'#' * 60}\n  ADVERSARIAL CODE LOOP v4\n"
          f"  Spec: {args.spec}\n  Feature: {feature}\n"
          f"  Max loops: {args.max_loops}\n"
          f"  Provider mode: {provider_mode}\n{'#' * 60}")

    try:
        code = _pipeline(
            args, dev_cmd, review_cmd, arbiter_cmd,
            workdir, feature, out_dir, state,
        )
    except KeyboardInterrupt:
        runner.terminate_active_processes()
        state["phase"] = "interrupted"
        state["costs"] = args._ledger.summary()
        _write_json(out_dir, "state.json", state)
        print("\nX Interrupted — restoring workdir "
              "(loop branch kept; rerun with --resume to continue)")
        code = EXIT_INFRA
    except NoProviderAvailable as exc:
        print(f"X no provider available for role '{exc.role}'", file=sys.stderr)
        aliases = set(exc.snapshots) | set(exc.reasons)
        for alias in sorted(aliases):
            snapshot = json.dumps(
                exc.snapshots.get(alias, {}), sort_keys=True, default=str
            )
            reason = exc.reasons.get(alias, "ineligible")
            print(
                f"  {alias}: {reason}; snapshot={snapshot}", file=sys.stderr
            )
        state["error"] = str(exc)
        state["provider_snapshots"] = json.loads(
            json.dumps(exc.snapshots, default=str)
        )
        state["costs"] = args._ledger.summary()
        _write_json(out_dir, "state.json", state)
        code = EXIT_REJECTED
    except gitops.GitError as exc:
        print(f"\nX git error: {exc}")
        state["error"] = str(exc)
        state["costs"] = args._ledger.summary()
        _write_json(out_dir, "state.json", state)
        code = EXIT_INFRA
    finally:
        _restore(workdir, state, out_dir)

    if args.show_costs:
        args._ledger.print_summary(file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
