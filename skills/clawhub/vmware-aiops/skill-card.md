## Description:

vmware-aiops helps agents manage VMware/vSphere/ESXi VM lifecycle, deployment, guest operations, cluster changes, alarm handling, and infrastructure triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure operators, and SREs use this skill to operate VMware/vSphere/ESXi estates through agent-guided CLI or MCP workflows for VM lifecycle, deployment, triage, and remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Destructive MCP operations can modify VMware infrastructure immediately with the configured vCenter or ESXi credentials.

Mitigation: Use a dedicated least-privilege service account, prefer read-only roles unless writes are required, and require operator review before write-capable workflows.

Risk: Guest command execution can run commands inside VMs with the supplied guest credentials.

Mitigation: Keep guest credentials separate from vCenter credentials, avoid root or administrator guest accounts, and omit guest credentials when guest operations are not needed.

Risk: Production use depends on the installed vmware-aiops package matching the reviewed release.

Mitigation: Pin and verify the package version before production deployment.

## Reference(s):

- [Project homepage](https://github.com/vmware-skills/VMware-AIops)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide CLI and MCP workflows that read or change VMware infrastructure using configured credentials.]

## Skill Version(s):

1.8.22 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
