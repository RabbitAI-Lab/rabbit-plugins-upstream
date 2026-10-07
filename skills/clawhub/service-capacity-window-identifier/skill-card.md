## Description:

Formats a requested service-capacity date and time as a timezone-aware capacity window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service planners use this skill to turn a requested date, time, and supported timezone into a timestamp for a capacity window. It does not confirm availability or make a reservation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Only UTC and Asia/Shanghai timezones are accepted.

Mitigation: Convert other requested times to a supported timezone before use and check the resulting offset.

Risk: The calculated window may be mistaken for a confirmed reservation or persisted record.

Mitigation: Verify availability and record any reservation separately; this skill only returns a timestamp.

## Reference(s):

- [Service Capacity Window Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/service-capacity-window-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The capacity_window field contains a timezone-aware date-time; no business artifact is saved.]

## Skill Version(s):

1.1.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
