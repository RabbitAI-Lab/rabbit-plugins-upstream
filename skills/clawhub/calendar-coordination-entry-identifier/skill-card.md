## Description:

Normalizes a supplied calendar event into a concise meeting handoff digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People coordinating meetings use this skill to turn a supplied calendar event into an event ID, start and end times, timezone, and duration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The returned digest can expose meeting location and raw timestamps alongside the core fields.

Mitigation: Provide only calendar events whose location and timestamp details are appropriate to include in the returned digest.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/calendar-coordination-entry-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON event digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event ID, start and end times, timezone, and duration; may also include location and raw timestamps.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
