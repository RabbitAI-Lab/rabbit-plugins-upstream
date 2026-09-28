## Description:

Derive obligation schedules and append renewal schedule records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agreement operations users use this skill to turn supplied agreement text into a concise renewal obligation schedule and to append approved obligation entries to a renewal schedule.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Schedule entries could be appended to the wrong renewal schedule or before the obligation schedule has been approved.

Mitigation: Confirm the append_renewal_schedule tool target and review the obligation_schedule content before allowing schedule entries to be appended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/agreement-renewal-desk)

## Skill Output:

**Output Type(s):** [text, structured data]

**Output Format:** [JSON-like objects containing obligation_schedule or schedule_receipt fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an obligation schedule with agreement_id and obligations, or a schedule receipt with schedule_id and rows.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
