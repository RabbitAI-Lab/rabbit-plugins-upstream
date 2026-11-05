## Description:

Work with Gmail, Google Calendar, Drive, Sheets, Tasks and Contacts, and read Search Console, Google Analytics 4 and Tag Manager, through the gsuite-sdk Python library and its `gsuite` CLI (JSON output for agents).

This skill is ready for commercial/non-commercial use.

## Publisher:

[pabloalaniz](https://clawhub.ai/user/pabloalaniz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the CLI or Python SDK to retrieve and manage Google Workspace email, calendars, files, spreadsheets, tasks and contacts, and to read Search Console, Analytics and Tag Manager data. The skill can also send messages, invite attendees, share files and change or delete records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional cloud setup exports login credentials without specifying file protection or cleanup.

Mitigation: Transfer tokens directly into Secret Manager, or use an owner-only temporary file outside repositories and build directories and remove it afterward. Grant only needed Google scopes and pin reviewed package versions.

Risk: The skill can send email, invite attendees, share files, or delete data.

Mitigation: Require user confirmation before sending, inviting, sharing, or deleting.

## Reference(s):

- [gsuite-sdk documentation](https://pabloalaniz.github.io/google-suite/)
- [Google OAuth credentials setup](https://pabloalaniz.github.io/google-suite/GETTING_CREDENTIALS/)
- [Gmail guide](artifact/references/gmail.md)
- [Calendar guide](artifact/references/calendar.md)
- [Drive guide](artifact/references/drive.md)
- [Sheets guide](artifact/references/sheets.md)
- [Tasks and Contacts guide](artifact/references/tasks-contacts.md)
- [Search Console, Analytics and Tag Manager guide](artifact/references/marketing.md)
- [REST API and deployment guide](artifact/references/rest-api.md)
- [MCP server guide](artifact/references/mcp.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON CLI responses and structured Python SDK data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or modify Google Workspace data; Search Console, Analytics and Tag Manager operations are read-only.]

## Skill Version(s):

0.10.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
