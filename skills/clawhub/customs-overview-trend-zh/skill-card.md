## Description:

查询进出口贸易趋势数据，按月份返回指定时间范围内的贸易总量趋势数据，并支持游标分页。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Trade analysts, supply-chain managers, and market researchers use this skill to query month-by-month import and export trade totals for a selected date range, compare trade trajectories, and identify seasonal patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an Upkuajing API key locally and may partially display credential material.

Mitigation: Use the skill only on trusted machines, restrict access to ~/.upkuajing/.env, and avoid sharing logs or screenshots that may expose credential fragments.

Risk: Trade-data queries use a paid API account and may create recharge payment URLs when requested.

Mitigation: Confirm pricing and user approval before chargeable queries or recharge flows, and use an account with appropriate spending controls.

Risk: The security summary flags under-disclosed version-check telemetry.

Mitigation: Review outbound network behavior before installing on shared or sensitive environments.

Risk: Diagnostic reports can include context about failed API calls.

Mitigation: Send error reports only after user confirmation and exclude secrets or private business data from diagnostic context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-trend-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer platform](https://developer.upkuajing.com/)
- [OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [国家贸易概览-进出口趋势 API 参考](references/customs-overview-trend-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with concise natural-language guidance and shell commands when execution is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and an UPKUAJING_API_KEY; query calls may return paginated monthly trade totals and fee information.]

## Skill Version(s):

1.0.1 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
