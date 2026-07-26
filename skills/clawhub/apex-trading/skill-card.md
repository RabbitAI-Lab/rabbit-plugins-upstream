## Description: <br>
Trade and monitor ApeX perpetual futures. Check balances, view positions with P&L, place/cancel orders, execute market trades, or submit trade reward enrollments. Use when the user asks about ApeX trading, portfolio status, crypto positions, activity enrollments, or wants to execute trades on ApeX. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joshlin111](https://clawhub.ai/user/joshlin111) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to monitor ApeX perpetual futures portfolios, analyze crypto market conditions, and prepare or execute ApeX trading actions through an agent. It is intended for users who intentionally connect ApeX credentials and understand the risks of live futures trading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place or cancel live ApeX futures orders without a built-in confirmation step. <br>
Mitigation: Use testnet first and require explicit user confirmation before every trade, close-position, cancel-all, or reward-enrollment action. <br>
Risk: ApeX API credentials and the Omni seed grant access to private account and trading operations. <br>
Mitigation: Keep the API key, secret, passphrase, and Omni seed out of chat and source control, and restrict API permissions where possible. <br>
Risk: Generated trade signals may be incorrect or unsuitable for the user's financial situation. <br>
Mitigation: Treat generated trade signals as informational, not financial advice, and verify position sizing, prices, and risk before acting. <br>
Risk: Local trading state can expose sensitive trading activity on shared or synced machines. <br>
Mitigation: Protect or delete trading-state.json when using shared, backed-up, or synced environments. <br>


## Reference(s): <br>
- [ApeX Omni API Reference](references/api.md) <br>
- [ApeX Omni mainnet API](https://omni.apex.exchange) <br>
- [ApeX Omni testnet API](https://qa.omni.apex.exchange) <br>
- [CoinGecko market chart API](https://api.coingecko.com/api/v3/coins/{coinId}/market_chart) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [JSON from CLI tools, with Markdown or plain-text summaries and inline shell commands for agent responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Private operations require ApeX API credentials and an Omni seed; trading outputs can include order IDs, status, balances, positions, fills, and market analysis.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
