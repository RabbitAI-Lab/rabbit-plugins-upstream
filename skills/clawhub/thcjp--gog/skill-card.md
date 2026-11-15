## Description:

Google Workspace command-line guidance for using gog to automate Gmail, Calendar, Drive, Contacts, Sheets, and Docs operations through OAuth-authenticated CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to compose and run gog CLI commands for Google Workspace search, export, mail, calendar, contact, document, and spreadsheet workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad Google Workspace reads and writes across mail, files, contacts, calendars, spreadsheets, and local outputs.

Mitigation: Authorize only the minimum Google services needed for the task and require the agent to state the account, service, target, and expected side effects before execution.

Risk: Using --no-input for sends, writes, clears, or exports can bypass interactive review of side effects.

Mitigation: Avoid --no-input for side-effecting commands unless the exact command has already been reviewed and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/gog)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, guidance, shell commands, configuration, markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide commands that read or modify Google Workspace data and local output files.]

## Skill Version(s):

1.0.1 (source: server-resolved release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
