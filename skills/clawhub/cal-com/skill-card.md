## Description:

Cal.com API integration with managed OAuth for managing event types, bookings, schedules, availability, calendars, conferencing, webhooks, teams, verified resources, and user profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Cal.com through Maton, inspect scheduling resources, create bookings, manage event types and schedules, and configure approved webhooks or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change Cal.com scheduling data through an authorized Maton connection.

Mitigation: Use OAuth where possible, default to read/list operations first, and require explicit user approval before any write or connection change.

Risk: Bookings and webhook payloads can include attendee names, email addresses, schedule details, and booking answers.

Mitigation: Retrieve only task-relevant fields, avoid logging raw responses, and do not send booking or attendee data to third-party URLs unless the user controls the destination and needs that flow.

Risk: Webhooks and trigger destinations can create persistent automatic forwarding of future event data.

Mitigation: Confirm the exact destination URL, controller, triggers, payload, and persistence with the user before creation, and review existing forwarding before adding another destination.

Risk: Raw API-key authentication can expose a long-lived credential if handled through environment variables or command output.

Mitigation: Prefer managed OAuth and the operating system credential store; do not print, export, write, or embed Maton or provider credentials.

Risk: External API responses and event payloads may contain untrusted content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and require a user-reviewed handler before local event execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/cal-com)
- [Maton homepage](https://maton.ai)
- [Cal.com API Documentation](https://cal.com/docs/api-reference/v2/introduction)
- [Cal.com API Reference](https://cal.com/docs/api-reference/v2)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [guidance, shell commands, configuration, code, json]

**Output Format:** [Markdown with inline shell, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed by the user before writes, connection changes, webhook creation, or automation deployment.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
