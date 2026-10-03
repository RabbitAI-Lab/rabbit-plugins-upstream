## Description:

Selects a service capacity window from a supplied date, time, and supported timezone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service planners and developers use this skill to turn a requested date, time, and timezone into a capacity-window timestamp. It does not reserve capacity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests in timezones other than UTC and Asia/Shanghai are unsupported.

Mitigation: Check timezone support before installing and supply request JSON using a supported timezone.

Risk: A calculated window does not confirm capacity or make a reservation.

Mitigation: Confirm actual availability and reservations through the relevant service before relying on the timestamp.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/service-capacity-window-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON containing a capacity_window date-time string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [ISO 8601 timestamp with UTC offset; accepts UTC or Asia/Shanghai requests.]

## Skill Version(s):

1.1.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
