## Description:

Provides an unofficial typed Go client for the Vercel REST API, with bearer-token authentication and typed request and response helpers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Go code that calls Vercel APIs for projects, deployments, domains, DNS, environment variables, and teams. It helps configure authentication, choose generated request and response types, and handle API errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel API calls can change or delete live projects, deployments, domains, DNS records, environment variables, or teams.

Mitigation: Confirm the intended target resources and make changes only when the user has requested them.

Risk: The client requires a Vercel bearer token to access account or team resources.

Mitigation: Use a token scoped to the intended account or team, store it in an environment variable, and do not hardcode, commit, or log it.

Risk: The Go module depends on a third-party runtime package and may be upgraded over time.

Mitigation: Consider pinning the dependency to a reviewed version.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel project homepage](https://github.com/psyb0t/go-vercel)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance for integrating a typed Go client; no files are produced by the library itself.]

## Skill Version(s):

0.13.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
