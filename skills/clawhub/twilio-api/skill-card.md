## Description:

Twilio API integration with managed OAuth for sending SMS messages, making voice calls, managing phone numbers, and working with Twilio resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to make user-approved Twilio API calls through Maton, including SMS, voice calls, account lookup, phone number management, and related hosted automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing Maton CLI or SDK packages introduces ordinary supply-chain risk when separate checksum or signature verification is unavailable.

Mitigation: Confirm the Maton distribution path is trusted, keep versions pinned to the reviewed release, and review release notes before upgrading.

Risk: Long-lived API keys can be exposed through environment variables, logs, committed files, or copied shell history.

Mitigation: Prefer OAuth and OS credential storage; if an API key is exposed, rotate it and remove copies from logs, files, and environment state.

Risk: SMS, calls, deletes, hosted functions, triggers, and trigger destinations can affect users, accounts, or persistent automations.

Mitigation: Approve the exact target, payload, destination host, network policy, and persistence period before execution, and remove connections or automations when no longer needed.

Risk: Twilio responses can contain personal data such as names, email addresses, phone numbers, message bodies, or call records.

Mitigation: Return only fields needed for the task and avoid writing raw responses to logs or files unless the user explicitly requests it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/twilio-api)
- [Twilio API Overview](https://www.twilio.com/docs/usage/api)
- [Messages API](https://www.twilio.com/docs/messaging/api/message-resource)
- [Calls API](https://www.twilio.com/docs/voice/api/call-resource)
- [Phone Numbers API](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource)
- [Applications API](https://www.twilio.com/docs/usage/api/applications)
- [Usage Records API](https://www.twilio.com/docs/usage/api/usage-record)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Twilio authorization.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
