## Description:

Choose a timezone interpretation for unlabeled milestones while preserving explicitly labeled timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project coordinators and developers use this skill to establish a consistent timezone interpretation for milestone deadlines before entering them in a schedule register.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When a request omits a timezone, unlabeled deadlines may be interpreted in UTC rather than the intended local timezone.

Mitigation: Provide an explicit default timezone and check the returned interpretation before scheduling deadlines.

## Reference(s):

- [Deadline Locale Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/deadline-locale-guidance-identifier)

## Skill Output:

**Output Type(s):** [Guidance]

**Output Format:** [JSON containing a timezone_mode string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interpretation guidance only; does not change a calendar or persist records.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
