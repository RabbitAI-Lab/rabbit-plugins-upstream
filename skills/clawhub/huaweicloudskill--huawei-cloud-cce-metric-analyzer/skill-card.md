## Description:

Queries and analyzes Huawei Cloud CCE cluster metrics and ECS, ELB, EIP, and NAT resource metrics with threshold status classification and anomaly detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and cloud operations teams use this skill to inspect Huawei Cloud CCE, AOM, and related cloud resource metrics, rank resource usage, and identify threshold-based anomalies before choosing follow-up diagnosis or remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads sensitive operational metadata from Huawei Cloud and Kubernetes environments.

Mitigation: Run it with least-privilege Huawei Cloud credentials and Kubernetes RBAC, and redact credentials, cluster IDs, node IPs, and workload identifiers from shared outputs.

Risk: Ingress certificate checks read TLS Secret references, and kubectl access may generate a temporary kubeconfig.

Mitigation: Limit Kubernetes permissions to the documented read-only paths and review the kubectl-cce plugin before installing or using it.

Risk: Monitoring gaps can produce empty or incomplete series when AOM Prometheus, ServiceMonitors, or PodMonitors are not configured.

Mitigation: Verify monitoring prerequisites before relying on results, and treat missing data as unknown rather than proof of healthy resources.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cce-metric-analyzer)
- [Workflow](references/workflow.md)
- [Risk Rules](references/risk-rules.md)
- [Output Schema](references/output-schema.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [kubectl-cce Usage](references/kubectl-cce.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with dispatcher shell commands and JSON metric outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-only metric summaries, status classifications, TopN rankings, and anomaly findings.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
