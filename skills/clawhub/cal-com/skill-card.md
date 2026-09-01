## Description:

Cal.com API integration with managed OAuth for managing event types, bookings, schedules, availability, calendars, conferencing, webhooks, teams, verified resources, and user profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to access Cal.com through Maton OAuth for scheduling workflows such as checking availability, creating bookings, configuring event types, and managing webhooks. It is intended for tasks where the user has authorized the relevant Cal.com account and confirms any write operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Cal.com scheduling data, including attendee names, emails, booking details, schedules, and user profile information.

Mitigation: Default to read and list calls, request only task-relevant data, and avoid exposing booking or attendee details unless the user explicitly needs them.

Risk: Write operations can create or change bookings, schedules, event types, webhooks, and related scheduling resources.

Mitigation: Require explicit user approval before POST, PUT, PATCH, or DELETE calls, including the target resource, payload, and intended effect.

Risk: Webhooks can send booking and event data to external subscriber URLs.

Mitigation: Confirm the subscriber URL, triggers, and user intent before creating or updating any webhook.

## Reference(s):

- [Cal.com ClawHub Listing](https://clawhub.ai/byungkyu/skills/cal-com)
- [Maton](https://maton.ai)
- [Cal.com API Documentation](https://cal.com/docs/api-reference/v2/introduction)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user approval for write operations.]

## Skill Version(s):

1.1.0 (source: release evidence; SKILL.md metadata version is 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
