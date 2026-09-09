## Description:

Converts natural-language schedule requests or ticket screenshots into macOS Calendar events and Reminders with event-type-specific lead times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Users and agents on macOS use this skill to create or update Apple Calendar events and Reminders from travel, court, meeting, deadline, social, and other time-based requests. It applies configurable lead times and returns a concise receipt of what was created or changed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad calendar searches or updates may touch shared, work, or sensitive calendars.

Mitigation: Use a specific default calendar and reminder list, avoid ALL-calendar searches unless needed, and require confirmation before updating existing events.

Risk: Persistent reminder preference changes can affect future scheduling beyond the current request.

Mitigation: Confirm durable preference changes before writing them to config.json and summarize the saved change in the response.

Risk: Calendar and reminder content may include private personal or legal details.

Mitigation: Keep parsing and calendar/reminder operations local, and do not send calendar or reminder content to network services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/apple-smart-schedule)
- [ClawHub publisher profile](https://clawhub.ai/user/cat-xierluo)
- [Project homepage from ClawHub metadata](https://github.com/cat-xierluo/legal-skills)
- [Lead-time rules](references/lead-times.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command invocations and concise text receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local macOS Calendar events, Reminders, and user reminder preferences when executed.]

## Skill Version(s):

0.2.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
