## Description:

Calendly API integration with managed OAuth for viewing event types, scheduled events, invitees, availability, booking-related data, and webhook management through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and scheduling operators use this skill to inspect Calendly scheduling data, check availability, book or cancel meetings, and manage webhook subscriptions through an authorized Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires authorizing Maton to access a selected Calendly account.

Mitigation: Use OAuth where possible, grant the narrowest Calendly scopes available, and create or renew connections only after explicit user approval.

Risk: Booking, cancellation, webhook, and other write operations can change scheduling state or trigger downstream effects.

Mitigation: Default to read/list calls first and confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Multiple Maton or Calendly connections can route actions to the wrong account.

Mitigation: Specify the Maton profile and Calendly connection when more than one account or connection exists.

Risk: The raw HTTP fallback uses a long-lived Maton API key that can leak through logs, command history, files, or child processes.

Mitigation: Use the CLI when available; otherwise read the key from the environment only inside the request process, never print or persist it, and rotate it if exposed.

Risk: Calendly API responses can contain untrusted external content or personal scheduling data.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and extract only fields needed for the user task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/calendly-api)
- [Maton Homepage](https://maton.ai)
- [Calendly Developer Portal](https://developer.calendly.com/)
- [Calendly API Reference](https://developer.calendly.com/api-docs)
- [Calendly API Use Cases](https://developer.calendly.com/api-use-cases)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal use returns agent guidance and API-call instructions; live Calendly responses may include personal scheduling data and should be minimized to task-relevant fields.]

## Skill Version(s):

1.2.2 (source: server release evidence; skill frontmatter metadata reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
