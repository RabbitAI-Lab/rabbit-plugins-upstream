## Description:

Software implementation planning with optional file-based persistence for unresolved architecture, scope, or multi-phase recovery needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this workflow to decide when implementation planning is warranted, structure vertical phases, preserve recovery state, and continue authorized implementation with clear verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Existing local planning state can be replaced when forcing a new plan.

Mitigation: Review .plan/task_plan.md before using --force, and update the existing plan in place when the same work is continuing.

Risk: A plan based on vague goals can preserve misleading scope, decisions, or acceptance criteria.

Mitigation: Use the Goal Quality Gate to define the outcome, evidence, success threshold, scope boundaries, and stop conditions before creating the plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [ia-planning specification](SPEC.md)
- [Execution & Decomposition Patterns](references/execution-and-methodology.md)
- [Operational Patterns](references/operational-patterns.md)
- [Plan Deepening](references/plan-deepening.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown planning artifacts, inline shell commands, checklists, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local .plan/task_plan.md and .gitignore when a full plan is scaffolded.]

## Skill Version(s):

4.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
