## Description:

Huawei Cloud AOM alarm correlation analysis skill for CCE operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to query Huawei Cloud AOM active and historical alarms, correlate CCE alarm signals, inspect cluster alarm health, and prepare or manage AOM alarm rules with confirmation controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the package exposes broader Huawei Cloud and Kubernetes administration behavior than the alarm-correlation description discloses, including secret-reading and infrastructure-changing actions.

Mitigation: Install only in a tightly restricted test environment or after the publisher removes the undeclared dispatcher actions and secret-return paths.

Risk: Broad Huawei Cloud or Kubernetes credentials could permit access beyond documented AOM alarm workflows.

Mitigation: Use a dedicated least-privilege identity limited to the documented AOM actions; do not use broad production credentials.

Risk: Command output or logs may expose sensitive cluster data.

Mitigation: Assume outputs are sensitive, avoid sharing raw logs, and verify that AK/SK, tokens, and other secrets are not included in responses.

Risk: Alarm rule creation, update, delete, enable, disable, and action-rule deletion can affect alerting coverage or notification behavior.

Mitigation: Use the documented preview-first workflow and execute mutations only after explicit confirmation with `confirm=true`.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pintudeyudi/skills/huawei-cloud-cce-alarm-correlation-engine)
- [Workflow](references/workflow.md)
- [Risk Rules](references/risk-rules.md)
- [Output Schema](references/output-schema.md)
- [CCE Event List](references/cce-event-list.md)
- [CCE Alarm Center Prometheus Metric Alarm Reference](references/cce-prometheus-metric-alarms.md)
- [Huawei Cloud CCE user manual event reference](https://support.huaweicloud.com/usermanual-cce/cce_10_0902.html)
- [Huawei Cloud API Explorer](https://support.huaweicloud.com/apiexplorer/index.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON alarm summaries and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alarm grouping, severity counts, timelines, related resources, and recommended next diagnostic skills; sensitive credentials must not be exposed.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
