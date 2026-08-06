## Description: <br>
Huawei Cloud CCE Metric Analyzer helps agents query and analyze CCE cluster, Kubernetes component, GPU, and ECS/ELB/EIP/NAT metrics with TopN rankings, status classification, and anomaly detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and cloud operations engineers use this skill to investigate Huawei Cloud CCE resource usage, component health, cloud resource metrics, and threshold-based anomalies before deciding on diagnosis or remediation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses broad Huawei Cloud and Kubernetes read access, including access paths that can inspect TLS Secrets and generate kubeconfig material. <br>
Mitigation: Install it with a least-privilege Huawei IAM user and Kubernetes RBAC limited to the documented read-only resources; avoid broad production or cluster-admin credentials. <br>
Risk: Credential material can be supplied through AK/SK parameters, environment variables, local profiles, and temporary security tokens. <br>
Mitigation: Prefer short-lived credentials, do not print or persist secrets, unset environment secrets after use, and rely on local hcloud profiles for normal cloud queries when possible. <br>
Risk: Ingress certificate checks require reading TLS Secret data. <br>
Mitigation: Set check_certificates=false unless TLS expiration status is specifically needed. <br>
Risk: Metric thresholds are operational signals and may not match every workload's SLOs. <br>
Mitigation: Treat critical and warning classifications as investigation leads, tune thresholds for the workload, and do not make automatic scaling or remediation decisions from this skill alone. <br>


## Reference(s): <br>
- [Workflow](references/workflow.md) <br>
- [Risk Rules](references/risk-rules.md) <br>
- [Output Schema](references/output-schema.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [kubectl-cce Usage](references/kubectl-cce.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with dispatcher command examples and JSON metric results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Time-bounded monitoring output with status classifications such as critical, warning, normal, and unknown.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
