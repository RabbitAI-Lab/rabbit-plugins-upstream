## Description:

Detect friction signals; graduate patterns into rules. Use for session retrospectives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to review session friction, identify recurring workflow patterns, and propose durable guidance after human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local friction records may retain session-derived details such as commands, file paths, prompts, or project context.

Mitigation: Review or periodically delete ~/.claude/friction and inspect ~/.claude/skills/LEARNINGS.md if those observations should not persist across sessions.

Risk: Recurring friction patterns could lead to incorrect or overly broad guidance if promoted without review.

Mitigation: Review friction reports and require explicit user approval before changing CLAUDE.md or skill instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-friction-detector)
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports with JSON session records and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose updates to persistent guidance, but documented behavior requires explicit user approval before permanent rule changes.]

## Skill Version(s):

1.9.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
