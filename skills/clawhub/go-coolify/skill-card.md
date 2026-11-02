## Description:

Writes Go code with go-coolify (package coolify, github.com/psyb0t/go-coolify), an unofficial generated client for the Coolify API covering applications, deployments, databases, services, projects, servers and teams. Use when Go code calls the Coolify API or already imports github.com/psyb0t/go-coolify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Go code that calls a Coolify instance API, including inspecting resources and making requested changes to applications, deployments, databases, services, projects, servers, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Go code can change Coolify infrastructure when it creates, updates, deletes, deploys, restarts, or stops resources.

Mitigation: Use a minimally privileged API token, verify the destination instance URL, review infrastructure-changing code, and perform changes only when requested.

## Reference(s):

- [Skill release page](https://clawhub.ai/psyb0t/skills/go-coolify)
- [Project homepage](https://github.com/psyb0t/go-coolify)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)
- [Setup and reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance, Shell commands]

**Output Format:** [Go code and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for using the Go client; API requests target the instance URL supplied by the user.]

## Skill Version(s):

0.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
