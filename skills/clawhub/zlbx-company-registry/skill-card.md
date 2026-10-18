## Description:

查询中国企业工商基本信息、股东与出资记录、分支机构、对外投资和工商变更，并可按需补充招投标信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts can verify Chinese company registration details and review shareholders, branches, investments, and corporate changes, with optional procurement history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lookup requests are sent to Zhiliaobiaoxun.

Mitigation: Confirm that sending the queried company details to the service is acceptable before use.

Risk: Optional automatic registration sends device characteristics, including a hashed MAC address.

Mitigation: Ask for user consent before registration, or provide an existing ZLBX_API_KEY to skip it.

Risk: Automatic registration can save an API key locally in ~/.zlbx/config.json.

Mitigation: Protect or remove the saved credential when it is no longer needed.

Risk: Additional queries and result pages can consume account credits.

Mitigation: Request only the needed endpoints and pages, and explain additional credit costs before expanding the search.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/zlbx-company-registry)
- [Company registry skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill/company-registry)
- [API quick reference](artifact/references/api-quick.md)
- [Optional registration and credential handling](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Markdown summaries or tables of company records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports source and query scope; paginated records and optional procurement results appear only when requested.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
