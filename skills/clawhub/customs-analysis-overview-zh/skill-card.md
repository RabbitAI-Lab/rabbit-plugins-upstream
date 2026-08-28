## Description:

按国家维度查询指定 HS 编码相关海关贸易概览数据，返回供应商和采购商数量汇总并支持游标分页。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Trade analysts, market researchers, and import/export operators use this skill to compare supplier and buyer presence by country for customs-market overview analysis and target-market planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a vendor API key in a plaintext home-directory .env file.

Mitigation: Use a dedicated API key, keep ~/.upkuajing/.env private, and rotate the key if it may have been exposed.

Risk: Normal query and recharge workflows can create paid vendor API activity.

Mitigation: Confirm pricing and obtain explicit user approval before billable calls or recharge-order creation.

Risk: Optional diagnostic error reports can send request context to the vendor.

Mitigation: Review report contents before submission and omit sensitive trade data or credentials from diagnostic context.

Risk: The implementation performs a vendor version-check side effect during API request handling.

Mitigation: Install and run only in environments where outbound version-check traffic to the vendor is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-overview-zh)
- [跨境魔方 Homepage](https://www.upkuajing.com)
- [跨境魔方 Developer Platform](https://developer.upkuajing.com/)
- [OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [分析报告-概览 API 参考](references/customs-analysis-overview-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with concise natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns paginated country-level supplier and buyer counts with fee and requestId metadata.]

## Skill Version(s):

1.0.1 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
