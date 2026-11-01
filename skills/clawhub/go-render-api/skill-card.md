## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add typed calls to Render's public API in a Go project, including listing services and deploys or managing Render resources. It guides setup, bearer-key authentication, pagination, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Render API key could be exposed through source code, logs, or request headers.

Mitigation: Read the key from a private environment variable such as RENDER_API_KEY; do not hardcode, commit, log, or print it.

Risk: Deploy, suspend, scale, update, or delete calls can change live infrastructure.

Mitigation: Review and pin the dependency version, use the documented Render API endpoint, and make changes only to services the user named and requested.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-render-api project](https://github.com/psyb0t/go-render-api)
- [go-render-api package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Go code, API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text guidance and code examples for a Go project.]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
