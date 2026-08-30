## Description:

Provides GPU and Private AI Service operations for VMware Private AI Foundation with NVIDIA on vSphere 9.x and VCF 9.1, including GPU inventory, vGPU utilization and profile management, PAIS model and knowledge-base listings, sizing guidance, and guarded vGPU assignment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect and manage the GPU and model-serving layer of VMware Private AI environments. It supports inventory, utilization triage, profile validation, PAIS model and knowledge-base discovery, local sizing or bundle checks, and a guarded vGPU assignment workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses VMware credentials and a PAIS bearer token.

Mitigation: Use a dedicated least-privilege service account, store secrets outside config files, and treat the PAIS token and vCenter password as sensitive credentials.

Risk: The vGPU assignment workflow can change one powered-off VM's vGPU profile.

Mitigation: Run validation and dry-run preview first, confirm the target VM is powered off, and review the proposed assignment before allowing the write.

Risk: TLS verification can be disabled for lab environments.

Mitigation: Keep TLS verification enabled outside labs and install the appropriate vCenter or PAIS certificate authority instead of disabling verification.

## Reference(s):

- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Publisher Profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured operational guidance with CLI commands and MCP configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read-only operational summaries, local sizing or bundle-analysis guidance, and guarded vGPU assignment instructions that require explicit confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
