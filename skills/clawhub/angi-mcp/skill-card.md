## Description:

Helps agents read Angi's U.S. home-service listings, provider profiles, ratings, and reviews through a browser-assisted command-line workflow without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find U.S. home-service professionals by trade and city, examine provider ratings and reviews, and browse the Angi trade and city taxonomy. An optional signed-in workflow can read the user's own Angi account information.

### Deployment Geography for Use:

Global (U.S. home-service listings)

## Known Risks and Mitigations:

Risk: Pairing a signed-in Angi tab can expose personal account information to the agent.

Mitigation: Pair and use my.angi.com only when you intentionally want the agent to read your account identity, project counts, or reviews.

Risk: Browser-assisted fetching grants access through the user's open Angi tab.

Mitigation: Keep the extension's site access and pairing limited to the intended Angi hosts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown guidance with shell examples and extracted JSON data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public Angi data; optional signed-in account data requires a separately paired tab.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
