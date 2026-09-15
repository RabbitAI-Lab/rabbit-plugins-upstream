## Description:

HyperNatt Terminal onboards agents to a remote MCP server with six crypto market, execution-context, and swap-routing tools, without local shell or filesystem access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dialloube-research](https://clawhub.ai/user/dialloube-research)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-agent operators use this skill to connect agents to HyperNatt Terminal's remote MCP tools for liquidation radar, execution-cost checks, execution reconciliation, and optional swap routing. The skill is onboarding guidance only and does not provide trading advice, submit orders, create wallets, or change local host configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote MCP calls may have financial implications because some calls cost 0.001 USDC and swap routing requires the user's own wallet approval.

Mitigation: Review payment behavior before use, rely on configured wallet authorization rules, and make clear that users choose whether to enable paid calls or swaps.

Risk: Market and execution-context outputs could be mistaken for trading advice.

Mitigation: Present outputs as market-data and execution analysis only, and preserve the artifact's no-trade-advice, no-custody, and no-performance-promise constraints.

Risk: Overstating the tool surface could cause agents to call unavailable or unsupported tools.

Mitigation: Describe exactly six remote MCP tools and avoid claiming local execution, filesystem access, wallet creation, or additional terminal capabilities.

## Reference(s):

- [HyperNatt Platform](https://hypernatt.com)
- [HyperNatt MCP Protocol](https://hypernatt.com/mcp/protocol)
- [HyperNatt MCP Server Card](https://hypernatt.com/.well-known/mcp/server-card.json)
- [Coinbase Agentic Wallet MCP Documentation](https://docs.cdp.coinbase.com/agentic-wallet/mcp/welcome)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions]

**Output Format:** [Markdown with JSON MCP call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No local shell commands or files; remote MCP calls may involve USDC payments and user-controlled wallet approval.]

## Skill Version(s):

1.6.1 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
