## Description:

Agent 团队 Telegram 通信规范。所有 Agent 向用户发送消息时必须遵循此规范，确保消息正确发送到 Telegram。

This skill is ready for commercial/non-commercial use.

## Publisher:

[shangchuanqiytu-ui](https://clawhub.ai/user/shangchuanqiytu-ui)

### License/Terms of Use:


## Use Case:

Agent operators and workspace administrators use this skill to standardize Telegram status updates from a defined team of agents, including account IDs, fixed recipient routing, message templates, and common delivery mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic agent updates to a fixed Telegram account could expose project information, file paths, or sensitive work context outside the intended private setup.

Mitigation: Install only when the workspace owner controls or explicitly trusts Telegram ID 5440561025, and change the recipient to a user-controlled configuration before broader use.

Risk: Routine progress messages may include confidential code, customer data, credentials, or sensitive paths.

Mitigation: Minimize message contents and require confirmation before sending updates from sensitive workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shangchuanqiytu-ui/skills/agent-telegram)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with JavaScript message examples and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fixed Telegram recipient and agent account mappings.]

## Skill Version(s):

1.0.0 (source: evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
