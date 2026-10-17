## Description:

Looks up Compass real-estate listings, property details, photos, price history, and addresses for agents responding to property questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate professionals use this skill to search Compass homes, inspect listing details and price history, compare properties, and estimate mortgage costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Property requests pass through a signed-in Compass browser tab, potentially exposing account-accessible data to the agent workflow.

Mitigation: Use only an account and browser profile containing data you are comfortable sharing with the MCP server and agent.

Risk: The integration depends on an npm package and browser extension operating in the signed-in session.

Mitigation: Review and trust both components before installing or enabling them.

## Reference(s):

- [ClawHub Compass skill release](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp package](https://www.npmjs.com/package/compass-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with property details, listing comparisons, or mortgage estimates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property lookups require a signed-in Compass browser session; saved homes and searches are not supported.]

## Skill Version(s):

1.1.11 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
