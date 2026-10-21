## Description:

Helps administrators inspect and manage Horizon desktop pools, sessions, machines, entitlements, health, and instant-clone image updates through a Connection Server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Horizon administrators and help-desk teams use this skill to diagnose VDI health and provisioning, inspect sessions and entitlements, and perform approved broker-layer actions such as logoffs, machine resets, and image updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative actions can disconnect users, reset desktops, change access, or recreate a pool's desktops.

Mitigation: Use a read-only Horizon account by default; review the affected resources and obtain user confirmation before enabling and executing writes.

Risk: Horizon credentials and remote management access require protection.

Mitigation: Use a production secret manager for passwords and keep the management connection local unless the network deployment is hardened.

## Reference(s):

- [ClawHub vmware-vdi release](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions may include a preview of affected resources before confirmation.]

## Skill Version(s):

2.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
