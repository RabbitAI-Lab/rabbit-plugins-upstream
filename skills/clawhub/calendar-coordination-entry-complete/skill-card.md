## Description:

Normalizes a calendar handoff into a coordination entry, writes a local calendar file, and optionally delivers the result to a configured target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to turn meeting calendar handoffs into local coordination entries and, when explicitly configured, submit them to a delivery target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabling HTTP delivery can send calendar details and the local artifact path to the configured endpoint.

Mitigation: Leave delivery endpoint and API-key settings unset unless delivery is intended; use a dedicated, trusted HTTPS endpoint.

## Reference(s):

- [Calendar Handoff Reader on ClawHub](https://clawhub.ai/wxt-ai/skills/calendar-coordination-entry-complete)

## Skill Output:

**Output Type(s):** [JSON, Calendar files]

**Output Format:** [JSON result and local ICS calendar file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event details, a local artifact receipt, and a delivery receipt when applicable.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
