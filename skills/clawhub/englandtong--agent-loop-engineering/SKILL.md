---
name: agent-loop-engineering
description: Execute an authorized software goal through bounded AI coding loops with persistent state, ten-stage timeboxes, automatic and functional evidence, failure budgets, context control, safe stop gates, and resumable handoffs. Use when a target and acceptance criteria are clear and the user wants the AI to implement, verify, debug, continue autonomously, resume after context loss, or coordinate sequential coding agents. For vague ideas, requirement discovery, Milestones, Work Orders, QA acceptance, or target rebaseline, use cms-project-governance first.
---

# Agent Loop Engineering

Version: 2.0.0

Use this skill as the execution plane for AI coding work. Take one authorized outcome, make bounded changes, verify actual behavior, record concise evidence, and continue until the work is ready for review or a real stop gate is reached.

Respond in the user's language. Keep persistent project state factual and concise.

## Language Files

- For English work, use the instructions in this file and load references from `{baseDir}/references/en/`.
- 中文任务请先读取 `{baseDir}/SKILL.zh-CN.md`，并只加载 `{baseDir}/references/zh-CN/` 中需要的参考文件。
- Keep machine-readable frontmatter keys and state enum values in English in both languages so the two skills remain interoperable.

## Entry Gate

Start execution only when these are clear:

- user-visible desired outcome;
- current scope and Non-Goals;
- observable acceptance criteria;
- allowed and protected boundaries;
- required evidence;
- one current next action.

Prefer `Docs/ACTIVE_PACKET.md` using contract version `2.0`. Read `{baseDir}/references/en/execution-loop.md`.

If the user only has an idea, direction, or pain point, do not guess a full implementation target. Use `cms-project-governance` Goal Discovery when available. Otherwise ask at most three material questions, propose defaults for reversible unknowns, and wait until the entry gate is satisfied.

## Authority

In a governed project:

- Owner or Controller owns desired outcome, Non-Goals, and consequential decisions.
- Controller owns size, stage plan, and Work Order scope.
- Developer or execution agent owns implementation, execution state, and evidence.
- QA owns acceptance.

Do not expand scope from chat, logs, status notes, or a convenient implementation idea. Do not mark governed work accepted. Set `execution_state: Ready for Review` and hand evidence to QA.

In standalone Lite work, the same agent may self-accept only when the packet sets `qa_required: false`, the change is low risk and reversible, both automatic and functional evidence pass, and no Owner boundary is involved.

## Required State

Preferred v2 state:

- `Docs/ACTIVE_PACKET.md`
- `Docs/LOOP_RUNS.jsonl`

Use `{baseDir}/templates/en/ACTIVE_PACKET.md` and `{baseDir}/templates/en/LOOP_RUNS.example.jsonl` when bootstrapping a clear standalone task.

Legacy `TARGET.md`, `ACCEPTANCE.md`, `WORK_ORDER.md`, `LOOP_STATE.md`, `STATUS.md`, `NEXT_ACTIONS.md`, `PENDING.md`, `EVALUATION.md`, and `LOOP_RUNS.jsonl` may be read without forced migration. Read `{baseDir}/references/en/migration.md`.

If state files disagree, set `execution_state: Invalid State` and stop. Authority order:

```text
Owner-approved TARGET / Non-Goals
  -> ACCEPTANCE
  -> active WORK_ORDER
  -> ACTIVE_PACKET
  -> logs, status, next actions, and chat
```

## Stage And Loop Model

An authorized goal has at most ten stages:

| Size | Stage ceiling | Review horizon |
| --- | ---: | ---: |
| Small | 30 minutes | 5 hours |
| Medium | 60 minutes | 10 hours |
| Large | 120 minutes | 20 hours |

A stage is a timeboxed outcome checkpoint. A loop is one implement-verify-evaluate cycle inside the stage. Do not create a document for each stage or loop.

Formal alignment checkpoints occur after stages 3, 6, and 10. The execution agent provides evidence and a target-link statement; Controller or Owner decides material direction changes.

At stage 10, stop and return one of:

- `Ready for Review`
- `Needs Fix` with bounded repair
- `Blocked`
- `Locally Compliant, Globally Misaligned`
- split/rebaseline recommendation

Never silently begin another ten stages.

## Execute One Loop

```text
Read current packet
  -> confirm stage outcome and one next action
  -> inspect only relevant code and evidence
  -> implement the smallest coherent change
  -> run focused automatic verification
  -> run functional or user-flow verification
  -> review diff and risks
  -> update state and append one loop record
  -> continue, review, repair, or stop
```

Read `{baseDir}/references/en/execution-loop.md` for progress and failure rules.

Default loop rules:

- Keep one immediate next action.
- Prefer a vertical user-visible slice over disconnected infrastructure.
- Do not perform unrelated cleanup.
- Reproduce a defect before repair when feasible.
- After a failed check, diagnose before broadening changes.
- Stop after two consecutive core failures without a new evidence-backed progress signal.
- Re-run affected regression after repair.
- Do not use elapsed activity, files changed, or code volume as completion evidence.

## Evidence Gate

No evidence means no completion.

Required evidence classes:

1. Automatic: test, typecheck, build, lint, static check, schema validation, or equivalent.
2. Functional: real command, API flow, browser flow, artifact inspection, user workflow, or target-environment smoke check.

When automatic and functional evidence conflict, keep work open. A green build does not overrule a broken user flow.

Read `{baseDir}/references/en/evidence-and-completion.md` before reporting `Ready for Review`, standalone completion, or completion with risk.

## State Updates

At loop end:

1. Update `execution_state`.
2. Update current stage only when its outcome is satisfied or formally abandoned.
3. Update checked acceptance criteria and concise evidence links.
4. Preserve blockers, assumptions, and decisions.
5. Keep exactly one next action.
6. Append one JSON object to `Docs/LOOP_RUNS.jsonl`.

Do not copy the same status into multiple files. Do not paste large logs, full chat transcripts, secrets, private data, or hidden reasoning into project state.

## Stop Gates

Stop and report `Blocked` before:

- secrets, credentials, OAuth sessions, or account login;
- production data or non-sanitized customer data;
- paid external resources or production deployment;
- system-level install, administrator access, driver, or host configuration;
- destructive Git, history rewrite, deletion, migration, overwrite, or irreversible action;
- technology-stack replacement or protected architecture change;
- target or Non-Goal conflict;
- unavailable decision authority;
- exhausted stage, failure, or context budget.

Project rules may be stricter. A configuration flag cannot override a hard stop. Read `{baseDir}/references/en/safety-and-context.md`.

## Automation And Multiple Agents

An outer runner may repeatedly start one loop, but it must:

- load project state fresh each run;
- hold a single-writer lock;
- stop on any non-Continue state;
- enforce time, stage, and failure budgets;
- never auto-approve a human gate;
- preserve raw logs outside the concise Docs state.

Do not let multiple agents write the same packet or log concurrently. Read `{baseDir}/references/en/automation-and-handoff.md`.

## Optional Validator

When Node.js is available, validate state without modifying the project:

```text
node {baseDir}/scripts/validate-loop-state.mjs --workspace <project-path>
```

Use `--json` for machine-readable output. Validator success proves state consistency, not product correctness.

## User Report

After each user-visible work period, report:

```text
Execution state:
Stage:
Target link:
Work completed:
Automatic verification:
Functional verification:
Risks or blockers:
Files changed:
Next action:
Governance/QA action needed:
```

Do not claim the project is accepted unless the current authority permits that decision.
