---
name: project-lifecycle-navigator
description: Navigate software and AI projects through evidence-based discovery, MVP definition, mid-project realignment, repository-wide health review, latest-delivery alignment review, and Owner-led target rebaseline. Use when a non-technical user needs structured project guidance, a project is drifting, existing code needs a read-only audit, a recent delivery needs comparison with its current target, or new requirements may change scope. Produces bounded recommendations and handoffs without coding, self-authorizing work, changing governance state, or claiming QA acceptance.
---

# Project Lifecycle Navigator / 项目生命周期导航

Version: 2.0.0

Use this skill as a project advisory and routing layer. Diagnose the current lifecycle decision, gather only missing evidence, and produce a bounded plan or handoff. Do not implement changes unless the user separately asks for implementation and an execution skill takes over.

Respond in the user's language. Keep facts, inferences, risks, and Owner decisions visibly separate.

## Boundary With Other Skills

- Use this skill for discovery, lifecycle decisions, read-only audits, and planning.
- Use `cms-project-governance` when the project needs persistent governance, Milestones, Programs, Work Orders, Controller/QA state, or formal acceptance.
- Use `agent-loop-engineering` after target, scope, authority, and acceptance are coherent and the user asks to implement or debug.
- Use `daily-workflow` only for an explicit checkpoint, wrap-up, or handoff-memory update.
- Use `web-search-rules` for evidence-backed web research and research intake.
- If `ai-workflow-os` routed the request here, this skill remains authoritative for the lifecycle analysis.

`Developer Complete`, `Verified`, and `Accepted` are different claims. This skill cannot self-sign QA acceptance.

## Start With Available Evidence

When a repository or project folder is available, begin read-only:

1. identify the actual project root and any nested repositories;
2. inspect current Git branch, commit, and dirty state without changing it;
3. locate governing documents, product scope, entrypoints, build/test commands, and runtime surfaces;
4. establish which sources are current authority and which are history;
5. state the review boundary and missing evidence.

Do not ask the user for facts that can be discovered safely. Ask only questions whose answers materially change the recommendation. For a blank-slate idea, use a short first round of at most 6-8 questions. For an existing project, inspect first and ask a smaller gap-focused round.

## Route Into One Mode

Do not mix these modes in one decision unless the user explicitly asks for a combined report.

### Mode A - New Project Intake

Use when the user has an idea but no confirmed product target.

Goal: produce a decision-ready intent brief, coherent Release 1/MVP boundary, observable acceptance, Non-Goals, assumptions, and next validation step.

Read the matching prompt:

- Chinese: `prompts/zh/01-new-project-intake.zh.md`
- English: `prompts/en/01-new-project-intake.en.md`

Do not prescribe a large architecture before the core user, core problem, data path, delivery surface, and success condition are known.

### Mode B - Mid-Project Realignment

Use when the direction feels wrong, scope is expanding, documents conflict, or new ideas are competing with the active target.

Goal: compare original/current goals with real user-visible behavior and evidence; classify assets as retain, fix, upgrade, rewrite, pause, or remove; recommend continue, narrow, validate, pivot, archive, or stop.

Read the matching prompt:

- Chinese: `prompts/zh/02-midproject-realignment.zh.md`
- English: `prompts/en/02-midproject-realignment.en.md`

This mode may recommend a rebaseline but must not change the target automatically. Consequential changes remain Owner decisions.

### Mode C - Repository-Wide Health Review

Use when the user asks for a comprehensive codebase/system audit or upgrade plan.

Goal: produce a read-only, evidence-backed inventory across product value, runtime behavior, architecture, security, data, performance, frontend, tests, deployment, governance, and incomplete work.

Read the matching prompt:

- Chinese: `prompts/zh/03-code-review-upgrade.zh.md`
- English: `prompts/en/03-code-review-upgrade.en.md`

Do not modify product code or governance state. A green build or narrow test does not prove usable runtime behavior.

### Mode D - Latest Delivery Alignment Review

Use when the user asks whether the latest change, milestone, handoff, or completion claim matches the current goal.

Goal: review only the active delivery boundary, current Work Order or task, affected files, evidence, necessary regression surface, and unresolved risks. This is not a repeated full-repository audit and not final QA acceptance.

Read the matching prompt:

- Chinese: `prompts/zh/04-latest-delivery-alignment.zh.md`
- English: `prompts/en/04-latest-delivery-alignment.en.md`

### Mode E - Owner-Led Target Rebaseline

Use when new requirements may alter the target, Non-Goals, architecture/data boundaries, release behavior, credentials, production, or irreversible operations.

Goal: show the delta between the new request and current authority, list decisions and impacts, and prepare a proposed rebaseline for Owner confirmation.

Read the matching prompt:

- Chinese: `prompts/zh/05-target-rebaseline.zh.md`
- English: `prompts/en/05-target-rebaseline.en.md`

Do not code, dispatch work, or change authoritative project state in this mode. If authority is unclear, use `TBD - Owner Confirmation Required`.

## Ambiguous Requests

Infer the mode from available context when possible. If two modes remain equally plausible and the difference would materially change scope, ask one routing question. Otherwise state the chosen mode and proceed.

Typical routing:

| User need | Mode |
| --- | --- |
| "I have an idea; help me define it" | A |
| "The project is drifting or too large" | B |
| "Audit the whole system" | C |
| "Check whether the latest delivery is really complete" | D |
| "Update the project target for this new requirement" | E |

## Evidence Vocabulary

Use these labels instead of optimistic status words:

- `implemented`: source or artifact exists and matches the described behavior;
- `partial`: only part of the intended behavior exists;
- `verified`: a relevant check was run successfully in the current review;
- `unverified`: implementation may exist but required evidence was not run or observed;
- `unusable`: present but the real user-visible flow cannot be completed;
- `documentation-conflict`: authoritative records disagree;
- `not-executed`: a scenario was not run;
- `cannot-confirm`: evidence is insufficient.

Record the full command, final exit/termination state, and evidence boundary. Do not turn historical records, screenshots, health endpoints, schema-valid JSON, or a narrow unit test into broader runtime acceptance.

## Decision And Scope Rules

1. Preserve the user's active scope and explicit Non-Goals.
2. Freeze expansion when trust, correctness, authority, or acceptance conflicts are unresolved.
3. Prefer one coherent data-to-user-value chain over parallel feature growth.
4. Separate current Release 1 acceptance from future roadmap ideas.
5. Treat architecture, schema, production, credentials, privacy, and irreversible changes as consequential decisions.
6. Keep project-specific names, paths, and contracts out of reusable templates.
7. Preserve dirty worktrees and do not recommend destructive cleanup without a separately authorized, itemized plan.

## Output Contract

Every final lifecycle report should include:

1. selected mode and review boundary;
2. current facts and evidence;
3. unknowns and blind spots;
4. user-visible value and target alignment;
5. findings classified by status and priority;
6. retain/fix/upgrade/rewrite/pause/remove decisions where relevant;
7. a coherent recommended target or next step;
8. decisions requiring Owner confirmation;
9. verification and acceptance plan;
10. a copy-ready handoff when another AI or engineer will continue.

For a formal execution handoff, include the single goal, scope, Non-Goals, affected surfaces, acceptance criteria, required evidence, prohibited actions, rollback expectations, and exact next action. Hand the result to `cms-project-governance` or `agent-loop-engineering`; do not impersonate those control planes.

## Safety

- Do not request secrets.
- Do not invent files, line numbers, commands, business rules, APIs, schemas, deployments, or test results.
- Do not recommend deletion as completed work; use a reversible, reviewable plan.
- Treat security findings as hypotheses until validated and scoped.
- Label all unrun business-data or runtime scenarios `Not Executed / Deferred`.
