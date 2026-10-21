## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

External developers and engineers use this skill to add typed Go integrations with the Render API, including service inspection, deploy workflows, and management of other Render resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration uses an unofficial Go dependency.

Mitigation: Review the dependency and pin the version used by the project.

Risk: A Render API key can grant access across the workspaces associated with the account, and some operations change live infrastructure.

Mitigation: Keep the key in an environment variable, never hardcode or log it, and make changes only to services and actions the user explicitly authorized.

Risk: Sending requests to an unintended base URL could expose credentials or affect the wrong service.

Mitigation: Use the official Render API base URL and verify the destination before requests are made.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-render-api source repository](https://github.com/psyb0t/go-render-api)
- [go-render-api package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may configure bearer-token authentication and typed API operations; the library itself reads and writes no files.]

## Skill Version(s):

0.1.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
