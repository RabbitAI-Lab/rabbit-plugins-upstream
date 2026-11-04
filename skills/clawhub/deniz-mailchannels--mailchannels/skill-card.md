## Description:

Send email via MailChannels Email API and ingest signed delivery-event webhooks into Clawdbot (Moltbot).

This skill is ready for commercial/non-commercial use.

## Publisher:

[deniz-mailchannels](https://clawhub.ai/user/deniz-mailchannels)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use this skill to send email through MailChannels and connect signed delivery events to Clawdbot or Moltbot workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MailChannels receives the messages and recipient information sent through this integration, and the API key grants access to send mail.

Mitigation: Protect MAILCHANNELS_API_KEY and choose an appropriate retention period for message and event data.

Risk: Webhook events can affect agent workflows, including actions triggered through hooks mappings.

Mitigation: Verify the signature and body digest, reject stale events, validate the account handle, and check that the event body is an array before acting.

Risk: A custom API destination or optional external discovery tooling may involve endpoints or code that have not been audited.

Mitigation: Verify custom API destinations; inspect linked repositories directly or pin reviewed tooling before using the optional discovery command.

## Reference(s):

- [MailChannels Email API documentation](https://docs.mailchannels.com/email-api/)
- [MailChannels Codex plugin](https://github.com/mailchannels/mailchannels-codex-plugin)
- [MailChannels Claude Code plugin](https://github.com/mailchannels/mailchannels-claude-code-plugin)
- [ClawHub release page](https://clawhub.ai/deniz-mailchannels/skills/mailchannels)

## Skill Output:

**Output Type(s):** [API calls, JSON, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and API endpoint details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes email compliance headers, webhook verification steps, and delivery-event handling guidance.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
