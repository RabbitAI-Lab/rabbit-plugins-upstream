## Description:

Helps an agent investigate behavior-correction feedback, improve its guidance to prevent recurrence, and resume the interrupted task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users invoke this skill after behavior-correction feedback to investigate a mistake, improve the relevant guidance, and complete the interrupted work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect broad agent history containing sensitive information.

Mitigation: Review the records it needs to access and limit exposure of unrelated or sensitive material.

Risk: It may make lasting changes to rules, memory, skills, hooks, or agent settings.

Mitigation: Prefer explicit /fix or fix: invocation and --local changes; review each confirmation and proposed persistent change before allowing global updates, hook changes, or plugin installs.

## Reference(s):

- [Fix on ClawHub](https://clawhub.ai/drumrobot/skills/fix)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with change summaries, proposed or applied edits, and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May revise agent guidance and resume the original task.]

## Skill Version(s):

0.7.1 (source: ClawHub release and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
