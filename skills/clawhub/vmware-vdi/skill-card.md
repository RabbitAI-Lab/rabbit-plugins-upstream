## Description:

VMware VDI helps agents operate VMware/Omnissa Horizon broker environments through a Connection Server, including desktop pools, RDS farms, published apps, user sessions, desktop machines, entitlements, health, events, statistics, and instant-clone image pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

IT operations, help-desk, and VDI platform teams use this skill to inspect and administer Horizon desktop pools, sessions, machines, entitlements, events, health, statistics, and image-push tasks. It is intended for Horizon broker-layer operations, not underlying vCenter VM lifecycle, read-only vSphere monitoring, or NSX microsegmentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes powerful Horizon administration actions such as image pushes, machine removals, resets, entitlement changes, and user logoffs.

Mitigation: Limit installation to Horizon VDI operators, use read-only Horizon roles for monitoring, reserve tightly scoped admin roles for writes, and require human approval for production-changing actions.

Risk: Horizon credentials and TLS settings are required for operation.

Mitigation: Keep TLS verification enabled, use verify_ssl:false only for self-signed lab certificates, and store passwords through a real secret manager when possible.

Risk: The artifact notes beta validation status for some live Horizon response projections.

Mitigation: Run vmware-vdi init and vmware-vdi doctor against a real Horizon environment before production use, then verify session, machine, pool, image-push, and entitlement outputs.

## Reference(s):

- [VMware VDI ClawHub page](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets a configured Horizon Connection Server through VMWARE_VDI_CONFIG and ~/.vmware-vdi/config.yaml.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
