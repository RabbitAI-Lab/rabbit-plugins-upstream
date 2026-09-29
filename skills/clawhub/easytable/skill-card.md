## Description:

Helps users check availability and create, change, or cancel reservations at restaurants using easyTable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People booking restaurants through easyTable can check available areas, dates, and times, look up bookings by mobile number, and request confirmed reservation changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or pairing an unverified browser extension could expose the user's booking session.

Mitigation: Verify the ContextMint Bridge extension source or release checksum, and pair it only when intending to manage an easyTable booking.

Risk: Creating, changing, or canceling a reservation affects a real booking.

Mitigation: Review the reservation details and obtain the user's explicit approval before confirming each change.

Risk: An uncertain booking response could lead to a duplicate reservation if retried.

Mitigation: Look up the booking by the guest's mobile number before retrying an uncertain create or modify request.

## Reference(s):

- [easytable skill on ClawHub](https://clawhub.ai/chrischall/skills/easytable)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability and reservation details, with approval previews for booking changes.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
