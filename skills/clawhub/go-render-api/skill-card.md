## Description:

An unofficial, typed Go client for calling the Render public REST API from Go applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that lists, inspects, and manages Render services and other API resources through the go-render-api client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Render API keys could be exposed if hardcoded, committed, logged, or printed in request headers.

Mitigation: Read the key from an environment variable, keep it out of source control and logs, and do not print request headers.

Risk: Deploy, suspend, scale, update, and delete operations can change live infrastructure.

Mitigation: Call these operations only for services the user named and only when the user requested that action.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-render-api project](https://github.com/psyb0t/go-render-api)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-render-api)
- [Render pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go API client usage guidance and typed request examples.]

## Skill Version(s):

0.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
