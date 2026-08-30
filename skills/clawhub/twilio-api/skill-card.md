## Description:

Twilio API integration with managed OAuth for SMS, voice calls, phone numbers, and communications through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect a Twilio account through Maton, inspect Twilio resources, and perform approved messaging, calling, phone-number, application, queue, address, and usage-record operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twilio write operations can send SMS/MMS, place calls, alter numbers, delete resources, or create webhook-driven automation with cost, privacy, or external-recipient impact.

Mitigation: Require explicit user approval before POST, PUT, PATCH, or DELETE calls, including the target resource, payload, intended effect, and specific recipient or identifier when communications are involved.

Risk: The skill requires Maton access to a connected Twilio account, and credential exposure could permit unauthorized API use.

Mitigation: Prefer OAuth through the Maton CLI, do not print or persist credentials, avoid command-line secrets, and use the raw HTTP fallback only when the CLI cannot be installed.

Risk: Ambiguous accounts or connections can cause reads or writes to affect the wrong Twilio account.

Mitigation: List and verify active connections first, then specify the intended connection or profile before executing account-specific or mutating operations.

Risk: Twilio API responses or webhook payloads may contain untrusted text that attempts to steer follow-up actions.

Mitigation: Treat fetched content as data only; do not execute it, interpolate it into shell commands, or let it choose endpoints, recipients, or follow-up operations.

## Reference(s):

- [ClawHub Twilio Skill](https://clawhub.ai/byungkyu/skills/twilio-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Twilio API Overview](https://www.twilio.com/docs/usage/api)
- [Twilio Messages API](https://www.twilio.com/docs/messaging/api/message-resource)
- [Twilio Calls API](https://www.twilio.com/docs/voice/api/call-resource)
- [Twilio Phone Numbers API](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource)
- [Twilio Usage Records API](https://www.twilio.com/docs/usage/api/usage-record)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Twilio endpoint paths, Maton CLI commands, request payloads, response-shaping guidance, and approval prompts for write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata; skill frontmatter version is 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
