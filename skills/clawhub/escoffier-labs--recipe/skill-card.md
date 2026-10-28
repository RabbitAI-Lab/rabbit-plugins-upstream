## Description:

Use when an approved spec or design needs to become an implementation plan, after mise and before any code. Also use when the user says "write the plan", "plan this out", or the work will be executed later, by someone else, or in a fresh session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[escoffier-labs](https://clawhub.ai/user/escoffier-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agentic workers use this skill to turn an approved design or specification into a precise, executable implementation plan for work done later or in a fresh session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The plan template's commit example stages all changes with `git add -A`, potentially including unrelated files.

Mitigation: Review staged changes before committing and stage only the intended files.

Risk: The skill hands work off to a companion execution skill.

Mitigation: Review the companion execution skill before using the handoff.

## Reference(s):

- [Recipe on ClawHub](https://clawhub.ai/escoffier-labs/skills/recipe)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown implementation plan with code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ordered, task-by-task steps with explicit file paths and expected test outcomes]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
