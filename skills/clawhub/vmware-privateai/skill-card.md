## Description:

Manage GPU inventory, vGPU profiles and assignments, and Private AI Service models and knowledge bases in VMware vSphere and VCF environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware and AI infrastructure engineers use this skill to inspect GPU capacity and Private AI Service resources, check readiness, and manage vGPU assignments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Powering off a VM to change its vGPU profile may interrupt active workloads.

Mitigation: Check workload state and obtain separate approval before shutdown; the vGPU assignment itself should only be applied to a powered-off VM.

Risk: Creating or printing an audit token can expose credential material beyond its intended use.

Mitigation: Review whether token creation is needed, handle tokens through an approved secret process, and revoke or replace any token that is exposed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Capabilities reference](artifact/references/capabilities.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured text and JSON results, with CLI commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational results depend on configured VMware and Private AI Service access.]

## Skill Version(s):

2.5.1 (source: server-resolved release metadata, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
