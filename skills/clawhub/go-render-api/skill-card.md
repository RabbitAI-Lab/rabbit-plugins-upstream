## Description:

Guides Go developers in using an unofficial typed client to call the Render REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the Go client to a project, authenticate to Render, and write code that inspects or manages Render resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing a Render API key through source code or request logs.

Mitigation: Read the key from an environment variable; do not commit it or log request headers.

Risk: Deploy, suspend, scale, update, or delete calls can change live infrastructure.

Mitigation: Require explicit confirmation and limit changes to the services and actions the user specified.

Risk: The Go client is an unofficial dependency.

Mitigation: Review the dependency before production use and install it only in projects that need Render API access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-render-api)
- [Publisher profile](https://clawhub.ai/user/psyb0t)
- [Go client repository (linked in skill)](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for authenticated requests, pagination, and API response handling.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
