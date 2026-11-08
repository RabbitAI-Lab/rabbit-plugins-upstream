## Description:

Provides Go developers with typed methods for reading and managing HubSpot API data through an unofficial Go client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and use the github.com/psyb0t/go-hubspot client for HubSpot API operations with typed requests and responses. It guides setup, authentication, endpoint discovery, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot access tokens can grant access to sensitive account data.

Mitigation: Use a token with only the scopes required; read it from an environment variable and never commit or log it.

Risk: Create, update, merge, archive, delete, and purge operations can change live HubSpot data.

Mitigation: Make account changes only when requested, and only on records in the task's scope.

Risk: The security review did not cover the external Go library's implementation.

Mitigation: Pin and review the unofficial dependency before production use.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Client package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [Project homepage](https://github.com/psyb0t/go-hubspot)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint coverage follows HubSpot's 2026-03 API specification; requires Go 1.26.10 or newer.]

## Skill Version(s):

0.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
