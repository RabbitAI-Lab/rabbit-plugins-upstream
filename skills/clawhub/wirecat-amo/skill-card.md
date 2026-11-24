## Description:

Use amo to read and change an amoCRM or Kommo account's CRM - deals, pipelines and the funnel, contacts (people), companies (organizations), tasks and notes, users - with the owner's profile and JSON answers. Deals and their clients are synced into the local WireCat store, read offline, and `changes list` shows what changed for a morning digest. Use when a question could be answered from the owner's amoCRM or Kommo sales data (how a deal stands, what is open, what changed, who a client is), when the owner asks to create, move, close or change a CRM record, or to set amo up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users who manage an amoCRM or Kommo account use this skill to answer questions from CRM data, review account changes, and carry out explicitly requested record updates or setup tasks through amo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks the skill suspicious because MCP writes may proceed without required approval; scan coverage is partial.

Mitigation: Before installation or use, review MCP write permissions and require client approval for amo_write or set write permissions to readonly or deny. Treat the scan as incomplete and review the missing-path coverage caveat.

## Reference(s):

- [MCP setup and permissions](references/mcp.md)
- [Reading CRM data](references/reading.md)
- [Writing CRM records](references/writing.md)
- [Output and exit codes](references/output.md)
- [Setup guide](references/setup.md)
- [amo MCP guide](https://github.com/WireCatLabs/amo-cli/blob/main/docs/mcp.md)
- [amo permissions guide](https://github.com/WireCatLabs/amo-cli/blob/main/docs/permissions.md)
- [amo installation guide](https://github.com/WireCatLabs/amo-cli/blob/main/docs/installation.md)
- [amo usage guide](https://github.com/WireCatLabs/amo-cli/blob/main/docs/usage.md)
- [amo configuration guide](https://github.com/WireCatLabs/amo-cli/blob/main/docs/configuration.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON CRM answers, concise text, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Limit CRM details to what the owner needs.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
