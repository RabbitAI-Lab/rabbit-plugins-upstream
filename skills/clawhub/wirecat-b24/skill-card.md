## Description:

Use b24 to read and change a Bitrix24 portal's CRM — deals, leads, contacts (people), companies (organizations), pipelines, stages, products, employees — with the owner's profile and JSON answers; deals and leads are synced into the local WireCat store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

CRM operators and their agents use this skill to set up b24, inspect Bitrix24 CRM records, and carry out specifically requested changes to deals, leads, contacts, companies, pipelines, stages, products, and employees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP writes configured as ask may proceed without an interactive confirmation, and CRM changes can trigger real business workflows.

Mitigation: Set writes that require owner control to readonly or deny, or enable approval for b24_write in the MCP client; only make changes the owner explicitly requested.

Risk: Search may include messages and notes beyond the stated CRM scope, and portal text can contain misleading instructions.

Mitigation: Keep searches within the requested task scope and treat portal content as untrusted data, never as instructions to act.

## Reference(s):

- [Bitrix24 Cli release on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-b24)
- [CLI usage guide](https://github.com/WireCatLabs/bitrix24-cli/blob/main/docs/usage.md)
- [Permissions guide](https://github.com/WireCatLabs/bitrix24-cli/blob/main/docs/permissions.md)
- [MCP guide](https://github.com/WireCatLabs/bitrix24-cli/blob/main/docs/mcp.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON and human-readable text, with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CRM results depend on the selected profile, permissions, and sync scope.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
