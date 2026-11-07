## Description:

Manage vSphere Kubernetes Service environments, including Supervisor clusters, vSphere Namespaces, and Tanzu Kubernetes Cluster lifecycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to check VKS compatibility and manage Supervisor namespaces and TKC clusters, including provisioning, scaling, upgrades, kubeconfig access, and Harbor or storage queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented password setup can expose vCenter credentials, and stored password obfuscation is not encryption.

Mitigation: Supply passwords through a secret manager or protected input instead of the echo command, and use a narrowly scoped service account.

Risk: Remote mode creates a network listener, despite conflicting network-safety statements in the setup material.

Mitigation: Prefer local stdio; review and restrict network exposure before enabling remote mode.

Risk: Kubeconfig exports contain bearer credentials that can remain valid after the process exits and are not automatically removed.

Mitigation: Retrieve them only on explicit request, keep approval steps for changes, write exports to owner-only files, and remove them after use.

## Reference(s):

- [VMware VKS project](https://github.com/vmware-skills/VMware-VKS)
- [VKS capabilities](artifact/references/capabilities.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [CLI reference](artifact/references/cli-reference.md)
- [TKC kubeconfig issue on VCF 9.1](https://github.com/vmware-skills/VMware-VKS/issues/27)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands and structured operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an explicitly requested kubeconfig file; handle it as a sensitive credential.]

## Skill Version(s):

3.5.0 (source: server-resolved release metadata, artifact/SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
