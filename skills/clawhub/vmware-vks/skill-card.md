## Description:

Helps operators manage vSphere Kubernetes Service namespaces and Tanzu Kubernetes clusters, including compatibility checks, lifecycle operations, and cluster access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to inspect and manage vSphere Kubernetes Service environments, including Supervisor namespaces, Tanzu Kubernetes clusters, and kubeconfig access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Namespace and cluster changes can disrupt or remove live workloads.

Mitigation: Limit use to authorized operators; review the proposed change and production policy rules before approving writes.

Risk: Cluster access can expose live kubeconfig credentials and vCenter passwords.

Mitigation: Use least-privilege vCenter accounts, keep TLS verification enabled, inject passwords from a secret manager, and delete exported kubeconfigs when finished.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](artifact/references/capabilities.md)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can export a kubeconfig containing live credentials when explicitly requested.]

## Skill Version(s):

2.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
