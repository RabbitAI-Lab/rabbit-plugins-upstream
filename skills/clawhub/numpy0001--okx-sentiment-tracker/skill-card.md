## Description: <br>
OKX News & Sentiment helps agents retrieve crypto news, coin sentiment, sentiment trends, source-filtered articles, and macroeconomic calendar data through the OKX CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[numpy0001](https://clawhub.ai/user/numpy0001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer crypto market intelligence questions, produce market briefings, and analyze sentiment or macroeconomic calendar events using OKX news data. It is intended for news, sentiment, and calendar workflows, not direct order placement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live OKX credentials may allow workflows to read private account positions or balances when position-impact analysis is requested. <br>
Mitigation: Require explicit user confirmation before any account-data access, prefer least-privileged read-only credentials, and require separate confirmation before any order-related action. <br>
Risk: News, sentiment, macro, and position-impact outputs can be interpreted as personalized trading guidance. <br>
Mitigation: Present outputs as informational analysis, include data source and timing context, and tell users to verify conclusions before making trading decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/numpy0001/okx-sentiment-tracker) <br>
- [OKX homepage](https://www.okx.com) <br>
- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires configured live OKX API credentials; economic calendar calls are rate-limited to 1 request per 5 seconds.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release evidence; artifact metadata references 1.3.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
