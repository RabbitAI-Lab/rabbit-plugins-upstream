## Description:

Provides VMware Private AI Foundation with NVIDIA GPU and model-serving operations for vSphere 9.x and VCF 9.1, including GPU inventory, vGPU consumers, utilization, profile validation and assignment, and PAIS model and knowledge-base listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and infrastructure operators use this skill to inspect VMware GPU capacity, triage vGPU utilization, validate or apply powered-off vGPU profile changes, and query Private AI Service model-serving resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs external runtime code that handles infrastructure credentials.

Mitigation: Verify package provenance before production use, prefer the installed console script over uvx, and inject secrets through a secret manager or environment variables.

Risk: The skill can perform a limited VM reconfiguration through vGPU assignment.

Mitigation: Use a dedicated least-privileged vCenter service account and grant write permissions only when vgpu_assign is needed.

Risk: Stored credentials may be exposed if local files are mismanaged.

Mitigation: Prefer secret-manager or environment injection over storing credentials in ~/.vmware-privateai/.env.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and structured MCP or CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational outputs may include vSphere or PAIS resource names, status fields, utilization metrics, validation reasons, and audit-oriented write previews.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
