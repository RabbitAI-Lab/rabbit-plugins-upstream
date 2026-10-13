## Description:

查询中国企业工商登记信息、股东、分支机构、对外投资及变更记录，并按需补充招投标战绩。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

企业核验人员及其他用户可按需查询企业身份、经营状态、股东出资、分支机构、对外投资和工商变更；招投标记录仅在需要时补充。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lookup queries are sent to zhiliaobiaoxun.com services.

Mitigation: Use the integration only when comfortable sharing the queried company with the provider.

Risk: First-use registration sends limited device characteristics to the provider.

Mitigation: Obtain user consent first; supply an API key manually to avoid automatic registration.

Risk: A locally stored API key may be exposed if its configuration file is shared.

Mitigation: Protect ~/.zlbx/config.json as a credential and avoid sharing its contents.

Risk: Paid queries and extra pages consume account credits.

Mitigation: Explain costs and request only the searches and pages the user needs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/zlbx-company-registry)
- [Company registry documentation](https://ai.zhiliaobiaoxun.com/docs/skill/company-registry)
- [API quick reference](references/api-quick.md)
- [Registration and credential guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Concise Markdown summaries or tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source dates, pagination details and links; unavailable fields are omitted.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
