## Description:

Helps agents manage vSphere Kubernetes Service supervisors, namespaces, and Tanzu Kubernetes clusters through guided checks and administrative operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to check VKS compatibility, administer vSphere namespaces and TKC clusters, and obtain cluster access when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative operations can modify or delete namespaces, clusters, and workloads.

Mitigation: Use least-privilege access, prefer read-only operations, review the proposed impact, and require explicit confirmation before changes.

Risk: Exported kubeconfigs contain live temporary credentials.

Mitigation: Export only on explicit request to an owner-only file, never paste tokens into responses, and delete the file when finished.

Risk: Disabling TLS verification can expose vCenter connections to interception.

Mitigation: Keep TLS verification enabled.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-vks)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-VKS)
- [Capabilities](artifact/references/capabilities.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide dry-run plans and paths to exported kubeconfig files; do not expose credential contents.]

## Skill Version(s):

3.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
