## Description:

企业信息精确查询。根据企业全名、注册号或统一社会信用代码精确匹配工商详情，返回法人、注册资本、经营范围、地址、主要人员、股东、分支机构、变更记录、经营异常。

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve detailed Chinese enterprise registration records by exact company name, registration number, or unified social credit code through the Juhe enterprise detail API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, registration numbers, or unified social credit codes are sent to Juhe during live lookups.

Mitigation: Use the skill only when sharing those identifiers with Juhe is acceptable for the user and organization.

Risk: The Juhe API key can be exposed if passed on the command line, embedded in URLs, or committed in a .env file.

Mitigation: Prefer the JUHE_ENTERPRISE_DETAIL_KEY environment variable and keep any local .env file out of version control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-detail)
- [Juhe enterprise detail API documentation](https://www.juhe.cn/docs/api/id/319)
- [Juhe API platform](https://www.juhe.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and formatted text or JSON lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a JUHE_ENTERPRISE_DETAIL_KEY API key; sends submitted company identifiers to Juhe for live lookup.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
