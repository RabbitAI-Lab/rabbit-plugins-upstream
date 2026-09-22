## Description:

Huawei Cloud AOM alarm correlation and alarm-rule management skill for CCE operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to query and correlate Huawei Cloud AOM alarms for CCE clusters, inspect alarm health, and manage AOM alarm and notification rules through preview-and-confirm workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Alarm and notification rule mutations can change monitoring coverage or remove protections in a Huawei Cloud account.

Mitigation: Use read-only commands first, review preview output for affected resources and impact, and only add confirm=true after explicit user approval.

Risk: Overbroad cloud credentials can expand the impact of an unintended rule-management action.

Mitigation: Use a least-privilege hcloud profile scoped to the intended AOM, CCE, and notification-rule operations.

Risk: Cloud credentials or tokens could be exposed through command output, logs, or generated files.

Mitigation: Do not print, persist, or include AK/SK, tokens, credential-derived secrets, or complete sensitive logs in responses.

Risk: A current-only alarm query can miss recently recovered incidents.

Mitigation: Cross-reference active and historical alarms before concluding that a CCE alarm condition has cleared.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cce-alarm-correlation-engine)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Operation Guide](references/operation-guide.md)
- [Risk Rules](references/risk-rules.md)
- [Output Schema](references/output-schema.md)
- [Workflow](references/workflow.md)
- [CCE Event List](references/cce-event-list.md)
- [CCE Alarm Center Prometheus Metric Alarm Reference](references/cce-prometheus-metric-alarms.md)
- [Huawei Cloud CCE Event Documentation](https://support.huaweicloud.com/usermanual-cce/cce_10_0902.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with dispatcher command examples and JSON-shaped alarm correlation outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes preview and confirmation states for mutation workflows; outputs should not expose credentials or sensitive logs.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
