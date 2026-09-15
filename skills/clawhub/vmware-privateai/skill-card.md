## Description:

Provides agent-assisted VMware Private AI Foundation with NVIDIA operations for GPU host and device inventory, vGPU consumers and utilization, vGPU profile validation and assignment, PAIS model and knowledge-base listing, and sizing or air-gap bundle checks on vSphere and VCF environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure engineers and platform operators use this skill to inspect VMware Private AI GPU capacity, triage vGPU utilization, validate or apply a vGPU profile change to a powered-off VM, and inspect PAIS model-serving resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reviewed installer metadata can resolve an unpinned executable package while the skill handles sensitive infrastructure credentials.

Mitigation: Pin installation to vmware-privateai==1.2.1 or an internally verified artifact, run under a dedicated low-privilege OS account, and prefer short-lived tokens or a secret manager over persistent .env secrets.

Risk: The skill includes one VM reconfiguration action for vGPU assignment.

Mitigation: Use the documented validation and preview flow first, require the VM to be powered off, rely on vCenter RBAC for authorization, and review audit records for applied changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured command or configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing guidance may include CLI commands, MCP tool routing, JSON-like result descriptions, and operational cautions.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
