## Description:

Helps users check restaurant availability and create, change, or cancel easyTable reservations through their browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant guests use this skill to find available tables and manage reservations at restaurants using easyTable, with confirmation before booking changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge extension acts on the user's open booking tab.

Mitigation: Install only if comfortable with that access, and verify the extension package or its published checksum before installation.

Risk: A mistaken booking change or cancellation can affect a real reservation.

Mitigation: Review the reservation preview and approve the specific action before it is sent.

Risk: A timed-out booking request may already have succeeded.

Mitigation: Look up reservations using the guest mobile number before retrying.

## Reference(s):

- [easytable skill listing](https://clawhub.ai/chrischall/skills/easytable)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability and reservation details, with previews for booking changes.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
