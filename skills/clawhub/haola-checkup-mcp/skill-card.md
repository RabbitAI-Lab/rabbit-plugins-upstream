## Description:

协助企业按人均预算获取员工体检分档方案与报价，并查询体检门店、常见问题和商务咨询渠道。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryanbihai](https://clawhub.ai/user/ryanbihai)

### License/Terms of Use:

MIT-0

## Use Case:

企业采购人员和员工可获取分档体检报价、查询合作门店与体检常见问题，并按需提交企业商务咨询。

### Deployment Geography for Use:

China (service describes coverage across 241 cities)

## Known Risks and Mitigations:

Risk: Quote inputs, clinic queries and any corporate inquiry details are sent to Haola's remote service.

Mitigation: Share only information needed for the request; submit a contact name and phone number only when the business wants follow-up.

Risk: Authenticated account features can create or manage reservations, orders or patient-related records.

Mitigation: Use logged-in features only when the user intends those actions, and avoid including account credentials in the skill package.

## Reference(s):

- [好啦体检方案 MCP 服务介绍](https://www.ihaola.com.cn/html/mcp-quote.html)
- [ClawHub skill release](https://clawhub.ai/ryanbihai/skills/haola-checkup-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Text or Markdown summaries of structured service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotation tiers can include itemized prices and plan IDs; clinic queries can include locations.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
