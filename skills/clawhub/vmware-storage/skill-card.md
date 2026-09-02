## Description:

VMware Storage helps agents manage VMware vSphere storage, including datastores, iSCSI targets, and vSAN clusters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, VMware administrators, and infrastructure operators use this skill to inspect datastores, find deployable images, configure iSCSI targets, and check vSAN health and capacity across configured vCenter or ESXi targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with privileged VMware storage-management access.

Mitigation: Use least-privilege VMware service accounts, require operator approval for writes, prefer dry-run previews, and review audit logs for state-changing operations.

Risk: Setup examples can normalize insecure TLS settings for vSphere connections.

Mitigation: Set verify_ssl to true in real environments and configure trusted CA certificates before relying on storage-management results.

Risk: Credentials in the local .env file or diagnostics run with skipped authentication can create operational blind spots.

Mitigation: Keep .env permissions restricted, protect VMware passwords with appropriate secret handling, and treat doctor --skip-auth as incomplete diagnostics rather than approval to run changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-storage)
- [VMware Storage Homepage](https://github.com/vmware-skills/VMware-Storage)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [VMware Storage Capabilities](references/capabilities.md)
- [Operating vmware-storage with a local / small model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-style VMware storage result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run recommendations, audit-log references, and concise summaries of datastore, iSCSI, or vSAN results.]

## Skill Version(s):

1.8.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
