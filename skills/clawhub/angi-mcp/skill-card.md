## Description:

Helps agents find Angi home-service professionals, profiles, ratings, reviews, and trade and city listings using shell commands without the Angi MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find US home-service professionals by trade and city, inspect public ratings and reviews, or optionally read their own signed-in Angi account data.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Browser-assisted requests can access pages through a paired Angi tab.

Mitigation: Install and pair the required CLI and extension only if comfortable allowing browser-tab reads; keep access scoped to Angi.

Risk: Signed-in account information and public reviews may contain personal data.

Mitigation: Use account commands only with a browser profile and account you control, and handle results in line with Angi's terms and applicable privacy rules.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi page extractor](references/rsc.mjs)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Angi results; optional signed-in account data requires the user's own browser session.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
