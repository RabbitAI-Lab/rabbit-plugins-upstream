## Description:

Scans tomorrow's Outlook calendar each night at 22:00, schedules Feishu reminders for morning and afternoon events, and sends a scan summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ilove323](https://clawhub.ai/user/ilove323)

### License/Terms of Use:


## Use Case:

Users who rely on Outlook calendar and Feishu notifications use this skill to create timed reminders for the next day's meetings and receive a daily calendar scan summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can repeatedly send private Outlook calendar details to a bundled Feishu recipient.

Mitigation: Replace the Feishu open_id before any run, and consider rewriting the code so it refuses to send messages until an explicit recipient is configured.

Risk: The skill registers recurring and one-time cron jobs that scan Outlook calendar data and deliver reminders.

Mitigation: Review the scheduled cron entry, confirm the Asia/Shanghai timing matches the intended use, and remove unwanted jobs before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ilove323/skills/calendar-reminder)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration]

**Output Format:** [Markdown with inline shell and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates OpenClaw cron entries and Feishu notification messages.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
