## Description:

One-shot bootstrap for the Simmer MCP server that detects your agent runtime, installs simmer-mcp via npm, writes the right MCP config, prompts a restart, and verifies the tool handshake for running Simmer trading strategies through an MCP-aware agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an MCP-aware agent to Simmer's market, portfolio, and trading tools after obtaining a Simmer API key. It guides runtime detection, MCP installation, configuration, restart, and handshake verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent MCP configuration can expose the Simmer API key or trading-related tools on shared or cloud runtimes.

Mitigation: Use project or scoped configuration where practical, avoid printing secrets in transcripts or logs, and restrict use to environments where stored secrets are protected.

Risk: Live trading tools may place real trades when the user deliberately enables live venues and trading gates.

Mitigation: Keep live-trading gates disabled unless real trading is intended; use paper or simulated trading defaults for setup and verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/simmer-mcp-setup)
- [Simmer MCP package](https://www.npmjs.com/package/simmer-mcp)
- [Simmer documentation](https://docs.simmer.markets)
- [Simmer dashboard](https://simmer.markets/dashboard?ref=sdk-skill&utm_campaign=sdk-skill)
- [Simmer Python SDK skill](https://clawhub.ai/skills/simmer)
- [Simmer wallet setup skill](https://clawhub.ai/skills/simmer-wallet-setup)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides persistent MCP configuration and verification; does not itself execute trades.]

## Skill Version(s):

0.3.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
