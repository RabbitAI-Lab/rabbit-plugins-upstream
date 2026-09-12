## Description:

vmware-vdi helps agents operate VMware/Omnissa Horizon VDI through a Connection Server, including desktop pools, RDS farms, published apps, sessions, machines, entitlements, health, events, statistics, and instant-clone image pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

IT operations, help-desk, and VDI platform engineers use this skill to inspect and administer Horizon broker-layer resources, troubleshoot user sessions and desktop pools, and perform controlled operational actions such as logoff, reset, entitlement changes, and image pushes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer VMware Horizon environments and may use production admin credentials.

Mitigation: Use a dedicated least-privilege Horizon account and verify the package or source before using it with production credentials.

Risk: Local credential handling can expose Horizon passwords if the generated environment file is treated as secret storage.

Mitigation: Prefer environment variables or a secret manager, and keep any local password file permission-restricted.

Risk: Disabling TLS verification can weaken connection security.

Mitigation: Keep TLS verification enabled except in isolated self-signed lab environments.

## Reference(s):

- [vmware-vdi ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vdi)
- [vmware-vdi declared source code](https://github.com/vmware-skills/VMware-VDI)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [vmware-aiops companion skill](https://github.com/vmware-skills/VMware-AIops)
- [vmware-monitor companion skill](https://github.com/vmware-skills/VMware-Monitor)
- [vmware-nsx-security companion skill](https://github.com/vmware-skills/VMware-NSX-Security)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured MCP-oriented operational guidance for Horizon administration tasks.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
