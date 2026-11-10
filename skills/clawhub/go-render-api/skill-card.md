## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this Go client to call Render's API to inspect services and deploys or manage Render resources from Go applications. Review the requested operation because deploy, suspend, scale, update, and delete calls can affect live infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploy, suspend, scale, update, and delete operations can change live Render infrastructure.

Mitigation: Use these operations only for services the user named and actions the user requested.

Risk: A Render API key could be exposed if it is hardcoded, committed, or logged.

Mitigation: Read the key from an environment variable, and never hardcode, commit, or log it or request headers.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Render API operations that change live infrastructure.]

## Skill Version(s):

0.7.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
