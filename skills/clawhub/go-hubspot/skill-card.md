## Description:

Guidance for using an unofficial typed Go client for HubSpot APIs, including authentication, endpoint calls, and typed responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go calls to HubSpot APIs, including CRM reads and writes, and to find the matching methods, request types, authentication setup, and response handling. It is intended for Go projects that need to access HubSpot data through the go-hubspot client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A HubSpot access token could be exposed if hardcoded or written to logs.

Mitigation: Read the token from an environment variable; do not commit it, log it, or print request headers.

Risk: Create, update, merge, archive, delete, and GDPR purge calls can change live HubSpot data.

Mitigation: Make these calls only when the user requested the change and only for records within the task's scope.

Risk: The security scan has incomplete coverage because it could not resolve a local reference at the end of SKILL.md.

Mitigation: Review the setup and security guidance and resolve the missing reference before relying on scan coverage.

## Reference(s):

- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-hubspot)
- [Project homepage](https://github.com/psyb0t/go-hubspot)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and API guidance for the go-hubspot client; requires the Go toolchain.]

## Skill Version(s):

0.5.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
