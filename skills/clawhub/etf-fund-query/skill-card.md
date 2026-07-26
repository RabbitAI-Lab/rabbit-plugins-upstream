## Description: <br>
Queries factual ETF information from 易方达指数直通车, including ETF basics, fees, holdings, historical dividends, returns, fund flows, leaderboards, and stock-to-ETF lookups; it does not provide investment advice or real-time market quotes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[e-fintech](https://clawhub.ai/user/e-fintech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to answer ETF information queries, compare ETF facts on a consistent data basis, inspect holdings and historical distributions, and explain available ETF metrics without giving investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer persistently stores the ETF API key in plaintext in the shell profile and local configuration file. <br>
Mitigation: Use a limited-scope API key, avoid sharing the installed directory or shell profile, and remove persisted key entries when uninstalling. <br>
Risk: The evidence reports an inconsistent boundary around real-time market-data support. <br>
Mitigation: Treat real-time market data as limited or unavailable unless the installed skill and current API response clearly support the requested field, and keep user-facing answers to sourced facts. <br>
Risk: ETF facts, comparisons, fund flows, heat lists, and short-term performance can be mistaken for investment advice. <br>
Mitigation: Use the bundled final-answer guardrail and include the required disclaimer that outputs are AI-generated information only and not investment advice, forecasts, or trading decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/e-fintech/skills/etf-fund-query) <br>
- [ETF query catalog](references/catalog-etf.md) <br>
- [易方达指数直通车 API service](https://www.etf.com.cn/api/etf-api-service) <br>
- [API key setup guide](https://cdn.efunds.com.cn/eda/h5/itcenter/pd/ai-skills-doc/readme.pdf) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown text with tables or lists for ETF facts and comparisons] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final answers must include data dates or reporting periods, avoid investment advice, and pass the bundled answer guardrail before being shown to users.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
