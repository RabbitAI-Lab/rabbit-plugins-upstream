## Description:

k8s-aiops helps agents inspect, diagnose, and operate kubeconfig-reachable Kubernetes clusters through CLI and MCP tools for resources, logs, metrics, rollouts, scaling, deletion, namespace management, and node maintenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and SREs use this skill to inspect Kubernetes resources, diagnose pod and workload health, read logs and events, and perform governed operational changes such as scaling, rollouts, deletion, namespace operations, and node maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Kubernetes changes, including workload deletion, namespace deletion, node drain, rollout undo, and other write operations.

Mitigation: Install and run it with a dedicated least-privilege kubeconfig, preferably read-only by default; only grant write RBAC for clusters and namespaces where the operator intends those changes.

Risk: The skill relies on kubeconfig RBAC and agent judgment rather than a built-in read-only mode or approval gate.

Mitigation: Use Kubernetes RBAC as the primary control boundary, review write requests before execution, and avoid admin or production contexts unless the operational intent is explicit.

Risk: Using an unpinned or unverified package could execute a release different from the reviewed artifact.

Mitigation: Prefer a pinned and verified package release before using the skill against real clusters.

## Reference(s):

- [k8s-aiops project homepage](https://github.com/AIops-tools/K8s-AIops)
- [k8s-aiops Capabilities](references/capabilities.md)
- [k8s-aiops CLI Reference](references/cli-reference.md)
- [k8s-aiops Setup Guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured CLI or MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Kubernetes resource summaries, diagnostics, log excerpts, dry-run previews, and operational recommendations scoped to the selected kubeconfig context.]

## Skill Version(s):

0.13.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
