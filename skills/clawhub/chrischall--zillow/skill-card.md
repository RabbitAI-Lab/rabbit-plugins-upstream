## Description:

Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP. Triggers on phrases like "find homes in", "what's the Zestimate for", "show my saved Zillow homes", "what's my saved Zillow search seeing", "what does Zillow say about", "Zillow market report for", or any request involving Zillow properties, prices, or your saved Zillow activity. Requires zillow-mcp installed and the ContextMint Bridge extension active (see Setup below).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching homes use the skill to search listings, review property and market information, check their saved Zillow activity, and calculate mortgage payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package and browser extension can access your signed-in Zillow session and saved activity.

Mitigation: Install only releases you trust, pin a reviewed package version, verify the extension download, and use project-local configuration where appropriate.

Risk: Unofficial Zillow endpoints may change.

Mitigation: Expect behavior to change as Zillow updates its web app, and review package updates before upgrading.

## Reference(s):

- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Structured data, Images]

**Output Format:** [Structured property and market information, histories, mortgage calculations, and property photos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
