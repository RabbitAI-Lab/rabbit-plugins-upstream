## Description:

Guides agents to query Compass real-estate listings, property and agent details, price history, and address suggestions with fpx through an active browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find US real-estate listings, inspect property and agent details, and resolve addresses without running the Compass MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Compass requests use the active browser session and may share its cookies or browsing state.

Mitigation: Use a dedicated browser profile to isolate Compass cookies and browsing state, and install only if comfortable with this access.

## Reference(s):

- [Compass request recipes](references/requests.md)
- [Compass page-data extraction helper](references/extract-global.mjs)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recipes can extract JSON from Compass pages and responses.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
