## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP. Triggers on phrases like "find homes on compass in", "compass property details for", "compass photos for", "compass price history for", "resolve this address on compass", "compare these compass listings", "what does compass say about", or any request involving Compass properties, prices, or comparisons. Requires compass-mcp installed and the ContextMint Bridge extension active (see Setup below).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers, renters, and real-estate researchers can use this skill to find and compare Compass listings, review property details and history, and resolve addresses. It also provides local mortgage and affordability estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP package and browser extension require trust and can access the signed-in Compass session.

Mitigation: Review and pin the MCP package version, verify the extension release, and approve only the Compass access needed.

Risk: Queries may run under the wrong signed-in account if multiple sessions are configured.

Mitigation: Confirm the intended Compass account before querying.

## Reference(s):

- [Compass skill listing](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp package](https://www.npmjs.com/package/compass-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Structured data, Analysis]

**Output Format:** [Structured property and listing results with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include property details, photo links, price history, listing comparisons, mortgage estimates, and affordability calculations.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
