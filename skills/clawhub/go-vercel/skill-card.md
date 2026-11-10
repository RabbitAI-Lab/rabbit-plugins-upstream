## Description:

An unofficial typed Go client for calling the Vercel REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or use go-vercel in Go projects that need to read or manage Vercel projects, deployments, domains, DNS, environment variables, or teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's examples require a Vercel access token, and the security review reports medium confidence with incomplete coverage.

Mitigation: Keep the token in an environment variable; do not hard-code, commit, or log it. Review the skill instructions and scan coverage before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel source repository](https://github.com/psyb0t/go-vercel)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover installation, authentication, typed API calls, and response handling.]

## Skill Version(s):

0.24.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
