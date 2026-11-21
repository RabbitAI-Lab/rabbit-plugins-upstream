## Description:

Use amo to read and change an amoCRM or Kommo account's CRM - deals, pipelines and the funnel, contacts (people), companies (organizations), tasks and notes, users - with the owner's profile and JSON answers. Deals and their clients are synced into the local WireCat store, read offline, and `changes list` shows what changed for a morning digest. Use when a question could be answered from the owner's amoCRM or Kommo sales data (how a deal stands, what is open, what changed, who a client is), when the owner asks to create, move, close or change a CRM record, or to set amo up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can ask an agent to answer questions from an amoCRM or Kommo account, review recent CRM changes, or carry out specifically requested record updates. They can also use it to set up the amo CLI integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP writes may change CRM records without a required confirmation; a deal move can also trigger messages or invoices through the account's automation.

Mitigation: Review write permissions before connecting the account. Set sensitive MCP writes to readonly or deny, or enable approval for amo_write in the MCP client.

## Reference(s):

- [Amo Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-amo)
- [MCP reference](references/mcp.md)
- [Reading reference](references/reading.md)
- [Writing reference](references/writing.md)
- [Setup reference](references/setup.md)
- [Output and exit codes](references/output.md)
- [MCP documentation](https://github.com/WireCatLabs/amo-cli/blob/main/docs/mcp.md)
- [Permissions documentation](https://github.com/WireCatLabs/amo-cli/blob/main/docs/permissions.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON CRM answers with concise explanatory text, plus shell commands and configuration guidance when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CRM data is scoped to the selected profile; writes should match the owner's explicit request.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
