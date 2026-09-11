## Description:

查询企业限制高消费信息，根据企业名称、统一社会信用代码、工商注册号或申请人调用聚合数据 API，并返回案号、执行法院、立案时间、案件状态、关联人、申请人及限令正文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check whether a Chinese enterprise has court-issued consumption restriction records by enterprise name, unified social credit code, business registration number, or applicant. It formats Juhe API results into a concise case summary with current or historical disclosure status, court, filing time, related person, applicant, publication and update dates, and optional order text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed if passed on the command line or committed in scripts/.env.

Mitigation: Use a host-managed JUHE_ENTERPRISE_RESTRICTION_KEY environment variable and keep local .env files out of shared or version-controlled directories.

Risk: Enterprise, applicant, case, and related lookup data is sent to Juhe for paid API queries.

Mitigation: Install and use the skill only when this third-party data transfer and billing model are acceptable for the user's workflow.

Risk: Restriction status may include historical records that are no longer publicly disclosed.

Mitigation: Choose the historical-data option intentionally and label results as current disclosure or historical/non-disclosed records when presenting them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-restriction)
- [Juhe enterprise restriction API documentation](https://www.juhe.cn/docs/api/id/836)
- [Juhe API endpoint](https://apis.juhe.cn/api_credit/query836)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and plain-text Chinese query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JUHE_ENTERPRISE_RESTRICTION_KEY. Query data is sent to Juhe for paid API lookup.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
