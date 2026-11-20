## Description:

Split an agreed design into phases and executable tasks with explicit dependencies and acceptance checks. Use for medium-sized changes or to update an existing task list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-en](https://clawhub.ai/user/peterflow-en)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to turn an agreed design or existing task list into phased, executable work with explicit dependencies, acceptance checks, and progress notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's tool scope is undeclared, and runtime permissions were not verified.

Mitigation: Review the host agent's required tool access and runtime permissions before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/peterflow-en/skills/tasks)
- [Task list template](assets/tasks.md)
- [Dependency checker](scripts/check_dependencies.py)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown task list with phases, tasks, dependencies, acceptance checks, and results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses stable phase and task IDs and records unresolved blockers.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
