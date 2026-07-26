---
name: cms-project-governance
description: Turn a vague idea, business problem, project direction, or new requirement into a clear outcome, minimal useful scope, acceptance evidence, sized plan, and controlled AI delivery. Use for non-technical requirement guidance, Small/Medium/Large sizing, Lite/Standard/Full governance, Milestones, Programs, Work Orders, QA acceptance, direction checks, drift recovery, target rebaseline, roadmap review, or reducing project-document overhead. Do not use for ordinary coding loops whose target and acceptance are already authorized; use agent-loop-engineering.
---

# CMS Project Governance

Version: 2.0.0

Use this skill as the human-facing control plane for AI-assisted software delivery. Help the user decide what outcome matters, authorize the smallest useful delivery, keep long-running work aligned, and separate implementation claims from acceptance.

Respond in the user's language. Use plain language before technical language.

## Language Files

- For English work, use this file and load references from `{baseDir}/references/en/`.
- 中文任务请先读取 `{baseDir}/SKILL.zh-CN.md`，并只加载 `{baseDir}/references/zh-CN/` 中需要的参考文件。
- Keep machine-readable frontmatter keys and state enum values in English in both languages so governance and execution remain interoperable.

## Core Principles

1. The user owns purpose, priorities, and consequential decisions.
2. The AI owns requirement analysis, options, recommendations, decomposition, and process guidance.
3. Do not require a non-technical user to design architecture, select a framework, or invent tests.
4. Governance should reduce uncertainty and rework, not maximize documents.
5. A Milestone is a coherent user-observable capability, not a short task or timed stage.
6. `Developer Complete` is not accepted work.
7. Evidence outranks status text.
8. Local compliance does not excuse global goal drift.
9. Use the lightest governance profile that controls the actual risk.
10. Keep Owner authority, Controller authority, Developer authority, and QA authority distinct.

## Relationship To Agent Loop Engineering

- This skill discovers, sizes, authorizes, reviews, and accepts work.
- `agent-loop-engineering` executes an authorized coding target through bounded loops.
- The handoff is one `Docs/ACTIVE_PACKET.md` using contract version `2.0`.
- Either skill may work alone. When both are installed, this skill owns target and acceptance authority; the execution skill owns implementation evidence.

Read `{baseDir}/references/en/execution-contract.md` before creating or reviewing an Active Packet.

## Choose One Mode

Choose exactly one authority mode for the current request. Do not mix modes in one pass.

| User need | Mode | Read |
| --- | --- | --- |
| "I have an idea but do not know how to build it" | Goal Discovery | `references/en/goal-discovery.md` |
| Turn a clear goal into a right-sized delivery | Planning and Sizing | `references/en/planning-and-sizing.md` |
| Create a Milestone, Program, or authorized Work Order | Dispatch | `references/en/governance-profiles.md`, `references/en/controller-qa.md` |
| Review only the latest delivery or handoff | Delivery Review / QA | `references/en/controller-qa.md` |
| Check whether current work still serves the original purpose | Direction Alignment | `references/en/alignment-and-rebaseline.md` |
| Assess a new requirement against the current target | Target Rebaseline | `references/en/alignment-and-rebaseline.md` |
| Audit the whole project or clarify the finish line | Audit / Roadmap | `references/en/alignment-and-rebaseline.md` |

Mode boundaries:

- Goal Discovery may produce an Intent Brief. It must not start implementation.
- Planning and Dispatch may authorize work. They must not implement it.
- Delivery Review / QA judges the latest authorized scope. It is not a whole-project audit.
- Direction Alignment checks drift. It must not silently rewrite the target.
- Target Rebaseline changes target or Non-Goals only with Owner authority.
- Audit / Roadmap is read-only unless the user separately authorizes state updates.

## Universal Workflow

```text
Idea or problem
  -> clarify desired outcome
  -> define simplest useful workflow
  -> expose assumptions and boundaries
  -> define observable success
  -> Ready for Planning
  -> classify Small / Medium / Large
  -> choose Lite / Standard / Full
  -> create Active Packet
  -> authorize execution
  -> direction checks
  -> QA decision
  -> accept, repair, split, rebaseline, or stop
```

Do not demand perfect requirements. Proceed with reversible uncertainty when assumptions are explicit. Stop only when an unknown can change the core target, create material risk, or waste substantial work.

## Readiness And Delivery States

Keep these dimensions separate:

| Dimension | Allowed values |
| --- | --- |
| Goal readiness | `Concept`, `Direction`, `Ready for Planning`, `Ready for Execution`, `Owner Decision Required` |
| Execution | `Ready`, `In Progress`, `Ready for Review`, `Needs Fix`, `Blocked`, `Invalid State` |
| Alignment | `Aligned`, `At Risk`, `Locally Compliant, Globally Misaligned`, `Owner Review Required` |
| QA decision | `Not Reviewed`, `Accepted`, `Accepted With Risk`, `Failed`, `Blocked`, `Not Required` |
| Project | `Active`, `Needs Fix`, `Blocked`, `Accepted`, `Accepted With Risk`, `Invalid State` |

Do not use one field to hide another. For example, a green implementation check may coexist with `alignment_state: Locally Compliant, Globally Misaligned`.

## Required Gates

- Do not authorize execution until outcome, minimum scope, Non-Goals, acceptance evidence, and material constraints are sufficiently clear.
- Do not mark accepted from Developer claims alone when `qa_required: true`.
- When QA fails, keep the same Milestone and Work Order, set `project_state: Needs Fix`, and issue a bounded repair against failed criteria.
- Do not move failed core behavior into `Accepted With Risk`.
- Stop for Owner decision on Core Target, Non-Goals, protected architecture or data boundaries, production access, credentials, deployment, destructive actions, paid external resources, or irreversible choices.
- At stage 10, accept, repair, split, or rebaseline. Do not silently renew another ten stages.

## Minimal Reading

Start with the smallest current packet:

1. `Docs/ACTIVE_PACKET.md` when present.
2. The files explicitly linked from that packet.
3. Latest relevant evidence and QA decision.
4. Historical files only when drift, contradiction, or audit scope requires them.

For legacy projects without an Active Packet, read the current `TARGET.md`, `ACCEPTANCE.md`, active `WORK_ORDER*.md`, latest `STATUS.md`, one immediate next action, blockers, and recent evidence. Do not scan every historical Milestone by default.

If files conflict, report `Invalid State`. Resolve authority in this order:

```text
Owner-approved TARGET / Non-Goals
  -> ACCEPTANCE
  -> active WORK_ORDER
  -> ACTIVE_PACKET current-stage projection
  -> status, next-action, and logs
```

## Document Discipline

Read `{baseDir}/references/en/governance-profiles.md` before creating files.

- Do not create files during early idea exploration unless the user asks for a durable brief.
- Do not create one file per stage, failed test, repair, or conversation.
- Keep one canonical Active Packet and link to evidence instead of copying logs.
- Create a new file only for a new authority boundary, independent QA decision, Owner decision, cross-agent handoff, formal rebaseline, or archive boundary.
- Archive completed history when an active file becomes difficult to scan; do not let status files become permanent journals.

## Output Contract

Every governance response must end with:

```text
Mode:
Current readiness/state:
Decision:
Why:
Do now:
Do later:
Do not do yet:
Owner decision needed:
Next evidence:
Files created or updated:
```

In Goal Discovery, use the Intent Brief format. In QA, include criterion, evidence, decision, correction, owner, and re-verification. Keep the response useful to a non-technical Owner.
