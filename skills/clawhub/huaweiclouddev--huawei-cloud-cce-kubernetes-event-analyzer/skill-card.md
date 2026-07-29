## Description: <br>
Query and analyze current and historical Kubernetes Events in Huawei Cloud CCE clusters to identify warnings, repeated failure patterns, affected resources, and diagnosis handoffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and Kubernetes operators use this skill to query Huawei Cloud CCE Events, analyze current or LTS-backed warning patterns, and package findings for follow-on diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud and Kubernetes credentials may grant broader access than event diagnostics require. <br>
Mitigation: Use short-lived or local hcloud profile credentials with least-privilege CCE, LTS, and read-only Kubernetes Event permissions. <br>
Risk: Event output may expose production namespaces, workloads, Pods, nodes, or other infrastructure identifiers. <br>
Mitigation: Redact sensitive identifiers in summaries and share only the fields needed for diagnosis. <br>
Risk: Unbounded historical or all-type Event queries can return excessive data and obscure the incident signal. <br>
Mitigation: Use explicit UTC time windows, namespace filters, limits, and the default Warning filter unless broader scope is required. <br>
Risk: The kubectl-cce fallback depends on a separately installed plugin and cloud credentials. <br>
Mitigation: Verify the plugin source before installation and use the fallback only when external kubeconfig access is unavailable. <br>


## Reference(s): <br>
- [Workflow](references/workflow.md) <br>
- [Risk Rules](references/risk-rules.md) <br>
- [Output Schema](references/output-schema.md) <br>
- [kubectl-cce Usage](references/kubectl-cce.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [kubectl-cce Plugin Release](https://github.com/pancake0001/kubectl-cce-plugin/releases/download/v0.1.0/kubectl-cce_0.1.0_linux_amd64.tar.gz) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only event query and analysis output; defaults to Warning Events and supports bounded current or LTS-backed historical windows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
