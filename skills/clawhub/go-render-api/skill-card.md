## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Go applications with Render's public API, including inspecting services and deploys and managing Render resources. It provides setup, authentication, pagination, and typed response guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Render API key could be exposed.

Mitigation: Read the key from an environment variable; do not hardcode, commit, log, or print request headers.

Risk: Deploy, suspend, scale, update, or delete operations can change live infrastructure.

Mitigation: Specify the exact services and actions, and perform them only when the user explicitly requests them.

Risk: The Go client is unofficial and depends on a separately versioned Go package.

Mitigation: Review and pin the go-render-api dependency version.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)
- [Project repository](https://github.com/psyb0t/go-render-api)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
