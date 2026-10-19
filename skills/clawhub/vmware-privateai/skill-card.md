## Description:

Helps agents inspect VMware GPU and Private AI infrastructure, review vGPU and model-serving resources, and assign a vGPU profile to a powered-off VM when explicitly approved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to inspect GPU hosts, vGPU consumers, utilization, profiles, and Private AI Service models and knowledge bases on VMware deployments. With explicit approval, they can change one powered-off VM's vGPU profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An approved vGPU assignment changes a VM's hardware profile.

Mitigation: Validate the profile first, require explicit confirmation, and limit writes to a powered-off VM using a dedicated least-privilege vCenter account.

Risk: vCenter passwords and PAIS tokens can be exposed if local secret storage is compromised.

Mitigation: Keep PAIS tokens short-lived and use protected secret storage; treat base64 obfuscation as non-encrypting.

Risk: Unnecessary write-tool exposure could allow unintended infrastructure changes.

Mitigation: Expose read-only MCP tools unless profile assignment is needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only infrastructure findings and, when approved, a guarded vGPU profile change.]

## Skill Version(s):

2.4.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
