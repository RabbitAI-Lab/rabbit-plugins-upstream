## Description:

Send push notifications via pushplus HTTP API to WeChat, WeChat ClawBot, 新消息ClawBot (cmcc), QQ bot (direct message or QQ group), email, webhook, SMS, App and more; also manage messages, topics, friends, friend/topic-user blacklists, channels, ClawBot, 新消息ClawBot, QQ bot binding/groups, and message forward rules via Open API when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pcstx](https://clawhub.ai/user/pcstx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to send user-approved PushPlus notifications and manage PushPlus messaging resources through documented HTTP APIs. It is suited for alerts, reminders, build status messages, delivery checks, and channel or account management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Message content is sent to PushPlus and may be forwarded to selected downstream channels.

Mitigation: Confirm notification title, content summary, destination channel, and recipient details before sending, and avoid secrets, credentials, regulated data, or private logs.

Risk: Account-management actions can persistently change bot bindings, blacklists, default settings, webhooks, or forwarding rules.

Mitigation: Require explicit user approval before making persistent PushPlus configuration changes.

Risk: Installing with an unpinned CLI version can make future installs less reproducible.

Mitigation: Prefer a pinned ClawHub CLI version when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pcstx/skills/pushplus-notification)
- [PushPlus message API documentation](https://www.pushplus.plus/doc/guide/api.html)
- [PushPlus Open API documentation](https://www.pushplus.plus/doc/guide/openApi.html)
- [PushPlus official site](https://www.pushplus.plus)
- [Open API reference](reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce PushPlus HTTP requests after user confirmation; message delivery is asynchronous and can return a shortCode for result lookup.]

## Skill Version(s):

1.3.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
