## Description:

通过企业 ID 查询海关数据中的月度贸易趋势，按月返回交易次数、数量、重量和金额，并支持日期、产品、HS 编码、国家、贸易伙伴和港口等可选筛选条件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams, analysts, and supply-chain managers use this skill to inspect a company's monthly customs trade activity and identify procurement cycles, seasonal changes, supplier sales signals, and longer-term import/export trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read or store the Upkuajing API key in plaintext at ~/.upkuajing/.env.

Mitigation: Keep the API key private, prefer a protected environment variable when possible, and restrict access to the local .env file.

Risk: The workflow uses paid API calls and can create recharge payment links when requested.

Mitigation: Review pricing and require explicit user confirmation before chargeable lookups or recharge actions.

Risk: Optional error reports may include request context or customer-related details.

Mitigation: Review and redact secrets or sensitive customer data before submitting an error report.

Risk: The automatic version check contacts openapi.upkuajing.com.

Mitigation: Install and run the skill only in environments where that network contact is acceptable.

## Reference(s):

- [公司贸易趋势 API 参考](references/customs-company-trends-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [跨境魔方](https://www.upkuajing.com)
- [跨境魔方开放平台](https://developer.upkuajing.com/)
- [开放平台价格说明](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid API calls should be confirmed by the user before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
