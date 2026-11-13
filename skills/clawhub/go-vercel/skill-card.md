## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add and use a typed client for Vercel's REST API, including project, deployment, domain, DNS, environment variable, and team operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review confidence is medium and coverage is incomplete because a path-like reference could not be resolved.

Mitigation: Review the setup instructions and confirm the referenced material before installing.

Risk: The client uses a Vercel bearer token, and many API endpoints can change or delete live resources.

Mitigation: Read the token from an environment variable, never commit or log it, and call change or delete operations only when requested for the intended resources.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel package source](https://github.com/psyb0t/go-vercel)
- [go-vercel Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and setup guidance for using a typed Go API client]

## Skill Version(s):

0.27.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
