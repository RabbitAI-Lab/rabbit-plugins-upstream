## Description:

Writes Go code with go-coolify (package coolify, github.com/psyb0t/go-coolify), an unofficial generated client for the Coolify API covering applications, deployments, databases, services, projects, servers and teams. Use when Go code calls the Coolify API or already imports github.com/psyb0t/go-coolify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that reads or manages Coolify applications, deployments, databases, services, projects, servers and teams through the go-coolify client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Coolify operations can change infrastructure, including creating, updating, deleting, deploying, restarting or stopping resources.

Mitigation: Perform changes only when the user requests them, and review generated code before running it.

Risk: A misdirected request could expose the Coolify API token, and the Go dependency version has not been audited in the security assessment.

Mitigation: Use the intended HTTPS instance and a token limited to required operations; review and select the dependency version before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-coolify package documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)
- [go-coolify project](https://github.com/psyb0t/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code with shell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
