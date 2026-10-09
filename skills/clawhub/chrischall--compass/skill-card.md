## Description:

Looks up Compass real-estate listings, property details, photos, price history, and address matches, and helps compare homes and estimate housing costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, renters, and real-estate professionals can search and compare Compass properties, review listing history and photos, and calculate estimated mortgage payments or affordability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Property lookups use a signed-in Compass browser tab through a third-party MCP server and browser extension.

Mitigation: Install only if comfortable trusting both components with this session; prefer project-level configuration and remove the server or extension when no longer needed.

Risk: Sign-in requirements, browser challenges, and batch timeouts can leave property results incomplete.

Mitigation: Confirm the Compass tab is signed in, resolve browser challenges there, and retry pending batch rows rather than treating them as missing listings.

## Reference(s):

- [Compass skill listing](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp package](https://www.npmjs.com/package/compass-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only property information and comparisons; mortgage and affordability estimates are calculated locally.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
