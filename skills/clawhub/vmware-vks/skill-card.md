## Description:

Helps agents manage vSphere Kubernetes Service Supervisor namespaces and Tanzu Kubernetes clusters through guided CLI and MCP workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to check VKS compatibility, manage vSphere Namespaces and TKC clusters, inspect storage and registry information, and obtain kubeconfigs when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Namespace and cluster changes can disrupt workloads or delete resources.

Mitigation: Use least-privilege access, review the proposed changes and blast radius, and require explicit confirmation before destructive operations.

Risk: Exported kubeconfigs and locally stored passwords can expose cluster access.

Mitigation: Issue kubeconfigs only on request, protect credentials with a secret manager where available, and delete exported kubeconfigs when finished.

Risk: Disabling TLS verification can expose administrative connections.

Mitigation: Keep TLS certificate verification enabled for vCenter and Supervisor connections.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide credential-bearing kubeconfig export when explicitly requested.]

## Skill Version(s):

3.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
