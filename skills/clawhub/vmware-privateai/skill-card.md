## Description:

vmware-privateai helps agents inspect VMware Private AI Foundation with NVIDIA GPU infrastructure, list PAIS model assets, and safely preview or apply one powered-off VM vGPU profile change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inventory GPU hosts and vGPU consumers, check utilization and readiness, inspect PAIS-served models and knowledge bases, and manage vGPU profile assignment within VMware Private AI environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive VMware GPU, vGPU, VM, and PAIS inventory through configured vCenter/ESXi and PAIS endpoints.

Mitigation: Use a dedicated least-privilege vCenter service account, scope it to the required GPU clusters, and inject credentials from a secret manager or short-lived environment variables.

Risk: The vgpu_assign action can change one VM's vGPU profile when the VM is powered off.

Mitigation: Review the blast-radius preview, pre-flight with vgpu_profile_validate, and pass confirm=true only after explicit user approval.

Risk: Disabling TLS verification or storing persistent secrets can weaken protection for vCenter and PAIS credentials.

Mitigation: Keep TLS verification enabled outside self-signed labs and avoid persistent .env secrets when managed secret injection is available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and structured MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools return paginated inventory or status data; the vGPU assignment write first returns a blast-radius preview and requires explicit confirmation.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
