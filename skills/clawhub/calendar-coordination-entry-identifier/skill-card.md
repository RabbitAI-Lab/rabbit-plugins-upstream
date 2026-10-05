## Description:

Normalize a calendar handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and assistants use a supplied calendar event to produce a concise meeting handoff with its event ID, start and end times, timezone, and duration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The digest may expose meeting location and raw calendar timestamps beyond the normalized fields.

Mitigation: Review the digest and remove sensitive details before sharing it.

## Reference(s):

- [Calendar Handoff Reader on ClawHub](https://clawhub.ai/wxt-ai/skills/calendar-coordination-entry-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON event digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event ID, start and end times, timezone, and duration; may also include location and raw calendar timestamps.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
