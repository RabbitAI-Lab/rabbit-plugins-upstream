## Description:

Twilio API integration with managed OAuth for SMS, voice calls, phone numbers, and Twilio resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate through Maton and perform Twilio account, messaging, voice, phone-number, application, queue, address, and usage-record operations. It is intended for read-first workflows with explicit user confirmation before new connections, writes, deletions, communications, billing-relevant changes, or webhook-related actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated access can act on the connected Twilio account, including live communications, webhooks, billing-relevant resources, and deletions.

Mitigation: Install only when this access model is acceptable, default to read and list calls, and verify the account, connection ID, recipient or resource, and payload before any write or account-changing action.

Risk: Deleting a Maton connection revokes the stored authorization and can break automation that still uses that connection ID.

Mitigation: List connections, match the exact connection ID with the user, and get explicit confirmation before deletion.

Risk: Twilio responses can contain personal data such as names, phone numbers, message bodies, and call details.

Mitigation: Minimize response data by extracting only fields needed for the task and avoid writing raw responses to logs, files, or other destinations unless the user asks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/twilio-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Twilio API Overview](https://www.twilio.com/docs/usage/api)
- [Twilio Messages API](https://www.twilio.com/docs/messaging/api/message-resource)
- [Twilio Calls API](https://www.twilio.com/docs/voice/api/call-resource)
- [Twilio Phone Numbers API](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource)
- [Twilio Applications API](https://www.twilio.com/docs/usage/api/applications)
- [Twilio Usage Records API](https://www.twilio.com/docs/usage/api/usage-record)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue authenticated Twilio API calls through the Maton CLI or Maton HTTP gateway when network access and valid Maton authentication are available.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
