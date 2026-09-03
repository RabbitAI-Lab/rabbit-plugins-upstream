## Description:

Tracks commitments, expiry dates, watch items, in-flight diagnoses, and publish queues so an agent can surface due items without reopening the original decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to persist reminders, commitments, review dates, and in-flight work across sessions, then check what is due by urgency. It is designed for tracking and surfacing decisions, not for independently executing the underlying actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent tracking and memory files can retain sensitive business details across sessions.

Mitigation: Use aliases or omit sensitive client names, amounts, and private business details in tracked entries.

Risk: The skill surfaces due commitments and reminders but does not perform the underlying action.

Mitigation: Review surfaced due items and explicitly decide whether to execute, archive, rewrite, or cancel each tracked item.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-track)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance, Configuration]

**Output Format:** [Markdown guidance and tracking records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create persistent dated tracking and memory files on disk when configured by the agent environment.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
