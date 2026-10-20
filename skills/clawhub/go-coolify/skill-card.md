## Description:

Helps developers write Go code using the unofficial go-coolify client to work with Coolify applications, deployments, databases, services, projects, servers, and teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write and test Go integrations with a user-specified Coolify instance, including reading resources and making explicitly requested infrastructure changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A token could be exposed or sent to the wrong Coolify instance.

Mitigation: Keep tokens out of code and logs, use a narrowly scoped token when possible, and confirm the intended HTTPS instance URL before sending requests.

Risk: Create, update, delete, deploy, restart, or stop operations can change live infrastructure.

Mitigation: Require explicit user approval before code performs those operations.

Risk: The Go client is unofficial and is installed as an external module.

Mitigation: Review the upstream module before installation and test request and response handling against a local HTTP test server.

## Reference(s):

- [go-coolify on ClawHub](https://clawhub.ai/psyb0t/skills/go-coolify)
- [Setup and reference](references/setup.md)
- [go-coolify Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)
- [Go client referenced by the skill](https://github.com/psyb0t/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the Go toolchain and a user-supplied Coolify API URL and token.]

## Skill Version(s):

0.2.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
