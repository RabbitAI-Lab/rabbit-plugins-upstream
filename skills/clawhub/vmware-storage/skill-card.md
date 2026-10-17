## Description:

Helps agents inspect VMware datastores, iSCSI, vSAN, and Fibre Channel storage and perform confirmed iSCSI changes and storage rescans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure engineers and administrators use this skill to inspect VMware storage inventory, health, and paths, and to configure iSCSI targets or rescan host storage with approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: iSCSI changes or host storage rescans could disrupt access to storage.

Mitigation: Use a least-privilege vSphere account, expose read-only tools unless changes are needed, and require a reviewed preview and explicit confirmation before writes.

Risk: Privileged vSphere passwords stored in a local .env file could be exposed.

Mitigation: Protect the file with owner-only permissions, or inject secrets externally in production.

Risk: Unreviewed storage activity may be difficult to investigate.

Mitigation: Keep audit logging enabled and review operation records.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage (skill metadata)](https://github.com/vmware-skills/VMware-Storage)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [Storage capabilities](artifact/references/capabilities.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses, CLI text, or structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Storage inventory and health results; write requests preview changes before confirmation.]

## Skill Version(s):

2.4.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
