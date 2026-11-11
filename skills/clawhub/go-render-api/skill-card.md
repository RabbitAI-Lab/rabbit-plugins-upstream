## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and call Render's REST API from Go code, including listing services and managing Render resources. It also helps projects that already depend on github.com/psyb0t/go-render-api.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls made with a Render API key can access account resources, and deploy, suspend, scale, update, or delete operations can change live infrastructure.

Mitigation: Read the API key from an environment variable, never commit or log it, and run mutating operations only for services the user named and explicitly asked to change.

## Reference(s):

- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API pagination](https://api-docs.render.com/reference/pagination)
- [Setup and reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance, API Calls]

**Output Format:** [Go code and concise Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
