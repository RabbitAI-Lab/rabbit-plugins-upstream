## Description:

根据招投标记录生成单家公司背调或双公司对比报告，梳理业务、客户与供应商、中标表现、竞争格局及公开风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

采购、销售及合作评估人员可用公司名称或公司链接生成招投标视角的企业背景报告，也可比较两家公司；公开风险信息仅供核验，不替代正式尽调。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries use an external service and can consume account credits.

Mitigation: Review the provider and expected credit cost before running a report; monitor account usage.

Risk: Optional trial registration sends a hashed device identifier to the provider.

Mitigation: Preconfigure ZLBX_API_KEY to skip registration, or consent explicitly before enrolling.

Risk: An API key and generated reports can remain on the local device.

Mitigation: Protect the key and periodically review or remove ~/.zlbx/config.json and ~/zlbx-company-intel-files/.

Risk: Shared reports may contain signed links that grant access to source records.

Mitigation: Check reports for sk-signed links before forwarding them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/company-background-check)
- [API quick reference](references/api-quick.md)
- [Background-check workflow](references/workflow.md)
- [Report templates](references/report-template.md)
- [Trial registration and account setup](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML report]

**Output Format:** [Conversational Markdown report and optional shareable HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-company or two-company comparison; cites source records and can include signed access links.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
