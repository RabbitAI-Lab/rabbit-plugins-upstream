## Description:

Helps agents work with Gmail, Google Calendar, Drive, Sheets, Tasks, and Contacts through the gsuite-sdk Python library and CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pabloalaniz](https://clawhub.ai/user/pabloalaniz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read and manage Google Workspace mail, calendars, files, spreadsheets, tasks, and contacts on behalf of a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a connected Google account may expose private mail, files, or contacts.

Mitigation: Use least-privilege OAuth scopes and keep credentials and tokens private.

Risk: Sending mail, sharing files, deleting items, or overwriting spreadsheet data can have unintended effects.

Mitigation: Require explicit user confirmation before these actions.

Risk: Unpinned package updates can change behavior between deployments.

Mitigation: Pin package versions for repeatable deployments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pabloalaniz/skills/gsuite-sdk)
- [gsuite-sdk documentation](https://pabloalaniz.github.io/google-suite/)
- [OAuth credentials setup](https://pabloalaniz.github.io/google-suite/GETTING_CREDENTIALS/)
- [MCP server](references/mcp.md)
- [REST API and deployment](references/rest-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands can return JSON when supported.]

## Skill Version(s):

0.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
