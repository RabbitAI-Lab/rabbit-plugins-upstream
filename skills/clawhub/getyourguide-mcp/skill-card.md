## Description:

This skill helps agents search and discover GetYourGuide tours, activities, day trips, attraction tickets, tour details, options, reviews, categories, and locations through a read-only MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect an agent to GetYourGuide search and discovery workflows for tours, activities, attraction tickets, availability options, and customer reviews. It is read-only; booking remains on GetYourGuide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external npm MCP server and requires a GetYourGuide partner API key.

Mitigation: Install only when that dependency is acceptable, provide the API key deliberately, and prefer project-level MCP configuration when narrower scope is needed.

Risk: Currency and language defaults can affect returned tour and ticket results.

Mitigation: Set GYG_CURRENCY and GYG_LANGUAGE intentionally for the intended audience or request context.

## Reference(s):

- [getyourguide-mcp on npm](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide Partner Program](https://partner.getyourguide.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/getyourguide-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or structured tool results from GetYourGuide search and discovery calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MCP tool responses; compact tour projections are the default for search and listing tools.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
