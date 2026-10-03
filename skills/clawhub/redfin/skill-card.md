## Description:

Helps agents find Redfin property listings, property details, housing-market reports, and a user's saved homes and searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers, real-estate researchers, and other users can ask an agent to search Redfin listings, inspect properties and market trends, estimate mortgage payments, or retrieve their own saved homes and searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in Redfin access can expose private saved homes and searches to the connected tools.

Mitigation: Request account-scoped tools only when the user intends to retrieve private Redfin data.

Risk: The MCP package and browser bridge operate through the user's Redfin browser session.

Mitigation: Review the npm package and browser extension source or releases before installation, and connect only if comfortable granting session access.

## Reference(s):

- [Redfin skill on ClawHub](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package (linked in skill)](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source (linked in skill; not verified import provenance)](https://github.com/chrischall/redfin-mcp)
- [ContextMint Bridge releases (linked in skill)](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance and structured Redfin tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing details, market metrics, mortgage calculations, and, when requested, saved-account data; results depend on Redfin availability and browser sign-in.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
