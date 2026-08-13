## Description:

Queries Huawei Cloud BSS account balances, outstanding debt, and account change records over a configurable time window using the official Huawei Cloud BSS SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operations engineers, and finance operations users use this skill to check Huawei Cloud cash or credit balances, debt, and recent recharge, consumption, refund, and adjustment records before renewals, deployments, or reconciliation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically sends billing-query inputs and results to a separate telemetry endpoint by default.

Mitigation: Review the telemetry behavior before installation and set SKILL_QUALITY_DISABLE=1 unless sending billing-query metadata and results to the configured endpoint is explicitly approved.

Risk: Huawei Cloud AK/SK credentials and billing information are sensitive.

Mitigation: Use least-privilege credentials limited to bss:balance:view and bss:bill:view, and do not paste, echo, print, or hardcode AK/SK values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-bss-account-balance)
- [IAM Permission Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [BSS Account Balance API Reference](references/bss-account-balance-api.md)
- [Huawei Cloud BSS endpoint](https://bss.myhuaweicloud.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration guidance]

**Output Format:** [JSON with Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud BSS results may include billing balances, debt, and account-change records.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
