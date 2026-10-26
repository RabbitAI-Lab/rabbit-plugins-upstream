## Description:

Provides guidance and Go examples for using the unofficial go-xai client to call xAI API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and use the go-xai Go client, construct typed requests to xAI APIs, configure bearer-key authentication, and handle API responses and errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed xAI API key could enable unauthorized API use.

Mitigation: Read the key from an environment variable such as XAI_API_KEY; never hardcode, commit, log, or print request headers.

Risk: Requests send data to xAI and may incur costs; uploads, public sharing, and deletions can affect account resources.

Mitigation: Review and pin the Go dependency version, consider costs and data sent, and make state-changing calls only for specific resources the user intends to affect.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-xai source repository and project homepage](https://github.com/psyb0t/go-xai)
- [go-xai package documentation](https://pkg.go.dev/github.com/psyb0t/go-xai)
- [xAI API](https://api.x.ai)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration guidance, Technical guidance]

**Output Format:** [Markdown with Go code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance for client setup, API requests, authentication, and response handling.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
