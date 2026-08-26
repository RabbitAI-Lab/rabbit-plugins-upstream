## Description:

Queries off-exchange index fund and ETF feeder fund information, including basic fund details, fees, risk level, managers, holdings, dividends, returns, tracking error, keyword search, and batch comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e-fintech](https://clawhub.ai/user/e-fintech)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer Chinese-language questions about off-exchange index funds, ETF feeder funds, fund comparison, holdings, returns, dividends, and purchase-process facts. It is for informational market-data lookup and objective comparison, not investment advice or account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an Index Hub API key locally and can also read API keys from environment variables.

Mitigation: Installers should protect the credentials file, avoid sharing environment values, and rotate the key if exposure is suspected.

Risk: The skill sends authenticated requests to etf.com.cn and depends on the availability and permissions of that market-data service.

Mitigation: Users should confirm network access and API-key validity before relying on the skill, and responses should clearly state when data is unavailable or permission-limited.

Risk: Fund data and AI summaries may be mistaken for investment advice or a recommendation.

Mitigation: Use the skill only for factual lookup and objective comparison, keep the required disclaimer, and avoid personalized buy, sell, allocation, or return-prediction guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/e-fintech/skills/open-fund-query)
- [Index Hub AI Skills Help](https://cdn.efunds.com.cn/eda/h5/itcenter/pd/ai-skills-doc/help.pdf)
- [OEF Query Catalog](artifact/references/catalog-oef.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese-language Markdown or plain text with concise tables, data dates, and risk notices; installation guidance may include shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Index Hub API key and returns informational fund-data summaries only.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
