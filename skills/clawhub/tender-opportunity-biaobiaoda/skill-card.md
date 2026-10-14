## Description:

帮助用户检索中国招投标公告、评估项目机会，并分析供应商、竞争对手和历史中标价格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

采购和投标团队可用它寻找招标机会、核查企业与历史中标记录，并辅助评估投标竞争形势；结果应依据实际返回的数据判断。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries use a third-party tender-data service and require an API key that may be stored locally.

Mitigation: Review the service before use, protect the API key and local configuration, and supply a manually configured key if preferred.

Risk: Automatic trial registration collects limited device features, including a hashed MAC address.

Mitigation: Request explicit consent before registration; use a manually configured API key to avoid device-based registration.

Risk: Tender and company records may be incomplete or outdated, and some data calls consume credits.

Mitigation: Base conclusions on returned records, check data dates and source scope, and limit paid queries to what the user requested.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/tender-opportunity-biaobiaoda)
- [Bid-search API reference](artifact/references/api-search.md)
- [Company-analysis API reference](artifact/references/api-company.md)
- [Market-analysis API reference](artifact/references/api-market.md)
- [Company-registry interpretation guide](artifact/references/api-registry.md)
- [Account API reference](artifact/references/api-account.md)
- [Registration and API-key setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables of tender, company, and market results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the provider's available records; some queries consume account credits.]

## Skill Version(s):

2.0.6 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
