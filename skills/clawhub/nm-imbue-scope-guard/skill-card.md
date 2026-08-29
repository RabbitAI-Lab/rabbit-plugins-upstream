## Description:

Scores feature worthiness and enforces branch-size limits against overengineering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to decide whether proposed features belong in the current branch, should be deferred to backlog, or require explicit justification before proceeding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent GitHub records that include detailed reasoning or project context.

Mitigation: Require explicit approval before creating issues, labels, comments, or Discussions, and review or redact content before publication.

Risk: Default Discussion publication may expose sensitive planning context in repositories where Discussions are visible to a broader audience.

Mitigation: Disable default Discussion publication for sensitive work or require an opt-in confirmation before posting.

Risk: Blocking hooks or branch thresholds can interrupt normal delivery work if applied without project-specific judgment.

Mitigation: Treat thresholds as governance prompts and document human-approved overrides when branch size is justified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-scope-guard)
- [Publisher profile](https://clawhub.ai/user/athola)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with decision tables, checklists, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce GitHub issue, label, comment, and Discussion content when documenting deferred work]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
