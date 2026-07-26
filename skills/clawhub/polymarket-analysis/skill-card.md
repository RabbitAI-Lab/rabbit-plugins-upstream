## Description: <br>
Analyzes Polymarket prediction markets for trading edges using pair-cost arbitrage, whale tracking, sentiment, momentum, and user profile signals without trade execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lukebaze](https://clawhub.ai/user/lukebaze) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and external users use this skill to inspect Polymarket markets, monitor price and volume changes, and summarize wallet positions or trading signals. It supports analysis and alerting only, not trade execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monitoring mode can continue sending alerts after the immediate analysis task is complete. <br>
Mitigation: Confirm the market, interval, delivery channel, and recipient before enabling monitoring, and remove the cron job when alerts are no longer needed. <br>
Risk: Saved market state can become stale or remain on disk after monitoring is no longer wanted. <br>
Mitigation: Use a deliberate state-file location, review it before reuse, and delete stored state when monitoring is disabled. <br>
Risk: Prediction-market signals can be misleading because prices, liquidity, and wallet behavior change quickly. <br>
Mitigation: Treat outputs as analysis and guidance only; verify market data and risk assumptions before making any trading decision. <br>


## Reference(s): <br>
- [Polymarket API Reference](references/polymarket-api.md) <br>
- [Market Monitoring Setup](references/market-monitoring-setup.md) <br>
- [Pair Cost Arbitrage Strategy](references/pair-cost-arbitrage.md) <br>
- [Momentum Analysis Strategy](references/momentum-analysis.md) <br>
- [Whale Tracking Strategy](references/whale-tracking.md) <br>
- [Sentiment Analysis Strategy](references/sentiment-analysis.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/lukebaze/skills/polymarket-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, JSON script output, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only API analysis with optional state files and monitoring alerts.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
