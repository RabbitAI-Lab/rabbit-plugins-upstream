## Description:

Estimates pre-purchase Huawei Cloud resource prices for monthly or annual plans and on-demand usage using read-only pricing queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud cost planners use this skill to compare Huawei Cloud resource specifications and estimate pre-purchase period or on-demand costs. It presents itemized CNY quotes from current pricing responses, not final bills.

### Deployment Geography for Use:

Huawei Cloud regions supported by the pricing service; pricing queries use the cn-north-1 endpoint.

## Known Risks and Mitigations:

Risk: The helper may collect local agent session metadata and transmit execution telemetry outside the pricing task.

Mitigation: Review or remove the quality-reporting helper when only local pricing queries are needed; otherwise disable reporting with SKILL_QUALITY_DISABLE=1 and avoid injecting SESSION_ID or .quality_report.json.

Risk: Pricing access with unnecessarily broad Huawei Cloud permissions could expose account information.

Mitigation: Use a low-privilege account limited to read-only pricing and IAM lookups; configure credentials locally rather than sharing them in chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cost-estimation)
- [Period pricing API documentation](https://support.huaweicloud.com/api-bpconsole/bcloud_01002.html)
- [On-demand pricing API documentation](https://support.huaweicloud.com/api-bpconsole/bcloud_01001.html)
- [CLI installation and authentication guide](references/cli-installation-guide.md)
- [Read-only IAM policies](references/iam-policies.md)
- [Quote verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text with itemized prices and totals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CNY estimates; discounted prices only when returned; marked as non-final bills.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
