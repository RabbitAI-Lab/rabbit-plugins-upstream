## Description:

A typed Go client for Vercel's REST API, with generated methods, typed parameters and responses, and bearer-token authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed Vercel API calls to a project, including operations for projects, deployments, domains, DNS, environment variables, and teams. It helps configure bearer-token authentication and interpret typed API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel API calls can change or delete live resources.

Mitigation: Use a token with only the access needed, verify the intended account or team and target resource, and make live changes only when the user requests them.

Risk: The external Go dependency's implementation was not covered by the security review.

Mitigation: Review and pin the dependency version before using it.

## Reference(s):

- [Setup and reference](references/setup.md)
- [GitHub repository](https://github.com/psyb0t/go-vercel)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.18.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
