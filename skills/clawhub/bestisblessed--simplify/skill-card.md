## Description:

Refactor code for clarity, consistency, and maintainability without changing behavior. Use when the user types /simplify or asks to simplify code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bestisblessed](https://clawhub.ai/user/bestisblessed)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to simplify recently modified or specified code while preserving behavior, public interfaces, outputs, and side effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A behavior-preserving refactor can accidentally change behavior.

Mitigation: Review the resulting diff and run relevant tests before accepting changes.

Risk: The skill may edit code when invoked for readability or simplification work.

Mitigation: Install and invoke it only when code-editing assistance for simplification is intended.

## Reference(s):

- [Simplify Code on ClawHub](https://clawhub.ai/bestisblessed/skills/simplify)
- [Declared homepage and reference](https://x.com/bcherny/status/2027534984534544489?s=20)

## Skill Output:

**Output Type(s):** [guidance, code, markdown, shell commands]

**Output Format:** [Markdown with proposed code edits and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-invoked refactoring guidance intended to preserve behavior.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
