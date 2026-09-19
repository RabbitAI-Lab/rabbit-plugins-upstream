## Description:

Provides a read-only MCP connector for searching and discovering GetYourGuide tours, activities, day trips, attraction tickets, tour details, options, reviews, categories, and locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to GetYourGuide's read-only travel-discovery tools for tour, activity, attraction-ticket, review, category, and location lookup. Booking remains outside the skill on getyourguide.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires adding an npm MCP server to agent configuration.

Mitigation: Review the npm package or source before using npx and approve the package in the MCP configuration used by the agent.

Risk: The skill requires a GetYourGuide API key in MCP configuration.

Mitigation: Store GYG_API_KEY carefully, limit access to the MCP config, and rotate the key if it is exposed.

Risk: Broad travel requests may invoke this GetYourGuide connector even when the user did not name it explicitly.

Mitigation: Confirm connector use when broad travel-discovery requests could affect user expectations or data-source choice.

## Reference(s):

- [getyourguide-mcp npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide Partner Program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON MCP configuration examples and tool-response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MCP tool results may be compact or full depending on tool arguments; requires GYG_API_KEY and can use optional currency and language defaults.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
