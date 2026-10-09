## Description:

Guides agents in querying US Redfin listings, property details, market data, and optional signed-in saved items through the fpx CLI and a paired browser extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up US homes, listings, prices, market trends, rentals, and climate risk from Redfin without running an MCP server. With explicit user intent, they can also retrieve saved homes and searches from a signed-in account.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Signed-in saved homes and searches can expose private account data to the agent.

Mitigation: Use saved-item endpoints only when the user specifically requests them; treat returned items as private.

Risk: Requests run through a paired extension using the user's browser session.

Mitigation: Install and pair the fpx CLI and ContextMint Bridge only if the user accepts browser-session Redfin access.

## Reference(s):

- [Redfin FPX ClawHub release](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [Stingray endpoint examples](artifact/references/stingray-endpoints.md)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redfin responses require prefix removal and result-code checking.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
