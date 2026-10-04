## Description:

Guides agents in using fpx and a browser tab to retrieve Zillow listings, property details, market reports, and signed-in saved items without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to search US real-estate listings and retrieve property details, price history, photos, market data, or their own saved Zillow items through a browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paired browser tab can expose account-specific saved searches and homes, and pairing persists until revoked.

Mitigation: Use a dedicated browser profile or sign out for public lookups; remove or revoke pairing when finished.

## Reference(s):

- [Zillow fpx on ClawHub](https://clawhub.ai/chrischall/skills/zillow-fpx)
- [Zillow page recipes](artifact/references/pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands retrieve Zillow page data, including account-specific saved items when the browser tab is signed in.]

## Skill Version(s):

1.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
