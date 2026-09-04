## Description:

One-shot bootstrap for the Simmer MCP server that detects the agent runtime, installs simmer-mcp, writes MCP configuration, prompts a restart, and verifies the tool handshake.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install and configure the Simmer MCP server so MCP-aware agents can query markets, run Simmer playbooks, and, with explicit safeguards, place paper or live trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill configures persistent access to a trading-capable MCP server through SIMMER_API_KEY.

Mitigation: Use a fresh limited or unclaimed agent key where possible, store it only in user-scoped configuration with restrictive file permissions, and keep claimed live-trading keys off shared runtimes.

Risk: The setup flow can install simmer-mcp through an unpinned npm command, so later package changes may affect behavior.

Mitigation: Prefer a pinned simmer-mcp package version and review the package source and publisher before installation.

Risk: Live trading can place real orders when the user enables the required live-trading gates.

Mitigation: Keep the paper sim venue as the default and enable live trading only after wallet, spending, and agent-control boundaries are clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/simmer-mcp-setup)
- [simmer-mcp npm package](https://www.npmjs.com/package/simmer-mcp)
- [Simmer documentation](https://docs.simmer.markets)
- [Simmer dashboard](https://simmer.markets/dashboard?ref=sdk-skill&utm_campaign=sdk-skill)
- [General Simmer skill](https://clawhub.ai/skills/simmer)
- [Simmer wallet setup skill](https://clawhub.ai/skills/simmer-wallet-setup)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell commands and JSON/YAML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides MCP setup for multiple agent runtimes; requires SIMMER_API_KEY and Node.js/npm.]

## Skill Version(s):

0.2.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
