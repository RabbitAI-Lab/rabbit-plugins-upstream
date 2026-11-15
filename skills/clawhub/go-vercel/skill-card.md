## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec. Package `vercel` from `github.com/psyb0t/go-vercel` gives `NewClientWithResponses` a typed `...WithResponse` method for every endpoint in the spec (projects, deployments, domains, DNS, env vars, teams and more), with typed params structs, `JSON200` response bodies and `As...` methods for oneOf unions. Auth is a bearer token added by a `RequestEditorFn`, with an optional `teamId` query parameter. Use when Go code needs to call the Vercel API, or the project already imports go-vercel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add or use the go-vercel Go client in Go applications that read or manage Vercel projects, deployments, domains, DNS records, environment variables, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Vercel access token could be exposed or used unintentionally when configuring API requests.

Mitigation: Read the token from an environment variable; do not hardcode, commit, or log it, and do not print request headers. Review the setup instructions and referenced material before installing.

Risk: Some Vercel API operations can change or delete live resources.

Mitigation: Call mutating operations only when the user requested the change, and limit them to the resources named in the task.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-vercel)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples show Vercel API client setup, authentication, typed request parameters, and response handling.]

## Skill Version(s):

0.28.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
