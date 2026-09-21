## Description:

vmware-storage helps agents manage VMware vSphere storage, including datastores, deployable-image scans, iSCSI targets, vSAN health and capacity, and Fibre Channel or multipath diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect and manage VMware storage resources, including datastore browsing, deployable image discovery, iSCSI configuration, vSAN checks, and Fibre Channel or multipath diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented default TLS setting could expose privileged vCenter or ESXi credentials.

Mitigation: Set target configs to verify_ssl: true or provide a trusted CA before using the skill against sensitive environments.

Risk: The skill requires VMware management credentials and can perform storage write operations.

Mitigation: Use least-privilege service accounts, inject secrets from a secret manager when possible, and review the previewed blast radius before approving write operations.

Risk: Removing an iSCSI target or approving other storage writes can affect datastore or LUN availability.

Mitigation: Treat iSCSI remove-target and other write operations as high-impact; approve them only after confirming paths, affected devices, and operational intent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-storage)
- [VMware-Storage homepage](https://github.com/vmware-skills/VMware-Storage)
- [Setup Guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to invoke local CLI or MCP tools that return text or JSON-like operational results.]

## Skill Version(s):

1.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
