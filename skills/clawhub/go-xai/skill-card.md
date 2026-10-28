## Description:

Unofficial Go client for the xAI (Grok) REST API at https://api.x.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add and call the go-xai client from Go projects. It guides setup, endpoint discovery, authentication, and response and error handling for xAI API requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed if they are hardcoded, committed, or logged.

Mitigation: Read XAI_API_KEY from the environment, avoid printing request headers, and do not commit the key.

Risk: API requests may incur costs and send data to xAI; uploads, deletions, and public file URLs can affect account resources or expose content.

Mitigation: Account for API costs and data sharing, and perform uploads, deletions, or public sharing only for resources the user specifically requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-xai project homepage](https://github.com/psyb0t/go-xai)
- [go-xai package documentation](https://pkg.go.dev/github.com/psyb0t/go-xai)
- [xAI API endpoint](https://api.x.ai)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use bearer API authentication with XAI_API_KEY; generated methods decode complete response bodies.]

## Skill Version(s):

0.2.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
