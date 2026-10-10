## Description:

Helps agents query U.S. Redfin listings, property details, market data, and, with a signed-in browser, saved homes and searches using fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Redfin property and market information from a shell without running an MCP server. Saved homes and searches require an explicitly paired, signed-in browser session.

### Deployment Geography for Use:

United States (Redfin property data)

## Known Risks and Mitigations:

Risk: Saved homes and searches may expose private account data.

Mitigation: Ask before accessing signed-in saved items; avoid logging or sharing raw results unnecessarily.

Risk: Browser pairing connects requests to the user's Redfin session.

Mitigation: Pair the bridge only with the user's explicit approval.

## Reference(s):

- [Redfin fpx skill release](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [Redfin endpoint reference](references/stingray-endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Fetchproxy extension information](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples and summaries of retrieved Redfin data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved-item results may contain private account data.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
