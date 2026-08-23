## Description:

Query and analyze Kubernetes Events in Huawei Cloud CCE clusters to identify warnings, repeated failure patterns, affected resources, and diagnosis handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and platform engineers use this skill to inspect current and historical Huawei Cloud CCE Kubernetes Events, group recurring warning patterns, and prepare evidence for diagnosis handoffs without changing cluster resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires read access to CCE Events, related Kubernetes resource status, default Event LogConfig data, and LTS event logs.

Mitigation: Use a least-privilege Huawei Cloud identity and read-only Kubernetes RBAC scoped to the clusters and namespaces that need investigation.

Risk: Credential and temporary kubeconfig handling can expose sensitive access material on shared machines.

Mitigation: Use approved local credential providers, avoid printing AK/SK, security tokens, or kubeconfig content, and treat temporary kubeconfig files as sensitive.

Risk: Broad all-event or unbounded historical queries can return excessive data and may expose production workload, Pod, or node identifiers.

Mitigation: Prefer Warning events, namespace filters, explicit limits, and bounded incident windows; redact production identifiers in summaries when they are not needed.

Risk: Event findings may suggest remediation, but this skill is designed for evidence gathering rather than cluster changes.

Mitigation: Keep this skill read-only and hand off summarized evidence to an appropriate diagnosis or remediation skill for any corrective action.

## Reference(s):

- [Event Query Workflow](references/workflow.md)
- [Risk Rules and Guardrails](references/risk-rules.md)
- [Output Schema](references/output-schema.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [kubectl-cce Usage](references/kubectl-cce.md)
- [kubectl-cce Plugin Release](https://github.com/pancake0001/kubectl-cce-plugin/releases/download/v0.1.0/kubectl-cce_0.1.0_linux_amd64.tar.gz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON query results and Markdown analysis summaries with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Event data, aggregated warning patterns, resource-status summaries, and actionable error messages; sensitive credentials and production identifiers should be redacted.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
