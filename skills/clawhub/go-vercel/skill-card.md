## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec. Package `vercel` from `github.com/psyb0t/go-vercel` gives `NewClientWithResponses` a typed `...WithResponse` method for every endpoint in the spec (projects, deployments, domains, DNS, env vars, teams and more), with typed params structs, `JSON200` response bodies and `As...` methods for oneOf unions. Auth is a bearer token added by a `RequestEditorFn`, with an optional `teamId` query parameter. Use when Go code needs to call the Vercel API, or the project already imports go-vercel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Vercel's REST API through the typed go-vercel client, including requests for projects, deployments, domains, DNS, environment variables, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial; a local path-like reference in SKILL.md was not matched to a bundled artifact.

Mitigation: Review the reference and source files before installing.

Risk: A Vercel token could be exposed if it is embedded in code or logged.

Mitigation: Load the token from an environment variable; do not hardcode it, commit it, or log it.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Go code, Configuration guidance, Shell commands, API integration guidance]

**Output Format:** [Go code examples and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples for client setup, authentication, request parameters, and typed API responses.]

## Skill Version(s):

0.31.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
