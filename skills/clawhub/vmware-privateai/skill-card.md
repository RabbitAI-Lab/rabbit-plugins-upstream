## Description:

Provides GPU and VMware Private AI Service operations for vSphere and VCF environments, including GPU inventory, vGPU consumers and utilization, profile catalogs and assignment, and PAIS model and knowledge-base listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and infrastructure engineers use this skill to inspect GPU capacity, monitor vGPU usage, list Private AI Service resources, and safely plan or apply vGPU profile changes in VMware Private AI Foundation with NVIDIA environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: vCenter and PAIS credentials can expose infrastructure access if handled carelessly.

Mitigation: Use a dedicated least-privilege vCenter service account scoped to GPU clusters, prefer environment or secret-manager injection, and protect any local .env file with restricted permissions.

Risk: The vGPU assignment tool can change VM configuration.

Mitigation: Review the blast-radius preview and approve the write only after confirming the target VM, profile, power state, and user intent.

Risk: Disabling TLS verification outside self-signed lab environments can expose credentials or infrastructure data.

Mitigation: Keep TLS verification enabled for normal use and install the appropriate vCenter or PAIS certificate authority instead of disabling verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON from MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [List operations may be paginated; vGPU assignment is a write action that should be previewed and explicitly confirmed.]

## Skill Version(s):

1.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
