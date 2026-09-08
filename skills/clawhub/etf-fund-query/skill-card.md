## Description:

Queries exchange-traded ETF information and market data from Chinese natural-language requests, including ETF details, holdings, dividends, returns, fund flows, rankings, hot searches, and intraday quote fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e-fintech](https://clawhub.ai/user/e-fintech)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer factual questions about listed ETFs, compare ETF characteristics, inspect holdings and returns, and retrieve live or recent ETF quote information. It is intended for information lookup and comparison, not account operations, trading instructions, investment advice, or return promises.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an Index Hub API key and stores it under the user's home directory.

Mitigation: Install only on trusted systems, keep the credentials file private, and rotate or remove the key when access is no longer needed.

Risk: ETF query parameters are sent to www.etf.com.cn for data lookup.

Mitigation: Submit only the ETF, index, stock, topic, or date information needed for the query, and avoid including personal or account information.

Risk: Financial lookup summaries could be mistaken for investment advice or return predictions.

Mitigation: Keep answers factual, include data dates or quote times, preserve the standard disclaimer, and avoid recommendations, trade instructions, or promised outcomes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/e-fintech/skills/etf-fund-query)
- [Index Hub AI Skills help](https://cdn.efunds.com.cn/eda/h5/itcenter/pd/ai-skills-doc/help.pdf)
- [ETF interface field reference](references/catalog-etf.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with concise tables or lists; setup guidance may include shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Index Hub API key for live data lookup; final user-facing answers retain the provider disclaimer and avoid investment advice.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
