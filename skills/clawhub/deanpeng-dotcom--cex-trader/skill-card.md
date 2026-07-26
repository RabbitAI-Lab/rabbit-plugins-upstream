## Description: <br>
Unified CEX trading capability layer for AI agents that supports OKX and Binance spot and futures trading, account balance queries, order management, position queries, leverage settings, market data, and guided API key setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deanpeng-dotcom](https://clawhub.ai/user/deanpeng-dotcom) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and trading agents use this skill to interact with OKX and Binance through MCP tools for spot trades, futures trades, market data, account balances, credential setup, and position management. It is intended for live exchange workflows and should be used with explicit human oversight for trading actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can transmit exchange API credentials to a hosted MCP service. <br>
Mitigation: Install only if you trust the MCP operator; use HTTPS or another trusted MCP_SERVER_URL, disable withdrawals and transfers on API keys, and apply IP restrictions where exchanges support them. <br>
Risk: The skill can place live spot and futures orders, change leverage, and close positions. <br>
Mitigation: Require explicit human confirmation before orders, leverage changes, credential setup, or full position closure; start with testnet or small limits. <br>
Risk: Leveraged futures trading can cause significant financial loss. <br>
Mitigation: Use small position limits, conservative leverage, margin monitoring, and only funds the user can afford to lose. <br>


## Reference(s): <br>
- [Cex Trader on ClawHub](https://clawhub.ai/deanpeng-dotcom/cex-trader) <br>
- [Publisher profile](https://clawhub.ai/user/deanpeng-dotcom) <br>
- [Hosted MCP endpoint](https://mcp-skills.ai.antalpha.com/mcp) <br>
- [Skill source](artifact/SKILL.md) <br>
- [User guide](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with MCP tool-call descriptions, Python examples, shell commands, and JSON responses from trading tools] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a streamable HTTP MCP endpoint and optional environment variables for OKX, Binance, and MCP server configuration.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
