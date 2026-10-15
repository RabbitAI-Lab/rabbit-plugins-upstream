## Description:

Helps agents query Redfin for US property listings, home details, market trends, rentals, climate risk, and signed-in saved homes and searches using browser-mediated shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve US real-estate listings, property details, local trends, and account-specific saved items from Redfin without running an MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Pairing a browser bridge to a signed-in Redfin tab may expose saved homes and searches to the agent.

Mitigation: Pair only if comfortable granting that access; use a signed-out or separate browser profile unless account-specific data is intentionally needed.

## Reference(s):

- [redfin-fpx ClawHub release](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [Redfin endpoint reference](references/stingray-endpoints.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell snippets and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account-specific results require a Redfin-signed-in browser tab.]

## Skill Version(s):

1.2.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
