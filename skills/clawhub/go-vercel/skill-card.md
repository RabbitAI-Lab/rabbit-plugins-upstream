## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec. Package `vercel` from `github.com/psyb0t/go-vercel` gives `NewClientWithResponses` a typed `...WithResponse` method for every endpoint in the spec (projects, deployments, domains, DNS, env vars, teams and more), with typed params structs, `JSON200` response bodies and `As...` methods for oneOf unions. Auth is a bearer token added by a `RequestEditorFn`, with an optional `teamId` query parameter. Use when Go code needs to call the Vercel API, or the project already imports go-vercel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed Vercel REST API calls to a Go project, including calls for projects, deployments, domains, DNS, environment variables, and teams. It provides setup, authentication, and response-handling guidance for the go-vercel package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel bearer-token access can reach operations that change or delete live account and team resources; the supplied security assessment is benign with medium confidence and notes that scanner analysis was partial.

Mitigation: Keep the token in an environment variable and out of source control and logs. Check the selected account or team and target resource, and make state-changing calls only when requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Go code, API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Vercel API requests authenticated with a user-provided bearer token.]

## Skill Version(s):

0.26.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
