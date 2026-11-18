## Description:

Use amo to read, summarize, set up, and change an owner's amoCRM or Kommo sales records, with JSON answers and local sync support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

CRM owners and their assistants use the skill to inspect sales records, summarize deal changes, set up the CLI, and make explicitly requested updates in amoCRM or Kommo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP writes may run without interactive confirmation, and moving or closing a deal can trigger CRM automation that messages or bills clients.

Mitigation: Review MCP write behavior before connecting a live CRM; configure readonly or deny permissions, or require approval in the MCP client for writes that need owner confirmation.

Risk: The security evidence is incomplete, and the available finding does not explain all of the suspicious verdict.

Mitigation: Review the MCP write and confirmation behavior and resolve outstanding security questions before installing against a live CRM.

## Reference(s):

- [Reading the CRM](references/reading.md)
- [Writing to the CRM](references/writing.md)
- [amo over MCP](references/mcp.md)
- [Output and exit codes](references/output.md)
- [Setting amo up](references/setup.md)
- [WireCat amo MCP guide](https://github.com/WireCatLabs/amo-cli/blob/main/docs/mcp.md)
- [WireCat amo permissions guide](https://github.com/WireCatLabs/amo-cli/blob/main/docs/permissions.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [JSON answers with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
