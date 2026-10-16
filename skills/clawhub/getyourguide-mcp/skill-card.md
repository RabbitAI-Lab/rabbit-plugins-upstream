## Description:

Helps agents discover GetYourGuide tours, activities, attraction tickets, options, and reviews through a read-only search connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents use this skill to find and compare GetYourGuide tours, activities, tickets, and reviews; bookings happen on GetYourGuide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP connector requires a GetYourGuide Partner API key.

Mitigation: Keep the key scoped to this use and prefer project-local MCP configuration.

Risk: Running the npm-based MCP server introduces a third-party package into the agent environment.

Mitigation: Review the linked package and source before running it with npx.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [npm package linked in skill documentation](https://www.npmjs.com/package/getyourguide-mcp)
- [Project source linked in skill documentation](https://github.com/chrischall/getyourguide-mcp)
- [GetYourGuide partner program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tour listings, options, and review summaries; booking links lead to GetYourGuide.]

## Skill Version(s):

2.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
