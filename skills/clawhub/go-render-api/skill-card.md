## Description:

Guides agents in using an unofficial typed Go client for Render’s public REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to call Render’s REST API to inspect resources and, when explicitly requested, make changes to named services or deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked Render API key may grant access to all workspaces available to its account.

Mitigation: Read the key from an environment variable; never hardcode, commit, or log it.

Risk: Deploy, suspend, scale, update, and delete operations can change live infrastructure.

Mitigation: Only act on services the user named and for actions they explicitly requested.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [go-render-api repository](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API authentication](https://api-docs.render.com/reference/authentication)
- [Render API pagination](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Go code and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live Render API operations; limit changes to services and actions the user explicitly authorized.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
