## Description:

Provides a typed Go client and usage guidance for calling Vercel REST API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Vercel API calls to Go projects and handle request parameters, responses, and errors. It is suited to projects that need to inspect or manage Vercel resources through Go.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls to mutating endpoints can change or delete live Vercel resources.

Mitigation: Use a token limited to the required account or team, supply it through VERCEL_TOKEN, keep the API address at https://api.vercel.com, and confirm the target resources and requested changes before execution.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go Vercel repository](https://github.com/psyb0t/go-vercel)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover typed API requests, response handling, authentication, and error handling.]

## Skill Version(s):

0.14.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
