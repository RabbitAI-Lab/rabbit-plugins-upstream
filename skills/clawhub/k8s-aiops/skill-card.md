## Description:

k8s-aiops helps agents inspect, diagnose, and operate kubeconfig-reachable Kubernetes clusters through governed CLI and MCP workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to inspect Kubernetes resources, read logs, run RCA, and perform governed operational actions such as scaling, rollouts, deletes, namespace changes, and node maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make destructive Kubernetes changes using the access granted by the active kubeconfig.

Mitigation: Use a dedicated least-privilege Kubernetes context, preferably read-only by default, and avoid production admin kubeconfigs unless writes are intended.

Risk: MCP write tools can perform real cluster changes even when audit, dry-run, and undo features are available.

Mitigation: Review planned write actions, use dry-run where available, confirm the target context and namespace, and rely on Kubernetes RBAC as the enforcement boundary.

Risk: The package installed at runtime may differ from the reviewed release if it is not pinned or verified.

Mitigation: Pin and verify the k8s-aiops package version before installation or execution.

## Reference(s):

- [k8s-aiops source repository](https://github.com/AIops-tools/K8s-AIops)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and Kubernetes operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide Kubernetes read and write operations through k8s-aiops; effects depend on the provided kubeconfig, RBAC, and selected dry-run or confirmation path.]

## Skill Version(s):

0.13.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
