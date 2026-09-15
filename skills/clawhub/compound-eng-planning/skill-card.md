## Description:

Software implementation planning with optional file-based persistence for unresolved architecture, scope, dependency, or session-continuity decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to decide when software implementation work needs a durable plan, define verifiable outcomes, decompose work into runnable phases, and preserve recovery state across longer tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The init-plan.sh helper writes .gitignore and .plan/task_plan.md, which can overwrite unintended files in repositories containing attacker-controlled symbolic links.

Mitigation: Before running the helper, confirm .gitignore, .plan, and .plan/task_plan.md are ordinary files or directories; in untrusted repositories, create the plan manually or use a hardened helper.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-planning)
- [Specification](SPEC.md)
- [Execution & Decomposition Patterns](references/execution-and-methodology.md)
- [Execution Handoff](references/execution-handoff.md)
- [Goal Definition](references/goal-definition.md)
- [Operational Patterns](references/operational-patterns.md)
- [Plan Deepening](references/plan-deepening.md)
- [Plan Format](references/plan-format.md)
- [Task Design](references/task-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Files]

**Output Format:** [Markdown plans with optional inline shell commands and file path references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally scaffold .plan/task_plan.md and update .gitignore through init-plan.sh.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
