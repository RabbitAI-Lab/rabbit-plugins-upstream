## Description:

Guides Go developers in adding and using the unofficial go-vercel client to call Vercel REST API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the go-vercel client and make typed requests to Vercel APIs for projects, deployments, domains, DNS, environment variables, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan has medium confidence and incomplete coverage because a reference in SKILL.md did not resolve to a bundled artifact.

Mitigation: Review the missing reference before installation if fuller assurance is needed.

Risk: Vercel access tokens authorize API requests, and some endpoints can change or delete live resources.

Mitigation: Read tokens from environment variables and never hardcode, commit, log, or print request headers; call write or delete operations only when requested and on the intended resources.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed Go client setup, request examples, response handling, and credential guidance.]

## Skill Version(s):

0.35.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
