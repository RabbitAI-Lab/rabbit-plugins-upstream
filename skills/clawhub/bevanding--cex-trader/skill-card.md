## Description: <br>
Unified CEX trading capability layer for AI agents that supports OKX and Binance spot and futures trading, account queries, order management, position queries, leverage settings, margin mode configuration, and guided API key setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bevanding](https://clawhub.ai/user/bevanding) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent place and manage OKX or Binance spot and futures trades through MCP tools. It is intended for users who deliberately want agent-assisted centralized exchange trading and have reviewed credential, leverage, and trade-execution risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real spot and leveraged futures trades on OKX or Binance. <br>
Mitigation: Use demo/testnet or very small balances first and require explicit user confirmation before any order, leverage change, or position close. <br>
Risk: Exchange credentials can be sent to the configured MCP server. <br>
Mitigation: Verify the MCP endpoint before sending credentials and use dedicated trade-only API keys with withdrawal and transfer permissions disabled. <br>
Risk: Compromised or over-permissive API keys could expose exchange accounts. <br>
Mitigation: Enable exchange IP allowlisting where possible and scope keys to the minimum trading permissions needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bevanding/cex-trader) <br>
- [Hosted MCP endpoint](https://mcp-skills.ai.antalpha.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [API calls, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [JSON tool responses, command-line output, and Markdown guidance with inline code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can initiate live spot or leveraged futures trading actions when connected to valid OKX or Binance credentials.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
