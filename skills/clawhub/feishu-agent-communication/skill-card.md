## Description:

Guides developers in connecting multiple AI agents through Feishu group chats using bots, message routing, and troubleshooting guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to set up Feishu bots for multi-agent collaboration in group chats and troubleshoot message delivery and routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bots may read sensitive messages in groups they can access.

Mitigation: Start in a dedicated non-sensitive group and grant only the required permissions.

Risk: Exposed Feishu credentials, tokens, user IDs, or message logs may disclose sensitive information.

Mitigation: Protect app credentials and tokens, and avoid unnecessary logging of open_id values or message payloads.

Risk: Separate paid deployment materials or scripts may introduce unreviewed behavior.

Mitigation: Review paid deployment documents or scripts separately before running them.

## Reference(s):

- [Feishu bot setup](artifact/references/feishu-bot-setup.md)
- [Gateway configuration](artifact/references/gateway-config.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Feishu Open Platform documentation](https://open.feishu.cn/document/home/index)
- [OpenClaw documentation](https://docs.openclaw.ai/)
- [ClawHub skill listing](https://clawhub.ai/zhouxin121/skills/feishu-agent-communication)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation guidance; no executable scripts bundled with this release.]

## Skill Version(s):

0.1.1 (source: ClawHub release, SKILL.md, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
