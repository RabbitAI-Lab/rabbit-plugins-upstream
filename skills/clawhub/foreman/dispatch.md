# foreman · Chapter 1 · Dispatch

## 0. Preconditions

- **Before any batch dispatch (2+ tasks)**: run `bash <skill-dir>/fleet-check.sh`. Any FAIL gets fixed the way the script says or routed around explicitly — never skipped silently. A single task does not need it.
- Confirm the repo root has a `BRIEFING.md` — the subcontractor briefing: why the stack was chosen, naming conventions, known traps, forbidden zones. If there isn't one, spend five minutes writing it before dispatching anything.
- Confirm `.foreman/` is in `.gitignore`.
- While scanning `.foreman/`, watch for two escalation signals worth reporting to the user unprompted: **forgotten overdue tasks while 3+ batches are in flight**, and **the same kind of task being dispatched twice within a week** (that second one means the work wants a standing rule, not another one-off dispatch).

## 1. Exemption check (objective: two questions and a clock)

1. Can you write a **task-specific assertion command** for this task? A generic `npm test` does not count.
2. If you can't → do a **5-minute spike** to probe the interface, then come back to question 1.
3. Still can't = it is exploratory work → exempt it: the main session does it directly. But **start a clock on disk first**:
   `.foreman/exempt-<slug>.json` ← `{"started_at": "<now>", "deadline_at": "<now+30min>"}`
   The next time foreman runs and sees it overdue → **force the dispatch**. The spike's findings go straight into the work order's "Must comply with" section; those 30 minutes were reconnaissance, not waste.

## 2. Assemble the work order

- Use the template at `<skill-dir>/work-order.md`. All six sections plus the allowed-paths whitelist get filled in.
- Reference `BRIEFING.md` **by path** ("read BRIEFING.md at the repo root before starting"), never inline its full text.
- Every order declares an **allowed-path whitelist**. Across parallel tasks, both the paths and the shared interface surface (schemas, route tables, shared types, lockfiles, migrations) must be mutually exclusive. Anything that overlaps gets serialized instead.
- A task estimated over an hour splits into two rounds: interface skeleton first → main session confirms the direction → then release the full implementation.
- Tag every verification command `persistent` (becomes a long-lived regression test after merge) or `one_shot` (retired after merge). **Commands with side effects** (migrations, seeds, one-time tokens) run only in final CI; the builder's self-check and your intake re-run use a side-effect-free preflight variant.

## 3. Dispatch

```bash
handoff new --backend deepseek --slug <slug> --write <<'__HF_EOF__'
[full work order]
__HF_EOF__
handoff run --backend deepseek ~/.handoff/tasks/<RUN_ID>.prompt.md   # run in background
```

`handoff` is a public CLI (`uv tool install handoff-cli && handoff init`); configure your backends in `~/.handoff/config.yaml`.

- One git worktree per task. For sensitive repos, switch the backend to `hosted` or `local`.
- **Caged dispatch (optional; for sensitive repos or when you want a hard blast radius)** — see the two commands below.
  The caged worker sees only the mounted worktree — the host `$HOME`, your other repos, and your primary agent login are all invisible to it, so `--dangerously-skip-permissions` only ever applies inside the cage.
  Limits: the worktree must live under your home directory (the VM shares only `~`); git is unavailable inside the cage (the worker was never allowed to commit anyway); there is no handoff lifecycle (`tail`/`list`), so results land in the redirected file and you run it in the background.

Build the worker image once. The Dockerfile is inlined here deliberately, so this step depends on nothing but Docker:

```bash
docker build -t foreman-worker - <<'DOCKERFILE'
FROM node:22.19-slim   # pin the tag; add a digest if your policy requires it
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates ripgrep \
    && rm -rf /var/lib/apt/lists/* \
    && npm i -g @anthropic-ai/claude-code@latest \   # pin an exact version for reproducible workers
    && useradd -m worker
USER worker
WORKDIR /work
ENTRYPOINT ["claude"]
DOCKERFILE
```

Then dispatch into the cage:

```bash
bash <skill-dir>/foreman-cworker.sh <absolute-worktree-path> <prompt-file> > result-file &
```

- Task state to disk at `.foreman/<task_id>.json`:
  `{task_id, attempt_id, handoff_run_id, dispatched_at, deadline_at, rework_count, repair_rounds, error_fingerprint, status}`
  `handoff_run_id` is the basename of the `.prompt.md` path that `handoff new` prints (that command pre-allocates the run and echoes the path, not a bare id). Write it at dispatch time and update it with `attempt_id` on every redispatch — the batch → task → delivery audit chain closes through that field.
- Batch state to disk at `.foreman/batch.json`: `{batch_id, members[], integration_sha: null, total_rounds: 0}`

## 4. Intake (three checks; failing any one is a rejection)

1. **Delivery header**: a JSON blob of ≤300 tokens (commands / exit codes / passed count / first failure summary / log path). Locate the delivered artifacts through `handoff_run_id` from the state file — `~/.handoff/tasks/<handoff_run_id>.result.md` and `.out.txt`. **Never guess by recency (`ls -t` and friends)**: on a reworked task with the same slug you will pick up the previous attempt's files. No delivery header = not a delivery; read `result` and `out` to tell a failure apart from a lost result.
2. **Diff boundary**: are the paths actually touched by `git diff` a subset of the allowed paths? Out of bounds → reject, and redispatch that task serialized.
3. **The ruler is untouched**: does the diff touch tests, assertions, or CI config? If it does → reject (global invariant 3).

- After all three checks, the main session re-runs the verification commands itself (side-effect-free variant) as a spot check.
- Results must correspond to the current `attempt_id`. A delivery from a stale attempt is void — discard it.

## 5. Rework and escalation

- Rejected: extract the `error_fingerprint` into the task state file, increment `rework_count`, update `attempt_id`, revise the work order with the failure evidence attached, and redispatch.
- **Stale-ruler conflict** (the builder delivered red, did not touch the ruler, and the failure is a test encoding behavior the spec has since removed): this is not builder error and **does not count as a rework round**. The trusted side (the main session) fixes the ruler in its own commit, with the message noting `Ruler update by trusted side` — every change to the measuring instruments needs its own auditable provenance.
- **Second occurrence of the same fingerprint**, or **batch `total_rounds` ≥ 4** → circuit-break: pull the task back to the main session, or escalate it to a stronger model (for genuinely high-risk work, dispatch to the strongest one you have from the start).

## 6. Exit

- All deliveries accepted → merge into the integration branch, write `integration_sha` into `batch.json` → **automatically read `verify.md` and enter the acceptance chapter**. Do not wait for an instruction.
- In "dispatch only" mode, stop here and remind the user that acceptance has not been done.
