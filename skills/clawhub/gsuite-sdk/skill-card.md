## Description:

Helps agents use the gsuite-sdk Python library and CLI to work with Gmail, Calendar, Drive, Sheets, Tasks and Contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pabloalaniz](https://clawhub.ai/user/pabloalaniz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read and manage Google Workspace email, calendars, files, spreadsheets, tasks and contacts through the CLI or Python SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Google Workspace permissions could expose private account data.

Mitigation: Use only the OAuth scopes needed for the task and keep credentials and token files private.

Risk: Sending mail, inviting attendees, sharing files, or changing and deleting data can affect other people or overwrite work.

Mitigation: Require explicit user confirmation before sending, inviting, sharing, overwriting spreadsheets, or deleting data.

Risk: An exposed REST server without authentication could allow unauthorized account actions.

Mitigation: Keep the server private and require an API key or equivalent access controls.

## Reference(s):

- [gsuite-sdk documentation](https://pabloalaniz.github.io/google-suite/)
- [Google Cloud credential setup](https://pabloalaniz.github.io/google-suite/GETTING_CREDENTIALS/)
- [Gmail reference](artifact/references/gmail.md)
- [Calendar reference](artifact/references/calendar.md)
- [Drive reference](artifact/references/drive.md)
- [Sheets reference](artifact/references/sheets.md)
- [Tasks and Contacts reference](artifact/references/tasks-contacts.md)
- [REST API and deployment reference](artifact/references/rest-api.md)
- [MCP server reference](artifact/references/mcp.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Python and CLI examples; JSON for supported CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some CLI commands do not support JSON output.]

## Skill Version(s):

0.5.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
