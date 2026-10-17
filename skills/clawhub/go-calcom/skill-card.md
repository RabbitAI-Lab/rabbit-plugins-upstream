## Description:

Guides Go developers using an unofficial typed client for Cal.com API v2 to inspect availability and manage scheduling resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Cal.com scheduling into Go applications, read availability and bookings, and manage account resources when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cal.com API credentials could be exposed in source code, logs, or request headers.

Mitigation: Supply the API key through CALCOM_API_KEY; never hardcode, commit, or log credentials or authorization headers.

Risk: Booking, schedule, team, event type, or webhook changes can alter account data.

Mitigation: Prefer read-only operations and review the intended resources before performing requested mutations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-calcom)
- [go-calcom project (skill homepage)](https://github.com/psyb0t/go-calcom)
- [Cal.com API v2 introduction](https://cal.com/docs/api-reference/v2/introduction)
- [Setup and reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Cal.com API credential for authenticated operations.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
