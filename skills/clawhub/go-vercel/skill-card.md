## Description:

Guides developers using a Go client to call the Vercel REST API with typed requests and responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Vercel projects, deployments, domains, and other account resources through the Vercel API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Vercel access token could be exposed through source code or logs.

Mitigation: Use a scoped token where possible, keep it in an environment variable, and do not commit or log it.

Risk: API calls can change or delete live Vercel resources.

Mitigation: Approve changes to projects, deployments, domains, DNS records, environment variables, or teams before running them.

## Reference(s):

- [Setup and API usage reference](references/setup.md)
- [go-vercel on ClawHub](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover bearer-token authentication and typed API responses.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
