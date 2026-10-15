## Description:

Helps agents inspect and administer VMware and Omnissa Horizon desktop pools, user sessions, machines, entitlements, and instant-clone images through a Connection Server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Horizon administrators and help-desk teams use this skill to investigate VDI health and sessions and, when authorized, manage desktop pools, machines, entitlements, and image updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can disconnect users, reset or remove desktops, change access, or push images across a pool.

Mitigation: Start with a read-only Horizon service account and expose read-only tools by default; grant write access only for approved workflows and review the impact preview before confirming.

Risk: High-privilege credentials stored in a local environment file can be exposed if the host is compromised.

Mitigation: Use a secret manager where available and avoid storing high-privilege passwords in the local .env file.

## Reference(s):

- [ClawHub vmware-vdi release](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown guidance, CLI commands, and structured MCP responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results describe Horizon resources; proposed writes include an impact preview and require confirmation.]

## Skill Version(s):

2.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
