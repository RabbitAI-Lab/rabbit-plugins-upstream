## Description:

Helps users check availability and create, change, or cancel reservations at restaurants using easyTable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant customers use this skill to find available tables and manage their easyTable reservations through their own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A browser extension paired to the wrong tab could access an unintended session.

Mitigation: Verify the ContextMint Bridge release or source and approve pairing only for the intended easyTable tab.

Risk: Creating, changing, or cancelling a reservation may expose guest details or alter a real booking.

Mitigation: Check the booking preview and guest details, including name and mobile number, before approving each change.

Risk: Changing a booking can erase existing email, comments, or company details that cannot be read back.

Mitigation: Ask the guest for the existing details and preserve them unless the guest explicitly wants to clear them.

Risk: Retrying after an uncertain booking response could create a duplicate reservation.

Mitigation: Look up reservations using the guest's mobile number before retrying.

## Reference(s):

- [easytable skill listing](https://clawhub.ai/chrischall/skills/easytable)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability results, booking details, and confirmation previews.]

## Skill Version(s):

1.2.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
