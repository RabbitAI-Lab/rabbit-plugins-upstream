## Description:

Helps Go developers use the unofficial go-render-api client to call the Render REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and integrate a typed Go client for listing, inspecting, and managing Render resources through the Render API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Render API credentials could be exposed in source code, logs, or request output.

Mitigation: Read the API key from an environment variable; do not hardcode, commit, or log it, and do not print request headers.

Risk: Deploy, suspend, scale, update, or delete operations can change live infrastructure.

Mitigation: Restrict changes to the service named by the user and perform only the action the user requested.

## Reference(s):

- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render API pagination documentation](https://api-docs.render.com/reference/pagination)
- [Package homepage](https://github.com/psyb0t/go-render-api)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
