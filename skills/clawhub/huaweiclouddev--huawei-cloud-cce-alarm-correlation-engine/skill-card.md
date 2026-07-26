## Description: <br>
Huawei Cloud AOM alarm correlation and alarm-rule management skill for CCE operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to query and correlate Huawei Cloud AOM alarms for CCE clusters, inspect alarm health, and manage alarm or notification rules with confirmation controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Alarm rule or notification rule changes can reduce observability or remove monitoring coverage. <br>
Mitigation: Review mutation previews, affected resources, and expected impact before setting confirm=true, especially for disable, delete, and cleanup actions. <br>
Risk: Cloud credentials or credential-derived secrets could be exposed in prompts, commands, logs, or responses. <br>
Mitigation: Use a least-privilege Huawei Cloud profile, prefer read-only access for inspection, and do not share AK/SK values or tokens in chat or logs. <br>
Risk: A lack of active alarms can hide recent or recovered incidents. <br>
Mitigation: Correlate active and historical alarms before concluding that a CCE alarm condition is resolved or absent. <br>


## Reference(s): <br>
- [Workflow](references/workflow.md) <br>
- [Risk Rules](references/risk-rules.md) <br>
- [Output Schema](references/output-schema.md) <br>
- [Operation Guide](references/operation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [CCE Prometheus Metric Alarms](references/cce-prometheus-metric-alarms.md) <br>
- [CCE Event List](references/cce-event-list.md) <br>
- [Huawei Cloud CCE Alarm Documentation](https://support.huaweicloud.com/usermanual-cce/cce_10_0902.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with dispatcher shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include alarm summaries, grouped findings, timelines, likely related resources, mutation previews, and confirmation requirements.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
