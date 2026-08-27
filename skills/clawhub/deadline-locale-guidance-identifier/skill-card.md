## Description:

Choose a timezone interpretation for unlabeled milestones while preserving explicitly labeled timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and schedule coordinators use this skill to define a consistent timezone interpretation policy for milestone notes that mix explicitly labeled timestamps with unlabeled deadlines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unlabeled or date-only deadlines can be interpreted differently across teams if UTC fallback and local cutoff expectations are not confirmed.

Mitigation: Confirm the default timezone, UTC fallback, daylight-saving date, and date-only handling with the schedule owner before applying the policy.

## Reference(s):

- [Deadline Locale Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/deadline-locale-guidance-identifier)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Concise string in the timezone_mode field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defines interpretation only and does not modify calendars or schedule registers.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
