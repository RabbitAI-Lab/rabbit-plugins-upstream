## Description:

查询中国证券指数的基础信息、成分股、收益风险、估值基本面和行情数据，并以面向普通投资者的方式整理事实信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[e-fintech](https://clawhub.ai/user/e-fintech)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer Chinese-language questions about domestic securities indexes, including index discovery, constituent lookups, comparative metrics, valuation, fundamentals, related funds, and current market quotes. It is intended for factual data lookup and comparison, not investment advice or account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an Index Hub API key and stores or reads that credential locally.

Mitigation: Install only where local credential storage is acceptable, keep the key private, and rotate the key if it is exposed.

Risk: The skill calls the provider's market-data service, so permissions, service availability, or missing data can limit answers.

Mitigation: Surface unavailable, unauthorized, or incomplete data states clearly and do not fabricate index values, holdings, returns, valuations, or quotes.

Risk: Market-data summaries may be mistaken for investment advice or predictions.

Mitigation: Keep outputs factual, include dates or quote timestamps, preserve the required disclaimer, and avoid buy, sell, allocation, return-promise, or recommendation language.

Risk: Final answers include the provider's fixed disclaimer and promotional footer.

Mitigation: Deploy only where that footer is acceptable to users and review generated answers before broad release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/e-fintech/skills/index-query)
- [Index Hub AI Skills help](https://cdn.efunds.com.cn/eda/h5/itcenter/pd/ai-skills-doc/help.pdf)
- [Index query capability catalog](references/catalog-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown responses with concise tables or lists, plus shell commands and configuration steps during installation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Index Hub API key for live queries and appends the provider's required disclaimer and footer to final answers.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
