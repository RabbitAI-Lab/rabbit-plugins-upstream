## Description:

Provides typed Go methods for calling Vercel's REST API from Go applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and configure a typed client for reading or managing Vercel resources through the Vercel REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel endpoints can change or delete live projects, deployments, domains, DNS records, environment variables, or teams.

Mitigation: Use a narrowly scoped token, verify the intended personal or team account, and request specific resource changes.

Risk: The Go client relies on an external module in production builds.

Mitigation: Review and pin the external Go dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel source repository](https://github.com/psyb0t/go-vercel)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover authentication, API calls, typed responses, and error handling.]

## Skill Version(s):

0.11.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
