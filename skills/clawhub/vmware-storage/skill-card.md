## Description:

Helps agents inspect VMware datastores, iSCSI storage, vSAN health, and Fibre Channel paths, and perform approved iSCSI configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure engineers and administrators use this skill to inspect vSphere storage, find datastore images, assess vSAN and storage paths, and manage iSCSI targets with approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: iSCSI changes can interrupt access to storage and workloads.

Mitigation: Use read-only access where possible; preview changes and require explicit human approval before production add, remove, or rescan operations.

Risk: vCenter or ESXi credentials can expose sensitive infrastructure.

Mitigation: Use least-privilege service accounts, protect credential files or use a secret manager, and review audit logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-Storage)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Capabilities and operating guardrails](artifact/references/capabilities.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with storage summaries and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only diagnostics and guided, approval-gated iSCSI changes.]

## Skill Version(s):

2.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
