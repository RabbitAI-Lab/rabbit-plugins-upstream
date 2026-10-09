## Description:

Helps agents search GetYourGuide tours, activities, and attraction tickets and retrieve options and reviews through a read-only connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel-planning agents and their users can discover tours, tickets, availability options, and customer reviews on GetYourGuide; bookings remain on GetYourGuide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector requires a GetYourGuide Partner API key.

Mitigation: Keep the key scoped to this service and prefer project-local configuration.

Risk: Installing an external npm package adds a supply-chain dependency.

Mitigation: Review or pin the package if stronger supply-chain controls are required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [getyourguide-mcp npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide Partner Program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only tour listings, details, options, reviews, and links; no booking actions.]

## Skill Version(s):

2.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
