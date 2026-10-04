## Description:

Creates a local milestone schedule record with an interpreted deadline and source timezone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and scheduling teams use this skill to interpret a milestone deadline and retain a local record of the input, UTC result, and source timezone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deadline conversion may silently record the wrong timezone or UTC value, particularly for named timezones, daylight saving transitions, date-only values, and unlabeled local times.

Mitigation: Use only for non-critical local testing until the publisher fixes the timezone implementation and interface contract; independently check deadline interpretations and saved records before relying on them.

## Reference(s):

- [Milestone Schedule Register on ClawHub](https://clawhub.ai/wxt-ai/skills/deadline-locale-guidance-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON registration record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a local artifact under the supplied output directory; does not modify an external calendar.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
