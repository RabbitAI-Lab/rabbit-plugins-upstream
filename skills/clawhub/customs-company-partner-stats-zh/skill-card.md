## Description:

调取海关进出口数据分析企业贸易伙伴分布情况，获取 HS 编码明细、产品品类分布以及月度交易时间，梳理合作客商结构，辅助外贸人员筛选优质供应商与潜在采购商。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams, procurement agents, and analysts use this skill to retrieve customs trade-partner structure for a company ID, including HS code distribution, product distribution, and monthly trade activity. It supports partner identification, product portfolio analysis, and trade network intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid customs API calls can consume the user's Upkuajing account balance.

Mitigation: Tell the user a query may incur charges and wait for an explicit confirmation before running paid calls.

Risk: The API key may be stored in plaintext in ~/.upkuajing/.env.

Mitigation: Treat the file as sensitive, restrict local access, and avoid sharing the key in prompts, logs, or reports.

Risk: Error reports may include request context or business data.

Mitigation: Ask for confirmation before reporting errors and avoid sending secrets or unnecessary private business details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-partner-stats-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Company partner stats API reference](references/customs-company-partner-stats-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)
- [Upkuajing API pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid queries return fee and requestId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
