## Description:

Helps users find restaurants and manage OpenTable reservations and favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

OpenTable users can search for restaurants and availability, book or change tables, review or cancel reservations, and manage favorite restaurants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party server and browser extension can access the signed-in OpenTable session and reservation or profile data.

Mitigation: Review and trust both components before installation, and use a browser profile appropriate for this access.

Risk: Bookings or cancellations may involve a saved card, cancellation fees, or an unintended reservation change.

Mitigation: Review the booking or cancellation preview, including any card hold and fee policy, and confirm the intended action before proceeding.

## Reference(s):

- [OpenTable skill listing](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp package](https://www.npmjs.com/package/opentable-mcp)
- [ContextMint Bridge setup and releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries and reservation confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include booking details, cancellation terms, and confirmation identifiers.]

## Skill Version(s):

1.2.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
