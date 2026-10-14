## Description:

按需查询中国企业的工商基本信息、股东、分支机构、对外投资和变更记录，并可补充招投标战绩。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

用户及企业分析人员可核验中国企业登记信息，按需查看股东、分支机构、投资和变更记录；查询会消耗平台积分。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contains hidden, behavior-affecting request and account instructions.

Mitigation: Review the hidden comment blocks and account instructions before installation.

Risk: The skill uses an API key and may store it in ~/.zlbx/config.json.

Mitigation: Prefer setting your own API key manually and protect the local credential file.

Risk: Automatic registration contacts zhiliaobiaoxun.com and sends a hashed MAC-derived device identifier.

Mitigation: Obtain informed user consent before auto-registration, or configure an API key to avoid device registration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/zlbx-company-registry)
- [Company registry skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill/company-registry)
- [API quick reference](artifact/references/api-quick.md)
- [Registration and credential setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Markdown summary or table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports source and available update time; limits results to requested queries and pages.]

## Skill Version(s):

1.0.2 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
