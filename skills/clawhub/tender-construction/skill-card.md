## Description:

帮助查询和分析建筑工程、市政等领域的招标、中标、企业及市场数据，并按用户指定范围调整检索。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购、投标及市场分析人员可检索招中标公告、跟踪工程项目、研究企业及竞争对手，并查看历史中标价格和账户余额。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement searches send requests to an external service.

Mitigation: Use the service only when its data handling suits the task and share only the information needed for the requested search.

Risk: Without a preconfigured key, trial signup collects limited hashed device attributes and stores the returned key locally.

Mitigation: Set ZLBX_API_KEY before use to avoid signup, or require informed consent before collecting attributes and creating an account.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-construction)
- [知了标讯服务](https://ai.zhiliaobiaoxun.com/?ch=s155)
- [Search API guidance](references/api-search.md)
- [Company registry guidance](references/api-registry.md)
- [Trial registration guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search scope and data source are stated; results depend on the available API records.]

## Skill Version(s):

1.0.4 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
