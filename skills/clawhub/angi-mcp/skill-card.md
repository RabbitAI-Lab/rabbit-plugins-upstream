## Description:

Reads Angi's US home-services listings through a browser-assisted shell workflow to find professionals, inspect profiles and reviews, and browse trade and city listings without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can find US home-service professionals by trade and city, compare profiles and reviews, and look up available trades and locations from a shell. An optional signed-in workflow can read their own Angi account data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser pairing on an Angi account tab can expose signed-in account information to the agent.

Mitigation: Pair only the Angi hosts needed; avoid pairing my.angi.com unless account access is intended, and do not retain or share account results unnecessarily.

Risk: Installing the fpx CLI and ContextMint Bridge adds a browser-assisted fetching capability.

Mitigation: Install only if comfortable with both tools and review the hosts approved for pairing.

## Reference(s):

- [angi-mcp on ClawHub](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [Angi trade sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Angi data retrieval; deduplicate search results by provider ID.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
