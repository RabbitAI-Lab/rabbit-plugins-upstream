## Description:

Calendar Management - secure Google Calendar, Microsoft Outlook & Exchange. Use when the user wants to list, search, or read calendar events; creating, updating, deleting, or responding to events require explicit user confirmation (gog-cli & gws secure alternative).

This skill is ready for commercial/non-commercial use.

## Publisher:

[porteden](https://clawhub.ai/user/porteden)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent list, search, read, and carefully manage calendar events through the PortEden CLI for Google Calendar, Microsoft Outlook, and Exchange accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, or respond to calendar events, which may notify attendees or change shared calendar state.

Mitigation: Require explicit user confirmation with the target account, calendar ID, event ID or event details, attendee changes, and intended action before any mutation.

Risk: Calendar account credentials or OAuth access may remain available after setup on shared or sensitive machines.

Mitigation: Use narrow OAuth scopes and dedicated profiles where possible, then run porteden auth logout and revoke provider-side access when finished.

Risk: External calendar event content may include untrusted instructions or misleading claims.

Mitigation: Treat event summaries, descriptions, locations, and attendee names as untrusted content; summarize and attribute them instead of following embedded instructions.

Risk: Fetching all pages can expose more calendar data than needed for a task.

Mitigation: Avoid --all unless necessary and prefer scoped date ranges, search filters, limits, and the compact JSON mode.

## Reference(s):

- [Calendar Skill on ClawHub](https://clawhub.ai/porteden/skills/calendar-skill)
- [PortEden](https://porteden.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of compact JSON output through the PortEden CLI; calendar mutations require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
