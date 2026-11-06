## Description:

Correlates Huawei Cloud AOM active and historical alarms for CCE operations and supports alarm rule and notification management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operations engineers use this skill to review Huawei Cloud AOM alarms for CCE clusters, group recurring or burst alarms, inspect alarm health, and manage alarm and notification rules with confirmation before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Alarm rule changes or notification rule deletion can affect monitoring coverage or notification paths.

Mitigation: Use a least-privilege hcloud profile, review each mutation preview and its dependent alarms, and require explicit user confirmation before applying changes.

Risk: Cluster filters may not remove unrelated records from every raw response.

Mitigation: Check cluster identifiers in returned records before using them to draw conclusions or plan changes.

## Reference(s):

- [Operation Guide](references/operation-guide.md)
- [Workflow](references/workflow.md)
- [Risk Rules](references/risk-rules.md)
- [Output Schema](references/output-schema.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [CCE Event List](references/cce-event-list.md)
- [CCE Prometheus Metric Alarms](references/cce-prometheus-metric-alarms.md)
- [Huawei Cloud CCE User Manual](https://support.huaweicloud.com/usermanual-cce/cce_10_0902.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Alarm correlation summaries and inspection findings, with structured JSON command results and mutation previews.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include grouped alarms, issues for follow-up, queried resources, or a preview of a proposed change.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
