## Description:

Read and write the signed-in user's Microsoft 365 / Outlook.com personal calendar via Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users can use this skill through an agent to inspect upcoming Outlook calendar events, create or update single events, delete events by id, and check token status for a signed-in Microsoft account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports Microsoft Graph permissions beyond calendar access may be requested, including contacts and tasks write permissions.

Mitigation: Review the Microsoft consent prompt during setup and prefer a release that limits delegated scopes to calendar access unless contacts or tasks access is intentional.

Risk: The security evidence reports token handling risks around locally stored Microsoft credentials.

Mitigation: Use a dedicated low-privilege Microsoft app registration or account where possible, keep local token files private, and clear stored tokens when the skill is no longer needed.

Risk: Calendar write and delete operations can modify user calendar data.

Mitigation: Use dry-run output to inspect proposed changes and require explicit confirmation before applying writes or deletes.

## Reference(s):

- [Outlook Calendar ClawHub listing](https://clawhub.ai/guoxh/skills/outlook-calendar)
- [Microsoft Graph calendar reference](references/graph-calendar.md)
- [Microsoft Graph documentation](https://learn.microsoft.com/graph/)
- [Microsoft Graph endpoint](https://graph.microsoft.com)
- [Microsoft identity platform endpoint](https://login.microsoftonline.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with shell commands and JSON or tabular calendar output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads and writes Microsoft Graph calendar data for the signed-in account; write and delete flows require explicit apply and confirmation controls.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
