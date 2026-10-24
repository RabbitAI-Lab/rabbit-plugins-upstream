## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec. Package `vercel` from `github.com/psyb0t/go-vercel` gives `NewClientWithResponses` a typed `...WithResponse` method for every endpoint in the spec (projects, deployments, domains, DNS, env vars, teams and more), with typed params structs, `JSON200` response bodies and `As...` methods for oneOf unions. Auth is a bearer token added by a `RequestEditorFn`, with an optional `teamId` query parameter. Use when Go code needs to call the Vercel API, or the project already imports go-vercel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go calls to the Vercel REST API, including managing projects, deployments, domains, DNS, environment variables, and teams. It guides installation, authentication, endpoint lookup, and handling typed responses and errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests can change or delete live Vercel resources within the token's permissions.

Mitigation: Limit token access, verify the intended account or team, and review the requested changes before execution.

Risk: The clean verdict covers the bundled instructions, not an audit of the downloaded dependency.

Mitigation: Review the downloaded dependency and its version before relying on it in a project.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-vercel)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance cover bearer-token authentication and typed Vercel API responses.]

## Skill Version(s):

0.6.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
