## Description:

Provides Go developers with guidance and examples for using the typed go-vercel client to call the Vercel REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add or maintain Go code that calls Vercel endpoints for projects, deployments, domains, DNS, environment variables, teams, and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Vercel access token can authorize actions on account or team resources, including operations that change or delete live resources.

Mitigation: Keep the token in an environment variable, never hardcode or log it, and call mutating operations only for resources the user asked to change.

Risk: The security scan reports incomplete evidence because a reference in the skill was unresolved.

Mitigation: Review the supplied skill and setup guide before use, especially its authentication instructions.

## Reference(s):

- [Setup and reference guide](references/setup.md)
- [go-vercel project](https://github.com/psyb0t/go-vercel)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover typed Vercel API requests, bearer-token authentication, and response handling.]

## Skill Version(s):

0.30.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
