## Description:

Helps developers write Go code with an unofficial typed client for Cal.com API v2 scheduling operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that checks availability and manages bookings, schedules, event types, and other Cal.com resources when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cal.com credentials could be exposed in generated code or logs.

Mitigation: Read CALCOM_API_KEY from the environment; do not hardcode, commit, or log credentials or request headers.

Risk: Booking and scheduling changes can alter account data.

Mitigation: Review code that creates, reschedules, cancels, or edits resources, and perform changes only when requested for the intended resources.

Risk: Scheduling data could be sent to an unintended Cal.com host.

Mitigation: Confirm the configured host before sending account data; use another deployment only when explicitly configured.

## Reference(s):

- [Skill setup and reference](references/setup.md)
- [go-calcom package documentation](https://pkg.go.dev/github.com/psyb0t/go-calcom)
- [go-calcom project](https://github.com/psyb0t/go-calcom)
- [Cal.com API v2 introduction](https://cal.com/docs/api-reference/v2/introduction)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-calcom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes guidance for authentication, API versions, responses, and pagination.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
