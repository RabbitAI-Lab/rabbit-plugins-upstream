## Description:

Advise deadline timezone policy and record UTC milestone conversions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams coordinating project milestones use this skill to choose timezone handling for unlabeled deadlines, preserve explicitly labeled timestamps, and record UTC conversions without changing external calendars.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect timezone interpretation can shift milestone deadlines.

Mitigation: Review the selected timezone_mode and recorded_timezone values before relying on them for scheduling decisions, especially around daylight-saving changes.

Risk: Users could mistake the output for a calendar update or invitation.

Mitigation: Treat the output as guidance and a traceable schedule record only; the skill documentation states that it does not alter external calendars.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/milestone-schedule-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [guidance, text, configuration]

**Output Format:** [Concise text strings and structured deadline records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces timezone_mode guidance and recorded_timezone records with input_deadline, utc_deadline, and source_timezone fields.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
