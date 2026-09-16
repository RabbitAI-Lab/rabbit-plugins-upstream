## Description:

vmware-privateai helps agents and operators inspect VMware Private AI Foundation GPU infrastructure, PAIS model-serving resources, and safely preflight or apply a powered-off VM vGPU profile change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure administrators and developers use this skill to inventory GPU hosts, physical GPU devices, vGPU consumers, utilization, profile catalogs, PAIS served models, knowledge bases, and data sources. It also supports a scoped vGPU assignment workflow for powered-off VMs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses sensitive vCenter credentials and PAIS bearer tokens.

Mitigation: Use a dedicated least-privilege vCenter account and short-lived PAIS tokens from a secret manager where possible.

Risk: The vGPU assignment workflow changes VM infrastructure state.

Mitigation: Treat vGPU assignment as an infrastructure-changing action; rely on preview, confirmation, powered-off VM requirements, and audit logging before applying changes.

Risk: The package source and exact release should be trusted before installation.

Mitigation: Verify the vmware-privateai package source and version through an internal mirror or provenance process before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational checks, setup guidance, and safety notes for VMware Private AI Foundation GPU and PAIS workflows.]

## Skill Version(s):

1.2.3 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
