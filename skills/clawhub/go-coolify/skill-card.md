## Description:

Writes Go code with go-coolify (package coolify, github.com/psyb0t/go-coolify), an unofficial generated client for the Coolify API covering applications, deployments, databases, services, projects, servers and teams. Use when Go code calls the Coolify API or already imports github.com/psyb0t/go-coolify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add or maintain integrations with Coolify using the unofficial go-coolify client. It guides setup, authentication, endpoint selection, and safe handling of API responses and infrastructure-changing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an unofficial third-party Coolify client.

Mitigation: Review the dependency version before use.

Risk: API tokens or requests could be sent to an unintended instance or exposed.

Mitigation: Verify the instance URL, use HTTPS for remote instances, limit token permissions to required operations, and never hardcode, commit, log, or print credentials.

Risk: Mutating API operations can change the user's infrastructure.

Mitigation: Perform create, update, delete, deploy, restart, or stop operations only when explicitly requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-coolify source repository](https://github.com/psyb0t/go-coolify)
- [go-coolify package documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-directed API integration; infrastructure-changing operations require explicit authorization.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
