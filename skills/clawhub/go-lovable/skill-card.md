## Description:

An unofficial typed Go client for Lovable's API, for Go code that manages projects, publishing, deployments, analytics, security data, workspaces, groups, and members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the client from Go code to access Lovable project, publishing, deployment, analytics, security, and workspace APIs. It is also useful when a Go project already imports github.com/psyb0t/go-lovable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project changes, publishing actions, and embed URL creation can affect account resources or access.

Mitigation: Perform these operations only when the user requests them and verify the intended project and action.

Risk: API keys and embed URLs contain credentials.

Mitigation: Read keys from the environment, keep credentials and authorization headers out of logs, and share embed URLs only with intended recipients.

Risk: The downloaded Go dependency and omitted upstream workflow/example files were not audited.

Mitigation: Review and pin a dependency version before use.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-lovable)
- [Project repository](https://github.com/psyb0t/go-lovable)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance for configuring the Go client and handling typed API responses.]

## Skill Version(s):

0.2.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
