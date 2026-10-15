## Description:

Helps agents inspect VMware datastores, iSCSI targets, vSAN health, and Fibre Channel paths, and make approved iSCSI configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure administrators and engineers use this skill to inspect vSphere storage, diagnose capacity and path health, and configure iSCSI targets with approval before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: iSCSI changes can disrupt access to storage and affected workloads.

Mitigation: Use read-only access unless writes are necessary; review change previews and require explicit confirmation before applying changes.

Risk: vCenter or ESXi credentials could be exposed if stored insecurely.

Mitigation: Use a least-privilege service account and inject passwords from a secret manager rather than storing production passwords in .env files.

Risk: Diagnostic results obtained with authentication checks skipped may miss access or connectivity failures.

Mitigation: Do not treat --skip-auth results as a complete health check; verify connectivity and authentication separately.

## Reference(s):

- [VMware Storage project homepage](https://github.com/vmware-skills/VMware-Storage)
- [ClawHub skill listing](https://clawhub.ai/zw008/skills/vmware-storage)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with CLI examples and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results and change previews can include datastore, iSCSI, vSAN, and path details.]

## Skill Version(s):

2.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
