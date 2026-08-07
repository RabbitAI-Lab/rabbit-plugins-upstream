## Description:

Sends proactive text, image, file, and video messages through a locally configured WorkBuddy ClawBot WeChat bot channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to send WeChat ClawBot notifications or attachments through the user's local WorkBuddy configuration. It is intended for explicit, recipient-aware outbound messaging rather than general chat automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses local WorkBuddy ClawBot credentials and session tokens to send external WeChat messages and attachments.

Mitigation: Install and run it only when this outbound channel is intended, and confirm the exact recipient, channel, and files before each send.

Risk: The security summary notes broad triggers and no required confirmation before sending.

Mitigation: Require explicit user approval before executing send commands, especially for attachments or sensitive content.

Risk: Selected content is transmitted to Tencent/WeChat services when messages or media are sent.

Mitigation: Avoid confidential attachments unless approved, and keep local credential and cursor files out of shared repositories, chats, and issue reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/weixinclaw-proactive-push)
- [Publisher profile](https://clawhub.ai/user/noaheleven)
- [WeChat ilink bot endpoint](https://ilinkai.weixin.qq.com)
- [WeChat CDN endpoint](https://novac2c.cdn.weixin.qq.com/c2c)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger outbound WeChat text or media sends when the local script is executed with valid WorkBuddy ClawBot credentials.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
