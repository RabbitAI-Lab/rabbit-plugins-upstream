## Description:

Query and analyze Kubernetes Events in Huawei Cloud CCE clusters. Trigger when users ask about CCE events, Kubernetes warning events, FailedScheduling, FailedMount, ImagePullBackOff, event patterns, historical events in LTS, or event-based diagnosis for a CCE cluster or namespace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inspect current and historical Kubernetes Events in Huawei Cloud CCE clusters, group recurring warning patterns, and prepare evidence for follow-up diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill touches sensitive Huawei Cloud credentials, kubeconfig access paths, and cluster event data.

Mitigation: Install it only where hcloud, kubectl, and kubectl-cce are trusted, and use least-privilege Huawei IAM and Kubernetes RBAC for event and log reads.

Risk: Credential values can be exposed if access keys or security tokens are passed through visible shell commands or unrelated environment state.

Mitigation: Prefer scoped profiles or short-lived credentials, avoid passing AK/SK in visible command lines when possible, and run in a shell that does not contain unrelated secrets.

Risk: Event summaries can reveal production workload, pod, namespace, or node identifiers.

Mitigation: Redact sensitive infrastructure identifiers from human-facing summaries unless the audience needs the exact values for diagnosis.

## Reference(s):

- [Workflow](references/workflow.md)
- [Risk Rules](references/risk-rules.md)
- [Output Schema](references/output-schema.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [kubectl-cce Usage](references/kubectl-cce.md)
- [kubectl-cce v0.1.0 release asset](https://github.com/pancake0001/kubectl-cce-plugin/releases/download/v0.1.0/kubectl-cce_0.1.0_linux_amd64.tar.gz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only event query and analysis results, including normalized Events, aggregate counters, repeated patterns, and resource status summaries.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
