## Description:

Helps agents search OpenTable restaurants and menus, check availability, and manage reservations and favorites through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to find restaurants and published menus, compare reservation slots, book or change tables, cancel reservations, and manage saved restaurants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration uses a signed-in OpenTable browser tab and the ContextMint Bridge extension.

Mitigation: Review the external components before installing and use a browser profile appropriate for this activity.

Risk: Bookings or changes may involve a card hold, cancellation terms, or fees.

Mitigation: Show the booking or modification preview and obtain the user's confirmation before committing; review cancellation details before canceling.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp source (linked in skill documentation; not verified release provenance)](https://github.com/chrischall/opentable-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with restaurant, menu, availability, and reservation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include booking previews, cancellation terms, and reservation confirmations.]

## Skill Version(s):

1.3.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
