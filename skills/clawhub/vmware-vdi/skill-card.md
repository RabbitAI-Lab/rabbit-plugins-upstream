## Description:

Operates VMware/Omnissa Horizon VDI environments through the Connection Server, including desktop pools, RDS farms, published apps, sessions, desktop machines, entitlements, events, health, statistics, and instant-clone image pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

IT administrators, help-desk staff, and developers use this skill to inspect Horizon health and sessions, run diagnostics, and perform controlled VDI administration actions such as logoff, reset, entitlement updates, pool enablement, task cancellation, and instant-clone image pushes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable operations can log off sessions, reset or remove desktops, modify entitlements, cancel tasks, or push images across a pool.

Mitigation: Use a read-only Horizon account for monitoring, separate write-capable credentials for administration, and review blast-radius previews before approving write actions.

Risk: The skill stores Horizon connection credentials locally for configured targets.

Mitigation: Protect ~/.vmware-vdi/.env, keep configuration permissions restrictive, and prefer secret-manager injection for production credentials.

Risk: Pool image pushes can affect many desktops and active users.

Mitigation: Review affected desktop and in-session user counts before approval, communicate planned maintenance, and avoid proceeding when occupancy or attribution is unknown.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool calls and blast-radius previews for write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
