## Description:

指数直通车ETF信息查询 helps agents answer Chinese ETF information and market-data questions using Index Hub data for ETF search, details, holdings, returns, dividends, rankings, and intraday quotes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e-fintech](https://clawhub.ai/user/e-fintech)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up exchange-traded ETF facts, compare products on objective metrics, and retrieve current or historical ETF market data without providing investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses a local Index Hub API key for ETF data access.

Mitigation: Install only when the user trusts the provider, store the key in the intended local credentials file, and rotate or remove the key if access is no longer needed.

Risk: ETF queries are sent to the disclosed provider service and can consume the user's daily quota.

Mitigation: Use the skill's batching and per-turn caching behavior, avoid unnecessary repeated calls, and explain unavailable results or quota issues plainly.

Risk: ETF facts, rankings, and short-term market data could be mistaken for investment advice.

Mitigation: Keep responses factual, include dates or quote times, avoid buy/sell recommendations or return promises, and retain the skill's customer-facing disclaimer.

## Reference(s):

- [ETF API field catalog](references/catalog-etf.md)
- [Index Hub AI Skills help](https://cdn.efunds.com.cn/eda/h5/itcenter/pd/ai-skills-doc/help.pdf)
- [ClawHub skill listing](https://clawhub.ai/e-fintech/skills/etf-fund-query)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional shell command snippets and tabular ETF data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Customer-facing answers should include data dates or quote times and avoid investment advice.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact metadata.version is 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
