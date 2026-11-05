## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate the Render API into Go projects, including inspecting services and deploys and managing Render resources through typed API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Render API keys can access all workspaces the user belongs to, and some API operations change live services.

Mitigation: Keep the key in an environment variable, never commit or log it, and authorize only the specific service and action requested.

Risk: The skill relies on a third-party Go dependency, and the security assessment covers the bundled Markdown rather than downloaded SDK code.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and usage guide](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API authentication](https://api-docs.render.com/reference/authentication)
- [Render API pagination](https://api-docs.render.com/reference/pagination)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-render-api)
- [Project homepage](https://github.com/psyb0t/go-render-api)

## Skill Output:

**Output Type(s):** [Code, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover authentication, typed API calls, pagination, and response handling.]

## Skill Version(s):

0.5.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
