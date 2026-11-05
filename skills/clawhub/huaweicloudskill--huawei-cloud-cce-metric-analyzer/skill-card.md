## Description:

Huawei Cloud CCE Metric analysis skill using the Python dispatcher with hcloud-backed cloud service queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to query Huawei Cloud CCE, Kubernetes component, and related ECS, ELB, EIP, and NAT metrics. It summarizes resource usage, trends, and threshold-based anomalies for investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-bearing process arguments may expose cloud credentials.

Mitigation: Use short-lived, least-privilege credentials and avoid passing secrets in command arguments; use a local hcloud profile where supported.

Risk: The separately downloaded kubectl-cce plugin release could not be verified.

Mitigation: Review the plugin before use and obtain it from a trusted build or authenticated release.

Risk: Kubernetes TLS Secret reads and temporary kubeconfig files can expose sensitive material or persist after abrupt termination.

Mitigation: Restrict Secret access to intended namespaces and remove temporary kubeconfig files after use; keep certificate verification enabled unless disabling it is necessary.

## Reference(s):

- [Metric query workflow](artifact/references/workflow.md)
- [Metric output schema](artifact/references/output-schema.md)
- [Risk rules](artifact/references/risk-rules.md)
- [IAM policies and Kubernetes RBAC](artifact/references/iam-policies.md)
- [CLI installation guide](artifact/references/cli-installation-guide.md)
- [kubectl-cce setup instructions](artifact/references/kubectl-cce.md)
- [kubectl-cce-plugin release archive](https://github.com/pancake0001/kubectl-cce-plugin/releases/download/v0.1.0/kubectl-cce_0.1.0_linux_amd64.tar.gz)
- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cce-metric-analyzer)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Metric summaries with status classifications, anomaly findings, and structured JSON time-series results where applicable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only metric analysis; query windows are time-bounded.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
