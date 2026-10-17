## Description:

Queries Huawei Cloud MaaS aggregate token usage, request counts, and errors for preset services, user services, or custom endpoints over a selected time range.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to review Huawei Cloud MaaS token consumption, request volume, and error rates for a selected service and period.

### Deployment Geography for Use:

Global; MaaS statistics queries are limited to Huawei Cloud region cn-southwest-2.

## Known Risks and Mitigations:

Risk: Cloud access keys or a local credentials file may be exposed when configuring usage queries.

Mitigation: Use least-privilege or temporary credentials; do not paste keys into chat, keep credential files outside repositories with restrictive permissions, and rotate exposed keys.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-maas-tokens-usage)
- [MaaS usage query workflow](artifact/references/task-query-tokens-usage.md)
- [MaaS metrics](artifact/references/maas-metrics.md)
- [IAM permissions](artifact/references/iam-policies.md)
- [Security design](artifact/references/security-design.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Usage summary and metric table; optional raw API response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports total, prompt, and completion tokens, requests, errors, error rate, and queried period.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
