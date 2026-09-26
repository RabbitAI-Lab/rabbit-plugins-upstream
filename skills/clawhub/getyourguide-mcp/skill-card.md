## Description:

Helps agents search GetYourGuide tours, activities, attraction tickets, options, and reviews through a read-only connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to discover and compare GetYourGuide tours, activities, tickets, and reviews. Booking remains on GetYourGuide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the connector requires a GetYourGuide Partner API key.

Mitigation: Provide the key through the MCP configuration and protect it as a credential.

Risk: Installing the npm package may not meet environments that require package provenance or supply-chain pinning.

Mitigation: Review the package and source separately and pin the dependency where required.

## Reference(s):

- [GetYourGuide skill release on ClawHub](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [getyourguide-mcp npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide partner program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with tour details and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only discovery; booking happens on GetYourGuide.]

## Skill Version(s):

2.1.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
