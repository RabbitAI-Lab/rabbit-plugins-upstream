## Description:

Provides Go developers with guidance and examples for using the go-vercel client to call Vercel's REST API, including bearer-token authentication and typed endpoint responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to install and work with the go-vercel client when their application needs to read or manage Vercel projects, deployments, domains, environment variables, or teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel API requests can change or delete live resources, and the bearer token grants account access.

Mitigation: Use a token limited to the intended Vercel scope, verify the target account or team, and make resource changes only when requested.

Risk: The third-party Go module implementation was not verified in this review.

Mitigation: Review and pin the module before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [go-vercel project page](https://github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and instructions for using typed Vercel API responses]

## Skill Version(s):

0.20.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
