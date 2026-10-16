## Description:

Helps agents inspect VMware Private AI GPU infrastructure and served models, and assign a powered-off VM's vGPU profile with confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to inspect VMware GPU hosts, vGPU consumers, utilization, profiles, and Private AI Service models and knowledge bases. They can also preview and confirm a vGPU profile change for a powered-off VM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changing a VM's vGPU profile could disrupt its intended GPU allocation.

Mitigation: Use a least-privilege account, validate the target profile, review the preview, and confirm the change only for a powered-off VM; review audit logs afterward.

Risk: The vCenter password and PAIS token could be exposed.

Mitigation: Keep credentials out of shared configuration, protect secret storage, and use a dedicated least-privilege service account.

Risk: An agent with write access could make an unintended infrastructure change.

Mitigation: Expose read-only tools unless vGPU changes are required, and require explicit confirmation before writes.

## Reference(s):

- [ClawHub release: vmware-privateai](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities](artifact/references/capabilities.md)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with CLI commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [GPU and model inventories, utilization summaries, and confirmation-gated vGPU profile changes.]

## Skill Version(s):

2.4.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
