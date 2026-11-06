## Description:

Queries and analyzes Huawei Cloud CCE Pod and Node metrics plus ECS, ELB, EIP, and NAT resource metrics, with threshold-based anomaly detection and status classification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inspect Huawei Cloud CCE cluster and cloud resource metrics, rank high-usage resources, and identify threshold-based anomalies before choosing a follow-up diagnosis or remediation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged dispatcher exposes cloud and Kubernetes administration, deletion, remediation, and secret-reading capabilities beyond the advertised metric analysis workflow.

Mitigation: Review the callable action surface before deployment and grant only tightly scoped test credentials until those capabilities are removed, separated, or documented accurately.

Risk: Metric outputs and related Kubernetes or cloud lookups may expose production pod names, node IPs, cluster IDs, or other operational identifiers.

Mitigation: Redact sensitive resource identifiers in shared summaries and avoid granting permissions that allow secret data to be returned.

Risk: Predefined utilization thresholds may not match workload-specific service objectives.

Mitigation: Use threshold results as triage signals and confirm findings against workload SLOs before taking operational action.

## Reference(s):

- [Workflow](references/workflow.md)
- [Risk Rules](references/risk-rules.md)
- [Output Schema](references/output-schema.md)
- [ClawHub Skill Page](https://clawhub.ai/pintudeyudi/skills/huawei-cloud-cce-metric-analyzer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON metric outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Metric results may include cloud resource identifiers, time-series values, status classifications, and anomaly summaries.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
