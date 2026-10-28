## Description:

Guides Go developers in using the go-vercel client to call Vercel's REST API with typed requests, response handling, and bearer-token authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when Go code needs to call or manage Vercel resources through the go-vercel client. It explains client setup, bearer-token authentication, typed endpoint methods, response decoding, and error handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel API calls can change or delete live projects, deployments, domains, DNS records, environment variables, and team resources.

Mitigation: Confirm the intended account or team and review the planned changes; act only on resources the user requested.

Risk: Bearer tokens can expose account or team access if disclosed.

Mitigation: Use a narrowly scoped token, keep it out of logs and source control, and avoid printing request headers.

Risk: The client depends on a third-party Go package.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [Source repository](https://github.com/psyb0t/go-vercel)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance for a Go Vercel API client.]

## Skill Version(s):

0.10.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
