## Description: <br>
Dynamic grid trading strategy for any token pair on EVM L2 chains via OKX DEX API, with asymmetric grid steps, multi-timeframe trend analysis, trend-adaptive sizing, risk controls, DEX execution, PnL calculation, and Discord notification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[synththoughts](https://clawhub.ai/user/synththoughts) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use this skill to create, configure, run, debug, and tune an autonomous EVM L2 grid-trading bot that trades token pairs through OKX DEX and reports status to notification channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autonomous live trading can move real funds and lose value during volatile or trending markets. <br>
Mitigation: Use only a dedicated low-balance wallet, test with read-only status commands first, and review grid, position, stop-loss, and trade-size settings before enabling the tick loop. <br>
Risk: The bot requires OKX credentials and wallet access for DEX execution. <br>
Mitigation: Use restricted OKX credentials, keep secrets out of shared logs, and verify wallet account selection before running trading commands. <br>
Risk: The reference implementation can create broad token approvals for DEX routers. <br>
Mitigation: Review approval behavior, restrict balances exposed to the trading wallet, and revoke unneeded router approvals after use. <br>
Risk: Cron scheduling and automatic stop-loss resume can restart trading without active operator review. <br>
Mitigation: Review or disable cron and auto-resume behavior until operational limits, stop conditions, and alerting channels are validated. <br>
Risk: Trading data may be sent to Discord or Telegram notification destinations. <br>
Mitigation: Use private notification channels and verify Discord and Telegram configuration before enabling notifications. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/synththoughts/grid-trading) <br>
- [README](README.md) <br>
- [Grid Algorithm Reference](references/grid-algorithm.md) <br>
- [Reference Configuration](references/config.json) <br>
- [Trading Bot Entrypoint](references/eth_grid.py) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, Python reference code, and structured JSON status blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger live trading operations when configured and run with wallet and OKX credentials.] <br>

## Skill Version(s): <br>
1.5.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
