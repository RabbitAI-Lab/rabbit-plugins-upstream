## Description:

vmware-vks helps agents manage vSphere Kubernetes Service environments, including Supervisor clusters, vSphere Namespaces, TKC cluster lifecycle operations, kubeconfig retrieval, and Harbor registry checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and platform engineers use this skill to inspect VKS readiness, manage vSphere Namespaces, deploy or modify Tanzu Kubernetes clusters, and retrieve access material for Kubernetes operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve live Supervisor or TKC kubeconfig material that may grant cluster access.

Mitigation: Use least-privilege vCenter accounts, require human approval for kubeconfig retrieval, write kubeconfigs only to secure file destinations, and avoid printing tokens or kubeconfig content in chat.

Risk: The skill can mutate infrastructure, including namespace and TKC cluster creation, scaling, upgrades, and deletion.

Mitigation: Require dry-run review and explicit approval for writes, keep destructive-operation confirmations enabled, and review policy and audit settings before production use.

Risk: The security evidence reports a suspicious verdict due to infrastructure mutation and inconsistent approval guidance.

Mitigation: Review the source, security guidance, and audit behavior before deployment, and install only where the agent is authorized to administer vSphere Kubernetes resources.

## Reference(s):

- [VMware VKS source homepage](https://github.com/vmware-skills/VMware-VKS)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vks)
- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local configuration paths and generated command plans; kubeconfig content should be written to files rather than displayed in chat.]

## Skill Version(s):

1.8.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
