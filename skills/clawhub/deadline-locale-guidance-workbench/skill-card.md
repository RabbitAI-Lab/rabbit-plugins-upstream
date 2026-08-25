## Description:

Normalize milestone deadlines to UTC and retain the source timezone used for each conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, scheduling agents, and external workflow users use this skill to normalize milestone deadlines to UTC while preserving the source deadline text and timezone interpretation for traceability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unlabeled local deadlines can be converted using an unintended default timezone.

Mitigation: Confirm the intended default timezone in timezone_mode before use and preserve source_timezone with the original input_deadline.

Risk: Impossible local times, such as daylight-saving transition gaps, could produce misleading UTC deadlines if shifted silently.

Mitigation: Reject impossible local times and require a corrected deadline or explicit timezone label.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/deadline-locale-guidance-workbench)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured schedule record with input_deadline, utc_deadline, and source_timezone fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves date-only inputs when no cutoff is provided and rejects impossible local times.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
