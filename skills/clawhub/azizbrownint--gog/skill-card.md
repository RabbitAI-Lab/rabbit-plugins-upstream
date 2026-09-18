## Description:

Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to set up and run gog commands for Gmail, Calendar, Drive, Contacts, Sheets, and Docs workflows that require Google OAuth access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide commands that access selected Google services through OAuth.

Mitigation: Grant only the minimum Google services needed for the task and review the OAuth services before use.

Risk: The skill can guide commands that send email, change calendar events, or modify Sheets data.

Mitigation: Manually confirm email sending, calendar changes, and Sheets modifications before running the generated commands.

## Reference(s):

- [gog homepage](https://gogcli.sh)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/gog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OAuth setup guidance, account-selection notes, and optional JSON-output command examples.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
