## Description:

Twilio API integration with managed OAuth for agents to send SMS messages, make voice calls, manage phone numbers, and work with Twilio resources through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect and manage Twilio account resources, including SMS/MMS messages, voice calls, phone numbers, applications, queues, addresses, and usage records. It is intended for mediated Twilio API work where read/list calls come first and account-changing operations require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad raw API passthrough can mutate Twilio account resources beyond common SMS and voice tasks.

Mitigation: Default to read/list calls, use the least Twilio scope available, and require explicit confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Long-lived Maton API keys or provider-issued credentials could leak through logs, files, command lines, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, never print or persist secrets, and use the raw HTTP/API-key fallback only when the CLI cannot be used.

Risk: Requests may run against the wrong Twilio connection or Maton profile when multiple accounts are configured.

Mitigation: Pin the intended connection and profile for account-changing operations, and verify account context with read-only calls before writing.

Risk: Sending SMS/MMS messages or voice calls can create cost, privacy, and reputation impacts.

Mitigation: Confirm recipients, sender numbers, message or call content, callback URLs, and expected side effects with the user before sending or initiating communications.

Risk: Twilio content and webhook payloads may contain untrusted instructions or adversarial text.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into commands, and do not let fetched content choose follow-up endpoints or recipients.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Twilio API Overview](https://www.twilio.com/docs/usage/api)
- [Twilio Messages API](https://www.twilio.com/docs/messaging/api/message-resource)
- [Twilio Calls API](https://www.twilio.com/docs/voice/api/call-resource)
- [Twilio Phone Numbers API](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource)
- [Twilio Applications API](https://www.twilio.com/docs/usage/api/applications)
- [Twilio Usage Records API](https://www.twilio.com/docs/usage/api/usage-record)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, Python, JavaScript, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Twilio API paths, form-encoded request payloads, JSON responses, and approval guidance for account-changing operations.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
