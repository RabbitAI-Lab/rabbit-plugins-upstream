## Description:

Helps agents find Angi home-service professionals by trade and city, inspect profiles and reviews, and list supported trades and locations using browser-assisted fetching rather than an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can look up US home-service professionals, compare ratings and reviews, and explore Angi's trade and city listings without running an MCP server. Optional account lookups require an explicitly paired signed-in tab.

### Deployment Geography for Use:

United States (Angi directory coverage)

## Known Risks and Mitigations:

Risk: The browser-paired fetch tool relies on an installed CLI and extension with access to an open Angi tab.

Mitigation: Install only if you trust @fetchproxy/cli and ContextMint Bridge; pair only www.angi.com for public lookups.

Risk: Pairing my.angi.com can expose signed-in account information to the agent, and extracted profiles or reviews may contain personal data.

Mitigation: Pair my.angi.com only when intentionally accessing your own account; handle extracted data carefully and follow Angi's terms.

## Reference(s):

- [Angi MCP on ClawHub](https://clawhub.ai/chrischall/skills/angi-mcp)
- [ContextMint Bridge source and setup](https://github.com/nullnet-app/contextmint-bridge)
- [Angi page shapes and recipes](artifact/references/angi-pages.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only directory and review lookups; optional signed-in account details require separate pairing.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
