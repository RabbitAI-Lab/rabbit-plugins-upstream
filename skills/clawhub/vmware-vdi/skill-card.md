## Description:

Operate VMware and Omnissa Horizon VDI environments through the Connection Server, including desktop pools, sessions, machines, entitlements, health, and image operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External IT administrators and help-desk operators use the skill to inspect Horizon VDI health and manage pools, sessions, desktop machines, entitlements, and image updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disabling TLS verification could expose VDI credentials to interception; scan coverage is incomplete.

Mitigation: Keep certificate verification enabled for production targets. Use disabled verification only for isolated self-signed certificate labs, and resolve the incomplete scan references before installation.

Risk: Some write operations can interrupt user sessions or recreate every desktop in a pool during an image push.

Mitigation: Review the operation preview and its affected users and desktops before confirming; use a read-only Horizon role when changes are not needed.

## Reference(s):

- [Capabilities](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [VMware VDI repository (linked by the skill)](https://github.com/vmware-skills/VMware-VDI)
- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-vdi)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, VDI status and operation guidance]

**Output Format:** [Human-readable summaries and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations can include previews and confirmation requirements for state-changing actions.]

## Skill Version(s):

2.4.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
