## Description:

供应商资质与履约能力核查助手，基于招投标数据帮助用户审查供应商资质、评估履约能力、核验业绩真实性，并支持单公司深度报告和两家候选供应商对比。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, bid managers, and agent users use this skill to investigate a company's supplier qualifications, public bidding history, customers, competitors, and visible risk signals before supplier onboarding or comparison decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a local API key and store credentials locally.

Mitigation: Prefer preconfiguring ZLBX_API_KEY, avoid exposing credentials in chat, and review local credential storage before installation.

Risk: Free signup may send a hashed device identifier for quota deduplication.

Mitigation: Use the automatic signup path only after explicit user consent, or skip it by providing an existing ZLBX_API_KEY.

Risk: Generated reports and returned platform links may contain sensitive commercial context or signed access parameters.

Mitigation: Treat reports and links as sensitive, store them in an access-controlled location, and avoid forwarding them beyond intended recipients.

Risk: The security verdict is suspicious.

Mitigation: Review the security summary and vendor behavior before deployment, and install only in environments where the API, local file output, and credential behavior are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/supplier-qualification-checker)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow reference](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-register flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with optional self-contained HTML report files and concise guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include locally saved report files, platform links returned by the service, and account or quota guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
