## Description:

Guides agents through disciplined, resumable execution of a single already-defined task with explicit planning, incremental validation, and final requirements checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to execute one concrete, already-specified task with a stable plan, controlled file changes, and observable validation before completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad requests such as execute this task or implement this ticket before the task is sufficiently concrete.

Mitigation: Confirm the request describes one already-defined task and stop for clarification when the specification is fuzzy.

Risk: Task plans, shell commands, or code changes proposed during execution may be incomplete or incorrect.

Mitigation: Require user approval before file changes, make changes incrementally, and validate each step with an observed command result or artifact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/task-executor)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Structured Markdown with inline commands and code references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires plan approval before file changes and validates each completed step with an observable signal.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
