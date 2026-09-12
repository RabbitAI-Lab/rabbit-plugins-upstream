## Description:

Sends PushPlus notifications via HTTP API to WeChat, ClawBot, QQ bot, email, webhook, SMS, App, and other channels, with Open API guidance for send-result lookup, account resources, blacklists, channel bindings, and message rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pcstx](https://clawhub.ai/user/pcstx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent send confirmed PushPlus alerts, reminders, build results, and reports across configured messaging channels. When needed, the same skill guides result lookup and PushPlus Open API management tasks such as topics, friends, blacklists, channel bindings, and message rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected message content and routing metadata are sent to PushPlus and may be forwarded to configured third-party channels.

Mitigation: Confirm the destination and content summary before each send, and avoid secrets, regulated data, or unnecessary personal data in notifications.

Risk: Shell-based curl examples can become unsafe if user-controlled titles or message bodies are interpolated into command strings.

Mitigation: Build request JSON with a serializer or structured HTTP client, or otherwise safely escape values before execution.

Risk: Open API operations can modify or delete messages, topics, friends, blacklists, bindings, channel settings, or message rules.

Mitigation: Require explicit user confirmation before destructive or account-changing actions and summarize the exact resource and operation.

Risk: Installing with an unpinned latest package can change installer behavior over time.

Mitigation: Prefer a pinned ClawHub CLI version or manual installation when reproducibility matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pcstx/skills/pushplus-notification)
- [PushPlus official site](https://www.pushplus.plus)
- [PushPlus message API V1.17](https://www.pushplus.plus/doc/guide/api.html)
- [PushPlus Open API V1.17](https://www.pushplus.plus/doc/guide/openApi.html)
- [Artifact Open API reference](artifact/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for PushPlus API calls; sends and destructive Open API actions require user confirmation.]

## Skill Version(s):

1.3.4 (source: evidence.json release version and artifact frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
