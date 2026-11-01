## Description:

Software implementation planning with optional file-based persistence. Use when asked to plan, when unresolved architecture or scope decisions need a durable record, or when multi-phase implementation needs recovery state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn software implementation requests into appropriately sized plans, from a short inline checklist to a durable multi-phase plan with decisions, verification steps, and recovery state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A plan can carry mistaken requirements or assumptions into implementation.

Mitigation: Check the plan against the user's requirements and verified facts, and review it before implementation.

Risk: The scaffolding script writes .plan/task_plan.md and updates .gitignore; forcing replacement can discard unfinished planning work.

Mitigation: Run it from the intended project directory, inspect the existing plan, and preserve unfinished work before using --force.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [SKILL.md](artifact/SKILL.md)
- [ia-planning specification](artifact/SPEC.md)
- [Goal definition](artifact/references/goal-definition.md)
- [Plan format](artifact/references/plan-format.md)
- [Task design](artifact/references/task-design.md)
- [Execution and methodology](artifact/references/execution-and-methodology.md)
- [Operational patterns](artifact/references/operational-patterns.md)
- [Plan deepening](artifact/references/plan-deepening.md)
- [Execution handoff](artifact/references/execution-handoff.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Shell commands]

**Output Format:** [Markdown plans or inline checklists, with shell commands where useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A durable plan may create .plan/task_plan.md and add .plan/ to .gitignore; a clear one-session task may use an inline checklist instead.]

## Skill Version(s):

5.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
