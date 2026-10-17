## Description:

Helps administrators inspect and manage VMware/Omnissa Horizon desktop pools, user sessions, machines, entitlements, health, and instant-clone image updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Horizon administrators and help-desk staff use this skill to investigate VDI health and sessions, manage pools and entitlements, and carry out approved desktop and image operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative actions can disrupt user sessions or replace desktops across a pool.

Mitigation: Use a least-privilege Horizon account, expose read-only tools by default, review the affected users and desktops, and obtain explicit approval before writes.

Risk: Stored Horizon credentials may be exposed if local files are compromised; documented base64 storage is not encryption.

Mitigation: Keep production passwords in a secret manager and restrict access to credential files.

Risk: Disabling TLS verification can expose Horizon connections to interception.

Mitigation: Keep TLS verification enabled outside isolated labs.

## Reference(s):

- [vmware-vdi on ClawHub](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read operations and previews can inform explicit confirmation before state-changing actions.]

## Skill Version(s):

2.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
