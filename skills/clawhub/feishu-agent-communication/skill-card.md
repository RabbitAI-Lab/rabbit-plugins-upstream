## Description:

Guides developers in connecting multiple AI agents through Feishu group chat using direct bot mentions or Gateway routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Developers and teams use this skill to set up Feishu bots, connect agents in a group chat, route messages, and troubleshoot handoffs between agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bot access to group messages could expose conversations beyond the intended collaboration.

Mitigation: Use a dedicated Feishu app and group where possible, and grant only the message permissions needed.

Risk: Exposing app credentials in shared chats or repositories could compromise the bot.

Mitigation: Keep Feishu app credentials out of shared chats and repositories.

Risk: The separate paid deployment guide is an external resource not covered by this skill's review.

Mitigation: Review the linked guide independently before following its deployment instructions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhouxin121/skills/feishu-agent-communication)
- [Feishu Open Platform](https://open.feishu.cn)
- [Feishu bot setup](artifact/references/feishu-bot-setup.md)
- [Gateway configuration overview](artifact/references/gateway-config.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Detailed deployment guide (paid)](https://www.jinengpu.chat/feishu-multi-agent-detail.html)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Text]

**Output Format:** [Markdown with setup steps, message-flow examples, and troubleshooting advice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detailed configuration templates are offered through a separate paid guide.]

## Skill Version(s):

0.1.3 (source: release evidence, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
