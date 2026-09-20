## Description:

vmware-storage helps agents manage VMware vSphere storage, including datastores, iSCSI targets, vSAN health and capacity, and Fibre Channel or multipath diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, and VMware operators use this skill to inspect datastore contents, scan deployable images, configure iSCSI storage, check vSAN health and capacity, and review Fibre Channel or multipath state from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can receive powerful VMware storage-management access, including operations that affect iSCSI configuration and storage visibility.

Mitigation: Use least-privilege vCenter service accounts, avoid ESXi root where possible, and manually review every write preview before confirming.

Risk: Setup guidance can lead to unsafe TLS or local password-file practices.

Mitigation: Use verify_ssl: true for production targets, trust the proper CA instead of disabling certificate checks, and replace local .env passwords with a secrets manager where possible.

Risk: Removing or changing iSCSI targets can make LUNs and dependent VMs inaccessible.

Mitigation: Rely on preview-first write behavior, inspect the reported blast radius, and proceed with confirm=true only after explicit operator approval.

Risk: Container-based installation can drift if an image is pulled without a stable reference.

Mitigation: Pin Docker images by tag or digest before deployment.

## Reference(s):

- [VMware Storage GitHub Repository](https://github.com/vmware-skills/VMware-Storage)
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-storage)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [VMware Storage Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can also guide MCP tool calls that return structured VMware storage data and write previews.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
