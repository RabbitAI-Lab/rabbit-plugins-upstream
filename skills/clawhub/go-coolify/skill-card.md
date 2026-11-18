## Description:

Writes Go code with go-coolify (package coolify, github.com/psyb0t/go-coolify), an unofficial generated client for the Coolify API covering applications, deployments, databases, services, projects, servers and teams. Use when Go code calls the Coolify API or already imports github.com/psyb0t/go-coolify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Go code that calls a Coolify instance through the unofficial go-coolify client. It helps with setup, authentication, endpoint selection, and response handling for reading or changing Coolify resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found an unresolved path-like reference in SKILL.md, and scan coverage is incomplete.

Mitigation: Review the missing reference yourself before installing if it matters to your use.

Risk: The API token could be exposed, or sent to an unintended Coolify instance.

Mitigation: Keep the token out of source control and logs, use HTTPS for remote instances, and send it only to the intended user-supplied instance URL.

Risk: Create, update, delete, deploy, restart, and stop operations change infrastructure.

Mitigation: Call state-changing operations only when the user has asked for that action.

## Reference(s):

- [Setup and usage guide](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)
- [Project homepage](https://github.com/psyb0t/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Go source code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and code use the caller's Coolify instance URL and API token.]

## Skill Version(s):

0.12.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
