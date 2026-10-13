## Description:

通过知了标讯数据查询临期招投标商机、采购客户和竞争对手动态，并汇总市场洞察。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

销售和投标团队使用中国招投标数据发现临期续约机会、潜在客户与供应商，并分析竞对中标和市场趋势。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender-search queries are sent to the Zhiliaobiaoxun service.

Mitigation: Use the service only when sharing the query is acceptable.

Risk: Optional trial registration sends device characteristics and stores a returned API key locally.

Mitigation: Prefer your own ZLBX_API_KEY; otherwise obtain consent before registration and protect ~/.zlbx/config.json.

Risk: Company matching or amount filters may lead to misleading opportunity analysis.

Mitigation: Confirm matched legal entities, applied filters, and amount units before relying on results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/tender-opportunity-intelligence-officer)
- [标讯搜索 API 说明](references/api-search.md)
- [企业分析 API 说明](references/api-company.md)
- [市场分析 API 说明](references/api-market.md)
- [账户与自动注册说明](references/auto-register.md)
- [知了标讯 Skill 文档](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports applied search filters and amounts in 万元; contact details may be masked for trial accounts.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
