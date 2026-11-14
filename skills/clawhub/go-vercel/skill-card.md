## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec. Package `vercel` from `github.com/psyb0t/go-vercel` gives `NewClientWithResponses` a typed `...WithResponse` method for every endpoint in the spec (projects, deployments, domains, DNS, env vars, teams and more), with typed params structs, `JSON200` response bodies and `As...` methods for oneOf unions. Auth is a bearer token added by a `RequestEditorFn`, with an optional `teamId` query parameter. Use when Go code needs to call the Vercel API, or the project already imports go-vercel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the typed Go client to call Vercel's REST API from Go applications, including managing projects, deployments, domains, DNS, environment variables, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is benign but has medium confidence and incomplete coverage; a local path-like reference could not be resolved.

Mitigation: Review the setup and authentication instructions before installing, and provide only the Vercel token needed for the task.

Risk: Some API operations can change or delete live Vercel resources.

Mitigation: Call resource-changing operations only when requested and only for the resources in scope.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [go-vercel repository](https://github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed Vercel API requests and responses; examples use a bearer token and optional team ID.]

## Skill Version(s):

0.28.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
