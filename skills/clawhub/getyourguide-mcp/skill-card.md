## Description:

Helps agents discover GetYourGuide tours, activities, tickets, options, and reviews through a read-only search connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners and their agents use this skill to search and compare GetYourGuide tours, activities, attraction tickets, and reviews. Booking takes place on GetYourGuide, not through this connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search terms are sent to the GetYourGuide API when the connector is used.

Mitigation: Avoid including sensitive personal information in searches.

Risk: Installation adds a persistent connector using an external npm package and a GetYourGuide API key.

Mitigation: Keep the API key private and use project-level configuration if global access is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [GetYourGuide MCP npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide partner program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tour listings and details, options, reviews, and booking links; compact responses by default, with full records on request.]

## Skill Version(s):

2.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
