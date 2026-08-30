## Description:

Queries U.S. import trade statistics by state or city from Upkuajing customs data, including import record counts, container counts, recent 90-day activity, and cursor pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade teams, logistics analysts, and developers use this skill to inspect U.S. import activity by state or city, monitor container-flow patterns, and evaluate market-entry signals from customs-derived data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid Upkuajing API account and can create recharge or payment links.

Mitigation: Confirm paid queries and any recharge action with the user before execution, and review payment links before opening or sharing them.

Risk: The API key may be stored in plaintext in ~/.upkuajing/.env.

Mitigation: Avoid printing or sharing raw .env contents, prefer environment variables when possible, and restrict local file access to trusted users.

Risk: Optional diagnostic reports may send request context to the provider.

Mitigation: Submit error reports only after user approval and avoid including secrets or unnecessary sensitive context.

Risk: The skill performs a provider version check during API request flow.

Mitigation: Review outbound network behavior during installation and account for the version-check call in environments with strict egress controls.

## Reference(s):

- [国家贸易概览-美国进口交易 API 参考](references/customs-overview-us-import-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-us-import-zh)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; paid query calls return fee details and may use cursor pagination.]

## Skill Version(s):

1.0.1 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
