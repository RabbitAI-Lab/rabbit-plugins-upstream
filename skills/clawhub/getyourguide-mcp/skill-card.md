## Description:

This skill helps agents search and inspect GetYourGuide tours, activities, attraction tickets, options, reviews, categories, and locations through a read-only MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs read-only discovery of GetYourGuide tours, activities, attraction tickets, bookable options, reviews, categories, or locations. It supports travel planning and activity research while directing actual booking to getyourguide.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses an unpinned npm package name through npx.

Mitigation: Review the package and source before installing, and pin a specific audited version for deployment.

Risk: The MCP server requires a GetYourGuide API key.

Mitigation: Keep GYG_API_KEY out of version-controlled configuration and provide it only through an appropriate secret-management path.

Risk: The security verdict is suspicious because the connector should be reviewed before installation.

Mitigation: Run the server with only the environment and filesystem access it needs, and review the release before enabling it for agents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide Partner Program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only tour, activity, option, review, category, and location data; compact responses are the default where supported.]

## Skill Version(s):

1.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
