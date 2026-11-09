## Description:

Use this skill to integrate Go applications with Vercel's REST API through a typed Go client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Vercel API calls to Go projects, including work with projects, deployments, domains, DNS, environment variables, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel API operations can change or delete live projects, deployments, domains, DNS records, environment variables, or teams.

Mitigation: Call mutating operations only when requested, and only for the resources in scope.

Risk: The bearer token can authorize account access.

Mitigation: Read the token from an environment variable, never hardcode, commit, or log it, and use only the access needed.

Risk: The security scan marked coverage partial because a referenced path did not resolve.

Mitigation: Review the setup instructions before installation, as advised by the release security guidance.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go Vercel project page](https://github.com/psyb0t/go-vercel)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [Vercel API](https://api.vercel.com)

## Skill Output:

**Output Type(s):** [Guidance, Go code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.23.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
