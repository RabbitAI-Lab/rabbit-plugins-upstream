## Description:

Helps users find restaurants and menus, check availability, and manage OpenTable reservations and favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

OpenTable users can search restaurants, view published menus and available tables, make or change bookings, cancel reservations, and manage saved restaurants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration accesses the user's signed-in OpenTable session through a browser extension.

Mitigation: Install only if comfortable granting session access to the MCP server and bridge extension.

Risk: Bookings, changes, or cancellations can affect reservations, and card holds or no-show fees may apply.

Mitigation: Review the action, payment hold, and cancellation policy before approving writes; keep confirmation prompts enabled.

## Reference(s):

- [OpenTable skill release](https://clawhub.ai/chrischall/skills/opentable)
- [ContextMint Bridge setup and releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language responses with restaurant, menu, availability, and reservation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and cancellation confirmations may include reservation identifiers; published menus and availability may change.]

## Skill Version(s):

1.3.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
