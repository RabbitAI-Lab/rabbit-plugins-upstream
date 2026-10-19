## Description:

Helps agents inspect, diagnose, and operate kubeconfig-reachable Kubernetes clusters through CLI and MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Kubernetes operators and developers use this skill to inspect workloads, logs, events, and cluster health, then perform authorized operations such as scaling, rollouts, deletion, and node maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent with a write-enabled kubeconfig can scale, roll back, delete resources, or drain nodes without a built-in MCP approval gate.

Mitigation: Use a narrowly scoped, preferably read-only RBAC identity by default; require separate client-side approval before granting production write access.

Risk: Cluster changes, including deletion and pod evictions, may disrupt workloads and may not be fully reversible.

Mitigation: Review the target cluster and intended change, preview writes with dry-run where available, and obtain operator confirmation before high-impact actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/k8s-aiops)
- [Project homepage listed in release metadata](https://github.com/AIops-tools/K8s-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and summaries of Kubernetes tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics and optional dry-run previews; write operations depend on the selected kubeconfig's RBAC permissions.]

## Skill Version(s):

0.15.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
