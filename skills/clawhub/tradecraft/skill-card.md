## Description: <br>
Execute trades, manage wallets, monitor signals, and collaborate in trading groups on Solana using Tradecraft.finance's API platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psuede](https://clawhub.ai/user/psuede) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to guide agents that interact with Tradecraft.finance APIs for Solana trading, wallet operations, signal monitoring, and trading group activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may be given authority over real crypto funds through live Solana trading and wallet trading-enable operations. <br>
Mitigation: Use a dedicated low-balance wallet, narrowly scoped and revocable API keys, and manual confirmation for every trade or wallet trading-enable action. <br>
Risk: Heartbeat loops can continue trading or posting group messages unattended. <br>
Mitigation: Set explicit position size, slippage, loss, and polling limits, and keep a clear stop mechanism available before enabling any continuous loop. <br>
Risk: Trading signals and group-chat activity may lead an agent toward unsafe, manipulative, or unwanted trades. <br>
Mitigation: Use trusted signal sources only and require human review before acting on new, untrusted, or high-impact signals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/psuede/skills/tradecraft) <br>
- [Tradecraft Web App](https://tradecraft.finance) <br>
- [Tradecraft Main Documentation](https://tradecraft.finance/skills.md) <br>
- [Authentication Documentation](https://tradecraft.finance/AUTH.md) <br>
- [Trading Documentation](https://tradecraft.finance/TRADING.md) <br>
- [Wallet Documentation](https://tradecraft.finance/WALLETS.md) <br>
- [Signals Documentation](https://tradecraft.finance/SIGNALS.md) <br>
- [Groups Documentation](https://tradecraft.finance/GROUPS.md) <br>
- [Heartbeat Guide](https://tradecraft.finance/HEARTBEAT.md) <br>
- [Error Code Reference](https://tradecraft.finance/ERRORS.md) <br>
- [Tradecraft Status](https://status.tradecraft.finance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documentation with curl and Python examples plus JSON request and response snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-supplied Tradecraft API keys, scoped permissions, wallet identifiers, token addresses, and operating limits before an agent can act on the documented API guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
