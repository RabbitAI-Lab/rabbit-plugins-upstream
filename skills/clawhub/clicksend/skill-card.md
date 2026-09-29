## Description:

Guides agents through authenticated ClickSend messaging, contact management, delivery tracking, and optional automation via Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to send ClickSend SMS, MMS, or voice messages, manage contacts and sender identities, and check delivery through an authorized Maton connection. It also describes optional scheduled or event-driven automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending messages or voice calls can reach unintended recipients and incur costs.

Mitigation: Confirm recipient, message content, and timing with the user before each send.

Risk: Contact, list, and verified sender changes can expose personal data or disrupt messaging.

Mitigation: Review the exact target and proposed change, and obtain explicit approval before modifying records.

Risk: Hosted functions, triggers, and destinations can create persistent automated forwarding.

Mitigation: Review each automation and destination separately, including what data is sent and where, before approval.

## Reference(s):

- [ClickSend skill on ClawHub](https://clawhub.ai/byungkyu/skills/clicksend)
- [Maton](https://maton.ai)
- [ClickSend REST API v3 documentation](https://developers.clicksend.com/docs)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with CLI examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; obtain explicit user approval before writes or new connections.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
