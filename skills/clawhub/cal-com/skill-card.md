## Description:

Cal.com API integration with managed OAuth for managing event types, bookings, schedules, availability, calendars, conferencing, webhooks, teams, verified resources, and user profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cal.com scheduling workflows through Maton, including bookings, event types, availability, calendars, schedules, webhooks, teams, verified resources, and user profile tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration can access scheduling resources through a connected Cal.com account.

Mitigation: Prefer OAuth, grant the narrowest scopes available, and connect only the account needed for the current task.

Risk: Writes, deletions, connection changes, and scheduling actions can modify user data or notify participants.

Mitigation: Confirm the target resource, payload, and intended effect with the user before allowing any write, deletion, or connection change.

Risk: Webhook subscriptions can send booking and event data to external URLs.

Mitigation: Confirm the subscriber URL, controller of the destination, and trigger list before creating or updating a webhook.

Risk: Bookings can expose attendee identities, email addresses, and schedule details.

Mitigation: Retrieve booking data only when requested and avoid logging or persisting raw responses unless the user explicitly asks.

## Reference(s):

- [ClawHub Cal.com Skill Page](https://clawhub.ai/byungkyu/skills/cal-com)
- [Maton Homepage](https://maton.ai)
- [Cal.com API Documentation](https://cal.com/docs/api-reference/v2/introduction)
- [Cal.com API Reference](https://cal.com/docs/api-reference/v2)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Cal.com API requests through Maton after user approval.]

## Skill Version(s):

1.2.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
