## Description:

View, find, add, update, move, and delete Outlook / Microsoft calendar events, including recurring events and free-time queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lovely-qianyun](https://clawhub.ai/user/lovely-qianyun)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to let an AI agent manage a connected Outlook or Microsoft 365 default calendar with explicit operations for availability, event creation, updates, moves, deletion, and recurring-event handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires full Outlook calendar read/write authorization to view, create, modify, move, and delete calendar events.

Mitigation: Grant access only to the intended account, prefer a dedicated test account or user-owned Azure app for evaluation, and verify the connected account before calendar writes.

Risk: Login and calendar commands may automatically install missing Python packages without pinned versions.

Mitigation: Run the skill in an isolated Python environment and review or preinstall dependencies before using calendar commands.

Risk: OAuth token files can expose calendar access if stored or committed carelessly.

Mitigation: Store token files outside Git repositories, use OCAL_TOKEN_PATH for isolated credentials, and verify ignore rules for any local token directory.

Risk: Incorrectly normalized dates, times, recurrence scope, or event identity can cause unintended calendar changes.

Mitigation: Freeze absolute dates, times, timezone, target event, and requested fields before writes; read existing events before updates or deletes and verify the result afterward.

## Reference(s):

- [Command Reference](references/commands.md)
- [Recurring Events](references/recurring-events.md)
- [Configuration](references/configuration.md)
- [Troubleshooting](references/troubleshooting.md)
- [Bring-Your-Own Azure App Registration Guide](references/azure-app-setup.md)
- [Microsoft Graph recurrencePattern resource type](https://learn.microsoft.com/en-us/graph/api/resources/recurrencepattern?view=graph-rest-1.0)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and parsed JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON mode for calendar operations; diagnostics may appear on stderr.]

## Skill Version(s):

3.0.0 (source: SKILL.md metadata, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
