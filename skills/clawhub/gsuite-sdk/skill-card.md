## Description:

Helps agents use the gsuite-sdk CLI and Python library to work with Gmail, Calendar, Drive, Sheets, Tasks, and Contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pabloalaniz](https://clawhub.ai/user/pabloalaniz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read and update Google Workspace data through the gsuite CLI or Python SDK, including email, calendars, files, spreadsheets, tasks, and contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to private Google Workspace data and locally stored OAuth tokens.

Mitigation: Grant only needed scopes, keep credential and token files private, and review data returned to the agent.

Risk: Email, sharing, deletion, or overwrite actions can affect other people or data.

Mitigation: Confirm recipients, file permissions, and targets with the user before high-impact actions.

Risk: An exposed REST API could allow unauthorized Workspace access.

Mitigation: Keep the server on localhost unless strongly authenticated and access-controlled.

Risk: An unpinned optional MCP package can change unexpectedly.

Mitigation: Pin the gsuite-mcp package version when using MCP.

## Reference(s):

- [gsuite-sdk documentation](https://pabloalaniz.github.io/google-suite/)
- [OAuth credentials setup](https://pabloalaniz.github.io/google-suite/GETTING_CREDENTIALS/)
- [Gmail reference](references/gmail.md)
- [Calendar reference](references/calendar.md)
- [Drive reference](references/drive.md)
- [Sheets reference](references/sheets.md)
- [Tasks and Contacts reference](references/tasks-contacts.md)
- [REST API and deployment reference](references/rest-api.md)
- [MCP server reference](references/mcp.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI and Python examples; JSON where supported by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI JSON output is not available for every command.]

## Skill Version(s):

0.6.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
