## Description:

Helps agents manage Cal.com scheduling, bookings, event types, availability, and webhooks through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to check Cal.com availability and manage event types, schedules, and bookings. With explicit approval, they can also configure webhooks and scheduling automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to the wrong account or resource could create unintended bookings or modify schedules.

Mitigation: Confirm the account, resource IDs, and exact write with the user before applying it.

Risk: Webhooks may send booking and attendee data to an external destination on an ongoing basis.

Mitigation: Before creating a webhook, confirm its destination URL, events, and data sent with the user.

Risk: Hosted functions and triggers can repeatedly act on connected accounts.

Mitigation: Require approval for the function and trigger, including the connections they can access and their destination.

## Reference(s):

- [Cal.com skill on ClawHub](https://clawhub.ai/byungkyu/skills/cal-com)
- [Maton](https://maton.ai)
- [Cal.com](https://cal.com)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cal.com account changes require explicit user approval.]

## Skill Version(s):

1.2.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
