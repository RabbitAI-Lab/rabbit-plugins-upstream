## Description:

vmware-privateai helps agents operate the GPU and AI-infrastructure layer of VMware Private AI Foundation with NVIDIA on vSphere 9.x and VCF 9.1, including GPU inventory, vGPU consumers, utilization, profile catalogs, controlled vGPU assignment, and Private AI Service model and knowledge-base listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and VMware administrators use this skill to inspect GPU-backed vSphere and VCF Private AI environments, understand vGPU usage and utilization, configure model-serving access, and make a guarded vGPU profile assignment when the target VM is already powered off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can apply one vGPU profile assignment to a VM.

Mitigation: Use dry-run or preview first, require explicit confirmation for writes, keep the VM powered off before applying, and scope the vCenter service account to the GPU clusters it is intended to manage.

Risk: vCenter passwords and PAIS bearer tokens grant access to infrastructure and model-serving resources.

Mitigation: Keep the .env file owner-only, prefer a secret manager for injected credentials, and use a dedicated least-privilege service account.

Risk: TLS verification can be disabled for self-signed lab targets.

Mitigation: Leave TLS verification enabled for normal environments and disable it only for intentional lab deployments with known certificates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON-style MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP list tools return paginated item envelopes; the vGPU assignment path supports preview before apply and records applied writes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
