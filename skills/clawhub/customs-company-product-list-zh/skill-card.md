## Description:

查询公司海关贸易产品列表数据，获取产品名称的贸易次数、金额、数量和关联 HS 编码，支持外贸团队进行产品组合分析、市场分析和竞品追踪。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams and agents use this skill to retrieve paginated company-level customs product data from Upkuajing, including trade counts, amounts, quantities, weights, share percentages, and associated HS codes. It supports product portfolio review, market analysis, and competitor tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid customs-data API and may initiate billable product-list queries or recharge-order flows.

Mitigation: Confirm each billable query or recharge-order action before execution and consult the published pricing information when cost details are needed.

Risk: The API key may be stored in a local plaintext ~/.upkuajing/.env file.

Mitigation: Install only when this storage model is acceptable, restrict local file access, and avoid sharing the UPKUAJING_API_KEY value.

Risk: Optional error reports can include request context or payload details.

Mitigation: Review error-report content before submission and avoid including customer secrets, tokens, or sensitive raw payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-product-list-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [公司贸易产品列表 API 参考](references/customs-company-product-list-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; customs product-list calls are billable and return paginated JSON data with fee and request identifiers.]

## Skill Version(s):

1.0.1 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
