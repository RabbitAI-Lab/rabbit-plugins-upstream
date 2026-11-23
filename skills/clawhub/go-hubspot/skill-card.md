## Description:

Unofficial Go client for the HubSpot API that provides typed methods across HubSpot's 2026-03 API, bearer token authentication, and typed JSON responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the go-hubspot client to a Go project and write typed requests for HubSpot CRM and related API data. It provides setup, credential, endpoint lookup, and response handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot operations can create, update, merge, archive, delete, or purge live account data.

Mitigation: Use mutating operations only when requested, and only for records in the task's scope.

Risk: Access tokens can expose HubSpot account data if they are committed or logged.

Mitigation: Read tokens from environment variables and do not hardcode, commit, or log them or request headers.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [Project homepage](https://github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and setup guidance for integrating the typed Go client; outputs depend on the user's task.]

## Skill Version(s):

0.5.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
