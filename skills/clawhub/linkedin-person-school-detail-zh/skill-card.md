## Description:

从 LinkedIn 数据按学校 ID 查询学校名称、类型、地理位置、网站与社媒链接等详细信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, researchers, and analysts can use this skill to verify education institutions, enrich school records, and support education-history or academic-network analysis. It requires a school ID, typically obtained from related education-history or alumni lookup skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or use a UPKUAJING API key and store it in plaintext under ~/.upkuajing/.env.

Mitigation: Use a dedicated key, restrict local file permissions, avoid shared machines, and rotate the key if exposure is suspected.

Risk: School-detail lookups are paid API calls and the helper scripts can assist with recharge or payment-order flows.

Mitigation: Confirm pricing and account balance first, and require separate explicit user approval before running any paid lookup or recharge action.

Risk: Error reports may include request parameters, response data, or context supplied by the agent.

Mitigation: Ask for user confirmation before reporting and redact sensitive or unnecessary personal data from error-report payloads.

Risk: The skill contacts the provider for lookups and version checks.

Mitigation: Tell users when requests will be sent to the provider and avoid submitting data that is not required for the school-detail lookup.

## Reference(s):

- [LinkedIn 学校详情 API 参考](references/linkedin-school-detail-api.md)
- [Agent调用Skill异常上报 API 参考](references/skill-error-report-api.md)
- [ClawHub skill listing](https://clawhub.ai/upkuajing/skills/linkedin-person-school-detail-zh)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a single school-detail lookup result per request, including fee information and request ID when the provider response includes them.]

## Skill Version(s):

1.0.5 (source: release evidence, frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
