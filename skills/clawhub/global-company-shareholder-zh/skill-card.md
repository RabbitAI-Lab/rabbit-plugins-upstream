## Description:

调取全球企业资料库查询股东信息以及实际受益所有人（Beneficial Owner），梳理企业股权架构、投资关联关系，协助销售、风控人员摸清企业真实管控背景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, investors, sales teams, and risk researchers use this skill to query company shareholder lists by company ID and review shareholder names, types, holding methods, holding percentages, and beneficial ownership context for due diligence and relationship analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an API key in ~/.upkuajing/.env.

Mitigation: Use a dedicated Upkuajing API account, protect the local credential file, and remove the key when the skill is no longer needed.

Risk: The skill can create recharge payment orders and query account balances.

Mitigation: Run account and recharge commands only after explicit user approval and with an account intended for paid API usage.

Risk: The shareholder lookup is a paid API call.

Mitigation: Confirm cost-bearing lookups with the user before execution and use the pricing command or pricing page for current rates.

Risk: Error reports may include request or response details.

Mitigation: Submit error reports only after user confirmation and avoid including sensitive request or response content.

Risk: The skill performs provider version-check requests with local cache writes.

Mitigation: Review this network behavior before installation in restricted environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-shareholder-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [全球企业库股东列表 API 参考](references/company-shareholder-list-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and concise natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; shareholder lookup responses include fee and requestId fields when available.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
