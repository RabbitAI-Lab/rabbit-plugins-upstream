## Description:

Use b24 to read and change a Bitrix24 portal's CRM — deals, leads, contacts (people), companies (organizations), pipelines, stages, products, employees — with the owner's profile and JSON answers; deals and leads are synced into the local WireCat store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to set up the b24 command line tool and read or update a company's Bitrix24 CRM records at the owner's direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release has a suspicious security verdict in the supplied evidence; no specific findings or explanation were provided.

Mitigation: Review the release and its publisher details before installation or execution.

Risk: CRM write operations can change real company records, and moving deals or leads may trigger portal automations.

Mitigation: Make changes only to the exact records and values requested by the owner, and use --dry-run to inspect a write before executing it.

Risk: Over MCP, an ask permission does not pause a write, and CRM responses may include client personal data.

Mitigation: Use readonly or deny permissions, or client-side approval for writes, and return only the client data needed by the owner.

## Reference(s):

- [Bitrix24 Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-b24)
- [Usage guide](https://github.com/WireCatLabs/bitrix24-cli/blob/main/docs/usage.md)
- [Permissions guide](https://github.com/WireCatLabs/bitrix24-cli/blob/main/docs/permissions.md)
- [MCP guide](https://github.com/WireCatLabs/bitrix24-cli/blob/main/docs/mcp.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions, Guidance, CRM record data]

**Output Format:** [JSON command responses and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CRM responses can contain personal information; read and write access depends on the configured profile and permissions.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
