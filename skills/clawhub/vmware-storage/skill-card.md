## Description:

Use this skill to manage VMware vSphere storage, including datastores, iSCSI targets, vSAN health and capacity, and read-only Fibre Channel and multipath diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware administrators and platform engineers use it to inspect storage inventory and health, locate deployable images, and configure iSCSI storage through vSphere or ESXi.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Removing an iSCSI target can make its LUNs inaccessible, affecting storage that depends on those paths.

Mitigation: Review the operation preview and its blast radius, verify that no LUNs are in use before removal, and confirm the change explicitly.

Risk: The skill uses VMware credentials, and the documented base64 storage form for passwords is obfuscation rather than encryption.

Mitigation: Use a least-privilege account and protected local storage or a secret manager; keep vSphere certificate verification enabled.

Risk: The security scan was partial, leaving some installation and configuration details unverified because local references could not be resolved.

Mitigation: Review setup and configuration guidance from a source you trust and validate the installation before connecting credentials.

## Reference(s):

- [Project homepage](https://github.com/vmware-skills/VMware-Storage)
- [Setup and security guide](references/setup-guide.md)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Model fit self-test](https://github.com/vmware-skills/marketplace/blob/main/MODEL_FIT_SELF_TEST.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured JSON tool results with concise natural-language summaries and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes storage inventory and diagnostics; state-changing iSCSI operations require explicit confirmation.]

## Skill Version(s):

2.6.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
