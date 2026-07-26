## Description: <br>
Email To Calendar turns Gmail messages into Google Calendar events by extracting meetings, appointments, RSVP deadlines, and action items, then proposing calendar changes for user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tonimelisma](https://clawhub.ai/user/tonimelisma) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees and external users who rely on Gmail and Google Calendar use this skill to convert event-related emails into reviewed calendar entries, deadline reminders, and follow-up prompts with duplicate checks and undo support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Gmail and Google Calendar authority and can change mailbox or calendar state. <br>
Mitigation: Review setup defaults before first use and disable mark_read, archive, or auto_dispose_calendar_replies when automatic mailbox changes are not desired. <br>
Risk: Persistent workspace behavior may be modified through proposed HEARTBEAT.md changes. <br>
Mitigation: Inspect any proposed HEARTBEAT.md updates before accepting them. <br>
Risk: Local logs may contain email subjects, event titles, message IDs, and calendar metadata. <br>
Mitigation: Store the workspace in a trusted local environment and handle generated logs as potentially sensitive user data. <br>


## Reference(s): <br>
- [Setup Guide](SETUP.md) <br>
- [Email Extraction Patterns](references/extraction-patterns.md) <br>
- [Workflow Example](references/workflow-example.md) <br>
- [gog Calendar CLI Reference](references/gog-commands.md) <br>
- [gog CLI](https://github.com/tonimelisma/gogcli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with structured event summaries and shell command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local JSON state and Gmail or Google Calendar records after user confirmation.] <br>

## Skill Version(s): <br>
1.13.3 (source: frontmatter and changelog, released 2026-06-30; server release version 1.13.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
