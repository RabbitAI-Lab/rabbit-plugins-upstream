## Description:

Provides meta-level decision monitoring that helps an agent decide whether to proceed, degrade, defer, seek help, or flag overconfidence, with added self-verification, reflection, and local learning notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to add a metacognitive checkpoint before or after agent actions, especially when a task requires calibrated confidence, escalation, or conservative fallback behavior. It is most useful as guidance for deciding when an agent should continue, seek help, or add verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to persist behavioral notes and user preferences locally.

Mitigation: Review learned notes periodically and delete learned_patterns.json when it may contain sensitive information.

Risk: The skill describes automatic instruction updates based on accumulated usage.

Mitigation: Route any proposed SKILL.md or threshold changes through explicit human review before applying them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-metacognitive-monitoring)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recommended learner commands and local reflection notes when the skill is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
