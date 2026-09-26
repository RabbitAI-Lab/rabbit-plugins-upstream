## Description:

Helps agents look up Redfin listings, property details, market reports, and a user's saved homes and searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and other users can ask an agent to find Redfin listings, review property and market information, and check their saved homes or searches when signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a signed-in Redfin session can expose saved homes and searches.

Mitigation: Enable this access only if comfortable sharing that activity; remove the MCP configuration or extension when no longer needed.

Risk: The external MCP package and browser extension require trust before installation.

Mitigation: Review the npm package and extension source before installing.

## Reference(s):

- [redfin-mcp package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source](https://github.com/chrischall/redfin-mcp)
- [fetchproxy browser extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include listings, property details, market summaries, and signed-in saved activity; compact responses omit some photo URLs.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
