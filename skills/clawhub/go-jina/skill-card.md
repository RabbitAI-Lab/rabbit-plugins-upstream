## Description:

An unofficial Go client integration for Jina AI APIs, covering embeddings, reranking, chat completions, batch jobs, model discovery, and web-page reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this skill to integrate Jina AI's hosted APIs for embeddings, reranking, chat completions, batch embeddings, and web-page reading. It provides setup, authentication, request, response, and error-handling guidance for the go-jina packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may send supplied content to Jina AI.

Mitigation: Send only content the user has approved sharing with Jina AI.

Risk: The JINA_API_KEY is a bearer credential.

Mitigation: Protect the API key and avoid exposing it in source code or logs.

Risk: Batch operations may incur charges.

Mitigation: Explicitly authorize paid batch operations before creating them.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-jina package documentation](https://pkg.go.dev/github.com/psyb0t/go-jina)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance for integrating with hosted Jina AI APIs.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
