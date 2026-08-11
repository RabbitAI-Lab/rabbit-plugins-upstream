## Description:

Sends push notifications through the PushPlus HTTP API to WeChat, ClawBot, email, webhook, SMS, App, and related channels, with optional Open API guidance for result lookup and account management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pcstx](https://clawhub.ai/user/pcstx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they want an agent to send alerts, reminders, workflow status updates, or delivery-result queries through PushPlus-supported messaging channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Notification content is transmitted through PushPlus and selected downstream channels.

Mitigation: Confirm the title and content summary before sending, and avoid secrets, raw logs, credentials, or personal data unless the user deliberately accepts that disclosure.

Risk: PushPlus token, secretKey, and accessKey values can authorize sends or account-management actions.

Mitigation: Use environment variables or direct user input, mask credential values in output, read only PUSHPLUS-related .env entries, and do not persist credentials.

Risk: Open API operations can delete messages, remove groups or friends, unbind ClawBot, or change sending settings.

Mitigation: Require explicit user confirmation before destructive or account-changing Open API calls.

Risk: SMS and voice notification channels can consume paid PushPlus points.

Mitigation: Warn the user about paid channel costs and obtain confirmation before sending through SMS or voice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pcstx/skills/pushplus-notification)
- [PushPlus message API V1.16](https://www.pushplus.plus/doc/guide/api.html)
- [PushPlus Open API V1.15](https://www.pushplus.plus/doc/guide/openApi.html)
- [PushPlus official site](https://www.pushplus.plus)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline curl commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces request guidance and notification-send commands for an agent; PushPlus may return asynchronous shortCode values for later result lookup.]

## Skill Version(s):

1.3.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
