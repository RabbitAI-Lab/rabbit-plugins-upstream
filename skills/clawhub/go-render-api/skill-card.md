## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Go engineers use this skill to integrate Go applications with Render’s public REST API, including listing services and managing deployments or other Render resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Render API credentials could be exposed if they are embedded in source code or logged.

Mitigation: Read the API key from an environment variable; never commit or log it, and never print request headers.

Risk: Deploy, suspend, scale, update, and delete operations can change live infrastructure.

Mitigation: Specify the exact resources and live changes, and call these operations only for services the user named and when the user requested that action.

Risk: The downloaded implementation of this unofficial Go dependency was not audited here.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
