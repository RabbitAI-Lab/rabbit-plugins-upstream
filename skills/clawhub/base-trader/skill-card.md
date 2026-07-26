## Description: <br>
Autonomous crypto trading on Base via Bankr for trading tokens, monitoring launches, executing strategies, and managing a trading portfolio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sp0oby](https://clawhub.ai/user/sp0oby) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to guide Base-chain crypto trading through Bankr, including portfolio checks, token research, buy/sell workflows, automation setup, and trade journaling. Because it can route an agent toward real crypto transactions, users should treat outputs as trade proposals requiring review and confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide actions that affect real crypto wallet funds. <br>
Mitigation: Use a dedicated low-balance wallet and require manual confirmation for every buy, sell, order, DCA, leverage, or standing automation. <br>
Risk: Autonomous trading workflows may continue placing or managing orders without clear per-trade consent. <br>
Mitigation: Do not enable cron, heartbeat, DCA, leverage, or standing orders until spending limits, cancellation steps, and Bankr permissions are understood. <br>
Risk: The skill depends on a separate Bankr skill and local wallet/API configuration. <br>
Mitigation: Inspect the Bankr skill, its permissions, and wallet configuration before installation or execution. <br>


## Reference(s): <br>
- [Automation Strategies](references/automation-strategies.md) <br>
- [Trade Execution](references/execution.md) <br>
- [Launch Sniping Guide](references/launch-sniping.md) <br>
- [Leverage Trading Guide](references/leverage-guide.md) <br>
- [Market Analysis](references/market-analysis.md) <br>
- [Market Research via Bankr](references/market-research-bankr.md) <br>
- [Risk Management](references/risk-management.md) <br>
- [Trading Strategies Deep Dive](references/strategies.md) <br>
- [Token Analysis Framework](references/token-analysis.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local Bankr scripts and maintain JSON trade and performance journals.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
