## Description: <br>
Sets up autonomous MoltMarkets trader, market creator, and resolution cron agents with Kelly criterion betting and learning loops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shirtlessfounder](https://clawhub.ai/user/shirtlessfounder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to configure a MoltMarkets bot that can trade, create markets, resolve outcomes, and maintain shared learning state. It is intended for users who are prepared to review and supervise autonomous prediction-market activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autonomous scheduled jobs can use stored MoltMarkets credentials to trade, create markets, post comments, and resolve outcomes. <br>
Mitigation: Review every cron before enabling it, use a low-balance or test account, and monitor logs or notifications for account-changing actions. <br>
Risk: Plaintext credentials are stored in a local MoltMarkets credentials file. <br>
Mitigation: Protect the credentials file, rotate keys if exposed, and use credentials with the minimum permissions and balance needed. <br>
Risk: Automatic resolution can produce incorrect or hard-to-reverse market outcomes. <br>
Mitigation: Keep resolution jobs manual or supervised unless you accept the risk, and verify oracle mappings and data sources before allowing automatic resolution. <br>


## Reference(s): <br>
- [MoltMarkets Skill Page](https://clawhub.ai/shirtlessfounder/skills/moltmarkets-trading) <br>
- [MoltMarkets API Reference](references/api-reference.md) <br>
- [Cron Job Definitions](references/cron-definitions.md) <br>
- [Kelly Criterion Guide](references/kelly-formula.md) <br>
- [Memory File Templates](references/memory-templates.md) <br>
- [MoltMarkets API](https://api.zcombinator.io/molt) <br>
- [CoinGecko Price API](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd) <br>
- [Binance Klines API](https://api.binance.com/api/v3/klines?symbol=BTCUSDT) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell, JavaScript, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup steps, cron definitions, memory templates, and trading strategy guidance for a MoltMarkets agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
