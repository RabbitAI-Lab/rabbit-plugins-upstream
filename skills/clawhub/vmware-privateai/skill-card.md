## Description:

vmware-privateai helps agents operate the VMware Private AI Foundation with NVIDIA GPU layer by inventorying GPU hosts and devices, reporting vGPU consumers and utilization, listing profile catalogs and PAIS resources, and guiding guarded vGPU assignment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect GPU capacity, vGPU consumers, utilization, profile catalogs, and Private AI Service resources in VMware vSphere 9.x / VCF 9.1 environments. They can also preflight and apply a constrained vGPU profile change for a powered-off VM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vGPU assignment action can change a powered-off VM's GPU profile.

Mitigation: Review the preview carefully, use the validation workflow first, and rely on a dedicated least-privilege VMware service account for enforcement.

Risk: PAIS bearer tokens and VMware credentials can grant infrastructure access if mishandled.

Mitigation: Keep PAIS tokens short-lived, store credentials outside the main config, and scope the VMware account to the minimum required privileges.

Risk: Disabling TLS verification can expose vCenter, ESXi, or PAIS connections.

Mitigation: Keep TLS verification enabled outside self-signed lab environments and install the appropriate CA where possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and structured operational results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces inventory, utilization, readiness, PAIS, sizing, and air-gap guidance; list outputs may be paginated, and the single vGPU assignment write is previewed before execution.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
