## Description:

Generates evidence-tracked A-share market environment and sentiment research for pre-market briefs, market health checks, sector rotation, and cross-market context without automatic stock recommendations or trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[georgetao730](https://clawhub.ai/user/georgetao730)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to prepare concise A-share market research based on dated, source-attributed public index data. It supports informational briefings and follow-up observation, not personalized investment advice, automatic stock selection, or trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may make network requests through AKShare to public market-data providers, so data availability, freshness, or provider schema changes can affect results.

Mitigation: Check the reported trade date, collection time, source names, missing fields, and errors before using the report.

Risk: Partial index data is not a complete market sentiment signal and could be mistaken for actionable trading advice.

Mitigation: Treat outputs as informational research only; require separate verified evidence for breadth, turnover, limit-up data, sector rotation, and cross-market news before forming conclusions.

Risk: Users could overextend the report into brokerage activity or personalized portfolio decisions.

Mitigation: Do not connect the skill to brokerage accounts or automated trading workflows, and keep any position discussion conditional and non-personalized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/georgetao730/skills/market-sentiment-radar)
- [Data and analysis method](references/research-method.md)
- [Risk boundaries](references/position-mapping.md)
- [AKShare index data documentation](https://akshare.akfamily.xyz/data/index/index.html)
- [Eastmoney quote source](https://quote.eastmoney.com/)
- [Sina Finance quote source](https://finance.sina.com.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text report or structured JSON from the local analyzer script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include trade date, collection time, cited data sources, missing evidence, partial index observations, and an informational disclaimer.]

## Skill Version(s):

1.3.2 (source: server release evidence and analyzer VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
