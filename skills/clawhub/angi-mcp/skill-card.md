## Description:

Helps agents find US home-service professionals, profiles, ratings, reviews, and trade and city listings on Angi using a browser-assisted command-line workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers researching US home-service providers can use this skill to find professionals by trade and city, inspect profiles and reviews, and discover supported locations without installing the Angi MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Pairing the browser bridge with extra hosts can expose more browsing-session data than needed.

Mitigation: Pair only the Angi hosts needed for the task; keep account access separate from public searches.

Risk: Optional account pages and public reviews may contain personal information, including reviewer names and review text.

Mitigation: Read signed-in account pages only with explicit user intent, minimize retained review details, and follow Angi's terms.

## Reference(s):

- [angi-mcp release](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)
- [Angi trade sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and commands; JSON records when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; optional signed-in account data requires separate host pairing.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
