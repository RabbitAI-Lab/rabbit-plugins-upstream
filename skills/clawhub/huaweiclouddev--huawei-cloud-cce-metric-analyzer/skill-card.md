## Description: <br>
Analyzes Huawei Cloud CCE, AOM, and related cloud-resource metrics through a Python dispatcher for read-only observability and anomaly review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations teams use this skill to query Huawei Cloud CCE Pod, Node, control-plane, add-on, and cloud-resource metrics, rank resource usage, and identify threshold-based anomalies. It is intended for read-only investigation and handoff to diagnosis or remediation workflows when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires read-only Huawei Cloud and Kubernetes permissions that can include cluster access setup and TLS Secret reads. <br>
Mitigation: Use a dedicated least-privilege IAM user and Kubernetes RBAC role, and set check_certificates=false unless certificate-expiration checks are needed. <br>
Risk: The skill handles cloud credentials and Kubernetes access material while querying AOM, hcloud, and kubectl paths. <br>
Mitigation: Avoid production-wide credentials, prefer scoped credentials, never print AK/SK or tokens, and verify the kubectl-cce plugin before use. <br>
Risk: Metric results may be incomplete when AOM Prometheus integration or component monitors are not enabled, and built-in thresholds may not match workload SLOs. <br>
Mitigation: Confirm AOM and required ServiceMonitor or PodMonitor coverage, keep queries time-bounded, and treat threshold status as an investigation lead rather than an automatic remediation trigger. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cce-metric-analyzer) <br>
- [Workflow](references/workflow.md) <br>
- [Risk Rules](references/risk-rules.md) <br>
- [Output Schema](references/output-schema.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [kubectl-cce Usage](references/kubectl-cce.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline dispatcher commands and JSON metric results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Metric outputs include status classifications, time-bounded query results, and anomaly summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
