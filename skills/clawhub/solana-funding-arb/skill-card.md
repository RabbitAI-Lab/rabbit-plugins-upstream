## Description: <br>
Solana perpetual DEX funding rate arbitrage scanner and auto-trader that compares funding rates across Drift and Flash Trade to find cross-DEX arbitrage opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zedit42](https://clawhub.ai/user/zedit42) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, and traders use this skill to scan Solana perpetual DEX funding rates, review delta-neutral arbitrage opportunities, configure dry-run or live-trading workflows, and run simulations or backtests before deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live trading paths are under-scoped and incomplete in ways that could put wallet funds at risk. <br>
Mitigation: Keep the skill in dry-run mode unless the code has been reviewed and the venue support, mock-data behavior, and failed-leg unwind handling are fixed. <br>
Risk: Using an important wallet key with experimental financial automation can expose meaningful funds to loss. <br>
Mitigation: Use a dedicated low-balance wallet and do not reuse important private keys. <br>
Risk: Cron or unattended live trading can amplify incomplete execution behavior. <br>
Mitigation: Avoid cron and live trading until the implementation has been reviewed and corrected. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zedit42/skills/solana-funding-arb) <br>
- [API Reference](references/api.md) <br>
- [Setup Guide](references/setup.md) <br>
- [Strategy Guide](references/strategies.md) <br>
- [Drift Protocol Docs](https://docs.drift.trade) <br>
- [Flash Trade](https://flash.trade) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, JSON, TypeScript, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce scanner results, dashboard usage guidance, trading configuration, simulation commands, and risk-control recommendations.] <br>

## Skill Version(s): <br>
2.1.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
