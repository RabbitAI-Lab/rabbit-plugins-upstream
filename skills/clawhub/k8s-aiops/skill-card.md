## Description:

k8s-aiops provides governed Kubernetes operations through CLI and MCP tools for inspecting resources, reading logs, running diagnostics, and performing audited writes such as scale, rollout, delete, namespace, and node maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Kubernetes operators use this skill to inspect kubeconfig-reachable clusters, troubleshoot pods and workloads, and execute common operations with audit and undo support where available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Kubernetes writes including deletes, rollbacks, namespace deletion, and node drain.

Mitigation: Use a dedicated read-only ServiceAccount by default, keep write-capable kubeconfigs separate, avoid cluster-admin contexts, and reserve destructive verbs for narrowly scoped contexts.

Risk: Write control depends on kubeconfig RBAC or agent judgment rather than a built-in read-only policy.

Mitigation: Enforce least privilege in the Kubernetes API server and validate intended permissions with kubectl auth can-i before allowing write operations.

Risk: Cluster operations can affect production availability if run against the wrong context or namespace.

Mitigation: Use named targets, explicit namespaces, dry-run previews where available, and separate production credentials from diagnostic or development contexts.

Risk: Local audit and undo data may contain operational details about cluster actions.

Mitigation: Store k8s-aiops state in an owner-only directory, relocate it with K8S_AIOPS_HOME when needed, and protect audit records according to operational policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/k8s-aiops)
- [Project homepage](https://github.com/AIops-tools/K8s-AIops)
- [Issue tracker](https://github.com/AIops-tools/K8s-AIops/issues)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or text with inline shell commands and structured Kubernetes tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Kubernetes API summaries, diagnostics, dry-run previews, and audited write results; secret values are not returned.]

## Skill Version(s):

0.13.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
