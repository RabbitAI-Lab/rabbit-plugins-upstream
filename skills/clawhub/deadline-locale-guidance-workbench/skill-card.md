## Description:

Normalize milestone deadlines to UTC and retain the source timezone used for each conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams maintaining milestone schedules use this skill to interpret deadlines, record their original timezone and UTC equivalent, and optionally register the result with a configured delivery target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured HTTP or SMTP delivery can transmit normalized records and local artifact paths to an unintended recipient.

Mitigation: Use only approved endpoints and recipients, and prevent ambient delivery settings or credentials from triggering unintended submissions.

Risk: An implicit source timezone can produce an incorrect UTC deadline.

Mitigation: Supply and review explicit source timezones; disable outbound delivery if only local normalization is needed.

## Reference(s):

- [Milestone Schedule Register on ClawHub](https://clawhub.ai/wxt-ai/skills/deadline-locale-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON schedule record and local business artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retains the input deadline and source timezone; includes a delivery receipt when outbound delivery is configured.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
