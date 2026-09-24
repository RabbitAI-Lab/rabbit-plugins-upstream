## Description:

Calendar management skill for working with Google Calendar, Microsoft Outlook, and Exchange schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to manage calendar events, cross-platform calendar views, and meeting scheduling across Google Calendar, Outlook, and Exchange. Because calendar data can be sensitive, users should apply it only to explicit calendar tasks with appropriate provider permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation is materially inconsistent and mixes calendar management with unrelated security-audit and project-management claims.

Mitigation: Review the skill before installation and constrain use to explicit calendar-management tasks.

Risk: Calendar events and scheduling context may contain sensitive personal or business information.

Mitigation: Avoid sharing sensitive event details unless provider permissions, data handling, and access scope are clear.

Risk: The skill may create, modify, sync, or share calendar events.

Mitigation: Require user confirmation before any event creation, modification, synchronization, or sharing action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/calendar-skill)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or describe calendar operations that should be confirmed before events are created, modified, synced, or shared.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
