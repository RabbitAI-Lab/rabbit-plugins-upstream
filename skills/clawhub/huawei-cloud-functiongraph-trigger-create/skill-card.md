## Description:

Creates and configures scheduled TIMER triggers for Huawei Cloud FunctionGraph functions using Quartz Cron or Rate schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to create, validate, and verify scheduled Huawei Cloud FunctionGraph triggers for periodic workloads such as backups, monitoring, notifications, and timed data processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Huawei Cloud credentials and permissions that can create FunctionGraph triggers.

Mitigation: Use least-privilege, preferably temporary credentials; keep AK/SK values out of shared terminals, logs, and committed files.

Risk: Created schedules can persist and invoke functions automatically, which may cause unwanted executions or cost.

Mitigation: Verify the function URN, region, and schedule before execution; create triggers as DISABLED for testing; monitor initial runs and remove test triggers.

Risk: The artifact includes troubleshooting guidance that disables SSL certificate verification.

Mitigation: Keep TLS certificate verification enabled and fix certificate, SDK, or environment issues instead of bypassing verification.

## Reference(s):

- [SDK Installation Guide](references/sdk-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Cron Expression Reference](references/cron-reference.md)
- [Huawei Cloud IAM Policy Syntax](https://support.huaweicloud.com/usermanual-iam/iam_01_001.html)
- [Huawei Cloud FunctionGraph Permissions](https://support.huaweicloud.com/productdesc-functiongraph/functiongraph_01_0024.html)
- [Huawei Cloud FunctionGraph Trigger Management](https://support.huaweicloud.com/api-functiongraph/FunctionGraph_06_0123.html)
- [Huawei Cloud FunctionGraph Console Guide](https://support.huaweicloud.com/usermanual-functiongraph/functiongraph_01_0100.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash and Python snippets plus JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of Huawei Cloud FunctionGraph TIMER triggers when the bundled Python script or generated commands are run with cloud credentials.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
