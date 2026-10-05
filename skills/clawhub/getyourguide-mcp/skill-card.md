## Description:

Helps agents find GetYourGuide tours, activities, and attraction tickets and retrieve their details and reviews through a read-only connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning agents can search tours and attraction tickets, compare options, and review details before booking on GetYourGuide. Use requires a GetYourGuide Partner API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the connector requires an API key and installs an external npm-hosted MCP server.

Mitigation: Install it only when GetYourGuide discovery is needed, and configure the partner key in the MCP environment.

Risk: Broad travel-planning requests may trigger GetYourGuide searches unintentionally.

Mitigation: Consider a project-local MCP configuration and restrict invocation to explicit GetYourGuide searches.

## Reference(s):

- [GetYourGuide MCP on ClawHub](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [GetYourGuide MCP npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide Partner Program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tour links, options, and reviews; booking takes place on GetYourGuide.]

## Skill Version(s):

2.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
