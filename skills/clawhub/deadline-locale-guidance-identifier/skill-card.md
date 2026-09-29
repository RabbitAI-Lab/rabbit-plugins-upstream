## Description:

Choose a timezone interpretation for unlabeled milestones while preserving explicitly labeled timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project coordinators and scheduling agents use this skill to choose a default timezone for unlabeled milestone deadlines while keeping explicitly labeled timestamps intact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An omitted or unsupported timezone can cause unlabeled deadlines to default to UTC.

Mitigation: Provide an explicit supported timezone and verify the returned policy before using it for scheduling.

Risk: The helper is too narrow for precise daylight-saving, legal, or compliance deadline conversion.

Mitigation: Validate actual deadline instants with a date-aware timezone tool and obtain appropriate review for high-stakes deadlines.

## Reference(s):

- [Deadline Locale Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/deadline-locale-guidance-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON with a timezone_mode string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes timezone interpretation; does not update a calendar or schedule.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
