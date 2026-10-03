## Description:

Enables external agent tools to check a local OpenClaw gateway, dispatch tasks to named agents, and send confirmed channel messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers using an external Agent Skills tool can query their local OpenClaw gateway, ask a specified agent to perform a task, or send a message to a specified channel after confirming its recipient and content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dispatching an agent can perform real work, including file changes or messages.

Mitigation: Confirm the named agent and exact task with the user before dispatch.

Risk: Channel messages can reach real recipients and disclose sensitive content.

Mitigation: Confirm the channel, recipient, and exact message; remove sensitive content before sending.

Risk: The skill uses locally discovered OpenClaw installations and inherited gateway credentials.

Mitigation: Verify the selected executable and intended local gateway before using an environment with gateway access.

## Reference(s):

- [OpenClaw Cross-Tool Commander on ClawHub](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-commander)
- [OpenClaw Cross-Tool Commander documentation](https://github.com/dtsola/xiaoyaoclaw-commander)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text or Markdown, with optional JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gateway health, agent and session status, task results, or message-send confirmation, depending on the requested action.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
