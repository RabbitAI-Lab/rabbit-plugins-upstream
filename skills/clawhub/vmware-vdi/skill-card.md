## Description:

Operates VMware/Omnissa Horizon VDI environments through a Connection Server for pool, farm, app, session, machine, entitlement, event, health, statistics, and instant-clone image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

IT administrators, help-desk engineers, and infrastructure operators use this skill to inspect and manage Horizon VDI broker-layer resources, troubleshoot sessions and machines, manage entitlements, and coordinate image-push operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write operations against Horizon VDI resources, including disruptive actions such as session logoff, machine reset or removal, disabling pools, task cancellation, and image pushes.

Mitigation: Install only where the operator is authorized to administer Horizon VDI, prefer read-only Horizon roles for monitoring, use write-capable credentials only when needed, and review dry-run or blast-radius output before disruptive actions.

Risk: Production credentials and Connection Server access can expose administrative authority over VDI resources.

Mitigation: Keep TLS verification enabled outside labs and use a real secret manager for production passwords.

Risk: Instant-clone image pushes can affect every desktop in a pool and may disrupt active users.

Mitigation: Check pool occupancy and session information before confirming image pushes, warn users when needed, and proceed only after the reported blast radius is understood.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run guidance, blast-radius review, and operational next steps for Horizon VDI tasks.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
