## Description:

Provides typed Go methods for calling Vercel REST API endpoints with bearer-token authentication and optional team selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go calls to Vercel's REST API, including project, deployment, domain, DNS, environment variable, and team operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Vercel token may permit changes to live projects and account resources.

Mitigation: Use a token with only the access needed, keep it in an environment variable rather than source or logs, and check the target account, team, and resources before making changes.

Risk: Downloaded dependency code and runtime behavior have not been audited.

Mitigation: Consider pinning the dependency version and review dependency code before relying on it.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [go-vercel project homepage](https://github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.15.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
