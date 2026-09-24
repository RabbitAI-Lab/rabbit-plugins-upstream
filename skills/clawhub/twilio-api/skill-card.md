## Description:

Twilio API integration with managed OAuth for SMS, voice calls, phone numbers, and communications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a Twilio account through Maton, inspect Twilio resources, send approved SMS messages, place approved voice calls, manage phone numbers, and configure approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton brokers access to the user's Twilio account, including sensitive communications data and live account resources.

Mitigation: Install only when that brokerage is intended, use least-privilege Twilio scopes, and confirm the exact connection before use.

Risk: SMS, voice calls, deletion, phone-number changes, functions, and triggers can create cost, reputation, privacy, or operational impact.

Mitigation: Confirm the target resource, payload, recipient or destination, and intended effect before each impactful action.

Risk: Trigger destinations can create persistent forwarding of event data to a host.

Mitigation: Avoid third-party trigger destinations unless the user explicitly trusts the host and understands what data will be forwarded.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Twilio API Overview](https://www.twilio.com/docs/usage/api)
- [Twilio Messages API](https://www.twilio.com/docs/messaging/api/message-resource)
- [Twilio Calls API](https://www.twilio.com/docs/voice/api/call-resource)
- [Twilio Phone Numbers API](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use authenticated Maton CLI or HTTP calls to reach Twilio only after the user approves sensitive actions.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
