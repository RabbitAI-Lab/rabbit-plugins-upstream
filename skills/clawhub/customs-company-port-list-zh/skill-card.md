## Description:

查询公司海关贸易港口列表数据，获取港口的贸易次数、金额和占比，用于物流分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade and logistics teams use this skill to query a company's customs trade port distribution and inspect port-level trade counts, value, quantity, weight, and percentage share for supply-chain route analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to an Upkuajing API key and may store the key in ~/.upkuajing/.env.

Mitigation: Install and run it only in an environment where storing that API key is acceptable, and restrict access to the local credential file.

Risk: Company port-list queries are paid API calls.

Mitigation: Confirm the cost-bearing action before execution and use the pricing endpoint or published pricing page instead of estimating fees.

Risk: Recharge flows can return payment URLs.

Mitigation: Review the URL and payment context before opening it or approving payment.

Risk: Diagnostic error reports may include operational request context.

Mitigation: Send error reports only after user confirmation and review the report context for sensitive or unnecessary details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-port-list-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [跨境魔方开放平台](https://developer.upkuajing.com/)
- [公司贸易港口列表 API 参考](references/customs-company-port-list-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; query calls are paid and return paginated port records plus fee and request identifiers.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
