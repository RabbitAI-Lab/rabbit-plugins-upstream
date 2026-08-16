## Description:

k8s-aiops helps agents perform governed Kubernetes operations for inspection, diagnostics, scaling, rollout management, deletion, namespace management, and node maintenance on kubeconfig-reachable clusters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and operators use this skill to inspect Kubernetes resources, diagnose workload health, review logs and events, and perform governed cluster changes such as scaling, rollout actions, deletion, namespace operations, and node maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes high-impact Kubernetes write actions without an in-skill read-only mode or approval gate.

Mitigation: Install it only with a kubeconfig or ServiceAccount scoped to the exact clusters, namespaces, and verbs the agent should use; for observation-only workflows, provide read-only RBAC so writes fail at the Kubernetes API server.

Risk: Production contexts and operations such as namespace deletion, deployment or job deletion, rollout undo, set-image, and node drain can materially affect running workloads.

Mitigation: Use dry-run previews where available, review destructive actions before execution, and avoid broad production credentials unless the operator intends those write capabilities.

Risk: ConfigMap values may contain sensitive operational data even though Kubernetes Secret values are documented as names and keys only.

Mitigation: Treat ConfigMap output as potentially sensitive and restrict cluster access according to the sensitivity of namespaces and configuration data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/k8s-aiops)
- [Project homepage](https://github.com/AIops-tools/K8s-AIops)
- [k8s-aiops Capabilities](references/capabilities.md)
- [k8s-aiops CLI Reference](references/cli-reference.md)
- [k8s-aiops Setup Guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Kubernetes diagnostics, dry-run recommendations, RBAC-aware safety guidance, and setup/configuration steps.]

## Skill Version(s):

0.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
