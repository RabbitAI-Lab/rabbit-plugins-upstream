## Description:

Provides unofficial, typed Go clients for eToro's public REST API and WebSocket streams, generated from eToro-published specifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with eToro's public REST API and WebSocket streams through typed clients. It guides setup, authentication, endpoint selection, and handling API responses and stream messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: eToro credentials can grant access to an account.

Mitigation: Use a Read-permission key for data access, load credentials from environment variables, and never hardcode, commit, or log them.

Risk: Transfers and public-content operations can move money or publish or remove content.

Mitigation: Default to read-only endpoints and perform a financial or public-content change only when the user explicitly requests that exact action.

## Reference(s):

- [Project repository](https://github.com/psyb0t/go-etoro)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [eToro authentication documentation](https://api-portal.etoro.com/core/getting-started/authentication)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for integrating typed REST and WebSocket clients in a Go project.]

## Skill Version(s):

0.4.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
