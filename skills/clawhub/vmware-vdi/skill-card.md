## Description:

Operates VMware/Omnissa Horizon VDI environments through a Connection Server, including desktop pools, RDS farms, published apps, sessions, desktop machines, entitlements, events, health, statistics, and instant-clone image pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VDI administrators, help-desk operators, and infrastructure engineers use this skill to inspect and manage Horizon broker-layer resources, troubleshoot stuck sessions or desktops, manage pool access, and coordinate image-push operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external vmware-vdi package is installed and executed locally.

Mitigation: Install only from a trusted package source and verify the release before deployment.

Risk: The skill can perform powerful Horizon administration actions, including session logoff, machine reset or removal, entitlement changes, task cancellation, and image pushes.

Mitigation: Use least-privilege Horizon accounts, prefer a read-only role for monitoring, and reserve write-capable credentials for approved operations.

Risk: Stored Horizon credentials can expose administrative access if mishandled.

Mitigation: Protect credential files, use environment variables or a secret manager for real deployments, and do not treat b64-obfuscated values as encryption.

Risk: Disabling TLS verification can expose Horizon credentials and operational commands to interception.

Mitigation: Keep TLS verification enabled outside self-signed lab environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, API Calls]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP tools return structured operational data from the configured Horizon Connection Server; destructive actions support dry-run previews and confirmation flows according to the artifact documentation.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
