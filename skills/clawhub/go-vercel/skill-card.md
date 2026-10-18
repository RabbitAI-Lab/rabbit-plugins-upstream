## Description:

Guides developers using a typed Go client for the Vercel REST API, including setup, authentication, API calls, and response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add or work with the go-vercel client when reading or managing Vercel projects, deployments, domains, environment variables, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Vercel token could be exposed or granted more access than needed.

Mitigation: Store a least-privilege token in an environment variable or secret manager; do not commit or log it.

Risk: API calls can change or delete live Vercel resources.

Mitigation: Only call modifying endpoints when requested, and verify the target projects, deployments, domains, DNS records, environment variables, or teams.

Risk: Installing the client introduces a third-party Go module.

Mitigation: Review the module before adding it to a project.

## Reference(s):

- [go-vercel on ClawHub](https://clawhub.ai/psyb0t/skills/go-vercel)
- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
