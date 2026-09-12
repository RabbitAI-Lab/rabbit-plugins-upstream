## Description:

Reads enterprise Microsoft 365 Outlook calendar events so an agent can answer questions about schedules, meetings, work items, and date ranges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ilove323](https://clawhub.ai/user/ilove323)

### License/Terms of Use:


## Use Case:

Employees and agents use this skill to retrieve Microsoft 365 Outlook calendar events for today, tomorrow, the current week, a month, or a custom date range, then summarize events or meeting time for the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact stores Microsoft 365 credentials and reusable cookies or bearer tokens under ~/.outlook.

Mitigation: Use only on trusted single-user machines, restrict ~/.outlook filesystem permissions, remove stale session files, and avoid shared or multi-tenant environments.

Risk: Reusable session material could allow calendar access beyond the immediate request if copied or exposed.

Mitigation: Prefer a Microsoft OAuth or Graph integration with calendar-read-only scope and rotate or delete cookies and token caches after use.

Risk: Debug screenshots and status logs may be written during login and can contain sensitive sign-in context.

Mitigation: Review and delete debug images and login status files after authentication, especially before sharing logs or packaging the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ilove323/skills/outlook-calendar)
- [Microsoft sign-in endpoint used by the artifact](https://login.microsoftonline.com)
- [Outlook calendar endpoint used by the artifact](https://outlook.office.com/calendar/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text or JSON calendar event summaries, with shell commands and configuration steps for setup and reauthentication.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calendar API times are returned as UTC in the artifact guidance and may need conversion for the user's locale.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
