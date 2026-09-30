## Description:

Helps agents manage Google Calendar events, calendars, and availability through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to check availability, list calendars and events, and create or update meetings with their approval. It also documents optional scheduled or event-driven automation through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an unintended Google Calendar account or granting unnecessary access.

Mitigation: Confirm the intended account and requested access before authorizing a new connection.

Risk: Calendar changes may modify or cancel events and notify other participants.

Mitigation: Check the exact calendar, event, participants, and proposed change; obtain explicit approval before every write.

Risk: Hosted functions, triggers, or destinations can keep processing or forwarding data without further prompts.

Mitigation: Approve each automation separately after reviewing the data flow, destination host, and how long it will run.

## Reference(s):

- [Google Calendar skill release on ClawHub](https://clawhub.ai/byungkyu/skills/google-calendar-api)
- [Maton](https://maton.ai)
- [Google Calendar API reference](https://developers.google.com/calendar/api/v3/reference)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calendar results depend on the permissions of the user's connected account.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
