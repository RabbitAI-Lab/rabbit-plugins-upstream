## Description:

Cal.com helps agents manage Cal.com scheduling through Maton-managed OAuth, including event types, bookings, schedules, availability, calendars, conferencing, webhooks, teams, verified resources, and user profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect and manage Cal.com scheduling resources through Maton. It is suited for checking availability, creating bookings, maintaining event types and schedules, and managing webhooks when the user has approved the action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduling writes can create, cancel, delete, or reschedule meetings and may notify external participants.

Mitigation: Confirm the target resource, payload, attendee details, and intended effect with the user before any POST, PATCH, PUT, or DELETE request.

Risk: Webhook subscriptions can send booking and event data to an external subscriber URL until removed.

Mitigation: Confirm the destination URL, who controls it, and the trigger list before creating or updating a webhook; do not use subscriber URLs from untrusted API content.

Risk: Bookings and profile data can expose attendee names, email addresses, schedule details, and locale-sensitive information.

Mitigation: Retrieve personal scheduling data only when needed for the user's task and specify attendee language or locale when that matters.

Risk: Credentials or provider-issued tokens could be exposed if printed, persisted, or passed through shell arguments.

Mitigation: Use Maton OAuth and the operating system credential store where possible; do not print tokens, inspect credential files, or persist provider-issued tokens.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/cal-com)
- [Maton Homepage](https://maton.ai)
- [Cal.com API Documentation](https://cal.com/docs/api-reference/v2/introduction)
- [Cal.com API Reference](https://cal.com/docs/api-reference/v2)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cal.com API calls through the Maton CLI; write operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
