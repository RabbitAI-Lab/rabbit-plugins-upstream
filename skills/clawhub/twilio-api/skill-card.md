## Description:

Twilio API integration with managed OAuth for sending SMS messages, making voice calls, managing phone numbers, and working with Twilio resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to perform Twilio account, messaging, voice, number, application, and usage-record tasks through a managed Maton connection. It supports read/list workflows by default and user-approved writes or automations for communications tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send messages, make calls, and perform other sensitive Twilio writes with cost, privacy, or reputation impact.

Mitigation: Default to read/list operations and require explicit user approval with the exact target, payload, and intended effect before any write.

Risk: Long-lived API keys and embedded credentials can expose Maton or provider access.

Mitigation: Prefer OAuth-backed Maton login, avoid printing or storing credentials, and never place Maton or provider tokens in trigger destinations.

Risk: Triggers and event watches can create persistent automation or forward data outside the platform.

Mitigation: Create triggers, destinations, and --exec watches only for user-named hosts or user-reviewed handlers, keep destinations on Maton-controlled URLs when possible, and remove automations when no longer needed.

Risk: Third-party API content and event payloads may contain untrusted or adversarial data.

Mitigation: Treat fetched content and event payloads as data, validate fields before use, and do not execute or interpolate them into commands or prompts.

## Reference(s):

- [ClawHub Twilio Skill](https://clawhub.ai/byungkyu/skills/twilio-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Twilio API Overview](https://www.twilio.com/docs/usage/api)
- [Twilio Messages API](https://www.twilio.com/docs/messaging/api/message-resource)
- [Twilio Calls API](https://www.twilio.com/docs/voice/api/call-resource)
- [Twilio Phone Numbers API](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code examples, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, Twilio API paths and payloads, hosted function examples, trigger configuration, and operational approval guidance.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
