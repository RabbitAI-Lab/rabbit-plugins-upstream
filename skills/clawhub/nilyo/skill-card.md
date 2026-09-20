## Description:

Give an agent access to the user's own LinkedIn, WhatsApp, Instagram, Telegram and Email accounts, supported calendars, and direct realtime event destinations through Nilyo's agent-friendly MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arnaudh458](https://clawhub.ai/user/arnaudh458)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use Nilyo to let agents work with the user's connected messaging, email, calendar, and webhook event destinations through a remote MCP instead of browser automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give agents broad access to sensitive messaging, email, calendar, and webhook data.

Mitigation: Review connected accounts before installing, grant only intended accounts, and revisit account and webhook settings whenever new accounts are added.

Risk: Generic IMAP setup may involve entering mailbox passwords in chat.

Mitigation: Use OAuth or secure connection links where available, and avoid pasting mailbox passwords into chat.

Risk: Webhook destinations can send account events to external receiver URLs.

Mitigation: Create webhook destinations only for HTTPS receiver URLs that the user controls and intends to receive account events.

## Reference(s):

- [Nilyo homepage](https://nilyo.com)
- [Nilyo remote MCP endpoint](https://nilyo.com/mcp)
- [ClawHub skill page](https://clawhub.ai/arnaudh458/skills/nilyo)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions]

**Output Format:** [Markdown guidance with MCP tool calls and webhook configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses exact provider IDs, account IDs, and event IDs returned by Nilyo MCP tools.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
