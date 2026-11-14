## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and use the go-render-api client for listing, inspecting, and managing Render resources from Go applications. It guides them through bearer-key authentication, typed API calls, cursor pagination, and handling decoded success and error responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Render operations may expose account data or change live infrastructure, including creating deploys, suspending, scaling, updating, or deleting services.

Mitigation: Keep the API key in an environment variable and out of logs; call mutating operations only for services the user named and actions they requested.

Risk: Using the skill involves contacting the external Render API and downloading the Go module through a module proxy.

Mitigation: Review network access and dependency sources before use, and use the documented Render API base URL.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project page](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a Render API key for authenticated API calls.]

## Skill Version(s):

0.10.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
