## Description:

Helps agents read and manage Zoho calendars, events, and meeting schedules through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to look up calendar availability, schedule meetings, and create, update, or delete Zoho Calendar events. It can also guide approved automations through Maton functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected account may expose sensitive calendar details.

Mitigation: Review connection scopes and share only the details needed for the task.

Risk: Calendar changes can reschedule meetings or notify attendees.

Mitigation: Confirm each write with the user before execution.

Risk: Triggers and destinations may run repeatedly or forward data until removed.

Mitigation: Get explicit approval for automation and destinations, review recipients, and remove them when no longer needed.

## Reference(s):

- [Zoho Calendar skill listing](https://clawhub.ai/byungkyu/skills/zoho-calendar)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Zoho Calendar API introduction](https://www.zoho.com/calendar/help/api/introduction.html)
- [Zoho Calendar events API](https://www.zoho.com/calendar/help/api/events-api.html)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown guidance with command examples and API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Zoho Calendar connection through Maton.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
