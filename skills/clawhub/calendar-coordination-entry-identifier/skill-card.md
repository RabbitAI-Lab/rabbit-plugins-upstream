## Description:

Normalize a calendar handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and agents use this skill to normalize a meeting handoff into a concise event digest from a supplied calendar event block.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar event blocks can contain sensitive meeting details.

Mitigation: Only provide calendar content that the user intends the agent to process in the current request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/calendar-coordination-entry-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, structured data]

**Output Format:** [Object with event_id, starts_at, ends_at, timezone, and duration_minutes fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Input is a user-supplied calendar event block in event_ics.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
