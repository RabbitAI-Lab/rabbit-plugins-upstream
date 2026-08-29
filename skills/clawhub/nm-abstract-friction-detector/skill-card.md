## Description:

Detect friction signals; graduate patterns into rules for session retrospectives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to review session friction, identify recurring correction and failure patterns, and propose user-approved guidance updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local friction records may include failure summaries, corrections, commands, file paths, and user feedback.

Mitigation: Avoid highly sensitive sessions unless local records under ~/.claude are acceptable, and periodically review or clear those records.

Risk: Recurring-pattern proposals could introduce incorrect or misleading guidance if promoted without review.

Mitigation: Require user approval before any permanent CLAUDE.md or skill update and review proposed rules against the supporting evidence.

Risk: Accumulated local logs can persist beyond a single session.

Mitigation: Use the documented retention and pruning approach for session logs and review pattern candidates before promotion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-friction-detector)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown reports with JSON session-capture records and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local friction session logs and index files under ~/.claude.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
