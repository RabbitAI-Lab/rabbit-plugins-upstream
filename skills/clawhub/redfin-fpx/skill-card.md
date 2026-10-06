## Description:

Guides agents in looking up US Redfin listings, property details, market trends, rentals, climate risk, and optionally saved homes and searches through a browser-connected command-line tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve US real-estate information from Redfin in shell workflows without running an MCP server; account-linked saved items are optional.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Redfin requests run through the user's browser session.

Mitigation: Use a separate or signed-out browser profile for public listing lookups.

Risk: Saved-home and saved-search lookups can expose account-linked Redfin data to the agent and shell output.

Mitigation: Run those lookups only when you intend to share the saved data.

Risk: Some listing searches may return a substituted region or incomplete result set.

Mitigation: Check the returned region and narrow broad searches before relying on results.

## Reference(s):

- [Redfin fpx skill release](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [Redfin endpoint guide](references/stingray-endpoints.md)
- [ContextMint Bridge source and releases](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and structured lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include property details, market data, and, when explicitly requested, account-linked saved items.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
