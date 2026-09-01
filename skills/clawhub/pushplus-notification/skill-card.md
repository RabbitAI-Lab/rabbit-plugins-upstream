## Description:

Enables agents to send PushPlus notifications through HTTP APIs across WeChat, ClawBot, QQ bot, email, webhook, SMS, App, and related channels, with optional Open API workflows for result lookup and account/channel management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pcstx](https://clawhub.ai/user/pcstx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when they want an agent to send approved notifications, alerts, reminders, delivery checks, or PushPlus account/channel management requests through PushPlus APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notification content, recipient details, and credentials are sent to PushPlus and may be forwarded to downstream channels.

Mitigation: Use the skill only for intended PushPlus delivery, avoid secrets or unnecessary personal data, and warn users before sending sensitive content.

Risk: PushPlus tokens, secret keys, access keys, webhook URLs, or email credentials could be exposed in logs or chat output.

Mitigation: Do not display full credentials, prefer POST body parameters over URL tokens, and read only required PUSHPLUS_* entries from environment files.

Risk: Open API account-management actions can delete messages, remove groups or friends, blacklist users, unbind bots, or change send settings.

Mitigation: Require explicit user confirmation before destructive or account-changing operations and summarize the exact target action first.

Risk: SMS and voice channels can consume PushPlus account points or paid quota.

Mitigation: Tell the user that the selected paid channel may consume points before sending.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pcstx/skills/pushplus-notification)
- [PushPlus message API documentation V1.17](https://www.pushplus.plus/doc/guide/api.html)
- [PushPlus Open API documentation V1.17](https://www.pushplus.plus/doc/guide/openApi.html)
- [Open API reference](artifact/reference.md)
- [PushPlus official site](https://www.pushplus.plus)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline curl commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send HTTP requests to PushPlus and downstream notification channels after user confirmation.]

## Skill Version(s):

1.3.3 (source: evidence.release.version and artifact frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
