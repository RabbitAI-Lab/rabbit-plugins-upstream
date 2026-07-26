## Description: <br>
Complete MoltMarkets trading agent setup with autonomous trader, market creator, and resolution crons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shirtlessfounder](https://clawhub.ai/user/shirtlessfounder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to configure a self-running MoltMarkets prediction-market agent that can trade, create markets, resolve outcomes, maintain local memory, and post comments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can repeatedly use a stored MoltMarkets API key to trade, create markets, resolve outcomes, and post comments with limited user visibility. <br>
Mitigation: Install only when a self-running MoltMarkets agent is intended; use a low-balance or scoped API key if available, restrict credentials file permissions, enable notifications, and keep a clear process to disable scheduled jobs and rotate the key. <br>
Risk: Autonomous cron jobs may increase financial exposure through frequent bets and market creation. <br>
Mitigation: Reduce bet and market-creation limits before enabling crons, review the configured edge threshold, Kelly multiplier, maximum position size, creator limits, and minimum balance. <br>
Risk: Automated resolution and comment behavior can affect public market outcomes and visible discussion. <br>
Mitigation: Review resolve and comment behavior before deployment, monitor outputs, and disable the scheduled jobs if behavior diverges from the operator's intent. <br>


## Reference(s): <br>
- [MoltMarkets Agent ClawHub Page](https://clawhub.ai/shirtlessfounder/skills/moltmarkets-agent) <br>
- [MoltMarkets API Reference](artifact/references/api-reference.md) <br>
- [Cron Job Definitions](artifact/references/cron-definitions.md) <br>
- [Kelly Criterion Guide](artifact/references/kelly-formula.md) <br>
- [Memory File Templates](artifact/references/memory-templates.md) <br>
- [MoltMarkets API Base URL](https://api.zcombinator.io/molt) <br>
- [CoinGecko Price API](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd) <br>
- [Binance Klines API](https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&startTime={ms}&limit=1) <br>
- [HN Algolia Items API](https://hn.algolia.com/api/v1/items/{storyId}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JavaScript cron definitions, JSON configuration, and setup code.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup instructions and agent job definitions for autonomous trading, market creation, resolution, commenting, and local memory maintenance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
