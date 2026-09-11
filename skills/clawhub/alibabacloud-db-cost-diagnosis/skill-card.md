## Description:

Provides read-only cost diagnostics and audits for Alibaba Cloud database products, including bill breakdowns, cost trend anomalies, renewal and expiry risk, idle instances, and optional paid feature attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, cloud operations teams, and FinOps users use this skill to investigate Alibaba Cloud database bills, explain cost spikes, and run read-only audits for renewal, idle capacity, and paid-feature charges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The renewal audit can pull and display account-wide Alibaba Cloud order history beyond database and RDS costs.

Mitigation: Install with a least-privilege Alibaba Cloud RAM identity, review the RAM policy before attaching it, remove unused permissions where possible, and share generated reports only with recipients allowed to see broader billing history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-db-cost-diagnosis)
- [Module 1: Bill & Cost Trend Query Orchestration](references/module1_cost_query.md)
- [Module 2: Customer-Facing Cost FAQ](references/module2_cost_faq.md)
- [Module 3: Cost Audit Orchestration](references/module3_cost_audit.md)
- [Minimal Read-Only RAM Policy](references/ram-policies.md)
- [Alibaba Cloud RDS billing overview](https://help.aliyun.com/zh/rds/product-overview/billing-overview)
- [Alibaba Cloud RDS billing FAQ](https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/billing-faq)
- [Alibaba Cloud DBS backup fees](https://help.aliyun.com/zh/dms/product-overview/backup-fees)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline shell commands; bundled scripts can also emit JSON summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics; conclusions must be grounded in returned billing and monitoring data.]

## Skill Version(s):

0.0.1 (source: server release metadata and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
