## Description:

Guides developers in using an unofficial, typed Go client to access the Vercel REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the Go client to a project, authenticate with a Vercel token, and write typed Go code to read or manage Vercel resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial Go dependency is added to the project.

Mitigation: Review the dependency before installing it.

Risk: A Vercel token or sensitive API responses could be exposed.

Mitigation: Keep the token in an environment variable; do not commit it or log request headers or sensitive response bodies.

Risk: Vercel API calls can change or delete live projects, deployments, domains, DNS records, environment variables, or teams.

Mitigation: Run resource-changing calls only when explicitly requested and limit them to the intended resources.

## Reference(s):

- [Setup and API usage guide](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [Go client source and documentation](https://github.com/psyb0t/go-vercel)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a Vercel token supplied through an environment variable.]

## Skill Version(s):

0.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
