## Description:

notify-hub lets agents send text, structured cards, and files to Feishu, WeCom, DingTalk, Slack, Telegram, and email, with dry-run previews and channel-specific rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and operations teams use this skill when an agent workflow needs to deliver reports, alerts, reminders, or files to configured chat and email destinations. It is especially suited to broadcasting the same generated content across multiple channels while preserving a single message definition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webhook URLs, bot tokens, and SMTP passwords grant sending access if exposed.

Mitigation: Keep credentials in the private notification config, avoid committing or sharing that file, and restrict file permissions where possible.

Risk: Broadcast targets and file attachments can send content to unintended recipients.

Mitigation: Use dry-run previews and explicit target lists before sending sensitive reports, alerts, or attachments.

Risk: Outbound messages may expose confidential or inappropriate content to chat groups or email recipients.

Mitigation: Review generated content before dispatch and match each message to the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiyanjun/skills/notify-hub)
- [Channel credential and rendering schema](references/channels-schema.md)
- [Feishu custom bot documentation](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [CLI commands, JSON card payloads, rendered channel messages, and dry-run previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Messages are rendered per destination channel, with card sections degraded where a channel lacks native table or button support.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
