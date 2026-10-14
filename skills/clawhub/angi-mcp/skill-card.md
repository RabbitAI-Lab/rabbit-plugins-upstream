## Description:

Guides agents in reading Angi's US home-service listings, provider profiles, ratings, reviews, and trade and city directories from a shell without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can find US home-service professionals by trade and city, compare profiles and reviews, and inspect available trade and city directories. An optional workflow reads the user's own Angi account pages when explicitly paired with a signed-in browser tab.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Pairing a signed-in Angi account tab may expose the user's account pages to the agent.

Mitigation: Pair my.angi.com only when account data is needed, and review retrieved information before sharing it.

Risk: Reading Angi pages requires the fpx CLI and ContextMint Bridge extension in the user's browser.

Mitigation: Install and pair these components only if comfortable fetching pages through the browser; use public sitemaps without the extension for directory lookup.

## Reference(s):

- [angi-mcp release on ClawHub](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](artifact/references/angi-pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Angi trade directory sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON data]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public listings and reviews; optional signed-in account data only when the user pairs an account tab.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
