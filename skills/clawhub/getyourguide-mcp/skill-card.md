## Description:

Enables agents to search and retrieve read-only GetYourGuide tours, activities, attraction tickets, options, reviews, categories, and locations through the GetYourGuide Partner API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent discover GetYourGuide tours, activities, day trips, attraction tickets, bookable options, reviews, categories, and locations. Booking remains outside the skill on getyourguide.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an npm MCP server that receives a GetYourGuide Partner API key.

Mitigation: Install it only in environments approved to run the npm package, and provide a scoped GetYourGuide Partner API key through MCP environment configuration.

Risk: The trigger scope covers broad tour, activity, day-trip, and attraction-ticket searches, including requests that do not explicitly mention GetYourGuide.

Mitigation: Review agent routing and user intent before invoking the connector in workflows where travel marketplace selection matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide Partner Program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [text, JSON, configuration, guidance]

**Output Format:** [Markdown with JSON configuration examples and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only travel discovery output; compact tour response views are the default where supported.]

## Skill Version(s):

2.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
