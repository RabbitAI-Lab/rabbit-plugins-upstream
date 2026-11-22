## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed calls to the Render REST API in a Go project, including inspecting resources and managing services. It provides integration guidance and examples for authentication, pagination, request handling, and response errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Render API key grants access to Render resources and could be exposed if embedded in code, committed, or logged.

Mitigation: Read the key from an environment variable such as RENDER_API_KEY; do not hardcode, commit, log, or print request headers.

Risk: Deploy, suspend, scale, update, and delete operations can change live infrastructure.

Mitigation: Call these operations only on services the user named and only when the user asked for that action.

## Reference(s):

- [Project homepage](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API pagination documentation](https://api-docs.render.com/reference/pagination)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-render-api)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance for using the Go client; calls may operate on live Render resources.]

## Skill Version(s):

0.14.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
