## Description:

Provides a typed Go client and usage guidance for calling the Vercel REST API through `github.com/psyb0t/go-vercel`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate Go applications with Vercel's REST API through a typed client, including reading and managing projects, deployments, domains, DNS, environment variables, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is benign with medium confidence, and scanner coverage is partial because a local reference could not be resolved.

Mitigation: Review the setup reference as well as the main skill guidance before use.

Risk: Vercel API calls use an access token, and some endpoints can change or delete live resources.

Mitigation: Read tokens from environment variables and never hard-code, commit, or log them; make changes only when requested for the resources in scope.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [Project homepage](https://github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.32.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
