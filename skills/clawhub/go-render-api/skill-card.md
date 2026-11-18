## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the typed Go client to a project and call Render API endpoints to inspect or manage services and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing the Render API key could grant access to the account’s Render resources.

Mitigation: Read the key from an environment variable, and never hardcode, commit, log, or print request headers containing it.

Risk: Deploy, suspend, scale, update, and delete operations can change live infrastructure.

Mitigation: Use these operations only on services the user named and only when the user asked for that action.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project homepage listed in the skill](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-render-api)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes usage guidance for read and state-changing Render API operations.]

## Skill Version(s):

0.12.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
