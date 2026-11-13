## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that calls the Render API to inspect or manage services and other Render resources, including deploys, environment variables, databases, and jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the Render API sends requests to an external service and may expose secrets or personal data if included in request data.

Mitigation: Use the skill only when you intend to access Render, avoid sending secrets or personal data in requests, and keep the API key in an environment variable rather than source code or logs.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go Render API project](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go examples, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
