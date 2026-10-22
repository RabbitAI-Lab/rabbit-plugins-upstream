## Description:

Unofficial Go client for the Render public REST API, generated with oapi-codegen. Package render (github.com/psyb0t/go-render-api) has render.NewClientWithResponses, which returns a client with one typed method per endpoint (services, deploys, env vars, Postgres, Key Value, custom domains, jobs and more). Auth is a bearer API key set through render.WithRequestEditorFn, list endpoints page with cursors, and responses decode into JSON200 and per-status error fields. Use when Go code needs to call the Render API or already imports go-render-api.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed calls to the Render REST API, including listing services and deploys or managing Render resources. It provides setup, authentication, paging, and response-handling guidance for projects using the go-render-api package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploy, suspend, scale, update, and delete operations can change live infrastructure.

Mitigation: Specify the target service and intended action, and perform changes only when the user requests them.

Risk: The Render API key could be exposed through source code or logs.

Mitigation: Read the key from an environment variable and do not hardcode, commit, or log it or request headers.

Risk: An unreviewed or unpinned dependency version may introduce production risk.

Mitigation: Review and pin the dependency version before production use, and retain the documented Render API endpoint.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-render-api package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API pagination documentation](https://api-docs.render.com/reference/pagination)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-render-api)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and setup guidance; the library itself reads and writes no files.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
