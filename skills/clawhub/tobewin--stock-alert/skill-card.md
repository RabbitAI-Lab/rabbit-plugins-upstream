## Description: <br>
Real-time stock query, portfolio analysis, and conversational threshold alerts for A-shares, Hong Kong stocks, and U.S. stocks without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual investors and agents assisting them use this skill to query stock prices, summarize simple portfolio or watchlist conditions, and manage conversational threshold alerts. The skill supports A-share, Hong Kong, and U.S. stock symbols and treats alerts as informational rather than trading advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stock symbols queried or monitored are sent to Sina Finance for price data. <br>
Mitigation: Install and use the skill only when that data sharing is acceptable, and avoid querying sensitive watchlists through the skill. <br>
Risk: Alert lists, thresholds, and pending alert results remain in local dotfiles until removed. <br>
Mitigation: Review and delete ~/.stock_alert_config.json and ~/.stock_alerts_pending.json when alerts are no longer needed. <br>
Risk: Price checks and alerts may be incomplete, delayed, or unsuitable as financial advice. <br>
Mitigation: Treat results as informational and verify important decisions with authoritative market or brokerage data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tobewin/skills/stock-alert) <br>
- [Sina Finance quote endpoint](https://hq.sinajs.cn/list={codes}) <br>
- [Sina Finance](https://finance.sina.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-formatted conversational responses with inline shell commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local alert configuration and pending-alert dotfiles in the user's home directory.] <br>

## Skill Version(s): <br>
1.4.0 (source: frontmatter, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
