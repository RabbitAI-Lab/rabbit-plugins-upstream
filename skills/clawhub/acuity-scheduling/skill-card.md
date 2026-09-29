## Description:

Helps agents manage Acuity Scheduling appointments, availability, clients, and calendars through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams managing appointments use this skill to check availability and client or calendar details, then schedule, reschedule, or cancel appointments with explicit approval for changes. It also explains optional user-approved scheduling automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Appointment changes or new connections may affect the wrong account or notify clients.

Mitigation: Confirm the intended account, appointment, and action before connecting or making any change; default to read-only requests.

Risk: Automations and event destinations can keep running or forwarding data until removed.

Mitigation: Get separate approval for functions, triggers, and destinations; review their scope and recipients and remove them when no longer needed.

Risk: Copied API keys or untrusted event data can expose credentials or lead to unsafe local execution.

Mitigation: Prefer device login over API keys; do not place credentials in event destinations, and review any local event handler before enabling it.

## Reference(s):

- [Acuity Scheduling skill release](https://clawhub.ai/byungkyu/skills/acuity-scheduling)
- [Maton homepage](https://maton.ai)
- [Acuity Scheduling API Quick Start](https://developers.acuityscheduling.com/reference/quick-start)
- [Acuity Scheduling OAuth2 documentation](https://developers.acuityscheduling.com/docs/oauth2)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and command examples; JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the authorized connection and its Acuity permissions.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
