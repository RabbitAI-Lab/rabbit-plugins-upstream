## Description:

Helps create and configure scheduled TIMER triggers for Huawei Cloud FunctionGraph functions using Quartz Cron expressions or fixed rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to schedule existing Huawei Cloud FunctionGraph functions, configure timer triggers, and check creation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad credentials or IAM permissions could affect unintended functions or regions.

Mitigation: Use temporary credentials and scope IAM permissions to the intended region, project and function; avoid wildcard or delete permissions unless needed.

Risk: Frequent schedules or testing against production triggers could cause unwanted invocations or disruption.

Mitigation: Confirm the target resource and schedule before creation; avoid one-minute test schedules and cleanup deletes on production triggers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-functiongraph-trigger-create)
- [Cron Expression Reference](artifact/references/cron-reference.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [SDK Installation Guide](artifact/references/sdk-installation-guide.md)
- [Verification Method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown instructions and commands; JSON trigger-creation status when the script runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes trigger identifier, schedule and enabled status on success, or an error code on failure.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
