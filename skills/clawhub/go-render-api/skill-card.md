## Description:

An unofficial Go client for making typed calls to the Render public REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that lists, inspects, or manages Render resources through the Render API. It is intended for Go projects that use the go-render-api package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests use a Render API key, and some operations can change live infrastructure.

Mitigation: Keep the key in an environment variable and never log it. Call deploy, suspend, scale, update, or delete operations only for services the user named and when the user requested that action.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Source repository](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, API calls, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed Render API requests; examples include bearer-key configuration and paginated response handling.]

## Skill Version(s):

0.7.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
