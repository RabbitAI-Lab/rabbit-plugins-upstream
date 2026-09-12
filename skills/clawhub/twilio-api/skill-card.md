## Description:

Twilio API integration with managed OAuth for sending SMS, making voice calls, managing phone numbers, and working with Twilio resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Twilio accounts, messages, calls, phone numbers, applications, queues, addresses, and usage records through Maton. It supports read-first workflows and user-confirmed write operations such as sending messages, placing calls, updating resources, and deleting connections or Twilio objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform real Twilio account actions, including sending messages, placing calls, changing resources, and deleting connections or objects.

Mitigation: Default to read and list operations; require explicit user confirmation of the account, connection, resource identifiers, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Using raw HTTP with MATON_API_KEY exposes a long-lived credential to the process environment.

Mitigation: Prefer Maton OAuth through the CLI; when an API key is unavoidable, never print, log, persist, or pass it on a command line, and send it only to api.maton.ai.

Risk: Multiple Maton profiles or Twilio connections can route requests to the wrong account.

Mitigation: List active connections first and pin the intended connection and profile for writes or account-sensitive reads.

Risk: Twilio responses may contain personal data such as phone numbers, names, message bodies, or usage details.

Mitigation: Filter server-side where possible and return only the fields needed for the user's task instead of dumping or storing raw responses.

Risk: The skill installs Maton CLI or SDK packages without pinned versions in the artifact examples.

Mitigation: Install from Maton's official sources and pin or review package versions before using the CLI or SDK in sensitive environments.

## Reference(s):

- [ClawHub Twilio Skill](https://clawhub.ai/byungkyu/skills/twilio-api)
- [Maton](https://maton.ai)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Twilio API requests and selected response summaries; users should minimize response data shown or stored.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
