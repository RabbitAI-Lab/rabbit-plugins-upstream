## Description:

Enables an OpenClaw agent to notify people through PingRoom, request human decisions, share progress, and receive replies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pingroom](https://clawhub.ai/user/pingroom)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to send phone notifications, request approvals or answers before proceeding, track live progress, and receive pings from a paired human.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages, files, links, and locations sent through PingRoom leave the agent's environment and reach a paired person's phone.

Mitigation: Share only task-necessary content with user consent; ask before sending files, locations, or ambiguous content.

Risk: PingRoom credentials and webhook URLs can authorize off-platform actions.

Mitigation: Keep credentials private and scoped, and treat room or webhook changes as actions requiring user authorization.

## Reference(s):

- [PingRoom OpenClaw command reference](https://pingroom.io/connect-openclaw.md)
- [PingRoom ClawHub release](https://clawhub.ai/pingroom/skills/pingroom)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may send selected content to PingRoom and wait for a human response.]

## Skill Version(s):

1.2.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
