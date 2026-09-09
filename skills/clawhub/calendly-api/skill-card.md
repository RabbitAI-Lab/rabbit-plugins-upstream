## Description:

Calendly lets agents access Calendly scheduling data through Maton-managed OAuth, including event types, scheduled events, invitees, availability, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and scheduling teams use this skill to inspect Calendly users, event types, scheduled events, invitees, availability, organization membership, and webhooks. They can also prepare booking, cancellation, connection, and webhook changes after confirming the affected resource and intended effect with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to a Calendly account through Maton and can access scheduling data in the connected account.

Mitigation: Prefer OAuth, review requested Calendly scopes, connect only the account needed for the task, and specify the intended connection when multiple accounts exist.

Risk: Booking, cancellation, connection, deletion, and webhook operations can change scheduling state or trigger downstream effects.

Mitigation: Default to read and list calls first, then require explicit user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key in the process environment.

Mitigation: Use the raw HTTP form only when the CLI cannot be installed, never print or persist the key, pass it only to api.maton.ai, and rotate it if exposed.

Risk: Calendly API responses can include personal data or adversarial external content.

Mitigation: Extract only task-relevant fields, avoid storing raw responses unless requested, and treat fetched content as data rather than instructions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/calendly-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Developer Portal](https://developer.calendly.com/)
- [Calendly API Reference](https://developer.calendly.com/api-docs)
- [Calendly API Use Cases](https://developer.calendly.com/api-use-cases)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue Calendly API calls through Maton CLI or raw HTTPS when the user has authorized access.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
