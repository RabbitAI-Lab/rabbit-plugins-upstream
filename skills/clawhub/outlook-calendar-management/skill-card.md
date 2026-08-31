## Description:

Helps an agent manage Outlook calendar events through local Python commands, including listing, searching, adding, updating, moving, deleting, recurring-event handling, free-time lookup, and JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lovely-qianyun](https://clawhub.ai/user/lovely-qianyun)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to operate a Microsoft Outlook calendar from natural-language requests while preserving event IDs, confirmations, and read-back verification for calendar changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read, create, update, move, and delete Outlook calendar events after authorization.

Mitigation: Grant access only when this level of calendar control is acceptable, confirm destructive requests, and read back modified events before reporting completion.

Risk: Recurring-event edits or deletes can affect either one occurrence or an entire series.

Mitigation: Confirm whether the user intends a single occurrence or whole series change before executing recurring-event operations.

Risk: Authentication tokens are stored locally at ~/.outlook_cal_token.json.

Mitigation: Protect the token file with normal account-level filesystem controls and reauthorize if credentials expire or are rotated.

Risk: The first run may install Python dependencies automatically.

Mitigation: Use a virtual environment for installation and review dependency installation failures before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lovely-qianyun/skills/outlook-calendar-management)
- [Server-resolved source repository](https://github.com/Lovely-Qianyun/outlook-calendar-management)
- [Command Reference](artifact/references/commands_EN.md)
- [Configuration](artifact/references/configuration_EN.md)
- [Recurring Events](artifact/references/recurring-events_EN.md)
- [Troubleshooting](artifact/references/troubleshooting_EN.md)
- [Azure App Setup](artifact/references/azure-app-setup_EN.md)
- [Microsoft Graph calendarView](https://learn.microsoft.com/en-us/graph/api/calendar-list-calendarview?view=graph-rest-1.0)
- [Microsoft Graph recurrence pattern](https://learn.microsoft.com/en-us/graph/api/resources/recurrencepattern?view=graph-rest-1.0)
- [Microsoft identity device-code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, text]

**Output Format:** [Markdown guidance with inline shell commands; command execution may return human-readable text or structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local Python scripts to call Microsoft Graph after user device-code authorization.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter reports 2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
