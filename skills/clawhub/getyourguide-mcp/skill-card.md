## Description:

This skill helps an agent use GetYourGuide to search and discover tours, activities, day trips, reviews, and attraction tickets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent discover GetYourGuide tours, activities, attraction tickets, availability options, locations, categories, and reviews through a read-only MCP connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic travel requests may be routed to this provider even when the user has not specifically chosen GetYourGuide.

Mitigation: Ask the agent to confirm before using GetYourGuide for generic travel planning.

Risk: The MCP server requires a GetYourGuide partner API key.

Mitigation: Provide only a partner API key you are comfortable using with this connector.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide Partner program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Configuration]

**Output Format:** [Text or Markdown responses grounded in GetYourGuide tour, activity, ticket, location, category, option, and review records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector; search and list tools default to compact responses, with full records available through the documented view parameter.]

## Skill Version(s):

1.3.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
