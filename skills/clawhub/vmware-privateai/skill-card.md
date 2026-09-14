## Description:

vmware-privateai helps agents inspect and operate the GPU and model-serving layer of VMware Private AI Foundation with NVIDIA, including GPU inventory, vGPU consumers and profiles, utilization, PAIS models and knowledge bases, and powered-off vGPU profile assignment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inventory VMware GPU resources, inspect vGPU utilization and PAIS model-serving assets, and prepare or apply a powered-off vGPU profile change with confirmation and audit controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer path can fetch runtime code while the package handles VMware and PAIS credentials.

Mitigation: Pin and verify vmware-privateai==1.2.0 where possible, prefer the installed console script over uvx fallback, and review the exact package release before deployment.

Risk: The skill handles vCenter credentials and PAIS bearer tokens.

Mitigation: Use a dedicated least-privilege VMware service account, separate read-only credentials from vGPU-write credentials, and prefer short-lived secret-manager injection over persistent .env storage.

Risk: The skill includes one infrastructure-changing vGPU assignment operation.

Mitigation: Run the read-only vgpu_profile_validate check and dry-run preview first, require the VM to be powered off, require confirmation before applying, and review audit records after changes.

## Reference(s):

- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational warnings, dry-run previews, pagination hints, and audit or approval guidance.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
