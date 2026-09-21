## Description:

Software implementation planning with optional file-based persistence for planning requests, unresolved architecture or scope decisions, and multi-phase implementation that needs recovery state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use ia-planning to decide when software implementation work needs a durable plan, an inline checklist, or direct implementation. The skill helps produce concrete phases, file ownership, verification steps, handoff posture, and recovery state for context-safe delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the durable plan scaffold can create or update local planning files and .gitignore entries.

Mitigation: Review the working tree before using the scaffold and confirm that .plan/ is appropriate for the repository.

Risk: Using --force can overwrite an existing plan with unchecked tasks.

Mitigation: Inspect .plan/task_plan.md first and use --force only after deciding which plan should remain authoritative.

Risk: Planning or delegated execution guidance can be mistaken for implementation approval.

Mitigation: Treat plans as proposals and continue implementation or delegation only when the user has authorized that work.

Risk: A weak or stale plan can mislead downstream implementation.

Mitigation: Verify that tasks are concrete, phase deliverables are runnable, and acceptance criteria still match the user's requirements before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [Publisher profile](https://clawhub.ai/user/iliaal)
- [Planning workflow](artifact/SKILL.md)
- [Skill specification](artifact/SPEC.md)
- [Plan format](artifact/references/plan-format.md)
- [Execution and decomposition patterns](artifact/references/execution-and-methodology.md)
- [Execution handoff](artifact/references/execution-handoff.md)
- [Goal definition](artifact/references/goal-definition.md)
- [Operational patterns](artifact/references/operational-patterns.md)
- [Plan deepening](artifact/references/plan-deepening.md)
- [Task design](artifact/references/task-design.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown plans and checklists with optional shell commands and local planning files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update .plan/task_plan.md and add .plan/ to .gitignore when the durable planning scaffold is used.]

## Skill Version(s):

4.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
