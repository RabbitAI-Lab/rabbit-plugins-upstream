## Description:

将仓库方提供的 Excel 收费清单与 WMS OpenAPI 业务记录逐笔核对，帮助验证出库费、退件处理费、包装费、仓租费和销毁费是否有对应业务依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[vinlin1](https://clawhub.ai/user/vinlin1)

### License/Terms of Use:

MIT-0

## Use Case:

External warehouse operations, finance, and e-commerce teams use this skill to compare third-party warehouse billing spreadsheets against WMS records and produce exception reports for routine reconciliation or billing disputes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles WMS credentials and warehouse billing data.

Mitigation: Use a least-privilege or temporary API key where possible, avoid exposing command-line credentials, and store generated reports in a private directory.

Risk: The skill sends reconciliation queries to the configured WMS API endpoint.

Mitigation: Confirm the WMS base URL with the warehouse provider before running and use the skill only for the intended WMS billing reconciliation workflow.

Risk: Generated JSON, HTML, and marked Excel outputs may contain sensitive operational or billing details.

Mitigation: Treat all generated reconciliation files as sensitive business records and review findings against source WMS data before acting on disputes.

## Reference(s):

- [WMS OpenAPI 接口参考](artifact/references/wms_api_reference.md)
- [WMS仓库收费对账 on ClawHub](https://clawhub.ai/vinlin1/skills/wms-reconciliation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands; generated reconciliation outputs may include HTML, JSON, and optionally marked Excel files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Excel billing file, WMS base URL, AppKey/AppSecret, warehouse ID, and reconciliation date range.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
