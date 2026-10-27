## Description:

Writes Go code with go-coolify (package coolify, github.com/psyb0t/go-coolify), an unofficial generated client for the Coolify API covering applications, deployments, databases, services, projects, servers and teams. Use when Go code calls the Coolify API or already imports github.com/psyb0t/go-coolify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go code that calls the Coolify API to inspect or manage applications, deployments, databases, services, projects, servers, and teams. Infrastructure-changing operations should be limited to actions the user requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A token sent to the wrong Coolify instance or granted more access than needed could expose infrastructure controls.

Mitigation: Use a task-scoped token, verify the instance URL, and keep credentials out of source code and logs.

Risk: Creating, updating, deleting, deploying, restarting, or stopping resources changes the user's infrastructure.

Mitigation: Review the requested change and perform these operations only when the user asks for them.

Risk: The bundled review does not fully audit the external Go library.

Mitigation: Review the dependency and pin its version when adding it to a project.

## Reference(s):

- [Setup and API usage](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
