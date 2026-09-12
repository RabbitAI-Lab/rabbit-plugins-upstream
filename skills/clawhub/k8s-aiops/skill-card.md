## Description:

k8s-aiops helps agents inspect, diagnose, and operate kubeconfig-reachable Kubernetes clusters with audited read and write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and operators use this skill to list Kubernetes resources, review logs and events, run read-only diagnostics, and perform governed operational actions such as scaling, rollouts, deletion, cordon, and drain. It is intended for clusters reachable through the user's kubeconfig, including standard Kubernetes, k3s, EKS, GKE, and AKS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose destructive Kubernetes actions without an enforced skill-side read-only or approval gate.

Mitigation: Use a deliberately scoped kubeconfig, prefer a read-only ServiceAccount by default, and withhold RBAC for node drain and namespace deletion unless those operations are explicitly needed.

Risk: An agent using a broad kubeconfig could perform unintended cluster changes.

Mitigation: Review proposed write actions, use dry-run previews where available, and verify the exact k8s-aiops package version and source before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/k8s-aiops)
- [Project homepage](https://github.com/AIops-tools/K8s-AIops)
- [agent-guardrails.md](references/agent-guardrails.md)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and structured Kubernetes operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run recommendations, RBAC checks, audit context, and Kubernetes resource names scoped to the selected kubeconfig target.]

## Skill Version(s):

0.13.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
