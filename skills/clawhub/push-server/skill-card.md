## Description:

Enables agents to send notifications to user-owned channels and webhooks, retrieve past messages, and manage notification channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[teakong](https://clawhub.ai/user/teakong)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users can have an agent deliver task results or batch updates to their notification channels or business webhooks, review sent messages, and manage channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A channel code grants access to a third-party push service.

Mitigation: Treat it as a credential; keep it out of shared files, logs, and notifications.

Risk: Notifications or webhooks could disclose sensitive content or reach the wrong channel.

Mitigation: Exclude secrets from messages and confirm that each destination belongs to the user before sending.

Risk: Deleting, resetting, or disabling a channel can interrupt notifications or invalidate existing codes.

Mitigation: Confirm the intended channel and change with the user before proceeding; update the configured code after a reset.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/teakong/skills/push-server)
- [Push Server setup](https://push.phprm.com/mcp.html)
- [HTTP API reference](references/api.md)
- [Notification examples](references/example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration guidance]

**Output Format:** [Notifications with a title and optional plain-text, Markdown, or JSON body]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a destination link; delivery results can include message IDs.]

## Skill Version(s):

1.5.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
