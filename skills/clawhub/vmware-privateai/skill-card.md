## Description:

vmware-privateai helps agents inspect and administer the GPU and model-serving layer for VMware Private AI Foundation with NVIDIA on vSphere 9.x and VCF 9.1.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inventory GPU hosts and devices, inspect vGPU consumers and utilization, list PAIS models and knowledge bases, and safely preflight or apply a vGPU profile change to a powered-off VM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change a powered-off VM's vGPU hardware profile.

Mitigation: Use the read-only vGPU profile validation or dry-run preview first, require explicit confirmation, and review the audit record after any applied change.

Risk: vCenter passwords and PAIS bearer tokens grant access to infrastructure resources.

Mitigation: Use a dedicated least-privilege vCenter account, store secrets outside shared configuration, and treat b64-at-rest values as obfuscated rather than encrypted.

Risk: Some PAIS paths and GPU metric fields are beta and may differ across live deployments.

Mitigation: Validate endpoints and GPU metrics against the target vSphere or VCF environment before relying on them for operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [capabilities.md](artifact/references/capabilities.md)
- [cli-reference.md](artifact/references/cli-reference.md)
- [setup-guide.md](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP tool calls return structured operational data; list tools paginate results at a default limit of 50.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
