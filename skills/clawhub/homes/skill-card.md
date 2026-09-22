## Description:

Look up real-estate listings, property details, price/tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query homes.com listings, property details, market reports, price and tax history, photos, saved homes, and local home-finance calculations through the homes-mcp integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in homes.com browser session to read account-specific saved homes and searches.

Mitigation: Use saved homes and saved searches tools only when the user is comfortable letting the agent read that account-specific homes.com data.

Risk: The skill depends on the homes-mcp package and the fetchproxy browser extension.

Mitigation: Review the homes-mcp package and fetchproxy extension before installing or enabling the integration.

## Reference(s):

- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source](https://github.com/chrischall/homes-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown guidance and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only homes.com data access through a signed-in browser session; selected compact responses strip media URLs by default.]

## Skill Version(s):

2.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
