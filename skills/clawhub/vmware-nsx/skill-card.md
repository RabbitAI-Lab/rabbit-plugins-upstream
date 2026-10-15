## Description:

Helps operators inspect, troubleshoot, and explicitly manage VMware NSX segments, gateways, NAT, routing, IP pools, and network health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators and engineers use this skill to inspect NSX networking and health, troubleshoot connectivity, and carry out specifically requested NSX configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network configuration changes can disrupt connectivity or delete resources.

Mitigation: Use least-privilege NSX credentials, require an explicit request for each change, and review dry runs and delete previews before confirmation.

Risk: Exposed credentials or disabled TLS verification can compromise NSX access.

Mitigation: Use a secret manager for production credentials, avoid entering passwords in shell history, and keep SSL verification enabled outside isolated labs.

Risk: Write access through MCP can exceed the needs of monitoring tasks.

Mitigation: Expose read-only MCP tools for monitoring and restrict write operations to approved service accounts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-nsx)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-NSX)
- [Capabilities](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report NSX inventory and health results or propose user-requested changes.]

## Skill Version(s):

1.13.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
