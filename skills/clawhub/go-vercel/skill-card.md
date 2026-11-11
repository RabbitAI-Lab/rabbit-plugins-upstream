## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec. Package `vercel` from `github.com/psyb0t/go-vercel` gives `NewClientWithResponses` a typed `...WithResponse` method for every endpoint in the spec (projects, deployments, domains, DNS, env vars, teams and more), with typed params structs, `JSON200` response bodies and `As...` methods for oneOf unions. Auth is a bearer token added by a `RequestEditorFn`, with an optional `teamId` query parameter. Use when Go code needs to call the Vercel API, or the project already imports go-vercel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and call a typed client for the Vercel REST API, including project, deployment, domain, DNS, environment variable, and team operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is incomplete because a local path-like reference in SKILL.md could not be matched to a bundled artifact.

Mitigation: Check the unmatched reference before installing the skill.

Risk: A Vercel access token is a credential.

Mitigation: Read it from an environment variable; do not hardcode, commit, log, or print request headers containing it.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-vercel source repository](https://github.com/psyb0t/go-vercel)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API calls that modify live Vercel resources; make changes only when requested and on the specified resources.]

## Skill Version(s):

0.25.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
