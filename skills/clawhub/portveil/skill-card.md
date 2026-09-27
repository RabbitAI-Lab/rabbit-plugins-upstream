## Description:

Helps an agent check and control Portveil VPN devices, including changing exit locations, scheduling rotations, reconnecting, and adding devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[roybogs](https://clawhub.ai/user/roybogs)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams running agents use this skill to inspect device protection and manage Portveil VPN connections and exit locations through Hermes.

### Deployment Geography for Use:

Global; documented VPN exit locations are the US and Finland.

## Known Risks and Mitigations:

Risk: A compromised API token could expose device information or allow network changes within its scope.

Mitigation: Use a separate read-only token first, grant control or admin only when necessary, keep it private, and revoke it if exposed.

Risk: Moving, disconnecting, or removing a device can disrupt its network access; scheduled rotation continues after the session ends.

Mitigation: Act only on the account owner's request, confirm ambiguous or destructive actions, and confirm rotation settings before starting them.

Risk: Device tunnel files contain private keys when a phone or laptop is added.

Mitigation: Transfer tunnel files privately to the intended device, remove temporary copies, and never print or share private keys.

## Reference(s):

- [Portveil homepage](https://portveil.com)
- [Portveil dashboard](https://portveil.com/dashboard/)
- [Portveil device setup](https://portveil.com/start/)
- [portveil-mcp release notes](https://github.com/roybogs/portveil-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown and plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide device status, exit location, and setup commands; VPN controls require an appropriately scoped token.]

## Skill Version(s):

1.0.2 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
