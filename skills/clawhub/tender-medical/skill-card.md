## Description:

查询和分析中国招投标公告、企业及市场数据，默认侧重医疗卫生领域。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

采购、投标和市场分析人员可检索招中标商机、追踪项目进展，并分析企业、供应商、品牌及历史中标价格；医疗卫生是默认检索方向，用户可指定其他范围。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Procurement searches use an external API that may consume paid credits.

Mitigation: Confirm API use and check account balance or costs before extensive queries.

Risk: Optional trial registration transmits device characteristics and stores an API key locally.

Mitigation: Prefer a user-provided API key; obtain consent before registration and protect ~/.zlbx/config.json.

Risk: Ambiguous company scope or inconsistent amount-unit documentation may mislead business decisions.

Mitigation: Confirm the company entities and monetary units against source results before relying on the analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-medical)
- [Publisher profile](https://clawhub.ai/user/bailianai)
- [Provider website](https://ai.zhiliaobiaoxun.com/?ch=s154)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Business registry API reference](references/api-registry.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Optional registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States the actual search scope and filters; may include linked procurement notices.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
