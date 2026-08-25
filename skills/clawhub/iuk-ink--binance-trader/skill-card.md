## Description:

Guides an AI assistant in using the binance-mcp-server MCP for Binance USD-margined futures market analysis, indicators, risk review, order management, and trading safety workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iuk-ink](https://clawhub.ai/user/iuk-ink)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to help agents choose Binance futures MCP tools, perform installation checks, plan market and risk analysis, and execute trading workflows with testnet-first and dry-run safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live Binance futures orders can affect real funds when mainnet is enabled or real API credentials are provided.

Mitigation: Keep the default testnet setting for practice, provide API keys only when trading is intended, and review dry-run results before allowing live trades.

Risk: Repeated order attempts after ambiguous exchange timeouts can create duplicate position exposure.

Mitigation: Wait for the MCP server's order verification result or query order status instead of retrying manually.

Risk: Missing MCP tools or credentials can lead to unsupported market or trading requests.

Mitigation: Run the documented tool availability check first and explain missing MCP, credentials, or domain filtering rather than fabricating market or account data.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/iuk-ink/binance-mcp-server/tree/main/skills/binance-trader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON configuration and tool workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to call Binance MCP tools, but does not itself execute trades.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
