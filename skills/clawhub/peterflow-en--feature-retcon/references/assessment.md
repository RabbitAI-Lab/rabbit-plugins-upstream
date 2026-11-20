# Assess impact and authority

Resolve the authoritative topic from (1) the user's explicit path, (2) the project's declared index/configuration, (3) status, supersession and live references, then (4) Git history as supporting evidence. A newer date or larger number alone cannot settle authority. Present unresolved candidates for a decision.

During assessment, read files, directories, scoped Git state and history. A new contract or generated artifact belongs to execution. For each work root record its absolute path, responsibility, repository, branch, baseline, uncommitted state, read/write scope and side effects of native checks. If a Git root encloses a larger tree, restrict status to the work root (`git -C <work-root> status --short --untracked-files=all -- .`). An unreadable Git status is an unknown. When there is no Git or no HEAD, preserve the actual starting files.

Compare pending edits with the change by path and meaning. Preserve unrelated edits. If ownership is clear, work from the authorized current state. Ask about a real overlap whose meaning or ownership is ambiguous and continue unaffected work.

Trace the old and new decision through derivation, implementation, validation and references. Report affected roots and repositories, file creates/edits/deletions, interfaces or state changes, tasks retained/reset/removed/split/merged/added, test and migration commands, external side effects, sensitive files and untestable behavior. Count concrete effects where known. List each proposed deletion, reason, active references and recovery method. Identify mandatory and optional hooks. A mandatory hook outside the authorized boundary remains blocked.

Cover these facts in the existing materials or conversation:

1. Superseded behavior, target, preserved behavior, exclusions and compatibility/migration impact.
2. Authoritative root, reasons, evidence gaps and deepest currently synchronized stage.
3. Artifact relationships, writable and read-only roots, conflicts, deletions and recovery limitations.
4. Candidate stopping points and their quantified effects. Distinguish what this execution may change from what the full round must reconcile.
5. Baseline and post-change checks, expected side effects, evidence still unavailable.
6. Existing decisions and their sources. Identify any extra authorization needed for material deletions, sensitive or large payloads, hooks, external changes or widening the scope.

User confirmation can already be present in the conversation. A brief acceptance adopts the specific assessment it refers to. Keep undisclosed risks, additional roots and new product decisions outside that authorization.
