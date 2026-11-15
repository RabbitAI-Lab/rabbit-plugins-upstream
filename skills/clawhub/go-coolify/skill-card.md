## Description:

Writes Go code with go-coolify (package coolify, github.com/psyb0t/go-coolify), an unofficial generated client for the Coolify API covering applications, deployments, databases, services, projects, servers and teams. Use when Go code calls the Coolify API or already imports github.com/psyb0t/go-coolify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Go code that calls a Coolify instance through the unofficial go-coolify client. It guides installation, authentication, endpoint selection, and safe handling of responses and infrastructure-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retrying an infrastructure-changing request after an unclear response could repeat an action that already succeeded.

Mitigation: Check whether the first request succeeded or inspect the resource state before retrying a create, update, deploy, restart, stop, or delete operation.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-coolify repository](https://github.com/psyb0t/go-coolify)
- [go-coolify Go documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go source code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to infrastructure through API calls; operations must be requested by the user.]

## Skill Version(s):

0.11.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
