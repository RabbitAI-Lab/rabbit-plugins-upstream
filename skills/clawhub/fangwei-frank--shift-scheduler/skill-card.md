## Description:

Staff shift scheduling and management assistant for retail store managers and employees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fangwei-frank](https://clawhub.ai/user/fangwei-frank)

### License/Terms of Use:

MIT-0

## Use Case:

Retail store managers and employees use this skill to query shifts, handle swap and time-off requests, send reminders, and route on-call escalations to the scheduled manager.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive employee schedule and operational data.

Mitigation: Limit access to approved schedule files and accounts, and store exported JSON securely.

Risk: Public-read schedule links could expose workplace staffing information.

Mitigation: Use restricted service-account or authenticated access for Google Sheets and calendars instead of public-read links.

Risk: Schedule changes or notifications could be sent without sufficient approval.

Mitigation: Require manager confirmation before activating schedule changes or sending notifications.

## Reference(s):

- [Schedule Data Formats](artifact/references/schedule-formats.md)
- [ClawHub Skill Page](https://clawhub.ai/fangwei-frank/skills/shift-scheduler)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON schedule output and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce structured schedule JSON when using the bundled parser.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
