## Description:

This skill helps an agent search and inspect GetYourGuide tours, activities, attraction tickets, options, locations, categories, reviews, and connector health through a read-only MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent discover GetYourGuide tours, attraction tickets, locations, categories, reviews, and available options before directing booking activity to GetYourGuide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger on broad travel-planning requests and route travel search queries through a GetYourGuide-focused connector.

Mitigation: Ask the agent to confirm before using the connector for generic trip planning, or narrow trigger wording to explicit GetYourGuide, tour, ticket, or activity searches.

Risk: Use requires a GetYourGuide Partner API key.

Mitigation: Provide the API key only in the MCP server environment and confirm the installation is appropriate for the travel search data being handled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide partner program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with inline JSON configuration examples and concise tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include tour search results, tour details, option availability, reviews, category or location identifiers, and health-check guidance.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
