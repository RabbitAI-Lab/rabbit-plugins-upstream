## Description:

One-shot bootstrap for the Simmer MCP server that detects the agent runtime, installs simmer-mcp via npm, writes the correct MCP config, prompts a restart, and verifies the tool handshake for Simmer trading workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to configure Simmer MCP access in MCP-aware runtimes so their agents can query markets, inspect portfolios, and run Simmer trading workflows with documented safety defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill configures an npm-launched MCP server with API-key access that may persist in agent runtime configuration.

Mitigation: Install only from trusted Simmer package sources, prefer pinning simmer-mcp to a reviewed exact version, and remove or disable the MCP entry when it is no longer needed.

Risk: Literal API keys in shared or persistent MCP configs can expose trading access.

Mitigation: Use runtime-supported environment forwarding or project-scoped config where practical, avoid shared hosted bot environments for claimed real-money keys, and keep secrets out of transcripts and committed files.

Risk: Real-money trading is possible when live venue settings and the live-trading environment gate are enabled.

Mitigation: Keep paper trading defaults for setup and verification, require explicit live-trading opt-in, and complete wallet setup only when the user intends real venue access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/simmer-mcp-setup)
- [simmer-mcp npm package](https://www.npmjs.com/package/simmer-mcp)
- [Simmer documentation](https://docs.simmer.markets)
- [Simmer dashboard](https://simmer.markets/dashboard?ref=sdk-skill&utm_campaign=sdk-skill)
- [Simmer SDK skill](https://clawhub.ai/skills/simmer)
- [Simmer wallet setup skill](https://clawhub.ai/skills/simmer-wallet-setup)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown instructions with inline shell commands and JSON/TOML/YAML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIMMER_API_KEY and Node.js/npm; optional Python setup is documented for the preflight tool.]

## Skill Version(s):

0.3.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
