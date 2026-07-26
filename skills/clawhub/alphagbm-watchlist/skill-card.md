## Description: <br>
Monitor a list of tickers for key changes in price, IV rank, unusual activity, earnings dates, and score changes, with support for custom watchlists and a default hot-options list. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and market-monitoring agents use this skill to manage ticker watchlists, review dashboard summaries, and surface price, volatility, unusual-options-activity, earnings, and priority alert changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Watchlist summaries and quick actions may influence trading decisions. <br>
Mitigation: Verify market data, options activity, earnings dates, and any trade idea independently before acting. <br>
Risk: Mock data and example API endpoints can be mistaken for live integrations. <br>
Mitigation: Treat documented mock data and sample endpoints as implementation examples unless connected to a verified live data source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-watchlist) <br>
- [AlphaGBM](https://alphagbm.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or structured text with watchlist dashboards, alert flags, daily summaries, and suggested actions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use ticker symbols, watchlist commands, alerts-only queries, and hot-options requests as input context.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
