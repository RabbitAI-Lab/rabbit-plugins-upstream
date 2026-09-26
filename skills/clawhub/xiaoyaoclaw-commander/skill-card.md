## Description:

Helps external agent tools check a local OpenClaw gateway, dispatch tasks to named agents, and send messages through named channels with confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other external agent-tool users can inspect their local OpenClaw gateway, assign work to a specified OpenClaw agent, or send a message through a specified channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A dispatched agent may modify files or send messages using existing OpenClaw permissions.

Mitigation: Confirm the named agent and exact task before dispatch.

Risk: A channel message may reach the wrong recipient or expose sensitive content.

Mitigation: Confirm the channel, recipient, and message content, and remove sensitive information before sending.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-commander)
- [Project documentation](https://github.com/dtsola/xiaoyaoclaw-commander)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires access to a local OpenClaw gateway; task dispatch and message sends require user confirmation.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
