## Description:

查询和分析招投标公告、企业及市场数据，默认检索浙江省，也可按用户指定的范围查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购、投标和市场分析人员可检索招中标公告、跟踪项目进展，并查询企业、竞争对手及价格趋势。浙江省是默认检索范围，用户可指定其他地区。

### Deployment Geography for Use:

Global; Zhejiang, China is the default data search region, not a restriction on use.

## Known Risks and Mitigations:

Risk: The skill uses an API credential for account checks and may check for update notices even when the user asks only for procurement data.

Mitigation: Review this behavior before installation and use only an account whose balance and notices you are comfortable querying.

Risk: With consent, trial registration sends limited device characteristics and saves the resulting API key locally.

Mitigation: Require explicit consent before registration; decline and request a key manually if device data collection or local secret storage is unacceptable.

Risk: Requests send package and source identifiers to the service, and some data queries consume account credits.

Mitigation: Review the service's data-sharing and credit terms, and limit queries to those needed for the user's task.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bailianai/skills/tender-zhejiang)
- [Product homepage](https://ai.zhiliaobiaoxun.com/?ch=s152)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Market API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language answers with lists, tables, and source details when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search scope should be stated; results depend on the external data service and account access.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
