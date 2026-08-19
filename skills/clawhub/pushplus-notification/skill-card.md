## Description:

pushplus lets agents send user-approved notifications through the PushPlus HTTP API to WeChat, ClawBot, email, webhook, SMS, apps, and related channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pcstx](https://clawhub.ai/user/pcstx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent send alerts, reminders, status updates, and delivery-result lookups through PushPlus after reviewing the message content and credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Message content is sent through PushPlus and may include sensitive or regulated information if the user provides it.

Mitigation: Review the message summary before sending and avoid sending secrets, credentials, regulated data, or unnecessary personal information.

Risk: Open API actions can delete messages, change settings, or manage friends, topics, and blacklists.

Mitigation: Require explicit confirmation before destructive or account-management actions and verify the target resource identifiers.

Risk: PushPlus tokens, secret keys, and access keys grant message-sending or account-management access.

Mitigation: Use environment variables or user-provided credentials only for the current request, mask credentials in output, and avoid persisting them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pcstx/skills/pushplus-notification)
- [PushPlus message API documentation V1.16](https://www.pushplus.plus/doc/guide/api.html)
- [PushPlus Open API documentation V1.16](https://www.pushplus.plus/doc/guide/openApi.html)
- [Open API reference](reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with inline shell commands and HTTP JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PushPlus request summaries, masked credential references, message short codes, and delivery-status guidance.]

## Skill Version(s):

1.3.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
