## Description:

Helps operators inventory GPUs and vGPU consumers, inspect utilization and profiles, manage vGPU assignments, and inspect Private AI Service models and knowledge bases in VMware environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to inspect VMware GPU resources and Private AI Service deployments, validate vGPU profiles, and assign a profile to a powered-off VM with approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials and PAIS tokens can expose infrastructure access if stored insecurely.

Mitigation: Use a least-privilege service account and inject secrets through a secret manager or environment rather than a persistent .env file when possible.

Risk: Disabling TLS verification can expose vCenter or PAIS connections to interception.

Mitigation: Keep TLS verification enabled outside isolated labs.

Risk: Assigning a vGPU profile changes a VM's device configuration.

Mitigation: Expose read-only tools by default; if assignment is needed, review the change preview and require explicit approval before applying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown guidance, CLI output, or structured JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory lists may be paginated; vGPU assignment requires a preview and confirmation.]

## Skill Version(s):

2.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
