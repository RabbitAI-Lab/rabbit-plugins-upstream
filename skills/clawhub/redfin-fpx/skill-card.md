## Description:

Guides agents to query Redfin listings, property details, market data, and signed-in saved items using fpx through a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to retrieve US real-estate listings, home details, market trends, and, with permission, saved homes or searches without running a separate MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and saved searches can expose private account data.

Mitigation: Request explicit permission before fetching these endpoints and avoid logging their responses.

Risk: Requests use a paired browser tab with access to the Redfin session.

Mitigation: Install and pair the browser bridge only if comfortable granting it access to that tab.

## Reference(s):

- [Redfin stingray endpoint guide](references/stingray-endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [fpx CLI and extension guidance](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes examples for parsing Redfin responses; signed-in account data requires explicit permission.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
