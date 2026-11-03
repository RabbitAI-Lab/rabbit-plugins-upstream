## Description:

Send email via MailChannels Email API and ingest signed delivery-event webhooks into Clawdbot (Moltbot).

This skill is ready for commercial/non-commercial use.

## Publisher:

[ttulttul](https://clawhub.ai/user/ttulttul)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to configure agents to send email through the MailChannels Email API and ingest signed delivery-event webhooks for delivery state updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can send email through the configured MailChannels account.

Mitigation: Install only when that capability is intended, protect MAILCHANNELS_API_KEY, and scope account credentials to the intended sending use.

Risk: Webhook routes could trigger broad or sensitive agent actions if mapped too generally.

Mitigation: Configure narrowly scoped webhook mappings, validate MailChannels signatures, reject stale signatures, and require customer_handle to match MAILCHANNELS_ACCOUNT_ID.

## Reference(s):

- [MailChannels Email API Documentation](https://docs.mailchannels.net/email-api/)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown guidance with inline API paths and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MailChannels account credentials and curl for the documented API interactions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
