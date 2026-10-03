## Description:

Helps users check availability and create, change, or cancel restaurant reservations through easyTable booking widgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and their assistants use this skill to find restaurant booking slots and manage easyTable reservations, including looking up existing bookings by phone number.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser extension uses the user's session on easyTable booking pages.

Mitigation: Install only if comfortable using ContextMint Bridge with that browser session.

Risk: Creating, changing, or canceling a booking can affect a real reservation associated with a phone number.

Mitigation: Review the booking preview and obtain the user's approval before confirming changes.

Risk: A timeout can leave the outcome of a booking request uncertain.

Mitigation: Look up bookings by the guest's phone number before retrying.

## Reference(s):

- [easytable on ClawHub](https://clawhub.ai/chrischall/skills/easytable)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text with booking options, reservation details, and confirmation previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking changes require user confirmation.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
