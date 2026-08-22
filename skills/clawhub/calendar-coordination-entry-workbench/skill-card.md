## Description:

Create a coordination calendar entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and scheduling assistants use this skill to turn a normalized event digest into a concise calendar artifact with ICS content for meeting coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect or incomplete event digest values can produce an inaccurate calendar entry.

Mitigation: Verify event_id, start time, end time, timezone, and duration before using the generated ICS content.

Risk: Meeting details may include sensitive scheduling information.

Mitigation: Provide only the event fields needed to create the calendar artifact and avoid unnecessary private details.

## Reference(s):

- [Coordination Calendar Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/calendar-coordination-entry-workbench)

## Skill Output:

**Output Type(s):** [Text, Configuration]

**Output Format:** [JSON-compatible object with ICS calendar text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns artifact_id, event_id, and ics_content; it does not directly access or modify calendar accounts.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
