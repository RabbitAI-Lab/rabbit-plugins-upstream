## Description:

Use this skill to operate a VMware/Omnissa Horizon VDI environment through its Connection Server, including desktop pools, RDS farms, published apps, user sessions, desktop machines, entitlements, events, health, statistics, and instant-clone image pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT operations staff, and help-desk operators use this skill to inspect and administer Horizon VDI broker-layer resources, troubleshoot user sessions and pool health, manage entitlements, and carry out controlled operational actions such as logoff, desktop reset, task cancellation, and golden-image push.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform powerful Horizon administration actions, including logging off users, resetting or removing desktops, changing entitlements, cancelling tasks, and pushing images.

Mitigation: Use least-privilege Horizon accounts, prefer read-only roles for monitoring, grant write privileges only to authorized operators, and require review of blast-radius previews before confirmed actions.

Risk: Golden-image pushes and some desktop operations can affect many desktops or active user sessions.

Mitigation: Use dry-run or preview flows, check session and occupancy data, warn affected users when appropriate, and rely on the documented confirmation gates and audit logging.

Risk: Local password storage is documented as b64 obfuscation rather than encryption.

Mitigation: Prefer a real secret manager for production credentials and protect local configuration and environment files with restrictive filesystem permissions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities Reference](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON/YAML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Horizon resource identifiers, blast-radius previews, troubleshooting steps, and setup or MCP configuration guidance.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata and artifact install instructions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
