## Description:

HyperNatt Terminal onboards agents to a remote MCP service with three tools for manifest lookup, liquidation radar data, and Nattswap swap routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dialloube-research](https://clawhub.ai/user/dialloube-research)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-agent operators use this skill to connect an agent runtime to HyperNatt Terminal's remote MCP service, inspect liquidation microstructure, and optionally prepare swap routing through a separate wallet-signing flow. The skill is onboarding guidance and does not provide trade advice, custody, local execution, or local file access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid x402 calls and wallet-signing flows can spend USDC or authorize transactions.

Mitigation: Review the remote MCP server and wallet-signing flow before use; connect only intended wallets and sign only transactions you understand.

Risk: Swap routing and liquidation-market context can be mistaken for trade advice or an execution guarantee.

Mitigation: Treat the skill as onboarding and market-data guidance only; make trading decisions and venue execution through separately reviewed controls.

Risk: The remote MCP service is an external dependency whose behavior is outside the local artifact.

Mitigation: Review the server card, source, and security policy before enabling the MCP endpoint in an agent runtime.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dialloube-research/skills/hypernatt-terminal)
- [Server-Resolved GitHub Source](https://github.com/DIALLOUBE-RESEARCH/hypernatt-terminal/tree/main/skills/hypernatt-terminal)
- [HyperNatt Platform](https://hypernatt.com)
- [HyperNatt MCP Protocol](https://hypernatt.com/mcp/protocol)
- [HyperNatt MCP Server Card](https://hypernatt.com/.well-known/mcp/server-card.json)
- [Security Policy](https://github.com/DIALLOUBE-RESEARCH/hypernatt-terminal/blob/main/SECURITY.md)
- [Coinbase Agentic Wallet MCP Docs](https://docs.cdp.coinbase.com/agentic-wallet/mcp/welcome)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with tables, ordered steps, links, and inline bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No local shell, filesystem, environment-variable, or secret access is requested by the artifact; remote MCP use may involve paid x402 calls and wallet signing.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
