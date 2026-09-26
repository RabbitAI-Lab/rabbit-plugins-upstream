## Description:

Helps agents look up Zillow listings, property details, Zestimates, market reports, and a user's saved homes and searches through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home seekers, real-estate professionals, and their agents can research listings, property estimates, market trends, and mortgage payments, or review their saved Zillow activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in browser session exposes saved homes and searches to the MCP server.

Mitigation: Use saved-activity tools only with the account holder's consent and review the server and browser extension before installing them.

Risk: The external zillow-mcp package and fetchproxy extension are required but are not bundled in this skill artifact.

Mitigation: Review both external components before installing and keep them updated through trusted channels.

Risk: Zillow's private web endpoints or captcha challenges may interrupt lookups.

Mitigation: Confirm important results on Zillow and resolve browser challenges in the signed-in tab when necessary.

## Reference(s):

- [ClawHub Zillow skill release](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp source (linked in skill; not verified release provenance)](https://github.com/chrischall/zillow-mcp)
- [fetchproxy extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of property records, market data, saved activity, and calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; saved activity requires a signed-in Zillow browser session.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
