## Description:

Provides a typed Go client and usage guidance for calling the Render REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed calls to Render's API, including service and deployment operations. It explains authentication, pagination, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Render API key could be exposed if it is hardcoded, committed, or logged.

Mitigation: Read the key from an environment variable such as RENDER_API_KEY, and never hardcode, commit, log, or print request headers.

Risk: Deploy, suspend, scale, update, and delete operations can change live infrastructure.

Mitigation: Call these operations only for services the user named and only when the user asked for that action.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-render-api)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.13.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
