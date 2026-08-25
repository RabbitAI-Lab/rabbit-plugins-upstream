## Description:

客服会话质检技能。批量分析客服聊天记录/会话导出文件（支持企业微信、千牛、美洽、Udesk、智齿等系统的逐条式与整段式导出），按可配置的质检规则逐条评分，自动脱敏，生成带扣分明细和待人工复核清单的质检报告表格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zenobiazizi](https://clawhub.ai/user/zenobiazizi)

### License/Terms of Use:

MIT-0

## Use Case:

Customer service supervisors, quality inspectors, and operations teams use this skill to review Chinese customer-service conversation exports, apply configurable quality rules, mask sensitive data, and produce reports with deduction evidence and manual-review items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports an automatic plaintext tracking call to a hard-coded external IP address before processing.

Mitigation: Review before installing and remove or disable the tracking step before using the skill with sensitive customer conversations.

Risk: The security scan verdict is suspicious despite the core QC behavior appearing mostly local.

Mitigation: Administrators should scan and review the skill before deployment and confirm that outbound network behavior matches their data-handling requirements.

## Reference(s):

- [README](README.md)
- [Default QC Rules](references/rules-default.md)
- [Custom Rules Guide](references/rules-guide.md)
- [Sample Report](examples/sample-report.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown report or Excel-style report with scored details, deduction evidence, and manual-review lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Masks sensitive customer data in outputs and keeps low-confidence findings in a manual-review list.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
