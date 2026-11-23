## Description:

Unofficial Go client for the Vercel REST API, generated with oapi-codegen from Vercel's OpenAPI spec. Package `vercel` from `github.com/psyb0t/go-vercel` gives `NewClientWithResponses` a typed `...WithResponse` method for every endpoint in the spec (projects, deployments, domains, DNS, env vars, teams and more), with typed params structs, `JSON200` response bodies and `As...` methods for oneOf unions. Auth is a bearer token added by a `RequestEditorFn`, with an optional `teamId` query parameter. Use when Go code needs to call the Vercel API, or the project already imports go-vercel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Go applications with the Vercel REST API, including reading or managing projects, deployments, domains, DNS, environment variables, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security analysis was partial because a path-like reference in SKILL.md could not be resolved.

Mitigation: Review the unresolved reference and the skill contents before relying on the benign scan verdict.

Risk: Vercel API operations can change or delete live projects, deployments, domains, DNS records, environment variables, or teams.

Mitigation: Call mutating operations only for the resource and change the user explicitly requested.

Risk: Bearer tokens can expose account access if committed or logged.

Mitigation: Read the token from an environment variable and do not hardcode, commit, log, or print request headers.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides edits in the current Go project; the client itself does not read or write files.]

## Skill Version(s):

0.34.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
