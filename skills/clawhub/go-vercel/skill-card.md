## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec. Package `vercel` from `github.com/psyb0t/go-vercel` gives `NewClientWithResponses` a typed `...WithResponse` method for every endpoint in the spec (projects, deployments, domains, DNS, env vars, teams and more), with typed params structs, `JSON200` response bodies and `As...` methods for oneOf unions. Auth is a bearer token added by a `RequestEditorFn`, with an optional `teamId` query parameter. Use when Go code needs to call the Vercel API, or the project already imports go-vercel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and integrate the go-vercel client when their code needs to read or manage Vercel projects, deployments, domains, environment variables, or teams. It provides typed API call guidance, setup instructions, and examples for handling authentication and responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the client requires a Vercel access token, and the security assessment notes a credential-related alert in setup guidance.

Mitigation: Read the token from an environment variable; never hardcode, commit, or log it, and do not print request headers.

Risk: Security coverage was partial because a referenced local path could not be resolved.

Mitigation: Review the complete skill contents, including the unresolved referenced path, before installation or use.

Risk: The API client can call operations that change or delete live Vercel resources.

Mitigation: Call mutation or deletion operations only when requested, and only for the resources named in the task.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-vercel)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.33.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
