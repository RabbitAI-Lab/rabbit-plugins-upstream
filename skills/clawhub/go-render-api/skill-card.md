## Description:

Guides Go developers in using an unofficial client for the Render API to inspect and manage Render resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the Go client to projects, authenticate with a Render API key, and work with Render services, deployments, and other resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Render API key could be exposed in code or logs.

Mitigation: Use a narrowly scoped key from the environment; never hardcode, commit, or log it or request headers.

Risk: Generated code could change live Render infrastructure.

Mitigation: Review code that deploys, suspends, scales, updates, or deletes resources before running it, and act only on explicitly requested resources.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API pagination](https://api-docs.render.com/reference/pagination)
- [go-render-api source](https://github.com/psyb0t/go-render-api)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
