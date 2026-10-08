## Description:

Helps users check restaurant availability and create, change, or cancel reservations at restaurants using easyTable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant guests use this skill to view available booking areas, dates, and times and to create, find, modify, or cancel their reservations through easyTable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unverified browser extension or unintended browser pairing could expose the user's booking session.

Mitigation: Verify the ContextMint Bridge release and checksum, and approve pairing only for the intended browser session.

Risk: Booking changes affect real reservations and may share the guest's name and mobile number with easyTable.

Mitigation: Review each create, modify, or cancel preview and obtain the user's confirmation before proceeding.

Risk: A timed-out booking request may have succeeded, so retrying immediately can create a duplicate reservation.

Mitigation: Look up bookings using the guest's mobile number before retrying an uncertain request.

Risk: Modifying a reservation can clear existing email, comments, or company details that cannot be read back.

Mitigation: Ask the guest for those existing details and preserve them unless the guest explicitly approves clearing them.

## Reference(s):

- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability details and confirmation previews before reservation changes.]

## Skill Version(s):

1.2.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
