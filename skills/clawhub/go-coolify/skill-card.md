## Description:

Helps developers write Go code using the unofficial go-coolify client to access Coolify applications, deployments, databases, services, projects, servers, and teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go projects with a Coolify instance for inspecting resources or performing explicitly requested infrastructure changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Coolify API token could be exposed or sent to an unintended instance.

Mitigation: Keep the token out of code and logs, confirm the user-supplied API URL, and use HTTPS for remote instances.

Risk: Create, update, delete, deploy, restart, or stop operations can change live infrastructure.

Mitigation: Review the target and operation with the user before running any infrastructure-changing request.

## Reference(s):

- [go-coolify on ClawHub](https://clawhub.ai/psyb0t/skills/go-coolify)
- [go-coolify setup and reference](artifact/references/setup.md)
- [go-coolify package documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)
- [go-coolify library homepage](https://github.com/psyb0t/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
